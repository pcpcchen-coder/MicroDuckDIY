# 逐件列印清單（步行版）

> 路線 A：官方 alpha / Radxa 參考。本次要跟帆哥製作，請改讀 [路線 B（11–14章）](11-fange-start.md)，勿混用ID、列印比例與操作命令。

來源版本：`cb70b792312d559a4da09064d92009079671815f`。數量由 `robot_walk.xml` 的 visual geom 計算；碰撞模型不重複計數。這是模型衍生清單，尚未完成實體試裝，不是原廠製造 BOM。

共 **30 種、36 件列印候選**，其中 4 件建議先試 TPU，其餘 32 件先用硬質材料試作。材料建議不是官方指定。所有尺寸、孔位與壁厚仍需檢查。

| 檔名（固定版本下載） | 數量 | 網格包圍盒 mm | 建議試作材料 |
|---|---:|---|---|
| [ankle_left.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/ankle_left.stl) | 1 | 39.4891 × 36.5 × 25.5 | PETG／PLA+ |
| [ankle_right.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/ankle_right.stl) | 1 | 39.4891 × 36.5 × 25.5 | PETG／PLA+ |
| [banana_pcb_locker.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/banana_pcb_locker.stl) | 1 | 54.0501 × 3.8 × 6.6524 | PETG／PLA+ |
| [bearing_roll.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/bearing_roll.stl) | 2 | 23.0 × 3.0 × 40.0 | PETG／PLA+ |
| [bottom_head_shell.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/bottom_head_shell.stl) | 1 | 91.763 × 116.7483 × 20.1363 | PETG／PLA+ |
| [face_part.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/face_part.stl) | 1 | 87.6507 × 12.5 × 44.6265 | PETG／PLA+ |
| [foot_left.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/foot_left.stl) | 1 | 40.0855 × 54.0 × 16.909 | PETG／PLA+ |
| [foot_right.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/foot_right.stl) | 1 | 40.0855 × 54.0 × 16.909 | PETG／PLA+ |
| [hip_l.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/hip_l.stl) | 2 | 32.4501 × 34.5 × 19.0 | PETG／PLA+ |
| [jaw.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/jaw.stl) | 1 | 91.4158 × 68.7105 × 29.4477 | PETG／PLA+ |
| [jaw_soft.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/jaw_soft.stl) | 1 | 87.6737 × 32.2339 × 8.4376 | TPU 95A |
| [left_shell.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/left_shell.stl) | 1 | 33.7145 × 80.8901 × 41.6905 | PETG／PLA+ |
| [leg.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/leg.stl) | 2 | 7.95 × 20.0 × 58.0 | PETG／PLA+ |
| [m12_lens_holder.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/m12_lens_holder.stl) | 1 | 24.0 × 14.8 × 16.0 | PETG／PLA+ |
| [motor_support.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/motor_support.stl) | 1 | 73.5 × 54.2 × 18.8 | PETG／PLA+ |
| [neck.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/neck.stl) | 2 | 2.0 × 20.0 × 11.0 | PETG／PLA+ |
| [neck_pitch.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/neck_pitch.stl) | 1 | 35.0 × 18.0 × 27.6931 | PETG／PLA+ |
| [noenoeil.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/noenoeil.stl) | 1 | 30.0 × 9.5 × 30.0 | PETG／PLA+ |
| [power_support.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/power_support.stl) | 1 | 54.5 × 17.0 × 83.4898 | PETG／PLA+ |
| [right_shell.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/right_shell.stl) | 1 | 31.7645 × 80.8979 × 41.6927 | PETG／PLA+ |
| [soft_mouth_top.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/soft_mouth_top.stl) | 1 | 87.822 × 32.5651 × 3.2762 | TPU 95A |
| [sole_left.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/sole_left.stl) | 1 | 41.0985 × 54.0 × 12.9074 | TPU 95A |
| [sole_right.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/sole_right.stl) | 1 | 41.0987 × 54.0 × 12.9076 | TPU 95A |
| [top_head_shell.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/top_head_shell.stl) | 1 | 91.7595 × 122.69 × 46.3361 | PETG／PLA+ |
| [trunk_base.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/trunk_base.stl) | 1 | 57.0 × 36.0 × 3.0 | PETG／PLA+ |
| [upper_leg_left.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/upper_leg_left.stl) | 1 | 28.0 × 47.6594 × 60.9966 | PETG／PLA+ |
| [upper_leg_right.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/upper_leg_right.stl) | 1 | 28.0 × 47.6594 × 60.9966 | PETG／PLA+ |
| [upper_leg_rigidity_plate.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/upper_leg_rigidity_plate.stl) | 2 | 1.0 × 44.9965 × 58.0577 | PETG／PLA+ |
| [yaw2roll.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/yaw2roll.stl) | 2 | 23.0 × 25.8 × 20.5 | PETG／PLA+ |
| [yaw_roll_motion.stl](https://raw.githubusercontent.com/pollen-robotics/microduck_rl/cb70b792312d559a4da09064d92009079671815f/src/mjlab_microduck/robot/microduck/assets/yaw_roll_motion.stl) | 1 | 34.0 × 35.9 × 22.5 | PETG／PLA+ |

## 不應當成列印件的模型

| 模型名稱 | 模型數量 | 處理 |
|---|---:|---|
| `elec_rpi_robot_hat_pcb` | 1 | PCB＋SMT；不能列印代替 |
| `lens` | 1 | 購買鏡頭／相機模組，光學件不能以不透明列印件取代 |
| `np_f970` | 1 | 僅為電池佔位模型；runtime 記載 NP-F550，不可按檔名買 F970 |
| `pcb__raspberry_pi_zero_2_w` | 1 | 僅為主板幾何參考；目前 runtime 支援 Radxa Zero 3W |
| `seeed_bearing__configuration__22x16x4` | 11 | 購買金屬軸承；檔名指向外徑22／內徑16／厚4 mm，網格也量得相同尺寸，仍須試裝 |
| `seeed_bearing__configuration_default` | 3 | 購買軸承；網格量測內10×外15×厚3 mm；先買樣品試裝，非原廠料號 |
| `speaker` | 1 | 購買喇叭；依空間與音訊電路確認阻抗功率 |
| `xl330` | 15 | 購買馬達；完整子型號須確認 |

## 本次不列印

- `ankle_l_v1`、`ankle_r_v1`：不是選定步行模型的 ankle_left/right，勿混用。
- `rim`、`tire`、`roller_blade`：輪滑選配，第一版不納入；須另讀 roller 模型計數。
- `.part`：Onshape 來源中繼資料，並非切片軟體零件檔。
- 相機、IMU、螺絲、線材不能因模型未列出就省略。

## 小批量試印順序

1. `bearing_roll` 1 件＋`motor_support` 1 件：軸承與馬達孔位／軸配合。
2. 左腳：`hip_l`、`yaw2roll`、`upper_leg_left`、`upper_leg_rigidity_plate`、`leg`、`ankle_left`、`foot_left`、`sole_left` 各 1 件。
3. 通過試裝後补右腳、軀幹及頸部。
4. 相機、板卡與線路位置確定後，最後列印頭殼及臉部。

完整切片、材料與驗收見 [列印教學](03-printing.md)。

## 幾何量測註記

包圍盒來自固定版本二進位STL，已轉毫米，不是含支撐的擺盤尺寸。軸承另以XY中心到頂點的最小／最大半徑估內外徑：22×16×4型為內16、外22、厚4 mm；default型為內10、外15、厚3 mm。以上為模型尺寸推導，採購前仍確認公差、密封型式與真實配合。喇叭佔位模型約35×25×7 mm，不足以判斷阻抗／功率。
