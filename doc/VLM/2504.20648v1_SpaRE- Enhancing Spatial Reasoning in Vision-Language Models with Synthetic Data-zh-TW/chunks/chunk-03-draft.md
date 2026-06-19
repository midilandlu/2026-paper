## **附錄 H：基礎空間關係分類法**

為了解構這些複雜的空間感，我們參考了 Liu 等人 (2023a) 的做法，建立了一套基礎的「空間關係分類架構」（**用來系統性分類和整理物體間各種空間關係的框架**）。我們把這些空間關係分門別類，從粗放的大方向到非常精細的關鍵字一網打盡。有了這套工具，我們就能像拿著顯微鏡一樣，好好分析視覺問答（**讓 AI 根據影像內容回答人類提問的任務**，簡稱 VQA）資料集裡，各種空間關係到底是如何分佈和被使用的。

在表 10 中，我們整理了這套分類法的核心統計數據。我們把每一個主要的「空間關係 (SR)」與其對應的「關鍵字 (K)」配對，藉此區分出粗略的宏觀類別與具體的微觀特例。在表格裡，你還能看到每個關鍵字在其空間關係群組中的佔比 (K %)、該空間關係在整個資料集中的總佔比 (SR %)，以及它在各個資料集之間的相對出現頻率。

我們所分析的資料集清單已列於表 2 中。這套分類法為空間關係的解讀建立了標準，也為視覺問答 (VQA) 及相關任務中的空間推理，提供了一個更系統化、結構化的研究方法。

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0015-00.png)

**問題：** 吹風機正朝向遠離人的方向。對還是錯？

|模型|預測結果|是否正確？|
|---|---|---|
|SpaRE-2B|True（對）|✔|
|Qwen2VL-2B|False（錯）|✘|
|InternVL2-2B|No（否）|✘|
|GPT-4o-mini|False（錯）|✘|

(a) 來自 VSR（**視覺空間關係基準測試**）的範例 1

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0015-04.png)

**問題：** 這個人正朝向哪個物體：筆記型電腦還是電視？

|模型|回答|是否正確？|
|---|---|---|
|SpaRE-2B|Laptop（筆記型電腦）|✔|
|Qwen2VL-2B|TV（電視）|✘|
|InternVL2-2B|TV（電視）|✘|
|GPT-4o-mini|TV（電視）|✘|

(b) 來自 3DSRBench（**三維空間關係基準測試**）的範例 2

圖 4：在我們的定性分析（**藉由具體案例來深入評估模型回答品質與推理邏輯的研究方法**）中，每個子圖都包含了一張影像、一個相對應的問題、不同模型的回答，以及它們的答案是否正確（✔ 或 ✘）。

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0016-00.png)

這是一根乳白色石柱的低角度特寫畫面，上面雕刻著埃及風格的插圖和象形文字。畫面中央的浮雕插圖描繪了一個人，他_右手裡_拿著一根頂端有著菱形物體的長杖，同時將長杖的底部立在地上；而他的_左手裡_則拿著一個_在其之上_有著彎曲手柄的十字形物體。這個人正面朝_影像的左側_，右腳在前，左腳在後。_在此人的左側_，有一個生物正坐在小階梯_之上_。這個生物坐著，雙膝彎曲，雙腳放_在身體前方_，其雙腳和臀部都_觸碰著表面_，而雙手則置於_膝頭上_。它戴著一個_在後方_很長的頭飾，頭飾_頂端_放著一個圓形物體。這個生物看起來不像人類，坐姿也不像人類。在這個插圖的_周圍與上方_，石柱上雕刻著象形文字和各種形狀。

圖 5：來自 DOCCI 的範例。DOCCI 是我們用來提取問答對的超詳細影像描述（hyper-detailed image-captioning，**提供極為詳盡細緻之畫面細節說明的圖像標註**）資料集之一。我們對空間相關的詞彙進行了_斜體_標示以示強調。

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0017-00.png)

這張照片拍的是一棟建築物的室外。那裡有一頂帳篷。帳篷_上_有一塊看板和一條橫幅。在帳篷_下_有椅子、人和一些其他東西。在_背景_中有一棟建築。天空非常晴朗。

圖 6：來自本地化敘事（**Localized Narratives**）的範例。Localized Narratives 是我們用來提取問答對的超詳細影像描述資料集之一。我們對空間相關的詞彙進行了_斜體_標示以示強調。

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0017-03.png)

