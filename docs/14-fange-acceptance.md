# 14｜帆哥路線：验收、缺口與施工紀錄

日期2026-09-23，來源版本見 [11章](11-fange-start.md)。本章分開記「本次已查驗」與「George待實測」，不得用程式碼檢查代替實機通過。

## 本次已查驗

| 項目 | 證據／結果 |
|---|---|
| 來源 | clone固定commit 49678215d0b40529522772a40c06c216390449dd |
| ID與校正常數 | constants.py：ID1–14、膝offset ±45°、IMU mount quaternion |
| 控制行為 | main.py啟動即扭矩ON與neutral；scheduler正常退出cleanup卸力；stop.py傳送停止請求 |
| USB橋接 | robot_controller.py優先OpenRB by-id、1Mbps；原廠OpenRB手冊確認橋接sketch |
| IMU | imu_reader.py、observer.py、imu_orientation_check.py；policy和body診斷使用不同frame／符號處理 |
| 3MF | SHA256已記錄，ZIP/XML可讀、mm、67 build items、5盤65實例、2未分盤idle_horn |
| ONNX | onnx.checker通過；CPU ONNX Runtime 1.30.0實際載入；obs[1,51]→actions[1,14]；零輸入輸出全為有限值 |
| 模型metadata | 14個joint_names順序吻合constants、default_joint_pos14筆、action_scale1.0 |
| 文件 | 本repo連結及原官方manifest檢查；新增來源lock及3MF盤點一致性檢查 |

未完成：3MF切片GUI與製造公差、模型的完整物理仿真、映像下載／刷寫、Pi ARM依賴安裝、板卡接線、電池峰值、實機組裝及步行。ONNX測試在開發環境CPU執行，不是Pi上50Hz效能證明。

## 已知差異及處理

| 項目 | 鎖定版觀察 | 實作處理／放行條件 |
|---|---|---|
| README的CAD路徑 | microduck/cad不存在 | 改用根目錄3MF，依物件ID對影片，缺件不自行混入官方版本 |
| 映像來源版本 | image.v1與HEAD關係未驗證 | hash核對、備份、源碼／模型比對，Pi上重做接口檢查 |
| nominal6V | 電池SKU／滿電範圍未交代 | 5V台架起步，整機電源按12章實測選型 |
| BAM_VIN=7.5 | constants仍有7.5V建模／電流代理假設 | 不作硬體額定；降低實際供電後需重驗動態，不能僅改此值聲稱模型已重訓 |
| 電流保護 | observe_current預設False，使用位置誤差代理；閾值15A | 外部量測及硬體保護必須獨立，不把估算當保險絲 |
| IMU過期 | scheduler對age超過dt顯示警告，未見該分支強制停止 | 初測全程監看，出现stale即停止；自動失效停機驗證前禁止無人運行 |
| 摔倒處理 | walk.step重力判斷可能直接return | 不等於扭矩OFF，不用摔倒測試代替緊急停機 |
| 啟動例外 | main啟用扭矩在scheduler正常cleanup之前；main的finally主要刪PID | 啟動錯誤立即實體斷馬達電源；軟體stop不是保證卸力 |
| 清理例外 | shutdown/input停止與bus卸力可能各自失敗 | 每次測q後確認實際卸力，不只看終端已退出 |
| 初始速度 | 上游上限前0.7m/s、後0.5m/s，原地轉3rad/s | 初測按13章降低命令上限，記錄変更 |
| 五金／軸承 | 未有逐件可確認的製造BOM | 先試裝後補單；不要把3MF盤名「軸承」當額定承載證明 |

本次只新增指引，沒有偷偷修改上游控制程式。若需要無人／長時間運行，另需實作並測試IMU invalid/stale停機、初始化全程try/finally卸力、通訊／手柄失聯歸零與實體電源保護；不是調一個常數就算完成。有人監看的支撐試驗可以先進行，未解除項目要如實記錄。

## George的验收表

以下秒數／距離／誤差是本專案初測建議，不是原廠保證；第一輪全部為「未測」。

