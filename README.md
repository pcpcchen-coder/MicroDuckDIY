# MicroDuckDIY｜MicroDuck 自製規劃與操作手冊

版本：v0.1 · 查核日期：2026-09-23 · 對象：George 的第一台 DIY MicroDuck。

**目標：自行採購、列印、組裝，完成可安全站立及遙控行走的雙足機器鴨。** 本 repo 提供繁體中文工程規劃、零件採購表、逐件列印表、軟體安裝及驗收教學。以官方 alpha／Radxa 路線為基線，先完成步行，再加影像、音訊與輪滑。

## 先看這三件事

1. **這不是原廠完整組裝套件。** 官方 runtime 開源；HAT 有公開製造檔；機構可由 RL 模型取得 STL。但本次查核未取得完整整機製造 BOM、螺絲表與 `imu_to_dxl` v2 板製造／韌體資料。因此文件完成不代表整台硬體已驗證可複製。
2. **不要一次買 15 顆馬達。** runtime 使用 XL330 控制介面，且記載 2S 電池直供；零售 XL330-M288-T 額定上限是 6 V。先以 5 V、單顆馬達與限流電源驗證，供電設計與策略相容性確認後再購齊。
3. **STL 不是直接丟進切片軟體就好。** 本次鎖定模型使用公尺座標，要轉成毫米；步行模型核算為 **30 種、36 件列印候選**，另有軸承、馬達、電池與板卡的參考模型不能拿來列印替代。

## 從這裡開始

| 你要做什麼 | 文件 |
|---|---|
| 看路線、時程、阻礙與完成定義 | [00 專案規劃](docs/00-project-plan.md) |
| 決定買什麼、買幾個、去哪找、估多少預算 | [01 採購清單](docs/01-purchasing.md) |
| 逐個下載列印檔、確認數量 | [02 列印清單](docs/02-print-list.md) |
| 轉單位、切片、試裝與列印驗收 | [03 列印教學](docs/03-printing.md) |
| 電路板代工、接線與供電 | [04 電子與供電](docs/04-electronics.md) |
| 馬達編號、機構組裝與校正 | [05 組裝教學](docs/05-assembly.md) |
| 電腦模擬、主板安裝、實機啟動 | [06 軟體教學](docs/06-software.md) |
| 遙控、關機、維護及故障排除 | [07 操作教學](docs/07-operation.md) |
| 照表驗收、記錄數據 | [08 驗收與施工紀錄](docs/08-acceptance.md) |
| 查證依據、版本及待確認問題 | [09 來源與缺口](docs/09-sources.md) |
| 看本次實際驗證範圍 | [10 驗證紀錄](docs/10-validation-report.md) |

## 第一個週末

- 電腦：按 06 章先啟動模擬，不必等硬體到貨。
- 詢價：Radxa Zero 3W、1 顆 XL330-M288-T、USB–Dynamixel TTL 工具、HAT PCBA。
- 列印：先印 `bearing_roll` 與 `motor_support`，別一次印完整頭殼。
- 確認：IMU v2 取得方式、馬達實際型號及容許電壓。這兩項是進入整機動態測試的必要條件。

## 檔案與工具

```text
README.md
docs/                   繁體中文手冊
data/print-manifest.json 38 種模型、數量、分類、下載網址及 Git blob SHA
data/upstream-lock.json  官方來源固定 commit
scripts/prepare_prints.py STL 下載、來源雜湊校驗、公尺轉毫米、尺寸報告
scripts/check_docs.py     內部文件連結及清單一致性檢查
```

```bash
python3 scripts/prepare_prints.py --list
python3 scripts/prepare_prints.py --download --only bearing_roll motor_support
python3 scripts/check_docs.py
```

工具不連接馬達、不修改機器人；STL 下載到本機 `build/`，不自動提交到 Git。材料、填充率、預算及驗收門檻均為本專案工程建議；有來源的官方事實另行標示。本文尚無實體組裝或行走驗證結果。

## 授權界線

本 repo 為獨立規劃，非 Pollen Robotics 官方產品支援。上游軟體與 HAT 為 Apache-2.0；RL README 對 3D 模型另標示 Creative Commons BY-SA-NC，不能因根目錄軟體授權而視為模型可任意商用。保留原作者、來源及授權；本 repo 不重新散布 STL、PCB 或上游韌體。[來源及授權說明](docs/09-sources.md)。
