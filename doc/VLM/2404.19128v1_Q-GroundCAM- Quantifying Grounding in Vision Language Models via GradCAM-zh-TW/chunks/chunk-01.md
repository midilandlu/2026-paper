# **Q-GroundCAM: Quantifying Grounding in Vision Language Models via GradCAM** 

## Navid Rajabi and Jana Koˇseck´a George Mason University 

_{_ nrajabi, kosecka _}_ @gmu.edu 

## **Abstract** 

_Vision and Language Models (VLMs) continue to demonstrate remarkable zero-shot (ZS) performance across various tasks. However, many probing studies have revealed that even the best-performing VLMs struggle to capture aspects of compositional scene understanding, lacking the ability to properly ground and localize linguistic phrases in images. Recent VLM advancements include scaling up both model and dataset sizes, additional training objectives and levels of supervision, and variations in the model architectures. To characterize the grounding ability of VLMs, such as phrase grounding, referring expressions comprehension, and relationship understanding, Pointing Game has been used as an evaluation metric for datasets with bounding box annotations. In this paper, we introduce a novel suite of quantitative metrics that utilize GradCAM activations to rigorously evaluate the grounding capabilities of pretrained VLMs like CLIP, BLIP, and ALBEF. These metrics offer an explainable and quantifiable approach for a more detailed comparison of the zero-shot capabilities of VLMs and enable measuring models’ grounding uncertainty. This characterization reveals interesting tradeoffs between the size of the model, the dataset size, and their performance._ 

**==> picture [210 x 230] intentionally omitted <==**

**----- Start of picture text -----**<br>
Prompt = “her head” BLIP  GradCAM AMC  GradCAM<br>GT BBoX  of “her head” BLIP PG Uncertainty BLIP NMS  Analysis<br>**----- End of picture text -----**<br>

Figure 1. Uncertainty in Pointing Game (PG) accuracy, when having multiple top- _k_ identical activations with _inconsistent_ PG binary labels ( **Scenario 1** ). As depicted in the bottom-right figure, three top high-confidence activations exist, each with a value of 1.0, after our NMS analysis. One falls _outside_ the bounding box, one _inside_ , and one at the _border_ . In these cases, PG lacks any additional clues or heuristics to determine which one to select. 

## **1. Introduction** 

Foundational Vision and Language Models (VLMs) have demonstrated impressive performance in various vision and language tasks, including visual question answering (VQA), retrieval, image-text matching, referring expression comprehension, or captioning. For instance, CLIP has become a widely-used backbone in various applications, ranging from open-vocabulary object localization & referring expression grounding [3, 27] , to in-context learning in generative Multimodal Large Language Models (MLLMs) such as LLaVa [18], and Embodied AI for navigation-related tasks [10]. Despite that, state-of-the-art VLMs still struggle to capture aspects of compositional scene understand- 

ing and lack proper grounding for noun phrases, verbs, or relations [9, 28, 33]. Earlier model architectures localize objects of interest by predicting bounding box locations and use traditional IoU evaluation metrics with respect to ground truth datasets [6, 8, 11]. Recent MLLMs forgo the bounding box prediction and tackle the location prediction on the language side [18, 20]. The ability to ground and localize the concepts continues to be of central interest [31], and GradCAM visualizations [25] or Pointing Game accuracy [34] are often used to quantify models’ grounding ability. Pointing Game (PG) considers grounding successful if the highest GradCAM activation falls inside the ground 

1 

**==> picture [496 x 150] intentionally omitted <==**

**----- Start of picture text -----**<br>
Model  Ground-truth  GradCAM  Soft  Binary  Ground-truth  Distance  Soft Distance  Binary Distance  Top-K Activations  IO Ratio<br>Output  Bounding Box  Activations  Activations  Activations  Binary Mask  Map  Penalties  Penalties  (NMS >= 0.7)  Metric<br>BLIP<br>Base 0.749<br>223 M<br>BLIP<br>Large 0.284<br>446 M<br>CLIP<br>gScoreCAM 0.243<br>291 M<br>ALBEF<br>AMC 0.949<br>208 M<br>**----- End of picture text -----**<br>

