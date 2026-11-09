# 15｜2026-11 路線更新：HD-1910 MicroDuck Replica、Open Duck Mini v2 與採購市場

查核日期：2026-11-09  
用途：MicroDuckDIY 新一輪方案決策、採購與實作前檢查。  
狀態：**研究完成，尚未由本 repo 實體重現。所有低價整機／套件在付款前都必須做 SKU 與內容物確認。**

## 結論先講

目前新增兩條值得保留的實作路線：

- **Route C — MicroDuck Replica / OpenMicroDuck：HD-1910 ×15 + Radxa Zero 3W（RK3566）**
  - 與正式 MicroDuck 尺寸與硬體方向最接近。
  - 中國社群已出現 CAD、BOM、映像、校正與實機行走資料。
  - **目前列為本 repo 的「優先採購候選」**。
- **Route D — Open Duck Mini v2：STS3215 + Raspberry Pi Zero 2 W**
  - 更偏完整 open-hardware / RL 教學平台。
  - CAD、BOM、列印與 RL 路線透明，適合從機構到 sim-to-real 全程學習。
  - 尺寸約 42 cm，並非 25 cm MicroDuck 等比例替代。

原本 Route B（帆哥 Pi Zero 2 W + OpenRB-150 + XL330）仍保留，因為本 repo 已整理固定版本、3MF 與 ONNX 驗證資料。**在 Route C 真機驗證前，不刪除或覆蓋 Route B。**

---

## 方案比較

| 項目 | Route C：HD-1910 MicroDuck Replica | Route D：Open Duck Mini v2 | 官方 MicroDuck | Route B：帆哥路線 |
|---|---|---|---|---|
| 目標尺寸 | 約 25 cm | 約 42 cm | 25 cm | 約 MicroDuck 級 |
| 舵機 | Feetech HD-1910-C001 ×15 | STS3215 ×14 + SG90 ×2 | 15 DOF | XL330 ×14（嘴部可後補） |
| 主控 | Radxa Zero 3W / RK3566 | Raspberry Pi Zero 2 W | RK3566 | Raspberry Pi Zero 2 W |
| IMU | LSM6DSV16X 路線 | BNO055 / 專案指定配置 | 官方整合 | BNO08x |
| MuJoCo / RL | 有社群路線 | 有 | 有 | 有 ONNX / 社群移植 |
| sim-to-real | 有實機案例 | 有 | 有 | 有社群案例 |
| 3D/CAD | 社群復刻公開 | 完整公開 | 官方硬體非完整開源 | 社群 3MF |
| 維修性 | 高 | 很高 | 中 | 高 |
| 跟官方 MicroDuck 相似度 | **高** | 中低 | 最高 | 高 |
| DIY 難度 | 中 | 中高 | 低 | 中高 |
| 目前建議 | **優先調查／採購候選** | 第二研究平台 | 有台灣可買時再比較 | 保留已驗證基線 |

---

# Route C：HD-1910 + Radxa Zero 3W

## 核心架構

```text
MuJoCo / RL
    │
    ▼
ONNX policy
    │
    ▼
Radxa Zero 3W (RK3566)
    │
    ├── IMU
    ├── Camera
    └── Servo bus
          │
          ▼
     HD-1910 ×15
          │
          ▼
     25 cm class MicroDuck
```

## 建議核心 BOM

> 下表是「採購規劃基線」，不是最終製造 BOM。實際數量、接頭、電源板與軸承應以選定 upstream commit 的 BOM/CAD 為準。

| 零件 | 建議規格 | 數量 | 2026-11 參考 |
|---|---|---:|---|
| Bus servo | Feetech HD-1910-C001 | 15 | 中國市場約 ¥118/顆級 |
| SBC | Radxa Zero 3W 2GB，RK3566 | 1 | 約 ¥300 級 |
| Robot HAT | Zero 3W 相容 Robot HAT | 1 | 約 ¥200–250 級 |
| IMU bridge | LSM6DSV16X / imu-to-servo 類板 | 1 | 約 ¥150–200 級 |
| microSD | 64 GB A1/A2 | 1 | 依品牌 |
| Camera | IMX219 / 相容 CSI camera | 1 | 依版本 |
| Bearings | 依 CAD BOM | 1 組 | 不可憑外觀替代 |
| Battery | 依選定電源板 | 1 組 | **未確認前不要先買** |
| Printed parts | PLA/PETG + TPU | 1 套 | 自印 |
| Fasteners / wires | M2/M2.5、servo 線、接頭 | 1 套 | 依 BOM |

