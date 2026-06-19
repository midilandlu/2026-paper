## **H Basic Spatial Relation Taxonomy** 

We define a basic taxonomy of spatial relations, inspired by Liu et al. (2023a), categorizing them into coarse- and fine-grained keywords. This framework helps analyze the distribution and use of spatial relations in VQA datasets. 

Table 10 outlines the taxonomy with key statistics. Each spatial relation (SR) is paired with relevant keywords (K), distinguishing broad categories from specific instances. The table also shows the percentage of each keyword within its SR group (K %), the overall share of each SR in the dataset (SR %), and its relative frequency across datasets. 

The datasets analyzed are listed in Table 2. This taxonomy standardizes spatial relation interpretation, promoting a structured approach to spatial reasoning in VQA and related tasks. 

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0015-00.png)

**Question:** The hair drier is facing away from the person. True or False? 

|Model|Prediction|Correct?|
|---|---|---|
|SpaRE-2B|True|✔|
|Qwen2VL-2B|False|✘|
|InternVL2-2B|No|✘|
|GPT-4o-mini|False|✘|

(a) Example 1 from VSR 

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0015-04.png)

**Question:** Which object is the person facing towards, the laptop or the TV? 

|Model|Answer|Correct?|
|---|---|---|
|SpaRE-2B|Laptop|✔|
|Qwen2VL-2B|TV|✘|
|InternVL2-2B|TV|✘|
|GPT-4o-mini|TV|✘|

(b) Example 2 from 3DSRBench 

Figure 4: For our qualitative analysis, each sub-figure contains an image, a corresponding question, different models’ responses, and their correctness (✔ or ✘). 

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0016-00.png)

A low-angle close-up view of an off-white pillar with Egyptian-style illustrations and hieroglyphics carved into it. The carved illustration in the middle of the image depicts a person holding a long staff with a diamond shaped object at the top of it _in their right hand_ as they are placing the bottom of the staff on the ground, and a cross-shaped object with a curved handle _on top of_ it _in their left hand_ . The person is facing _the left side of the image_ with their right foot ahead of their left. _To the left of the person_ is a being sitting _on top of_ a small set of stairs. The being is sitting with its knees bent and its feet _in front of their body_ , its feet and rear are both _touching the surface_ , and its hands are placed _in its lap_ . It is wearing a head dress that is long _in the back_ with a circular object placed _on top_ . The being doesn’t look human nor is it sitting like a human. There are hieroglyphs and shapes carved in the pillar _around and above_ this illustration. 

Figure 5: An example from DOCCI, one of the hyper-detailed image-captioning datasets that we extract QA pairs from. We _italicize_ spatially relevant words for emphasis. 

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0017-00.png)

The image is outside a building. There is a tent. There is a board and banner _on_ the tent. _Under_ the tent there are chairs, people, and some other stuff. In the _background_ there is a building. The sky is clear. 

Figure 6: An example from Localized Narratives, one of the hyper-detailed image-captioning datasets that we extract QA pairs from. We _italicize_ spatially relevant words for emphasis. 

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0017-03.png)

The image captures the cozy interior of a camper van on a bright sunny day. Dominating the scene is a booth-like, U or C-shaped seating area upholstered in light teal or mint green cushions, accented by colorful throw pillows. This seating _encircles_ a tan rectangular table _supported_ by a chrome pole. _Atop_ the table rests a green vase filled with red flowers, each featuring prominent yellow centers. The camper is adorned with mustard yellow polka-dotted curtains framing the windows, which allow views of bricks outside, indicating the presence of a nearby building. _Towards the back_ of the camper, there is an area separated by teal curtains, which likely serves as a bedroom featuring a rounded bed draped in a quilt with light green and white pastels. The camper’s interior is enhanced by white cupboards running _along_ the upper portions, providing ample storage. A crocheted throw with multicolored squares is casually draped over one of the bench seats, hinting at the occupant’s knack for needlework. _On_ the dark brown wooden floor, the slightly cramped yet inviting space emphasizes both comfort and practical use of space _in_ this quaint, mobile home. 

Figure 7: An example from PixMo-Cap, one of the hyper-detailed image-captioning datasets that we extract QA pairs from. We _italicize_ spatially relevant words for emphasis. 

Table 10: Our taxonomy of spatial relations shows relations, sub-keywords, and their percentages and frequencies observed in selected VQA datasets. The covered datasets are detailed in Table 2. **Spatial relation (SR)** : High-level relation category. **Keyword (K)** : Sub-keyword representing the SR. **K %** : Percentage of the sub-keyword among all keywords in its SR group. **SR %** : Percentage of the high-level spatial relation in the dataset. **Dataset freq.** : Relative frequency (in %) of the spatial relation in the datasets. 

|Spatial relation|Keyword|K (%)|SR (%)|
|---|---|---|---|
||left|7.41|19.28|
||at the left|1.27||
||on the left|1.24||
|left|to the left of|3.04||
||left of|3.75||
||left side of|1.31||
||at the left side of|1.25||
||right|8.04|21.65|
||at the right|1.42||
||on the right|1.75||
|right|to the right of|3.40||
||right of|4.03||
||right side of|1.59||
||at the right side of|1.42||
||above|1.64|2.35|
||directly above|�0.00||
||over|0.37||
|above|over the|0.34||
||upward of|�0.00||
||overlying|�0.00||
||on|9.29|13.04|
||on top of|1.72||
||atop|�0.00||
|on|on the top of|0.04||
||on top|1.72||
||lying on|0.04||
||sitting on|0.22||
||positioned on|�0.00||
||placed on|�0.00||
||overlaying on|�0.00||
||below|1.42|8.32|
||under|1.98||
||beneath|1.29||
|below|directly below|�0.00||
||down|0.13||
||underneath|0.04||
||under the|1.98||
||below the|1.40||
||lower|0.06||
||down from|�0.00||
||front|3.66|10.60|
||in front of|3.40||
||in the front of|0.02||
|front|directly in front of|�0.00||
||front of|3.51||
||confronting|�0.00||