Figure 2. Given the _**”his daughter”**_ prompt, PG returns the same accuracy of 1 for all four model outputs in a _discrete_ manner, and overlooks the differences in their holistic grounding qualities ( **Scenario 2** ). On the other hand, our **IO** _ratio_ metric can differentiate and rank them in a more _explainable_ and _continuous_ manner by quantifying them each as a single normalized value between 0 and 1. 

truth bounding box [7]. While Pointing Game has been utilized effectively in characterization of grounding performance [1, 2, 4, 7, 29, 31], it offers only coarse 0/1 characterization, which is susceptible to spurious local maxima or existence of multiple maxima, and does not capture well the confidence in the grounded concept. The examples in Figures 1 & 2 would be incorrectly handled by the Pointing Game approach due to the following scenarios: 

- **Scenario 1:** Highly confident activations, some in and some outside of the bounding box, are predicted by the model as in Figure 1. In these cases, the Pointing Game must randomly pick the local maximum. We refer to this as PG _Uncertainty_ metric and report the total number of cases where this type of uncertainty occurs for each dataset in Table 1. 

- **Scenario 2:** Pointing Game does not consider the spurious activation predictions outside the ground-truth bounding box when comparing the performance of different models on the same instance. As shown in Figure 2, while PG returns the label of 1 for all four models, our IO _ratio_ metric provides a finer-grained characterization of grounding quality. 

In order to provide a finer-grained characterization of the model’s grounding ability, we propose a set of metrics to (1) compute the similarity between the GradCAM activation maps and ground-truth binary mask, (2) reward the activations inside while penalizing the _spurious_ activations outside of the ground-truth bounding box, and (3) measure the **Scenario 1** uncertainty. Our inspiration stems from the Attention Mask Consistency loss (AMC) introduced in [31] which is designed to **maximize** the activations **inside** and **minimize** them **outside** the ground-truth bounding box, used in the pre-training of ALBEF [15]. Since our metrics are applicable to a wide range of VLMs, including both patch-based ViT [5] and CNN-based vision transformer en- 

coders [3, 23], they can thoroughly assess the grounding ability of VLMs, even without the bounding box prediction mechanism. The proposed metrics can distinguish nuances in the comparison of models’ grounding abilities that PG cannot capture. We will use these metrics to evaluate four state-of-the-art VLMs (BLIP _base_ [16], BLIP _large_ [16], CLIP gScoreCAM [3, 23], and the AMC [31] variation of ALBEF [15]) on a wide spectrum of grounding tasks[1] . 

## **2. Method** 

Consider GradCAM activation map _Ai,j_ , obtained by passing an image and a corresponding text prompt to the model, and _Mi,j_ are pixel locations of the binary ground-truth bounding box mask. For computing IoU _Soft_ and Dice _Soft_ , we’ve followed the formulas used for semantic segmentation, according to [19]. We first apply the threshold of 0.5 to each pixel value in _Ai,j_ and pass the thresholded binary activation maps to compute the IoU _Binary_ and Dice _Binary_ . **Distance Maps.** Given the bounding box coordinates as ( _y_ 0 _, x_ 0 _, y_ 1 _, x_ 1), distance maps _Di,j_ is computed as for all ( _i, j_ ) where 0 _≤ i < H,_ 0 _≤ j < W_ : 

**==> picture [234 x 11] intentionally omitted <==**

And the weighted penalties matrix _Pi,j_ is computed as: 

**==> picture [183 x 12] intentionally omitted <==**

**Weighted Distance Penalty (WDP)** is designed to penalize the _spurious_ activations outside the ground-truth bounding box, proportional to their _magnitudes_ and _distances_ from it, computed and normalized as follows: 

**==> picture [223 x 32] intentionally omitted <==**

> 1We release the code at Github.com/NavidRajabi/Q-GroundCAM. 

2 