在一個陽光明媚的日子裡，這張照片捕捉到了一輛露營車內溫馨舒適的景象。畫面中最醒目的是一個卡座式、呈 U 形或 C 形的座位區，上面鋪著淡藍綠色或薄荷綠色的坐墊，並點綴著色彩繽紛的抱枕。這個座位區_環繞著_一張呈黃褐色的矩形桌子，桌子是由一根鍍鉻金屬支柱所_支撐_。桌子_上方_放著一個綠色花瓶，裡面插滿了紅色的花朵，每朵花都帶有明顯的黃色花芯。露營車內裝飾著芥末黃色圓點圖案的窗簾，框架著窗戶。透過窗戶可以看到外面的紅磚，這暗示了附近有一棟建築物。_往露營車的後方_，有一個用藍綠色窗簾隔開的區域，那裡很可能是臥室，裡面有一張圓形床，上面鋪著淡綠色與白色相間的粉彩薄被。露營車的上方_沿著_車身裝有一排白色儲物櫃，提供了充足的收納空間。一張帶有多彩方格的鉤針編織毯隨意地搭在其中一張長椅上，暗示著車主精湛的針線活手藝。在深褐色的木地板_上_，這個雖然有些狹窄卻極具吸引力的空間，既強調了舒適感，也展現了在這個精緻移動小屋_內_對空間的實用規劃。

圖 7：來自 PixMo-Cap 的範例。PixMo-Cap 是我們用來提取問答對的超詳細影像描述資料集之一。我們對空間相關的詞彙進行了_斜體_標示以示強調。

表 10：我們的空間關係分類法展示了在選定視覺問答 (VQA) 資料集裡觀察到的空間關係種類、子關鍵字，以及它們的百分比與頻率。所涵蓋的資料集詳見表 2。
- **空間關係 (SR)**：高階的關係類別。
- **關鍵字 (K)**：代表該空間關係的子關鍵字。
- **關鍵字佔比 (K %)**：該子關鍵字在所屬空間關係群組所有關鍵字中的百分比。
- **空間關係佔比 (SR %)**：該高階空間關係在整個資料集中的百分比。
- **資料集頻率 (Dataset freq.)**：該空間關係在各個資料集中的相對出現頻率（以 % 表示）。

|空間關係|關鍵字|K (%)|SR (%)|
|---|---|---|---|
||left|7.41|19.28|
||at the left|1.27||
||on the left|1.24||
|左 (left)|to the left of|3.04||
||left of|3.75||
||left side of|1.31||
||at the left side of|1.25||
||right|8.04|21.65|
||at the right|1.42||
||on the right|1.75||
|右 (right)|to the right of|3.40||
||right of|4.03||
||right side of|1.59||
||at the right side of|1.42||
||above|1.64|2.35|
||directly above|≈0.00||
||over|0.37||
|上方 (above)|over the|0.34||
||upward of|≈0.00||
||overlying|≈0.00||
||on|9.29|13.04|
||on top of|1.72||
||atop|≈0.00||
|在……上 (on)|on the top of|0.04||
||on top|1.72||
||lying on|0.04||
||sitting on|0.22||
||positioned on|≈0.00||
||placed on|≈0.00||
||overlaying on|≈0.00||
||below|1.42|8.32|
||under|1.98||
||beneath|1.29||
|下方 (below)|directly below|≈0.00||
||down|0.13||
||underneath|0.04||
||under the|1.98||
||below the|1.40||
||lower|0.06||
||down from|≈0.00||
||front|3.66|10.60|
||in front of|3.40||
||in the front of|0.02||
|前方 (front)|directly in front of|≈0.00||
||front of|3.51||
||confronting|≈0.00||

續下頁

|**表 10（續）**|**表 10（續）**|||
|---|---|---|---|
|空間關係 (SR)|關鍵字 (K)|K %|SR %|
||back|0.30|3.75|
||behind|3.04||
||at the back of|0.19||
|後方 (back)|in back of|≈0.00||
||directly behind|≈0.00||
||rear of|≈0.00||
||backing onto|≈0.00||
||back of|0.22||
||near|0.75|1.12|
||near to|0.02||
||nearby|0.02||
|鄰近 (near_close)|close to|0.32||
||close by|≈0.00||
||in proximity to|≈0.00||
||within sight of|≈0.00||
||far|1.08|2.07|
||far from|0.28||
||far away from|0.71||
|遙遠 (far)|farther than|≈0.00||
||distant from|≈0.00||
||remote from|≈0.00||
||inside|0.56|7.97|
||within|0.15||
||inside of|0.04||
|內部/之內 (inside_within)|contained in|≈0.00||
||enclosed by|≈0.00||
||in|7.22||
||outside|0.09|0.17|
||out of|0.09||
|外部/之外 (outside)|outer<br>outside of|≈0.00<br>≈0.00||
||outlying|≈0.00||
||next to|1.79|3.60|
||beside|0.62||
||adjacent|0.34||
||adjacent to|0.34||
|旁邊/相鄰 (next_to_beside_adjacent)|by<br>at the side of|0.19<br>0.30||
||by the side of|≈0.00||
||side by side with|≈0.00||
||contiguous with|≈0.00||
||opposite|0.09|0.17|
||opposite to|0.09||
|對面 (opposite)|opposite side of<br>diagonally across|≈0.00<br>≈0.00||
||opposite from|≈0.00||
||opposed to|≈0.00||
||facing|0.62|0.62|
||facing toward|≈0.00||
|朝向 (facing)|looking at|≈0.00||
||confronting|≈0.00||
||in view of|≈0.00||
||parallel to|0.13|0.13|
|平行於 (parallel_to)|in line with<br>aligned with|≈0.00<br>≈0.00||
||running parallel to|≈0.00||