### 初估 DIY 成本

以中國散件價格級距估算，主要零件約 **¥2,600–3,200**；加上列印、運費、備品與失敗成本後，預留 **¥3,500** 較保守。

這個估算只作採購比較，**不是付款預算承諾**。

---

## Route C upstream

### 1. fanhao375/microduck-replica

- Repo：https://github.com/fanhao375/microduck-replica
- 用途：優先參考實機復刻、映像、標定、控制、行走與實作記錄。
- 本 repo 後續要做的事：
  1. 固定 commit；
  2. 逐項核對 BOM；
  3. 下載並驗證 CAD / 3MF / STL；
  4. 核對 servo ID、方向、零位；
  5. 核對 power rail；
  6. 核對 ONNX observation/action dimensions；
  7. 建立台灣可買料號表。

### 2. JoyandAI/OpenMicroDuck

- Repo：https://github.com/JoyandAI/OpenMicroDuck
- 用途：BOM、HD-1910 + Zero 3W 路線與社群硬體資料交叉比對。

### 3. 官方 MicroDuck

- 官方頁：https://pollen-robotics.com/microduck/
- 官方 repo：https://github.com/pollen-robotics/microduck
- 用途：作為軟體／行為／架構基線；**不要把官方硬體視為完整 open hardware BOM。**

---

# 2026-11 市場與賣場紀錄

> 價格會變動；下列是 2026-11-09 調查時看到的市場資訊。  
> 部分連結是中國電商鏡像／聚合頁，不代表本 repo 背書賣家，也不能保證該價格 SKU 是「完整整機」。

## A. 約 ¥1,280 的 MicroDuck RK3566 復刻整機頁

### 候選 1：變色龍Ultra
- 市場頁：https://www.taouq.com/id-bz6vMAKhgtoRXP8r6ASyyMuQt6-nMYPPWFjbBaGYqRUM/
- 調查時顯示：MicroDuck / Hugging Face / RK3566 類復刻商品。
- 調查時看到低價 SKU：約 ¥1,280。
- **風險：價格低於合理散件 BOM，必須先確認不是訂金、殼件、空機、特定 SKU 或限時補貼。**

### 候選 2：中國農家小二
- 市場頁：https://www.taouq.com/id-6NkqQwmU8tGRd4DxbwtwwOSot3-4RDrrQF9YODgO9dfN/
- 調查時看到低價 SKU：約 ¥1,280。
- 相較候選 1，有看到一些歷史銷售跡象。
- **同樣必須確認內容物。**

## B. 約 ¥1,899 的 DIY 套件頁

### Box2AI
- 市場頁：https://www.taouq.com/id-ODQvJVWIzt6new3vMJiN4gcMtJ-63XvvVc6mN33rB6I9/
- 商品方向：MicroDuck / 飛特舵機版 / DIY 復刻零件。
- 調查時價格：約 ¥1,899。
- **優先確認是否包含 15 顆 HD-1910、Zero 3W、HAT、IMU、線材、五金與列印件。**

## C. 搜尋入口

- MicroDuck 相關中國市場聚合搜尋：https://www.taouq.com/w-microduck/

建議同時在淘寶／1688／拼多多使用以下關鍵字交叉搜尋：

```text
microduck RK3566
microduck HD1910
microduck 飞特舵机
microduck Zero 3W
microduck hat
imu_to_dxl LSM6DSV16X
OpenMicroDuck
```

---

# 付款前必問賣家的 10 個問題

直接複製以下文字給賣家：

```text
你好，我要做 MicroDuck 二次開發，請確認這個價格對應的 SKU：

1. 是否包含 15 顆 Feetech HD-1910-C001 舵機？
2. 是否包含 Radxa Zero 3W？RAM 容量是多少？
3. 是否包含 servo bus / Robot HAT？
4. 是否包含 IMU？IMU 型號是什麼？
5. 是否包含相機？
6. 是否包含電池與充電方式？電池規格與電壓是多少？
7. 是否包含完整 3D 列印件與五金？
8. 收到後是否可直接刷系統、校正、站立與行走？
9. 是否提供系統映像、校正工具、servo ID/方向表與 ONNX policy？
10. 請提供實際出貨內容物照片，以及目前版本的 BOM。
```