|**Dataset**<br>**Model**|**IoU**_↑_<br>**Soft**<br>**Binary**|**Dice**_↑_<br>**Soft**<br>**Binary**|**Dice**_↑_<br>**Soft**<br>**Binary**|**WDP**_↓_<br>**Soft**<br>**Binary**|**WDP**_↓_<br>**Soft**<br>**Binary**|**IO**_ratio ↑_<br>**LogSig**|**PG**<br>**Accuracy**_↑_<br>**Uncertainty**_↓_|
|---|---|---|---|---|---|---|---|
|||||||||
|Flickr30K Entities<br>BLIP_base_<br>(TEST)<br>BLIP_large_<br>CLIP_gScoreCAM_<br>ALBEF_AMC_|0.12<br>0.09<br>0.14<br>0.11<br>**0.21**<br>**0.23**<br>0.19<br>0.16|0.21<br>0.23<br>**0.33**<br>0.31|0.15<br>0.17<br>**0.34**<br>0.25|0.95<br>0.94<br>0.92<br>**0.86**|0.79<br>0.77<br>**0.56**<br>0.60|0.43<br>0.44<br>0.44<br>**0.62**|60.08<br>317 / 14481<br>71.43<br>965 / 14481<br>75.41<br>**0**/ 14481<br>**87.69**<br>10<br>/ 14481|
|||||||||
|RefCOCO+<br>BLIP_base_<br>(TESTA)<br>BLIP_large_<br>CLIP_gScoreCAM_<br>ALBEF_AMC_|0.10<br>0.06<br>0.10<br>0.06<br>**0.17**<br>**0.15**<br>0.14<br>0.09|0.18<br>0.18<br>**0.28**<br>0.24|0.10<br>0.10<br>**0.24**<br>0.15|0.98<br>0.98<br>0.98<br>**0.96**|0.75<br>0.76<br>0.68<br>**0.66**|0.39<br>0.38<br>0.34<br>**0.54**|67.90<br>198 / 5726<br>67.27<br>336 / 5726<br>63.36<br>**0**/ 5726<br>**78.81**<br>14<br>/ 5726|
|||||||||
|RefCOCO+<br>BLIP_base_<br>(TESTB)<br>BLIP_large_<br>CLIP_gScoreCAM_<br>ALBEF_AMC_|0.11<br>0.06<br>0.11<br>0.06<br>**0.18**<br>**0.19**<br>0.16<br>0.11|0.20<br>0.20<br>**0.29**<br>0.27|0.11<br>0.11<br>**0.29**<br>0.19|0.98<br>0.98<br>0.97<br>**0.96**|0.86<br>0.87<br>0.85<br>**0.76**|0.31<br>0.30<br>0.30<br>**0.45**|46.96<br>201 / 4889<br>46.71<br>449 / 4889<br>49.02<br>**0**/ 4889<br>**64.34**<br>16<br>/ 4889|
|||||||||
|SpatialSense<br>BLIP_base_<br>(TRIPLETS)<br>BLIP_large_<br>CLIP_gScoreCAM_<br>ALBEF_AMC_|0.11<br>0.12<br>0.12<br>0.12<br>0.16<br>**0.20**<br>**0.17**<br>0.16|0.20<br>0.21<br>0.26<br>**0.27**|0.18<br>0.19<br>**0.30**<br>0.26|0.97<br>0.97<br>0.95<br>**0.93**|0.75<br>0.73<br>0.81<br>**0.71**|0.29<br>0.31<br>0.28<br>**0.42**|46.99<br>50 / 1811<br>51.68<br>100 / 1811<br>50.57<br>**0**/ 1811<br>**67.64**<br>3<br>/ 1811|
|||||||||
|SpatialSense<br>BLIP_base_<br>(SUBJECTS)<br>BLIP_large_<br>CLIP_gScoreCAM_<br>ALBEF_AMC_|0.10<br>0.08<br>0.11<br>0.11<br>**0.17**<br>**0.23**<br>0.16<br>0.15|0.17<br>0.20<br>**0.28**<br>0.27|0.14<br>0.17<br>**0.34**<br>0.24|0.97<br>0.97<br>0.95<br>**0.89**|0.76<br>0.74<br>**0.69**<br>0.70|0.29<br>0.30<br>0.31<br>**0.52**|39.81<br>42 / 1811<br>49.75<br>116 / 1811<br>60.07<br>**0**/ 1811<br>**70.01**<br>4<br>/ 1811|
|||||||||
|SpatialSense<br>BLIP_base_<br>(OBJECTS)<br>BLIP_large_<br>CLIP_gScoreCAM_<br>ALBEF_AMC_|0.11<br>0.07<br>0.12<br>0.08<br>**0.20**<br>**0.21**<br>0.16<br>0.12|0.19<br>0.21<br>**0.32**<br>0.27|0.12<br>0.13<br>**0.32**<br>0.19|0.92<br>0.92<br>0.90<br>**0.81**|0.69<br>0.74<br>**0.65**<br>**0.65**|0.42<br>0.40<br>0.41<br>**0.63**|50.02<br>37 / 1811<br>54.55<br>158 / 1811<br>64.93<br>**0**/ 1811<br>**78.24**<br>3<br>/ 1811|

