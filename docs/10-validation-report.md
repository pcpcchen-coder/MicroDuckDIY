# 10｜本次文件與工具驗證紀錄

> 路線 A：官方 alpha / Radxa 參考。本次要跟帆哥製作，請改讀 [路線 B（11–14章）](11-fange-start.md)，勿混用ID、列印比例與操作命令。

日期：2026-09-23。

| 已執行檢查 | 結果 |
|---|---|
| 官方runtime、RL、HAT版本識別 | 三份commit已記於upstream-lock.json |
| robot_walk.xml逐visual geom計數 | 38種類、70實例；碰撞重複未計入 |
| 列印候選分類 | 30種類、36件；購買品模型排除 |
| 30個候選STL來源 | 全數以Git blob SHA及檔案長度核驗通過 |
| STL轉換 | 30個二進位STL可解析、座標均為有限數、成功m→mm |
| 尺寸交叉核對 | trunk_base 57×36×3mm；軸承兩種約內16外22厚4及內10外15厚3mm |
| 工具異常輸入測試 | 截斷STL會拒絕，法向量不被誤縮放 |
| repo本地文件連結 | check_docs.py通過 |

原始網路下載路徑已對bearing_roll、motor_support、trunk_base實際測試。其餘候選使用同commit官方git checkout放入本機cache後，由相同工具校驗及轉換。生成的STL保留於本機build、不納入repo；使用者可以用相同工具重建。

**尚未測試：** 網格封閉性／製造性、實際列印、板卡焊接、接線、馬達校正、OS燒錄、provision、模擬GUI、控制策略與實體行走。因此結果不能表述為「機器人已測試完成」或「零件買齊一定能走」。已確定的供電及IMU缺口列在04／09章。
