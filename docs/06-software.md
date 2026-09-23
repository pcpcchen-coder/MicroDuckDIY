# 06｜軟體安裝：先模擬，再實機

> 路線 A：官方 alpha / Radxa 參考。本次要跟帆哥製作，請改讀 [路線 B（11–14章）](11-fange-start.md)，勿混用ID、列印比例與操作命令。

來源鎖在`data/upstream-lock.json`。以下命令由官方文件與原始碼核對，**本專案未在實體Radxa／馬達上執行**。前半可於開發機嘗試；後半只有04、05章驗收後才執行。

## A. 開發機模擬

需要Git、Rust/Cargo、uv/Python與對應原生依賴；macOS適合開發／CPU模擬，官方MuJoCo Warp訓練需要CUDA GPU，不能把Apple GPU當成CUDA使用。Windows建議Linux／WSL2環境，但GUI、藍牙、USB轉接各須另驗，不宣稱與Linux完全等效。

```bash
mkdir -p microduck-work
cd microduck-work
git clone https://github.com/pollen-robotics/microduck.git
git clone https://github.com/pollen-robotics/microduck_rl.git
git -C microduck checkout ac7531a77adae5e9c49d1a3f5d23f72f9af7fee1
git -C microduck_rl checkout cb70b792312d559a4da09064d92009079671815f
cd microduck_rl
uv sync
cd ../microduck
```

若`uv sync`於非CUDA平台失敗，保留錯誤訊息，依上游當前`pyproject.toml`平台條件建立CPU模擬環境；不要因為CUDA訓練安裝失敗就判定機器人需要GPU隨身運算。版本升級時重新記錄commit。

Linux原生依賴（官方CONTRIBUTING列出的建置需求）：

```bash
sudo apt-get update
sudo apt-get install -y libudev-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev
```

macOS影像模擬依賴：

```bash
brew install gstreamer libnice-gstreamer
```

開始與停止模擬：

```bash
scripts/duck-sim
scripts/duck-sim status
scripts/duck-sim ctl health
scripts/duck-sim monitor
scripts/duck-sim drive
scripts/duck-sim down
```

首次會建置，需可下載依賴與策略資產。兩個repo放同一父資料夾；若不在旁邊，用`DUCK_SIM_RL`指向RL checkout。模擬驗收：有視窗、health有回應、可觀察站立／行走、能正常down；它不能驗證實際馬達、I²C、電源或相機驅動。

## B. 準備Radxa

上游安裝文件使用 **Radxa Zero 3／Armbian26.2.1 Minimal**。從[官方安裝入口](https://www.armbian.com/radxa-zero-3/)確認映像適用板版號，寫入前核對目標儲存裝置，保留一張未修改救援卡。燒錄時設定自己的帳號、Wi-Fi及SSH，勿照抄他人預設密碼。

```bash
# 範例地址及帳號要換成自己的；先在路由器查DHCP租約
ssh radxa@192.168.1.42
# 回開發機設定SSH key登入
ssh-copy-id radxa@192.168.1.42
```

主板先獨立測啟動、SSH、重啟及網路。**電源與馬達相容性未解決，不要接上馬達跑provision**；它可能啟動daemon，daemon會寫馬達暫存器。僅主板測試時health缺馬達／IMU是合理失敗，不代表已完成整機安裝。

## C. 安裝官方軟體（相容硬體分支）

在開發機`microduck`目錄執行上游已核對命令：

```bash
./scripts/provision-board.sh --pause-btd-on-pair --name GeorgeDuck radxa@192.168.1.42
```

此步會安裝服務並重啟；需要SSH key及正常外網。上游文件說公開repo不需要token，只有限流或非公開資產才可能需要。不要把GitHub token寫進repo或操作紀錄。

注意：固定本地checkout能固定你審阅的程式，**不保證provision下載的remote release／policy也固定**。安裝後記錄`robotctl health`、update status、實際OS/kernel／policy版本，才能重現。進階固定release依官方安裝／更新文件操作，勿把移動的main當不可變版本。

```bash
# 以下在Radxa上
robotctl --help
robotctl health
robotctl update status
systemctl status robotd --no-pager
journalctl -u robotd -n 100 --no-pager
```

配置位於`/etc/robot/robotd.toml`，先備份再改。IMU尚未完成或使用改裝供電的DIY分支：停在此之前，先完成04章適配，不能靠忽略health或關閉保護直接往下。

## D. 通訊檢查

確認15個ID及IMU200、1Mbps與`/dev/ttyS2`。一次只能一個程式佔bus；停止daemon後才用Wizard／其他串口工具。上游設定腳本會處理serial-getty，若全部裝置都消失，可查：

```bash
sudo fuser -v /dev/ttyS2
journalctl -u robotd -n 150 --no-pager
```

若硬體不支援Fast Sync Read，可在既有`[bus]`區段設定`fast_sync_read = false`（不要重複新增同名區段），支撐機器且確定停止動作後再重啟服務。XL330 fast read須相容韌體，IMU也要支援；換成普通read後仍必須確認50Hz控制時序。

## E. 首次動作

必要前置：完成供電相容性、15軸方向與零位、IMU方向、機構手動行程及停機方式驗收；使用支撐架，地面鋪軟墊。

```bash
# 先讀狀態
robotctl health
robotctl monitor
# 確認支撐好；會驅動全部關節到home
sudo robotctl robot init
# 已支撐好再卸力；全機可能倒下
sudo robotctl robot relax --yes
```

`init`不是校正向導，它直接移動全部關節。沒有通過單關節測試時不要使用。確認init／relax可控，再配對手把：

```bash
sudo robotctl pad pair
robotctl pad status
```

在有支撐的低風險條件試Start→home，再試政策啟動；下架慢走方法見07章。未驗證供電／質量的DIY機器不能直接假設原廠政策可用。

## F. 更新與回復

動作停止、機器有支撐且電源穩定後才更新。先存`/etc/robot/robotd.toml`、health、policy來源與自己的補丁。官方命令：

```bash
robotctl update status
sudo robotctl update apply daemon
robotctl health
# 只有存在前一個版本時才可rollback
sudo robotctl update rollback daemon
```

第一次安裝不一定有前版可退。啟動問題先留journal與OS映像，不要反覆刷機抹掉校正資料。改裝供電／IMU若修改原始碼，須有自己的版本及重建方式；自動升級官方版可能覆蓋適配。

## G. 自己訓練（選修）

先用官方策略建立基準再改。官方RL環境使用CUDA、MuJoCo Warp與PPO；沒有合適GPU可評估Hugging Face Jobs的付費作業。不要在未確認費用時直接排大規模訓練。

```bash
# CUDA開發主機、microduck_rl目錄
uv run list-envs
uv run train Mjlab-Velocity-Flat-MicroDuck --env.scene.num-envs 4096
# 訓練完成後，把參數換成自己的wandb run
uv run scripts/export.py Mjlab-Velocity-Flat-MicroDuck --wandb-run-path ENTITY/PROJECT/RUN_ID
```

部署使用官方export產出的ONNX，內含觀測正規化；目標介面`[1,61]→[1,14]`。不要直接手轉checkpoint或把嘴部塞進14維輸出。電壓／馬達／重心変更先更新模型，先模擬，再支撐實機，小步驗證。