Table 1. Quantitative results comparison for all settings where numbers are reported as mean IoU ( **mIoU** ) across each setting. For each setting, the top performance across all models is highlighted as **bold** , and the second-best with underline. 

**Inside/Outside Activations Ratio (** IO _ratio_ **)** is computed as follows: 

**==> picture [186 x 68] intentionally omitted <==**

**==> picture [192 x 25] intentionally omitted <==**

**Pointing Game Uncertainty Analysis:** We extract the local maxima ( _v_ ) of the activation map _Ai,j_ higher than the activation threshold ( _τ_ ) of 0 _._ 7 as the set of _V_ = _{v_ 1 _, v_ 2 _, ..., vn}_ . _V_ is then sorted, followed by an additional NMS step of suppressing maxima that are within Euclidean distance _δ_[2] of larger extremum. _Vnms_ and _Cnms_ , represent remaining activation values and their corresponding coordinates. For every point in _Cnms_ , we check whether it falls inside the ground-truth bounding box and count the number of cases where top- _k_ equal activations in _Vnms_ are **not** all either inside or outside of the bounding box. 

## **3. Experiments** 

We’ve conducted experiments to evaluate the grounding ability of four state-of-the-art VLMs (BLIP _base_ , 

BLIP _large_ , CLIP gScoreCAM, and the AMC variation of ALBEF) on a wide range of grounding tasks, varied by the text prompt granularity, and with both in-distribution (ID) and out-of-distribution (OOD) data. The quantitative results are summarized in Table 1, and sample score distributions are shown in Figure 3. For phrase grounding and referring expression comprehension, we used the test split of Flickr30K Entities [21] and RefCOCO+ testA & testB [12] datasets that are considered from in-domain distribution for the models. In order to investigate the outof-distribution generalizability of these models, we ran the same experiment on the SpatialSense [30] dataset test split, which has both **visual** domain shift due to the inclusion of NYU dataset [26] images with a total of 3,679 unique objects, including small/long-tail concepts, and the **language** domain shift by the annotation of 17,498 triplets including spatial relations. The dataset is designed for spatial relationship recognition and is annotated in the triplet _{_ SUBJECTRELATION-OBJECT _}_ format with the ground-truth OBJECT and SUBJECT bounding boxes. We ran our experiments in three different settings for TRIPLET, SUBJECT, and OBJECT grounding. An instance of the SpatialSense dataset is demonstrated in Figure 4. Experiment details for all settings can be found in the Appendix 6. Additional qualitative results can be found in Appendix 7, where another case of **Scenario 1** uncertainty is shown in Figure 6, obtained by BLIP _base_ in the top-left sub-figure of the first example. 

> 2 _δ_ = 50 in our experiments 

3 

**==> picture [496 x 123] intentionally omitted <==**

Figure 3. Histogram of IoU _Soft_ and IO _ratio_ distributions for **ID** vs. **OOD** . Note that the histograms are more peaked for in-distribution datasets, as shown in **blue** on the left, and for better-performing models, they are shifted to the right. The out-of-distribution experiments for all models have less peaked, flatter histograms, where shown in **orange** on the right. Full visualizations can be found in Appendix 8. 

