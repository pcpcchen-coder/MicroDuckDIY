# MicroDuckDIY｜MicroDuck 自製規劃與操作手冊

版本：v0.2 · 查核日期：2026-09-23 · 對象：George 的第一台 DIY MicroDuck。

**目標：自行採購、列印、組裝，完成可安全站立及遙控行走的雙足機器鴨。** 本 repo 提供繁體中文工程規劃、零件採購表、逐件列印表、軟體安裝及驗收教學。首次實作優先採用帆哥社群路線 B；官方 alpha／Radxa 路線 A 保留為研究基線。先完成步行，再考慮影像、音訊與輪滑。

## George：第一次照做，從路線 B 開始

**[11 帆哥方案總覽與實作順序](docs/11-fange-start.md)** → **[12 採購與5盤列印表](docs/12-fange-parts-printing.md)** → **[13 接線、刷機、校正與操作](docs/13-fange-build-run.md)** → **[14 驗收與施工紀錄](docs/14-fange-acceptance.md)**。

- 配置：Pi Zero 2 W＋OpenRB-150＋BNO08x＋14顆XL330；嘴部第15顆暫不裝。
- 有作者實機展示及映像，但本repo尚未實體重現。先買1顆測試，再增至5顆單腿，通過後補至14顆。
- 帆哥3MF已是毫米；5盤65個已分盤實例，另2個未分盤物件。不得套用官方STL放大1000倍或30種36件清單。
- 本次實際檢查附帶ONNX為51輸入／14輸出，不能混用官方61維模型；膝偏移、IMU方向及電源仍須按實物驗證。
- 「6V電池」未指定完整SKU，不能保證滿電不超XL330額定；先用5V限流台架，最終電源按12章選型。

## 路線 A：官方版本研究參考

下方00–10章與 `prepare_prints.py` 都屬於路線 A。官方runtime、RL機構與HAT來源已固定，但完整製造BOM與IMU橋接資料仍有缺口；2S供電假設也不可直接用於零售XL330。A與B的採購、ID、列印單位、IMU及操作命令不可混用。

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

## 第一個週末（路線 B）

1. 依11章下載帆哥固定版本，觀看作者組裝影片，開3MF確認自己的機型與尺寸。
2. 詢價Pi Zero 2 W、OpenRB-150、BNO08x、1顆XL330與配套線材，不必先買GPU。
3. 按12章試印舵機配合件，13章先做單顆通訊與IMU測試。
4. 用14章記錄結果；還沒完成單腿前，不先買齊14顆及整套電池。

## 檔案與工具

```text
README.md
docs/                   繁體中文手冊
data/print-manifest.json 38 種模型、數量、分類、下載網址及 Git blob SHA
data/upstream-lock.json  官方來源固定 commit
data/fange-lock.json     帆哥來源、3MF／ONNX雜湊及映像校驗資訊
data/fange-print-inventory.json  帆哥3MF盤點（非製造BOM）
scripts/prepare_prints.py STL 下載、來源雜湊校驗、公尺轉毫米、尺寸報告
scripts/check_docs.py     內部文件連結及清單一致性檢查
```

以下列印工具僅適用路線 A；路線 B直接使用作者3MF。

```bash
python3 scripts/prepare_prints.py --list
python3 scripts/prepare_prints.py --download --only bearing_roll motor_support
python3 scripts/check_docs.py
```

工具不連接馬達、不修改機器人；STL 下載到本機 `build/`，不自動提交到 Git。材料、填充率、預算及驗收門檻均為本專案工程建議；有來源的官方事實另行標示。本文尚無實體組裝或行走驗證結果。

## 授權界線

本 repo 為獨立規劃，非 Pollen Robotics 官方產品支援。上游軟體與 HAT 為 Apache-2.0；RL README 對 3D 模型另標示 Creative Commons BY-SA-NC，不能因根目錄軟體授權而視為模型可任意商用。保留原作者、來源及授權；本 repo 不重新散布 STL、PCB 或上游韌體。[來源及授權說明](docs/09-sources.md)。

帆哥路線另有MIT根授權、GPL標示子目錄與模型上游權利，詳見[11章](docs/11-fange-start.md)。
