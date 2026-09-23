# 11｜路線 B：跟著帆哥製作第一台會走的 MicroDuck

更新：2026-09-23。**George 的第一次實作，優先走這條社群路線；原 00–10 章保留為路線 A（官方 alpha / Radxa）研究參考。** 本路線有作者實機展示、程式、模型與系統映像，具備動手驗證的基礎；本專案尚未實體重現，不能承諾買齊便能走。先以單顆舵機、IMU、試印件完成小規模驗證。

## 來源與目標

- 作者：[AI研究室－帆哥／AI-FanGe](https://github.com/AI-FanGe/Microduck-build-tutorial)。
- [B 站完整製作影片](https://www.bilibili.com/video/BV1uUbG6FEfb/)；[YouTube 同名影片](https://www.youtube.com/watch?v=Vep8AjoCnEM)。影片負責實物裝配方向，本手冊負責版本、檢查與驗收；本次未逐幀核對影片。
- 本次逐檔查核版本：[49678215d0b40529522772a40c06c216390449dd](https://github.com/AI-FanGe/Microduck-build-tutorial/tree/49678215d0b40529522772a40c06c216390449dd)。來源雜湊見 [fange-lock.json](../data/fange-lock.json)。
- 第一階段目標：14 軸、鍵盤遙控、平地慢行、能停止及正常關機。嘴部第 15 軸、相機、語音、翻滾與輪滑不在首次驗收範圍。

## 兩条路線不可混用

| 項目 | A：原官方基線（00–10章） | B：本次帆哥方案（11–14章） |
|---|---|---|
| 主控 | Radxa Zero 3W | Raspberry Pi Zero 2 W |
| 舵機介面 | 官方 HAT／TTL 介面 | OpenRB-150 USB 橋接 |
| 平衡 IMU | LSM6DSV16X + imu_to_dxl | BNO080/085/086、I²C |
| ID | 10–14、20–24、30–34 | 1–14，嘴部 15 選配 |
| 執行程式 | Rust robotd / robotctl | Python main.py / scheduler.py |
| 模型 | 官方策略及其 manifest | 同版 walk.onnx 與其 metadata |
| 觀測 | 61 維官方配置 | 程式基底 51 維，含 phase 時 53；以本版模型查驗為準 |
| 列印 | 官方 STL 候選 30 種36件，m→mm | 作者 3MF，原生 mm，5盤，另有未分盤物件 |
| 電源 | 原軟體2S假設與零售馬達額定不符 | README 稱6V電池；仍須確認滿電／瞬態不超6V |

不要把路線 A 的 ID、重力座標、零位、robotctl、STL 比例或 ONNX 直接搬進 B。`walk.py` 要求模型的 `joint_names` 與 `OBSERVATION_DOF_ORDER` 完全一致，輸入維度相同仍不代表可互換。

## 實作順序與放行條件

| 階段 | 做什麼 | 通過才往下 |
|---|---|---|
| B0 電腦準備 | 下載固定版、看影片、開3MF、確認 BOM | 檔案雜湊一致；切片尺寸與馬達孔距合理 |
| B1 小額採購 | Pi、OpenRB、IMU、1顆XL330、線材、SD、5V限流電源 | USB可識別、單顆可讀寫、IMU可讀 |
| B2 試印／校正 | 舵機固定件、惰輪配合；單顆小角度測試 | 不干涉、不裂、電壓正常、可卸力 |
| B3 單腿 | 再買4顆，組5軸腿 | 逐軸方向／零位通過，線材不受拉 |
| B4 整機 | 再買9顆，共14顆；完成剩餘列印與固定 | 14 ID唯一、兩膝偏移及IMU方向通過 |
| B5 支撐啟動 | 首先只鍵盤，實體支撐防墜 | neutral無碰撞、60秒穩定、停止可用 |
| B6 平地驗收 | 低速前後、左右轉、歸零、停機 | [14章](14-fange-acceptance.md) 完成且留影片 |

工時先預留 4–6 個週末；這是安排建議，不含採購交期、列印失敗或必要機構修改。現階段不需要購買訓練 GPU，先用作者附的模型。

## 開始操作

依序閱讀：

1. [12 採購與列印](12-fange-parts-printing.md)：這條路線自己的購物與分盤表。
2. [13 接線、刷機、校正與操作](13-fange-build-run.md)：每個命令標明在電腦或 Pi 執行。
3. [14 驗收、已知問題及施工紀錄](14-fange-acceptance.md)：保留自己的實測證據。

在開發電腦終端執行（macOS/Linux；Windows 可在 Git Bash 中操作 Git）：

```bash
git clone https://github.com/AI-FanGe/Microduck-build-tutorial.git Microduck-FanGe
cd Microduck-FanGe
git checkout --detach 49678215d0b40529522772a40c06c216390449dd
git rev-parse HEAD
```

首次不要 `git pull` 更新成另一版。自己的校正修改應另開分支 `git switch -c george-build-01`；保存原始常數與變更原因。SD 映像不一定與此 commit 完全一致，刷機後先比對，見13章。

## 為什麼有影片仍需分階段

查核發現：README 的 `microduck/cad/` 在鎖定版不存在，3MF 才是實際提供的列印入口；3MF 的物件名稱多為無語意名稱；膝關節有作者專用 ±45° 偏移；程式對 IMU stale 主要是警告；初始化失敗不保證卸力。這些已轉成13–14章的具體檢查，不應把作者成功展示等同每一套硬體無須調整。

授權：根目錄 LICENSE 為 MIT，但 `microduck/` 及多個源碼標示 GPL-3.0-or-later，模型另有上游權利；不要將整套資產一律當 MIT。本 repo 只放獨立中文指引、來源索引及分析結果，不重新散布作者3MF、模型或映像。