**==> picture [75 x 56] intentionally omitted <==**

**==> picture [74 x 56] intentionally omitted <==**

**==> picture [74 x 56] intentionally omitted <==**

**==> picture [215 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) Triplet GT-bbox (b) Subject GT-bbox (c) Object GT-bbox<br>**----- End of picture text -----**<br>

Figure 4. A sample from SpatialSense NYU bedroom set. We consider the _”wifi router to the right of television”_ prompt as TRIPLET, _”wifi router”_ as SUBJECT, and _”television”_ as OBJECT. 

## **4. Discussion** 

According to Table 1, ALBEF _AMC_ is the winner, considering the combination of PG _Accuracy_ , PG _Uncertainty_ , and IO _ratio_ metrics. This highlights the importance of finetuning ALBEF bounding box-level supervision, compared to scaling models’ size and training set size using often noisy image-text pairs. Regarding the similarity between the activations and ground-truth masks, CLIP _gScoreCAM_ and ALBEF _AMC_ are the best and second-best performing models according to IoU and Dice, while in terms of WDP, it is reversed in most cases. This suggests that CLIP has more spurious GradCAM activations. Furthermore, we believe that due to the prevalent noisiness in GradCAM activations, the WDP _Soft_ penalization is much more strict than WDP _Binary_ variation, making WDP _Binary_ a more practical metric to use. PG _Uncertainty_ is zero in CLIP _gScoreCAM_ , which we believe stems from the difference in the vision backbone and nuances in how the GradCAM is being computed in [3]. ALBEF _AMC_ is the second-best in PG _Uncertainty_ , marginally. In contrast, BLIP _large_ has shown the highest relative PG _Uncertainty_ across all the settings. Our IO _ratio_ metric has a strong positive correlation with PG _Accuracy_ while being more strict. This makes it a suitable standalone metric for assessing the model’s grounding performance, as it considers both inside & outside activations, in addition to PG _Accuracy_ . Note that 

PG _Accuracy_ is not positively correlated with PG _Uncertainty_ in all models. This finding is insightful as it demonstrates that not always the better performing model in terms of PG _Accuracy_ has the lowest PG _Uncertainty_ . Our OOD experiments also demonstrate the applicability of our metrics to the evaluation of triplet-based spatial understanding grounding [13, 24], and shifted visual domains. 

**Model size vs. training data impact.** Apart from the ALBEF _AMC_ superiority, our experiments show that BLIP _large_ , which has _∼_ 446M parameters and pre-trained on 129M image-text pairs, _under-performs_ BLIP _base_ , which has _∼_ 223M parameters and pre-trained on 14M image-text pairs, in terms of the PG _Uncertainty_ in all 6 dataset splits, and in 2 dataset splits in terms of PG _Accuracy_ . Considering CLIP, which is pre-trained on _∼_ 400M imagetext pairs, as the highest end, and both ALBEF & BLIP _base_ as the lowest end of the model & data size spectrum in our experiments, the performance of ALBEF _AMC_ again highlights the effectiveness of finer-grained fine-tuning. We suggest running our IO _ratio_ , PG _Uncertainty_ , WDP _Binary_ , and either of IoU _Soft_ or Dice _Soft_ metrics, in addition to PG _Accuracy_ , for a thorough grounding evaluation. 

## **5. Conclusion** 

We first demonstrate two scenarios that the Pointing Game (PG) evaluation metric fails to handle properly, and introduce a new set of metrics for evaluation of models’ grounding ability that captures finer-grained differences between models. According to our experiments, ALBEF _AMC_ has shown its superiority quantitatively, compared to the other three models, and demonstrated better performance qualitatively in terms of the sharpness of the activations it predicts inside the ground-truth bounding box, as characterized by IO _ratio_ . The proposed metrics enable a finer-grained evaluation of grounding ability for phrase grounding and referring expression comprehension, and how it varies across indistribution and out-of-distribution datasets. 

4 

## **References** 

- [1] Hassan Akbari, Svebor Karaman, Surabhi Bhargava, Brian Chen, Carl Vondrick, and Shih-Fu Chang. Multi-level multimodal common semantic space for image-phrase grounding. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 12476–12486, 2019. 2 

