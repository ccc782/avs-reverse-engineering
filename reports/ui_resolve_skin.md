# Fusion 皮肤包解剖（DaVinci Resolve 21.2 内嵌 Fusion）

- 包体：`Fusion.fuskin`，22.1 MB
- 条目：**7201**（PNG 7190 / skin 3 / 其它 8）
- HiDPI 变体（@2x/@3x）：**3444** 个，占 48%

## 一、顶层分区（资产按 UI 区域组织）

| 分区 | 资产数 |
| --- | ---: |
| `Tools` | 4376 |
| `Tracker` | 350 |
| `ViewStrip` | 324 |
| `Icons` | 282 |
| `Polyline` | 222 |
| `Text` | 168 |
| `Spline` | 166 |
| `Transport` | 158 |
| `Paint` | 148 |
| `Controls` | 110 |
| `Color` | 86 |
| `Views` | 82 |
| `FlagMarkers` | 68 |
| `Arrows` | 52 |
| `TimeSlider` | 50 |
| `Strokes` | 48 |
| `MultiText` | 40 |
| `Mesh` | 40 |
| `PointCloud` | 40 |
| `Slider` | 36 |

## 二、状态资产（交互态是切图，不是代码）

| 状态 | 资产数 |
| --- | ---: |
| active | 1474 |
| hover | 1250 |
| light | 196 |
| mask | 148 |
| disabled | 110 |
| selected | 18 |
| focus | 18 |
| dark | 10 |

## 三、`Fusion.skin`（Fu80 / Fusion 8，282 KB）

- 颜色令牌：**38** 个（含别名 42）
- 尺寸常量：**9** 个
- 控件类别：**107** 个

### 调色板（前 40）

| 令牌 | HEX | RGBA |
| --- | --- | --- |
| `DropShipGray` | `#303039` | [48, 48, 57] / a=255 |
| `PoseidonGray` | `#2f3036` | [47, 48, 54] / a=255 |
| `DolphinGray` | `#37393e` | [55, 57, 62] / a=255 |
| `NewtGray` | `#28292e` | [40, 41, 46] / a=255 |
| `JaguarGray` | `#24242a` | [36, 36, 42] / a=255 |
| `JellyFishGray` | `#43474d` | [67, 71, 77] / a=255 |
| `JellyFishGray40` | `#43474d` | [67, 71, 77] / a=102 |
| `JellyFishGray70` | `#43474d` | [67, 71, 77] / a=178 |
| `OctopusGray` | `#17181a` | [23, 24, 26] / a=255 |
| `OctopusGray40` | `#17181a` | [23, 24, 26] / a=102 |
| `PenguinGray` | `#28282e` | [40, 40, 46] / a=255 |
| `PlanktonGray` | `#616770` | [97, 103, 112] / a=255 |
| `SquidGray` | `#ababab` | [171, 171, 171] / a=255 |
| `SquidGray40` | `#ababab` | [171, 171, 171] / a=102 |
| `White` | `#ffffff` | [255, 255, 255] / a=255 |
| `White40` | `#ffffff` | [255, 255, 255] / a=102 |
| `Transparent` | `#000000` | [0, 0, 0] / a=0 |
| `OrcaGray` | `#212126` | [33, 33, 38] / a=255 |
| `OrcaGray40` | `#212126` | [33, 33, 38] / a=102 |
| `SealGray50` | `#2c2d32` | [44, 45, 50] / a=255 |
| `ThunderstormGray` | `#1f1f1f` | [31, 31, 31] / a=255 |
| `ThunderstormGray40` | `#1f1f1f` | [31, 31, 31] / a=102 |
| `LicoriceGray` | `#070707` | [7, 7, 7] / a=255 |
| `LicoriceGray40` | `#070707` | [7, 7, 7] / a=102 |
| `StarfishGray` | `#2d2f33` | [45, 47, 51] / a=255 |
| `NautilusGray` | `#252525` | [37, 37, 37] / a=255 |
| `SmokeGray` | `#929292` | [146, 146, 146] / a=255 |
| `SmokeGray40` | `#929292` | [146, 146, 146] / a=102 |
| `TintGray` | `#090909` | [9, 9, 9] / a=255 |
| `TintGray40` | `#090909` | [9, 9, 9] / a=102 |
| `CoralRed` | `#e64b3d` | [230, 75, 61] / a=255 |
| `WinterSkyGray` | `#474747` | [71, 71, 71] / a=255 |
| `ParakeetGreen` | `#66dd27` | [102, 221, 39] / a=255 |
| `BonesGray` | `#d0d0d0` | [208, 208, 208] / a=255 |
| `BonesGray40` | `#d0d0d0` | [208, 208, 208] / a=102 |
| `TabButtonGray` | `#222226` | [34, 34, 38] / a=255 |
| `TabButtonGray40` | `#222226` | [34, 34, 38] / a=102 |
| `HalfCoralRed` | `#73261f` | [115, 38, 31] / a=255 |

### 尺寸指标（前 40）

| 常量 | 值 |
| --- | ---: |
| `LabelW` | 132 |
| `ResetW` | 40 |
| `ReferenceW` | 400 |
| `ButtonH` | 22 |
| `CheckBoxH` | 17 |
| `ComboH` | 20 |
| `EditW` | 55 |
| `EditH` | 20 |
| `LabelH` | 16 |

