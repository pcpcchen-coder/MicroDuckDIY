# 09｜查核來源、版本與尚缺資料

查核日期2026-09-23。本文件基於原廠公開資料及本次直接分析；沒有把第三方復刻推測當成官方製造BOM。GitHub分支會移動，因此以commit鎖定資料。

## 固定來源

| 來源 | 固定版本／連結 | 用途 |
|---|---|---|
| runtime | [ac7531a77adae5e9c49d1a3f5d23f72f9af7fee1](https://github.com/pollen-robotics/microduck/tree/ac7531a77adae5e9c49d1a3f5d23f72f9af7fee1) | 控制架構、CLI、板卡初始化 |
| RL／機構模型 | [cb70b792312d559a4da09064d92009079671815f](https://github.com/pollen-robotics/microduck_rl/tree/cb70b792312d559a4da09064d92009079671815f) | robot_walk.xml、STL與模型授權 |
| RPI Robot HAT | [88d51faf7f5fcc845d2e3b42d4f05ebb98b963b9](https://github.com/pollen-robotics/elec_RPI_Robot_HAT/tree/88d51faf7f5fcc845d2e3b42d4f05ebb98b963b9) | KiCad9、Gerber、BOM、POS及原理圖 |

## 事實追溯

| 文件／官方頁面 | 本規劃使用的資訊 |
|---|---|
| runtime `duck-control/src/model.rs` | 15個ID、home、IMU200、1Mbps、NP-F550與電壓假設、shutdown設定 |
| runtime `duck-control/src/bus.rs` | XL330控制器、位置轉換、fast read、替換一顆馬達條件 |
| runtime `duck-control/src/imu.rs` | LSM6DSV16X、位址124讀取12 bytes、安裝方向 |
| runtime `docs/robot/install-dev.md` | Radxa／Armbian與provision流程 |
| runtime `docs/robot/cheatsheet.md` | init／relax、手把按鍵、更新及rollback |
| runtime `docs/robot/simulation.md` | 開發機duck-sim、依賴及模擬限制 |
| runtime `scripts/setup-board.sh`、`deploy/audio/*.dts` | HAT音訊、I²C及ToF整合 |
| RL `robot_walk.xml` | visual geom 38種類／70實例；排除碰撞重複後30種36件候選列印件 |
| RL `assets/trunk_base.stl` | 座標量測約0.057×0.036×0.003，證實需要m→mm |
| HAT `elec_RPI_Robot_HAT.kicad_pcb` | 4層及1.0mm板厚 |
| [ROBOTIS手冊](https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/) | 零售XL330-M288-T電壓3.7–6V、5V下1.47A失速電流、通訊介面 |
| [ROBOTIS商店](https://en.robotis.com/shop_en/item.php?it_id=902-0163-000) | 本次USD23.90、包裝內線材與螺絲，未確認台灣即時庫存 |
| [Radxa ZERO3文件](https://docs.radxa.com/en/zero/zero3) | 板卡資訊入口 |
| [Radxa硬體介面](https://docs.radxa.com/en/zero/zero3/hardware-design/hardware-interface) | 主板僅5V輸入 |
| [Microduck產品頁](https://pollen-robotics.com/microduck/) | 約25cm／800g、15馬達及USD399起價對照 |
| [Issue168](https://github.com/pollen-robotics/microduck/issues/168) | 軟體開源不等於完整機構／BOM開源；討論關閉不代表資料齊備 |
| [Issue174](https://github.com/pollen-robotics/microduck/issues/174) | 維護者提及量產機板上充電；不可外推至DIY HAT |

上述GitHub檔案可在固定版本目錄中按路徑查閱；模型及下載工具的每檔Git blob SHA在manifest。表中的計數是本專案直接解析結果，與其他日期／變體的38種75件等數字可能不同，不能混用。

## 尚未取得的資料及解除條件

| 缺口 | 影響 | 如何解除 |
|---|---|---|
| 整機確切馬達SKU／額定電源 | 無法保證零售件直接重現原策略 | 原廠／供應商正式規格＋單顆台架驗證 |
| imu_to_dxl v2製造檔／韌體／完整pinout | 原版控制IMU不可照表製作 | 取得相容完成板，或另做自製硬體／韌體專案 |
| 全套製造CAD、公差、螺絲表、扭力 | STL可視不代表可直接製造 | 實物試裝量測、逐孔五金紀錄、必要機構修訂 |
| default軸承精確尺寸／料號 | 不能整批下單 | 網格已量得內10×外15×厚3mm；仍需確認公差、密封型式及樣品試裝 |
| 相機／喇叭／電池接點／線束SKU | 裝殼、供電及接頭仍需設計 | 模組工程圖與板卡原理圖交叉比對 |
| 台灣現貨、PCBA報價與交期 | 總價和完成日期仍有區間 | 供應商實際報價，不以網頁標價當到手價 |
| 實體列印／裝配／行走紀錄 | 無法宣稱已驗證可複製 | 按08章完成並留證據 |

`imu_to_dxl`公開URL本次回404，只能表述本次無法取得，不能推定不存在。HAT則已實際取得完整repo與production檔，不能說所有電子硬體都未公開。

## 給供應商／Pollen的詢問模板（尚未寄送）

> 我計畫個人研究用途自行組裝MicroDuck，參考runtime ac7531a與RL cb70b79。請協助確認：
>
> 1. 15顆馬達確切型號、是否為零售XL330-M288-T，以及容許持續／峰值電壓。runtime描述2S直供，但零售規格上限6V，應採哪種相容配置？
> 2. 能否取得imu_to_dxl v2完成板或製造檔、韌體、接線／供電規格、fast sync read支援與安裝方向？
> 3. 公開HAT C1是否適用目前Radxa Zero3W配置？與量產充電／電源板的差異為何？
> 4. 是否有可供個人自製的製造CAD、列印建議、兩種軸承料號、五金及線束表？
> 5. 可供應的零件、台灣出貨、稅運、MOQ及交期為何？

## 授權與維護

軟體Apache-2.0與3D資產授權不同；RL README寫Creative Commons BY-SA-NC，未在此擅自推定版本號。個人使用、修改公開、商業製造的條件需逐一依上游實際授權確認。repo只存我們的規劃與來源索引；下載後保存來源／作者與授權，不把上游資產改標為我們的著作。

上游更新時：先建立新版本記錄→重算visual數量→比對馬達ID／IMU／電壓／CLI→試印受影響零件→重新驗收，不覆寫舊版施工紀錄。