- [2] Assaf Arbelle, Sivan Doveh, Amit Alfassy, Joseph Shtok, Guy Lev, Eli Schwartz, Hilde Kuehne, Hila Barak Levi, Prasanna Sattigeri, Rameswar Panda, et al. Detector-free weakly supervised grounding by separation. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 1801–1812, 2021. 2 

- [3] Peijie Chen, Qi Li, Saad Biaz, Trung Bui, and Anh Nguyen. gscorecam: What objects is clip looking at? In _Proceedings of the Asian Conference on Computer Vision_ , pages 1959– 1975, 2022. 1, 2, 4 

- [4] Samyak Datta, Karan Sikka, Anirban Roy, Karuna Ahuja, Devi Parikh, and Ajay Divakaran. Align2ground: Weakly supervised phrase grounding guided by image-caption alignment. In _Proceedings of the IEEE/CVF international conference on computer vision_ , pages 2601–2610, 2019. 2 

- [5] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al. An image is worth 16x16 words: Transformers for image recognition at scale. _arXiv preprint arXiv:2010.11929_ , 2020. 2 

- [6] Zi-Yi Dou, Aishwarya Kamath, Zhe Gan, Pengchuan Zhang, Jianfeng Wang, Linjie Li, Zicheng Liu, Ce Liu, Yann LeCun, Nanyun Peng, et al. Coarse-to-fine vision-language pre-training with fusion in the backbone. _Advances in neural information processing systems_ , 35:32942–32956, 2022. 1 

- [7] Tanmay Gupta, Arash Vahdat, Gal Chechik, Xiaodong Yang, Jan Kautz, and Derek Hoiem. Contrastive learning for weakly supervised phrase grounding. In _European Conference on Computer Vision_ , pages 752–768. Springer, 2020. 2 

- [8] Tanmay Gupta, Amita Kamath, Aniruddha Kembhavi, and Derek Hoiem. Towards general purpose vision systems: An end-to-end task-agnostic vision-language architecture. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , pages 16399–16409, 2022. 1 

- [9] Lisa Anne Hendricks and Aida Nematzadeh. Probing image-language transformers for verb understanding. _arXiv preprint arXiv:2106.09141_ , 2021. 1 

- [10] Chenguang Huang, Oier Mees, Andy Zeng, and Wolfram Burgard. Visual language maps for robot navigation. In _2023 IEEE International Conference on Robotics and Automation (ICRA)_ , pages 10608–10615. IEEE, 2023. 1 

- [11] Aishwarya Kamath, Mannat Singh, Yann LeCun, Gabriel Synnaeve, Ishan Misra, and Nicolas Carion. Mdetrmodulated detection for end-to-end multi-modal understanding. In _Proceedings of the IEEE/CVF International Conference on Computer Vision_ , pages 1780–1790, 2021. 1 

- [12] Sahar Kazemzadeh, Vicente Ordonez, Mark Matten, and Tamara Berg. Referitgame: Referring to objects in pho- 

tographs of natural scenes. In _Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP)_ , pages 787–798, 2014. 3 

- [13] Ranjay Krishna, Yuke Zhu, Oliver Groth, Justin Johnson, Kenji Hata, Joshua Kravitz, Stephanie Chen, Yannis Kalantidis, Li-Jia Li, David A Shamma, et al. Visual genome: Connecting language and vision using crowdsourced dense image annotations. _International journal of computer vision_ , 123:32–73, 2017. 4, 1 

- [14] Dongxu Li, Junnan Li, Hung Le, Guangsen Wang, Silvio Savarese, and Steven C.H. Hoi. LAVIS: A one-stop library for language-vision intelligence. In _Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)_ , pages 31–41, Toronto, Canada, 2023. Association for Computational Linguistics. 1 

- [15] Junnan Li, Ramprasaath Selvaraju, Akhilesh Gotmare, Shafiq Joty, Caiming Xiong, and Steven Chu Hong Hoi. Align before fuse: Vision and language representation learning with momentum distillation. _Advances in neural information processing systems_ , 34:9694–9705, 2021. 2 