### 控件类别树

```
System
Controls
Style
Button
Combo
CheckBox
Progress
RadioButton
ScrollBar
Spin
Tree
Button
CheckBox
CheckList
Clip
Color
ColorField
ColorRanges
ColorSuppression
ColorWheel
Combo
File
Fontfile
Gamma
Gamut
Gradient
Histogram
Image
Inspector
Label
Levels
LevelsOutput
Library
List
Log
LUT
Matrix
MultiButton
Nest
Offset
Range
Screw
ScriptValList
Slider
Separator
Spacer
Tabs
TextEdit
Titles
TrackerPattern
Other
Hourglass
AudioDisplay
Preferences
Appearance
TimeSlider
Transport
Flow
Tiles
Bins
StudioPlayer
SplineEditor
TimeLine
Views
Toolbar
Layoutbar
GainGamma
Tabs
Debug
ToolControl
Toolbars
ScriptView
ConsoleView
EffectsLibraryView
StatusBar
Icons
Guides
NGon
Rotation
Outline
Text
Control
Anchor
Emphasis
MultiText
Anchor
Alignment
Justification
AlignLayers
Emphasis
Indentation
CameraTracker
Polyline
Spline
Paint
Brush
Apply
Mesh
Tracker
Pattern
MagicMask
SurfaceTracker
Positioner
Transform
PointCloud
Tools
ViewStrip
```

## 三、`Neutral.skin`（Ne80 / Fusion 8，7 KB）

- 颜色令牌：**26** 个（含别名 26）
- 尺寸常量：**0** 个
- 控件类别：**29** 个

### 调色板（前 40）

| 令牌 | HEX | RGBA |
| --- | --- | --- |
| `DropShipGray` | `#303030` | [48, 48, 48] / a=255 |
| `PoseidonGray` | `#323232` | [50, 50, 50] / a=255 |
| `DolphinGray` | `#393939` | [57, 57, 57] / a=255 |
| `NewtGray` | `#292929` | [41, 41, 41] / a=255 |
| `JaguarGray` | `#242424` | [36, 36, 36] / a=255 |
| `JellyFishGray` | `#474747` | [71, 71, 71] / a=255 |
| `JellyFishGray40` | `#474747` | [71, 71, 71] / a=102 |
| `OctopusGray` | `#181818` | [24, 24, 24] / a=255 |
| `OctopusGray40` | `#181818` | [24, 24, 24] / a=102 |
| `PenguinGray` | `#282828` | [40, 40, 40] / a=255 |
| `PlanktonGray` | `#676767` | [103, 103, 103] / a=255 |
| `SquidGray` | `#ababab` | [171, 171, 171] / a=255 |
| `SquidGray40` | `#ababab` | [171, 171, 171] / a=102 |
| `White` | `#ffffff` | [255, 255, 255] / a=255 |
| `White40` | `#ffffff` | [255, 255, 255] / a=102 |
| `Transparent` | `#000000` | [0, 0, 0] / a=0 |
| `OrcaGray` | `#212121` | [33, 33, 33] / a=255 |
| `OrcaGray40` | `#212121` | [33, 33, 33] / a=102 |
| `SealGray50` | `#2d2d2d` | [45, 45, 45] / a=255 |
| `MilkGray` | `#f1f1f1` | [241, 241, 241] / a=255 |
| `StarfishGray` | `#2f2f2f` | [47, 47, 47] / a=255 |
| `SmokeGray` | `#929292` | [146, 146, 146] / a=255 |
| `SmokeGray40` | `#929292` | [146, 146, 146] / a=102 |
| `CoralRed` | `#e64b3d` | [230, 75, 61] / a=255 |
| `TabButtonGray` | `#222222` | [34, 34, 34] / a=255 |
| `TabButtonGray40` | `#222222` | [34, 34, 34] / a=102 |

### 控件类别树

```
System
Controls
Style
Button
Combo
Tree
ColorRanges
Gamma
Log
MultiButton
Range
Slider
Screw
Tabs
TrackerPattern
Other
TimeSlider
Flow
Bins
SplineEditor
TimeLine
Views
Toolbar
Layoutbar
Toolbars
ScriptView
EffectsLibraryView
StatusBar
ViewStrip
```

## 三、`Tablet.skin`（Tb80 / Fusion 8，43 KB）

- 颜色令牌：**0** 个（含别名 0）
- 尺寸常量：**9** 个
- 控件类别：**40** 个


### 尺寸指标（前 40）

| 常量 | 值 |
| --- | ---: |
| `LabelW` | 132 |
| `ResetW` | 60 |
| `ReferenceW` | 460 |
| `ButtonH` | 26 |
| `CheckBoxH` | 17 |
| `ComboH` | 24 |
| `EditW` | 55 |
| `EditH` | 24 |
| `LabelH` | 16 |

### 控件类别树

```
Controls
Button
CheckBox
CheckList
Clip
Color
ColorField
ColorRanges
ColorSuppression
ColorWheel
Combo
File
Fontfile
Gamma
Gamut
Gradient
Histogram
Image
Label
Levels
LevelsOutput
Library
List
Log
LUT
Matrix
MultiButton
Nest
Offset
Range
Screw
ScriptValList
Slider
Separator
Spacer
TextEdit
Titles
TrackerPattern
Icons
Text
```