續下頁

**表 10（續）**

|空間關係 (SR)|關鍵字 (K)|K %|SR %|
|---|---|---|---|
||perpendicular to|0.15|0.15|
|垂直於 (perpendicular_to)|perpendicular with<br>orthogonal to|≈0.00<br>≈0.00||
||at right angles to|≈0.00||
||toward|0.15|0.15|
||towards|≈0.00||
||proceeding to|≈0.00||
|向著 (toward_towards)|progressing toward|≈0.00||
||moving toward|≈0.00||
||heading toward|≈0.00||
||approaching|≈0.00||
||away|1.40|2.80|
||away from|1.40||
||moving away from|≈0.00||
|遠離 (away_from)|departing from|≈0.00||
||receding from|≈0.00||
||withdrawing from|≈0.00||
||retreating from|≈0.00||
||between|0.02|0.02|
||among|≈0.00||
|之間 (between)|amid<br>amidst|≈0.00<br>≈0.00||
||amongst|≈0.00||
||betwixt|≈0.00||
||through|0.02|0.04|
||passing through|≈0.00||
||traversing|≈0.00||
|穿過 (through)|transiting|≈0.00||
||running through|≈0.00||
||crossing|0.02||
||piercing|≈0.00||
||around|0.17|0.22|
||circling|≈0.00||
||encircling|≈0.00||
||surrounding|0.04||
|周圍 (around)|enveloped by|≈0.00||
||enclosing|≈0.00||
||skirting|≈0.00||
||encompassing|≈0.00||
||encircled by|≈0.00||
||overlapping|≈0.00|≈0.00|
||overlapping with|≈0.00||
||intersecting with|≈0.00||
|重疊/相交 (overlapping_intersecting)|interlacing with<br>intertwined with|≈0.00<br>≈0.00||
||interlocking|≈0.00||
||crisscrossing|≈0.00||
||interlaced with|≈0.00||
||connected to|≈0.00|≈0.00|
||connected with|≈0.00||
||attached to|≈0.00||
||attached with|≈0.00||
|連接/附著 (connected_attached)|linked to|≈0.00||
||joined to|≈0.00||
||contiguous with|≈0.00||
||linked with|≈0.00||
||adjoined to|≈0.00||

續下頁

||**表 10（續）**|||
|---|---|---|---|
|空間關係 (SR)|關鍵字 (K)|K %|SR %|
||at the edge of|0.65|0.65|
||at the corner of|≈0.00||
|邊界內 (within_boundary)|on the edge of<br>bordering|≈0.00<br>≈0.00||
||edged by|≈0.00||
||at the boundary of|≈0.00||
||north of|≈0.00|≈0.00|
||south of|≈0.00||
||east of|≈0.00||
|基本方位/羅盤方向 (cardinal_directions)|west of<br>northeast of|≈0.00<br>≈0.00||
||northwest of|≈0.00||
||southeast of|≈0.00||
||southwest of|≈0.00||
||center of|0.04|0.60|
||at the center of|≈0.00||
||in the center of|0.04||
|中心位置 (central_position)|middle of|0.26||
||in the middle of|0.26||
||in the midst of|≈0.00||
||amidst|≈0.00||
||part of|0.34|0.34|
||has as a part|≈0.00||
||consists of|≈0.00||
||comprising|≈0.00||
|一部分 (part_of)|including|≈0.00||
||possessing|≈0.00||
||containing|≈0.00||
||consisting of|≈0.00||
||made up of|≈0.00||
||relative to|0.02|0.02|
||relationship to|≈0.00||
|相對於 (relative_to)|in relation to<br>with respect to|≈0.00<br>≈0.00||
||regarding|≈0.00||
||respecting|≈0.00||
||along|≈0.00|0.15|
||alongside|0.15||
|沿著 (movement_along)|running along<br>stretching across|≈0.00<br>≈0.00||
||progressing along|≈0.00||
||moving along|≈0.00||
|總計||100.00|100.00|