- [16] Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi. Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation. In _International Conference on Machine Learning_ , pages 12888– 12900. PMLR, 2022. 2 

- [17] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ramanan, Piotr Doll´ar, and C Lawrence Zitnick. Microsoft coco: Common objects in context. In _Computer Vision–ECCV 2014: 13th European Conference, Zurich, Switzerland, September 6-12, 2014, Proceedings, Part V 13_ , pages 740–755. Springer, 2014. 1 

- [18] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. In _NeurIPS_ , 2023. 1 

- [19] Angelo Monteux. Metrics for semantic segmentation, 2019. 2 

- [20] Zhiliang Peng, Wenhui Wang, Li Dong, Yaru Hao, Shaohan Huang, Shuming Ma, and Furu Wei. Kosmos-2: Grounding multimodal large language models to the world. _arXiv preprint arXiv:2306.14824_ , 2023. 1 

- [21] Bryan A. Plummer, Liwei Wang, Chris M. Cervantes, Juan C. Caicedo, Julia Hockenmaier, and Svetlana Lazebnik. Flickr30k entities: Collecting region-to-phrase correspondences for richer image-to-sentence models. In _Proceedings of the IEEE International Conference on Computer Vision (ICCV)_ , 2015. 3, 1 

- [22] Mengxue Qu, Yu Wu, Wu Liu, Qiqi Gong, Xiaodan Liang, Olga Russakovsky, Yao Zhao, and Yunchao Wei. Siri: A simple selective retraining mechanism for transformer-based visual grounding. In _European Conference on Computer Vision_ , pages 546–562. Springer, 2022. 1 

- [23] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual models from natural language supervision. In _International Conference on Machine Learning_ , pages 8748–8763. PMLR, 2021. 2 

5 

- [24] Navid Rajabi and Jana Kosecka. Towards grounded visual spatial reasoning in multi-modal vision language models. _arXiv preprint arXiv:2308.09778_ , 2023. 4 

- [25] Ramprasaath R Selvaraju, Michael Cogswell, Abhishek Das, Ramakrishna Vedantam, Devi Parikh, and Dhruv Batra. Grad-cam: Visual explanations from deep networks via gradient-based localization. In _Proceedings of the IEEE international conference on computer vision_ , pages 618–626, 2017. 1 

- [26] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob Fergus. Indoor segmentation and support inference from rgbd images. In _Computer Vision–ECCV 2012: 12th European Conference on Computer Vision, Florence, Italy, October 7-13, 2012, Proceedings, Part V 12_ , pages 746–760. Springer, 2012. 3, 1 

- [27] Sanjay Subramanian, Will Merrill, Trevor Darrell, Matt Gardner, Sameer Singh, and Anna Rohrbach. Reclip: A strong zero-shot baseline for referring expression comprehension. _arXiv preprint arXiv:2204.05991_ , 2022. 1 

- [28] Tristan Thrush, Ryan Jiang, Max Bartolo, Amanpreet Singh, Adina Williams, Douwe Kiela, and Candace Ross. Winoground: Probing vision and language models for visiolinguistic compositionality. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 5238–5248, 2022. 1 

- [29] Liwei Wang, Jing Huang, Yin Li, Kun Xu, Zhengyuan Yang, and Dong Yu. Improving weakly supervised visual grounding by contrastive knowledge distillation. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 14090–14100, 2021. 2 

- [30] Kaiyu Yang, Olga Russakovsky, and Jia Deng. Spatialsense: An adversarially crowdsourced benchmark for spatial relation recognition. In _International Conference on Computer Vision (ICCV)_ , 2019. 3, 1 

- [31] Ziyan Yang, Kushal Kafle, Franck Dernoncourt, and Vicente Ordonez. Improving visual grounding by encouraging consistent gradient-based explanations. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 19165–19174, 2023. 1, 2 

- [32] Peter Young, Alice Lai, Micah Hodosh, and Julia Hockenmaier. From image descriptions to visual denotations: New similarity metrics for semantic inference over event descriptions. _Transactions of the Association for Computational Linguistics_ , 2:67–78, 2014. 1 