| 關卡 | 通過條件 | 實測／日期／證據 |
|---|---|---|
| B0版本 | Git commit、3MF、ONNX及image hash齊全 | 未測 |
| B1電源 | 主控5V、舵機3.7–6V內且有瞬態餘量；極性、共地、斷電開關正確 | 未測 |
| B1單軸 | Wizard讀寫、唯一ID、1Mbps、小角度正反轉及卸力 | 未測 |
| B1IMU | I²C可讀、valid、靜態gyro近0、無持續stale | 未測 |
| B2試印 | 舵機座／舵盤／惰輪配合無裂紋、不鬆動、可自由轉 | 未測 |
| B3單腿 | 5軸方向與零位逐項通過，無機構及線束干涉 | 未測 |
| B4整機 | 14軸唯一ID，膝offset與實物一致，板卡固定牢靠 | 未測 |
| B4模型 | Pi上51→14、joint_names順序與hash通過 | 未測 |
| B4IMU方向 | body-frame直立重力近[0,0,-1]；前後左右傾方向正確 | 未測 |
| B5neutral | 有支撐啟動不撞限位／無突跳，q後確認卸力 | 未測 |
| B5零命令 | walk零命令60秒，無持續抖動、異常熱、壓降重啟 | 未測 |
| B5停機 | x歸零、q退出、stop.py、實體斷馬達電源各自測試 | 未測 |
| B5失聯 | 支撐下確認手柄／通訊中斷不持續移動；不合格不得自由行走 | 未測 |
| B6慢行 | 低速前進2m、後退、左右轉及停穩；記錄跌倒次數 | 未測 |
| B6供電 | 帶載最低／最高電壓、峰值電流、溫升及Pi狀態均記錄 | 未測 |
| B6重複性 | 相同場地連續3次通過，而非只保留最好的一次影片 | 未測 |
| 手柄 | START/A/B/雙扳機、失聯及Wi-Fi恢復皆實測 | 未測 |

測試時先關機接妥線，不在帶電狀態拔IMU/舵機測故障。失效測試優先用可控軟體故障注入或停止輸入來源，支撐機體並保留實體斷電。電池充電先與機器人斷開。

## 施工記錄模板（複製後填）

```text
日期／操作者：
路線：B / FanGe
上游commit：49678215d0b40529522772a40c06c216390449dd
本地校正commit：
SD image SHA256／OS／Python／ONNX Runtime：
ONNX SHA256：
電池型號／化學體系／容量／滿電電壓：
舵機供電實測min/max／峰值電流／量測方法：
Pi 5V實測／是否曾重啟：
整機重量／電池重量／IMU安裝照片：
測試地面／命令／持續時間：
通過項目／失敗時間點／影片位置：
下次只改哪一件事：
```

| ID | 舵盤基準照片 | sign | 軟體offset rad | EEPROM Homing Offset | neutral實物姿態 | 正反方向 | 結果 |
|---|---|---|---|---|---|---|---|
| 待填1–14 | 待填 | 待填 | 待填 | 待填 | 待填 | 待填 | 未測 |

| 盤號/object ID | 用途／裝配位置 | 材料／層高／壁數 | 實印數量 | 關鍵尺寸 | 螺絲牙型長度 | 試裝結果 |
|---|---|---|---|---|---|---|
| 待填 | 待填 | 待填 | 待填 | 待填 | 待填 | 未測 |

## 原始查核入口

- [固定版源碼](https://github.com/AI-FanGe/Microduck-build-tutorial/tree/49678215d0b40529522772a40c06c216390449dd)：上表提到的檔案均在microduck/src下。
- [列印缺件Issue 6](https://github.com/AI-FanGe/Microduck-build-tutorial/issues/6)、[STEP問題Issue 9](https://github.com/AI-FanGe/Microduck-build-tutorial/issues/9)：使用者回報不等於作者已確認；本次以實際tree與3MF為準。
- [XL330原廠規格](https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/)、[OpenRB接線與橋接](https://emanual.robotis.com/docs/en/parts/controller/openrb-150/)。
- X貼文是發現來源；可重現的工程依據以固定源碼／模型／原廠手冊及你的實測記錄為準。「全網第一」未獨立證實，也不影響本次選型。