## 下單 Gate

只有在以下條件成立時，才把「¥1,280 整機」視為比 DIY 更划算：

- [ ] 15 顆 servo 全含；
- [ ] SBC 是 RK3566 / Zero 3W 類完整主控，不是空殼；
- [ ] HAT / bus interface 全含；
- [ ] IMU 全含；
- [ ] 電源方案完整；
- [ ] 機構件全含；
- [ ] 有可取得的 image / runtime；
- [ ] 有 servo calibration 方法；
- [ ] 有站立／走路實拍；
- [ ] 可以確認 SKU 與實拍是同一版本。

只要其中 2–3 項答不清楚，就退回 **散件 Route C**，不要用低價賭整機。

---

# Route D：Open Duck Mini v2

## 適用情境

如果目標是：

- 完整理解機構；
- 自己修改 CAD；
- 學 actuator characterization；
- 從 MuJoCo / PPO 到 sim-to-real；
- 需要更完整的 open-hardware 教材；

那 Open Duck Mini v2 仍然很值得做。

## 核心配置

- STS3215 ×14
- SG90 ×2
- Raspberry Pi Zero 2 W
- IMU
- Bus servo adapter
- 18650 / power subsystem
- 3D printed body

Upstream：

- https://github.com/apirrone/Open_Duck_Mini

社群／套件參考：

- Tnkr：https://tnkr.ai/open-duck-mini/open-duck-mini-v2
- NavBot：https://navbot.com/products/openduck-mini-desktop-reinforcement-learning-robot-kit
- CEREBOTO：https://cereboto.com/product/open-duck-mini-v2/

## 與 Route C 的差異

Route D 的重點不是「做一隻最像 MicroDuck 的鴨」，而是「拿到一台更透明的 legged robotics / RL 教學平台」。

因此：

- 想做 **MicroDuck replica** → Route C。
- 想做 **open robotics / RL research platform** → Route D。
- 想最快得到官方體驗 → 官方 MicroDuck。
- 想延續本 repo 已整理過、固定版本的社群方案 → Route B。

---

# 本 repo 的新推薦決策樹

```text
我要一隻 25 cm、外型與官方 MicroDuck 接近的 DIY 機器鴨
        │
        ├─ 願意自己組裝 / 校正
        │       │
        │       └── Route C：HD-1910 + Radxa Zero 3W   ← 目前優先候選
        │
        └─ 想買完整整機
                │
                ├─ 中國復刻整機：先過「10 問 + 下單 Gate」
                └─ 官方 MicroDuck：台灣可購買時重新比較

我要完整 open hardware、自己改機構、研究 RL
        │
        └── Route D：Open Duck Mini v2

我要沿用 2026-09 已整理的社群固定版本
        │
        └── Route B：帆哥 XL330 路線
```

---

# Route C 正式升級為 Build V1 前的驗收標準

目前只能稱「優先候選」，必須完成以下項目後才改成 Build V1：

1. **BOM 固定**：所有核心零件有確定型號、數量、接口。
2. **CAD 固定**：列印檔 commit / hash 可追溯。
3. **單顆 servo 測試**：通訊、ID、零位、限位、溫度與堵轉保護。
4. **單腿測試**：至少 5 個關節完成方向、零位、承重驗證。
5. **電源測試**：滿電電壓、峰值電流、brownout 與保護確認。
6. **IMU 測試**：坐標系、更新率、姿態方向正確。
7. **整機站立**：連續站立 10 分鐘無異常過熱。
8. **行走**：平地可重複走 10 次，不靠人工扶持。
9. **跌倒起身**：至少一種標準姿態可重複復原。
10. **軟體可重建**：從乾淨 SD card 依文件可重新安裝並重現。

全部通過後，再把 README 的「第一次照做」主線從 Route B 切換成 Route C。

---

# 下一步

1. 先詢問 ¥1,280 與 ¥1,899 三個賣家，取得**實拍、完整 BOM、SKU、映像與行走影片**。
2. 同時固定 `microduck-replica` 與 `OpenMicroDuck` 的 upstream commit。
3. 根據回覆決定：
   - **整機 reference hardware**；
   - **DIY 散件 Build V1**；
   - 或保留 Route B。
4. 下單前再建立新的 `Route C 採購表`，把每一個零件的實際下單連結、單價、數量與替代料號鎖死。