- [33] Mert Yuksekgonul, Federico Bianchi, Pratyusha Kalluri, Dan Jurafsky, and James Zou. When and why visionlanguage models behave like bag-of-words models, and what to do about it? _arXiv preprint arXiv:2210.01936_ , 2022. 1 

- [34] Jianming Zhang, Sarah Adel Bargal, Zhe Lin, Jonathan Brandt, Xiaohui Shen, and Stan Sclaroff. Top-down neural attention by excitation backprop. _International Journal of Computer Vision_ , 126(10):1084–1102, 2018. 1 

6 

## **Q-GroundCAM: Quantifying Grounding in Vision Language Models via GradCAM** 

## Supplementary Material 

## **6. Experiments Details** 

For the _**phrase grounding**_ experiments, we used the test split of Flickr30K Entities [21] dataset, specifically, the _merged_ version which has also been used by MDETR [11] and SiRi [22]. In terms of the pre-trained checkpoints, we used blip-image-text-matching checkpoint for BLIP (both variations of base and large), through the LAVIS [14] codebase. For ALBEF _AMC_ , we used the best-flickr checkpoint released by AMC [31] where sample qualitative results are shown in Figure 1 & 2. For all CLIP _gScoreCAM_ experiments, we used the RESNET50 _×_ 16 variation of CLIP with the average pooling of top 300-channel activation maps, as the bestperforming setting reported by [3]. 

For the _**referring expressions comprehension**_ experiments, we used the same checkpoints as _phrase grounding_ ones for both BLIP experiments, but used the best-refcoco checkpoint released by [31], where sample qualitative results are shown in Figure 5 & 6. Also, an additional example of PG Uncertainty ( **Scenario 1** ) is demonstrated in the first example of Figure 6, in the topleft GradCAM activations of the first obtained by running BLIP _base_ . Again, there are two top activations with a value of 1.0 each, while one of them falls inside and the other one outside of the ground-truth bounding box. In these cases, PG becomes indecisive in picking the maximum to compute the accuracy, as this part of the evaluation becomes stochastic and directly affects the evaluation reliability. 

For the _**Out-of-Ditribution (OOD)**_ experiments, we ran the models on the SpatialSense [30] dataset. We consider the Spatial Sense dataset OOD because it has a domain shift in both visual side (due to including new images from Flickr [32] and NYU [26], instead of widelyused pre-training/fine-tuning datasets like MSCOCO [17] and Visual Genome [13]), and language side, by including spatial clauses and small/long-tail objects for increasing the detection/grounding difficulty. To be more specific, we ran this experiment on the instances with True labels in the test set, with a total number of 1811 instances in three settings. The first setting grounds the entire triplet _{_ SUBJECT-RELATION-OBJECT _}_ and we consider the SUBJECT ground-truth bounding box as the correct bounding box supervision for the entire triplet, since according to their convention, the SUBJECT acts as the target and OBJECT as reference. Also, we have conducted two separate experiments for individual object grounding for SUBJECTS and OBJECTS using their corresponding ground- 

truth bounding boxes each. In addition to confirming the high degree of difficulty we have seen during the Spatial Sense experiments, in which we have also shown a sample qualitative example in Figure 7, we’ve noticed that in some of the instances, grounding the SUBJECTS is more complicated due to the underlying ambiguities/distractions when grounding the SUBJECT as a standalone phrase. This happens because of the dependency on the RELATION and OBJECT as the context required for disambiguation, which is shown in Figure 8 as an example. Therefore, the TRIPLET and OBJECT grounding settings results seem more reliable in general, but since we are comparing different models on exactly the same footing, our SUBJECT grounding results should also be considered fair among all the models. 

## **7. Sample Qualitative Results** 

Flickr30K Entities examples are provided in Figure 1 & 2. RefCOCO+ **testA** example is provided in Figure 5. RefCOCO+ **testB** example is provided in Figure 6. SpatialSense **first** example is provided in Figure 7. SpatialSense **second** example is provided in Figure 8. 