Continued on next page 

|**Table 10(continued)**|**Table 10(continued)**|||
|---|---|---|---|
|Spatial relation (SR)|Keyword (K)|K %|SR %|
||back|0.30|3.75|
||behind|3.04||
||at the back of|0.19||
|back|in back of|�0.00||
||directly behind|�0.00||
||rear of|�0.00||
||backing onto|�0.00||
||back of|0.22||
||near|0.75|1.12|
||near to|0.02||
||nearby|0.02||
|near_close|close to|0.32||
||close by|�0.00||
||in proximity to|�0.00||
||within sight of|�0.00||
||far|1.08|2.07|
||far from|0.28||
||far away from|0.71||
|far|farther than|�0.00||
||distant from|�0.00||
||remote from|�0.00||
||inside|0.56|7.97|
||within|0.15||
||inside of|0.04||
|inside_within|contained in|�0.00||
||enclosed by|�0.00||
||in|7.22||
||outside|0.09|0.17|
||out of|0.09||
|outside|outer<br>outside of|�0.00<br>�0.00||
||outlying|�0.00||
||next to|1.79|3.60|
||beside|0.62||
||adjacent|0.34||
||adjacent to|0.34||
|next_to_beside_adjacent|by<br>at the side of|0.19<br>0.30||
||by the side of|�0.00||
||side by side with|�0.00||
||contiguous with|�0.00||
||opposite|0.09|0.17|
||opposite to|0.09||
|opposite|opposite side of<br>diagonally across|�0.00<br>�0.00||
||opposite from|�0.00||
||opposed to|�0.00||
||facing|0.62|0.62|
||facing toward|�0.00||
|facing|looking at|�0.00||
||confronting|�0.00||
||in view of|�0.00||
||parallel to|0.13|0.13|
|parallel_to|in line with<br>aligned with|�0.00<br>�0.00||
||running parallel to|�0.00||

Continued on next page 

**Table 10 (continued)** 

|Spatial relation (SR)|Keyword (K)|K %|SR %|
|---|---|---|---|
||perpendicular to|0.15|0.15|
|perpendicular_to|perpendicular with<br>orthogonal to|�0.00<br>�0.00||
||at right angles to|�0.00||
||toward|0.15|0.15|
||towards|�0.00||
||proceeding to|�0.00||
|toward_towards|progressing toward|�0.00||
||moving toward|�0.00||
||heading toward|�0.00||
||approaching|�0.00||
||away|1.40|2.80|
||away from|1.40||
||moving away from|�0.00||
|away_from|departing from|�0.00||
||receding from|�0.00||
||withdrawing from|�0.00||
||retreating from|�0.00||
||between|0.02|0.02|
||among|�0.00||
|between|amid<br>amidst|�0.00<br>�0.00||
||amongst|�0.00||
||betwixt|�0.00||
||through|0.02|0.04|
||passing through|�0.00||
||traversing|�0.00||
|through|transiting|�0.00||
||running through|�0.00||
||crossing|0.02||
||piercing|�0.00||
||around|0.17|0.22|
||circling|�0.00||
||encircling|�0.00||
||surrounding|0.04||
|around|enveloped by|�0.00||
||enclosing|�0.00||
||skirting|�0.00||
||encompassing|�0.00||
||encircled by|�0.00||
||overlapping|�0.00|�0.00|
||overlapping with|�0.00||
||intersecting with|�0.00||
|overlapping_intersecting|interlacing with<br>intertwined with|�0.00<br>�0.00||
||interlocking|�0.00||
||crisscrossing|�0.00||
||interlaced with|�0.00||
||connected to|�0.00|�0.00|
||connected with|�0.00||
||attached to|�0.00||
||attached with|�0.00||
|connected_attached|linked to|�0.00||
||joined to|�0.00||
||contiguous with|�0.00||
||linked with|�0.00||
||adjoined to|�0.00||

Continued on next page 

||**Table 10(continued)**|||
|---|---|---|---|
|Spatial relation (SR)|Keyword (K)|K %|SR %|
||at the edge of|0.65|0.65|
||at the corner of|�0.00||
|within_boundary|on the edge of<br>bordering|�0.00<br>�0.00||
||edged by|�0.00||
||at the boundary of|�0.00||
||north of|�0.00|�0.00|
||south of|�0.00||
||east of|�0.00||
|cardinal_directions|west of<br>northeast of|�0.00<br>�0.00||
||northwest of|�0.00||
||southeast of|�0.00||
||southwest of|�0.00||
||center of|0.04|0.60|
||at the center of|�0.00||
||in the center of|0.04||
|central_position|middle of|0.26||
||in the middle of|0.26||
||in the midst of|�0.00||
||amidst|�0.00||
||part of|0.34|0.34|
||has as a part|�0.00||
||consists of|�0.00||
||comprising|�0.00||
|part_of|including|�0.00||
||possessing|�0.00||
||containing|�0.00||
||consisting of|�0.00||
||made up of|�0.00||
||relative to|0.02|0.02|
||relationship to|�0.00||
|relative_to|in relation to<br>with respect to|�0.00<br>�0.00||
||regarding|�0.00||
||respecting|�0.00||
||along|�0.00|0.15|
||alongside|0.15||
|movement_along|running along<br>stretching across|�0.00<br>�0.00||
||progressing along|�0.00||
||moving along|�0.00||
|Total||100.00|100.00|