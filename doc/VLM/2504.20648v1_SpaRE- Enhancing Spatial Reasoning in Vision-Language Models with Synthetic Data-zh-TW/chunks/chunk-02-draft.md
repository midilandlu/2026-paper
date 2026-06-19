## **4.6 定性分析** 

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0008-04.png)

|問題|模型<br>回答|
|---|---|
|如果我站在圖中人物的位置，<br>面向他所面對的方向，<br>桌子是在我的左邊<br>還是右邊？|SpaRE-7B<br>右邊 (Right)<br>✔<br>Qwen2-VL-7B<br>左邊 (Left)<br>✘<br>Qwen2-VL-72B<br>左邊 (Left)<br>✘<br>InternVL2-76B<br>左邊 (Left)<br>✘<br>GPT-4o<br>左邊 (Left)<br>✘|

圖 2：不同視覺語言模型 (VLMs)（**結合視覺圖像理解與自然語言處理能力的 AI 模型**）對同一個空間推理問題的回答對比。 

在圖 2 中，當我們拋出這個棘手的問題：「……桌子是在我的左邊還是右邊？」時，SpaRE-7B 乾脆俐落地答對了「右邊」，但其他對手模型卻全軍覆沒，通通答成「左邊」。這個問題之所以難，是因為這需要切換視角！從我們這些螢幕前的「旁觀者」（也就是大多數視覺語言模型的預設視角）來看，桌子明明在左邊；但如果我們想像自己就是畫面裡的那個人，轉過身去，桌子其實就在右邊了。這個例子很直觀地證明了我們的訓練方法有多有效。雖然這種需要「感同身受」的視角切換對 SpaRE 模型來說依然是個不小的挑戰（我們待會兒會聊到這個），但它的表現已經遠遠把其他模型甩在身後了。我們在附錄的圖 4 中準備了更多對比範例。

## **4.7 錯誤分析** 

雖然我們的模型在 VSR 和 What's Up 基準測試上表現強悍，但在 3DSRBench 上的進步幅度卻相對有限。我們發現，這與 Zhang 等人 (2024) 的研究結論不謀而合：當前的視覺語言模型在面對需要「感同身受」的同理空間推理（**empathetic spatial reasoning，即設身處地從他人角度來判斷空間關係的能力**）時，往往會顯得手足無措。簡單來說，它們沒辦法換位思考。這種根深蒂固的「自我中心偏差」（**egocentric bias，總是從觀察者自身視角出發的傾向**）大多源自於原始的資料集，而我們生成的合成資料集也不幸繼承了這個缺點。要解決這個難題，我們未來可能需要更精準的資料集，專門人工標記場景中不同參考框架（frames of reference）的視角資訊。

## **5 結論** 

在這項研究中，我們迎難而上，針對視覺語言資料集中極度缺乏空間推理（**理解與解釋圖像中物體之間空間位置關係的能力**）資料的痛點，利用大語言模型 (LLMs) 從超詳細的影像描述中，點石成金般地生成了豐富的合成問答對。實測結果非常令人振奮！我們的訓練方法大幅提升了視覺語言模型的空間推理能力，在各大基準測試中都取得了顯著的成長，而且最棒的是，這完全沒有犧牲模型原本通用的視覺語言理解能力。

透過將豐富的空間描述轉化為多樣且精準的問答對，我們成功為視覺語言模型注入了學習空間概念所需的訓練資料。這項成果再次印證了在訓練強健的視覺語言模型時，資料的品質與多樣性是多麼關鍵，同時也為機器人、自主導航以及擴充實境（**Extended Reality, XR，包含虛擬實境 VR、擴增實境 AR 和混合實境 MR 的總稱**）等前沿領域開闢了新的研究道路。我們由衷希望這項工作能激發大家對合成資料的更多探索，一同突破視覺語言模型的瓶頸，打造出更聰明、更多才多藝的多模態 AI 系統。

## **6 限制** 

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0008-14.png)

圖 3：沒有明確參考框架時空間關係的模糊性：從「觀察者」或「畫中女子」的視角來看，這盆植物到底是在長椅的「右邊」還是「左邊」？ 

儘管我們的新方法大幅提升了視覺語言模型的空間推理身手，但我們也坦承它並非十全十美。例如，如果沒有給定明確的「參考框架」（**Frames of Reference, FOR，即用來定義空間方向的基準，如『以我為中心』或『以物體為中心』**），空間描述就會變得非常含糊不清 (Levinson, 2003; Liu et al., 2023a)。此外，我們與 Zhang 等人 (2024) 都觀察到，現有的視覺語言模型在進行空間推理時，還無法很好地理解不同的參考框架。就像圖 3 所示，那盆植物到底是在長椅的「右邊」還是「左邊」，完全取決於你是站在觀察者的角度，還是站在長椅或畫中女子的角度——一旦少了參考框架的提示，我們就很難判定標準答案到底是什麼。

在未來的計畫中，我們打算把明確的參考框架標記引入合成資料的生成流程中，以克服這個痛點。同時，我們也想探索更有效率的大語言模型合成資料生成方法，並嘗試將這套方法推廣到其他語法結構更複雜（例如具有豐富詞形變化）的語言中。

## **7 倫理聲明** 

我們的研究是利用從超詳細影像描述中生成的合成資料（**Synthetic Data，非真實採集、由演算法或模型人工生成的資料**）來強化視覺語言模型的空間推理能力。我們使用的原始資料皆為公開資源，且不包含任何敏感資訊。然而，由於空間推理能力的提升會直接影響到機器人或自主導航等實際應用，因此在正式部署這些模型之前，進行全面且嚴格的安全測試至關重要。同時，我們也注意到，用來生成合成資料的大語言模型本身可能會帶有其訓練資料中的偏見。為了促進社群的檢驗與後續研究，我們計劃以開源形式釋出我們的程式碼 and 資料集。

## **References** 

- Marah Abdin, Sam Ade Jacobs, Ammar Ahmad Awan, Jyoti Aneja, Ahmed Awadallah, Hany Awadalla, Nguyen Bach, Amit Bahree, Arash Bakhtiari, Harkirat Behl, et al. 2024. Phi-3 technical report: A highly capable language model locally on your phone. _arXiv preprint arXiv:2404.14219_ . 

- Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. 2023. Gpt-4 technical report. _arXiv preprint arXiv:2303.08774_ . 

- Palaash Agrawal, Haidi Azaman, and Cheston Tan. 2023. Stupd: A synthetic dataset for spatial and temporal relation reasoning. _arXiv preprint arXiv:2309.06680_ . 

- S. Balakrishnan, M.Syed Shahul Hameed, Kavya Venkatesan, and G Aswin. 2021. Interaction of spatial computing in augmented reality. _2021 7th International Conference on Advanced Computing and Communication Systems (ICACCS)_ , 1:1900–1904. 

- James Betker, Gabriel Goh, Li Jing, † TimBrooks, Jianfeng Wang, Linjie Li, † LongOuyang, † JuntangZhuang, † JoyceLee, † YufeiGuo, † WesamManassra, † PrafullaDhariwal, † CaseyChu, † YunxinJiao, and Aditya Ramesh. 2023. Improving image generation with better captions. 

- Boyuan Chen, Zhuo Xu, Sean Kirmani, Brain Ichter, Dorsa Sadigh, Leonidas Guibas, and Fei Xia. 2024a. Spatialvlm: Endowing vision-language models with spatial reasoning capabilities. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 14455–14465. 

- Lin Chen, Jinsong Li, Xiaoyi Dong, Pan Zhang, Conghui He, Jiaqi Wang, Feng Zhao, and Dahua Lin. 2025. Sharegpt4v: Improving large multi-modal models with better captions. In _European Conference on Computer Vision_ , pages 370–387. Springer. 

- Zhe Chen, Weiyun Wang, Hao Tian, Shenglong Ye, Zhangwei Gao, Erfei Cui, Wenwen Tong, Kongzhi Hu, Jiapeng Luo, Zheng Ma, et al. 2024b. How far are we to gpt-4v? closing the gap to commercial multimodal models with open-source suites. _Science China Information Sciences_ , 67(12):220101. 

- Jaemin Cho, Abhaysinh Zala, and Mohit Bansal. 2022. Dall-eval: Probing the reasoning skills and social biases of text-to-image generation models. _2023 IEEE/CVF International Conference on Computer Vision (ICCV)_ , pages 3020–3031. 

- Matt Deitke, Christopher Clark, Sangho Lee, Rohun Tripathi, Yue Yang, Jae Sung Park, Mohammadreza Salehi, Niklas Muennighoff, Kyle Lo, Luca Soldaini, Jiasen Lu, Taira Anderson, Erin Bransom, Kiana Ehsani, Huong Ngo, YenSung Chen, Ajay Patel, Mark Yatskar, Chris Callison-Burch, Andrew Head, Rose Hendrix, Favyen Bastani, Eli VanderBilt, Nathan Lambert, Yvonne Chou, Arnavi Chheda, Jenna Sparks, Sam Skjonsberg, Michael Schmitz, Aaron Sarnat, Byron Bischoff, Pete Walsh, Chris Newell, Piper Wolters, Tanmay Gupta, Kuo-Hao Zeng, Jon Borchardt, Dirk Groeneveld, Jen Dumas, Crystal Nam, Sophie Lebrecht, Caitlin Wittlif, Carissa Schoenick, Oscar Michel, Ranjay Krishna, Luca Weihs, Noah A. Smith, Hannaneh Hajishirzi, Ross Girshick, Ali Farhadi, and Aniruddha Kembhavi. 2024. Molmo and pixmo: Open weights and open data for state-of-the-art multimodal models. _Preprint_ , arXiv:2409.17146. 

- Haodong Duan, Junming Yang, Yuxuan Qiao, Xinyu Fang, Lin Chen, Yuan Liu, Xiaoyi Dong, Yuhang Zang, Pan Zhang, Jiaqi Wang, et al. 2024. Vlmevalkit: An open-source toolkit for evaluating large multi-modality models. In _Proceedings of the 32nd ACM international conference on multimedia_ , pages 11198–11201. 

- Tejas Gokhale, Hamid Palangi, Besmira Nushi, Vibhav Vineet, Eric Horvitz, Ece Kamar, Chitta Baral, and Yezhou Yang. 2023. Benchmarking spatial relationships in text-to-image generation. _Preprint_ , arXiv:2212.10015. 

- Yash Goyal, Tejas Khot, Douglas Summers-Stay, Dhruv Batra, and Devi Parikh. 2017. Making the v in vqa matter: Elevating the role of image understanding in visual question answering. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , pages 6904–6913. 

- Tianrui Guan, Fuxiao Liu, Xiyang Wu, Ruiqi Xian, Zongxia Li, Xiaoyu Liu, Xijun Wang, Lichang Chen, Furong Huang, Yaser Yacoob, Dinesh Manocha, and Tianyi Zhou. 2024. Hallusionbench: An advanced diagnostic suite for entangled language hallucination and visual illusion in large vision-language models. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , pages 14375–14385. 

- Suriya Gunasekar, Yi Zhang, Jyoti Aneja, Caio César Teodoro Mendes, Allie Del Giorno, Sivakanth Gopi, Mojan Javaheripi, Piero Kauffmann, Gustavo de Rosa, Olli Saarikivi, et al. 2023. Textbooks are all you need. _arXiv preprint arXiv:2306.11644_ . 

- Jack Hessel, Ari Holtzman, Maxwell Forbes, Ronan Le Bras, and Yejin Choi. 2021. Clipscore: A referencefree evaluation metric for image captioning. _arXiv preprint arXiv:2104.08718_ . 

- Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. 2021. Lora: Low-rank adaptation of large language models. _arXiv preprint arXiv:2106.09685_ . 

- Drew A. Hudson and Christopher D. Manning. 2019. Gqa: A new dataset for real-world visual reasoning and compositional question answering. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ . 

- Justin Johnson, Bharath Hariharan, Laurens Van Der Maaten, Li Fei-Fei, C Lawrence Zitnick, and Ross Girshick. 2017. Clevr: A diagnostic dataset for compositional language and elementary visual reasoning. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , pages 2901–2910. 

- Amita Kamath, Jack Hessel, and Kai-Wei Chang. 2023. What’s ”up” with vision-language models? investigating their struggle with spatial reasoning. In _Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing_ , pages 9161– 9175, Singapore. Association for Computational Linguistics. 

- Douwe Kiela, Hamed Firooz, Aravind Mohan, Vedanuj Goswami, Amanpreet Singh, Pratik Ringshia, and Davide Testuggine. 2020. The hateful memes challenge: Detecting hate speech in multimodal memes. _Advances in neural information processing systems_ , 33:2611–2624. 

- Alina Kuznetsova, Hassan Rom, Neil Alldrin, Jasper Uijlings, Ivan Krasin, Jordi Pont-Tuset, Shahab Kamali, Stefan Popov, Matteo Malloci, Alexander Kolesnikov, 

et al. 2020. The open images dataset v4: Unified image classification, object detection, and visual relationship detection at scale. _International journal of computer vision_ , 128(7):1956–1981. 

- Christian Landsiedel, Verena Rieser, Matthew R. Walter, and D. Wollherr. 2017. A review of spatial reasoning and interaction for real-world robotics. _Advanced Robotics_ , 31:222 – 242. 

- Stephen C. Levinson. 2003. _Space in Language and Cognition: Explorations in Cognitive Diversity_ . Language Culture and Cognition. Cambridge University Press. 

- Yuanzhi Li, Sébastien Bubeck, Ronen Eldan, Allie Del Giorno, Suriya Gunasekar, and Yin Tat Lee. 2023. Textbooks are all you need ii: phi-1.5 technical report. _arXiv preprint arXiv:2309.05463_ . 

- Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and C Lawrence Zitnick. 2014. Microsoft coco: Common objects in context. In _Computer Vision– ECCV 2014: 13th European Conference, Zurich, Switzerland, September 6-12, 2014, Proceedings, Part V 13_ , pages 740–755. Springer. 

- Fangyu Liu, Guy Emerson, and Nigel Collier. 2023a. Visual spatial reasoning. _Transactions of the Association for Computational Linguistics_ , 11:635–651. 

- Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. 2023b. Visual instruction tuning. In _Advances in Neural Information Processing Systems_ , volume 36, pages 34892–34916. Curran Associates, Inc. 

- Yangzhou Liu, Yue Cao, Zhangwei Gao, Weiyun Wang, Zhe Chen, Wenhai Wang, Hao Tian, Lewei Lu, Xizhou Zhu, Tong Lu, et al. 2024a. Mminstruct: A high-quality multi-modal instruction tuning dataset with extensive diversity. _Science China Information Sciences_ , 67(12):1–16. 

- Yuan Liu, Haodong Duan, Yuanhan Zhang, Bo Li, Songyang Zhang, Wangbo Zhao, Yike Yuan, Jiaqi Wang, Conghui He, Ziwei Liu, et al. 2024b. Mmbench: Is your multi-modal model an all-around player? In _European conference on computer vision_ , pages 216–233. Springer. 

- Wufei Ma, Haoyu Chen, Guofeng Zhang, Celso M de Melo, Alan Yuille, and Jieneng Chen. 2024. 3dsrbench: A comprehensive 3d spatial reasoning benchmark. _arXiv preprint arXiv:2412.07825_ . 

- Kenneth Marino, Mohammad Rastegari, Ali Farhadi, and Roozbeh Mottaghi. 2019. Ok-vqa: A visual question answering benchmark requiring external knowledge. In _Proceedings of the IEEE/cvf conference on computer vision and pattern recognition_ , pages 3195–3204. 

- Nora S. Newcombe, Janellen, Huttenlocher, I. Campari, Nora S. Janellen Huttenlocher, and Janellen Huttenlocher. 2000. Making space: The development of spatial representation and reasoning. 

- Yasumasa Onoe, Sunayana Rane, Zachary Berger, Yonatan Bitton, Jaemin Cho, Roopal Garg, Alexander Ku, Zarana Parekh, Jordi Pont-Tuset, Garrett Tanzer, Su Wang, and Jason Baldridge. 2024. DOCCI: Descriptions of Connected and Contrasting Images. In _ECCV_ . 

- Jordi Pont-Tuset, Jasper Uijlings, Soravit Changpinyo, Radu Soricut, and Vittorio Ferrari. 2020. Connecting vision and language with localized narratives. In _ECCV_ . 

- Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. 2021. Learning transferable visual models from natural language supervision. In _International conference on machine learning_ , pages 8748–8763. PMLR. 

- Viresh Ranjan, Udbhav Sharma, Thu Nguyen, and Minh Hoai. 2021. Learning to count everything. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 3394–3403. 

   - Peter Young, Alice Lai, Micah Hodosh, and Julia Hockenmaier. 2014. From image descriptions to visual denotations: New similarity metrics for semantic inference over event descriptions. _Transactions of the Association for Computational Linguistics_ , 2:67–78. 

   - Xiang Yue, Yuansheng Ni, Kai Zhang, Tianyu Zheng, Ruoqi Liu, Ge Zhang, Samuel Stevens, Dongfu Jiang, Weiming Ren, Yuxuan Sun, et al. 2024. Mmmu: A massive multi-discipline multimodal understanding and reasoning benchmark for expert agi. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 9556–9567. 

   - Zheyuan Zhang, Fengyuan Hu, Jayjun Lee, Freda Shi, Parisa Kordjamshidi, Joyce Chai, and Ziqiao Ma. 2024. Do vision-language models represent space and how? evaluating spatial frame of reference under ambiguities. _Preprint_ , arXiv:2410.17385. 

   - Bolei Zhou, Hang Zhao, Xavier Puig, Tete Xiao, Sanja Fidler, Adela Barriuso, and Antonio Torralba. 2019. Semantic understanding of scenes through the ade20k dataset. _International Journal of Computer Vision_ , 127:302–321. 

- Shuai Shao, Zeming Li, Tianyuan Zhang, Chao Peng, Gang Yu, Xiangyu Zhang, Jing Li, and Jian Sun. 2019. Objects365: A large-scale, high-quality dataset for object detection. In _Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)_ . 

- Oleksii Sidorov, Ronghang Hu, Marcus Rohrbach, and Amanpreet Singh. 2020. Textcaps: a dataset for image captioning with reading comprehension. In _Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part II 16_ , pages 742–758. Springer. 

- Amanpreet Singh, Vivek Natarajan, Meet Shah, Yu Jiang, Xinlei Chen, Dhruv Batra, Devi Parikh, and Marcus Rohrbach. 2019. Towards vqa models that can read. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ . 

- Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan, Jinze Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, et al. 2024. Qwen2-vl: Enhancing vision-language model’s perception of the world at any resolution. _arXiv preprint arXiv:2409.12191_ . 

- An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, et al. 2024. Qwen2. 5 technical report. _arXiv preprint arXiv:2412.15115_ . 

- Shukang Yin, Chaoyou Fu, Sirui Zhao, Ke Li, Xing Sun, Tong Xu, and Enhong Chen. 2023. A survey on multimodal large language models. _arXiv preprint arXiv:2306.13549_ . 

## **A 實驗** 

## **A.1 超參數調整** 

為了在硬體限制下達到我們報告的批次大小，我們採用了梯度累積（**gradient accumulation，一種在多個小批次上累積梯度後再進行更新以模擬大批次訓練的技術**）技術。表 4 和表 5 分別整理了訓練 SpaRE-2B 與 SpaRE-7B 模型時，我們進行的超參數搜尋以及最終選定的數值。我們的搜尋範圍涵蓋了不同的學習率 (LR)、批次大小、訓練輪數 (epochs)、優化器 (optimizer)、預熱步數 (warm-up steps)、隨機丟棄率 (dropout rate) 以及學習率排程。針對這兩個模型，最優超參數的抉擇都是根據模型在獨立保留集（**held-out subset，未參與訓練的測試數據集**）上的表現來決定的。 

|超參數|嘗試範圍|最終選定|
|---|---|---|
|學習率 (Learning rate)|1 × 10⁻⁵, 3 × 10⁻⁵|3 × 10⁻⁵|
|批次大小 (Batch size)|32, 64|64|
|訓練輪數 (Epochs)|1, 2, 3|2|
|優化器 (Optimizer)|AdamW, AdamW8bit|AdamW8bit|
|預熱步數 (Warm-up steps)|500, 1000, 1500|1000|
|隨機丟棄率 (Dropout)|0, 0.1|0.1|
|學習率排程 (Schedule)|線性 (Linear), 餘弦 (Cos), 固定 (Fixed)|餘弦 (Cos)|

表 4：SpaRE-2B 訓練超參數搜尋及最終選定值總覽。 

|超參數|嘗試範圍|最終選定|
|---|---|---|
|學習率 (Learning rate)|3 × 10⁻⁴, 1 × 10⁻⁴|1 × 10⁻⁴|
|批次大小 (Batch size)|32, 64|64|
|訓練輪數 (Epochs)|1, 2, 3|2|
|優化器 (Optimizer)|AdamW, AdamW8bit|AdamW|
|預熱步數 (Warm-up steps)|500, 1000, 1500|1000|
|隨機丟棄率 (Dropout)|0, 0.1|0.1|
|學習率排程 (Schedule)|線性 (Linear), 餘弦 (Cos), 固定 (Fixed)|餘弦 (Cos)|

表 5：SpaRE-7B 訓練超參數搜尋及最終選定值總覽。 

## **B 流程消融實驗** 

接下來，我們將說明針對「問答對生成」和「原始資料集篩選」這兩個關鍵步驟所進行的消融實驗（**Ablation Studies，透過逐一拆除或替換系統的某些部件，來研究其對整體效能影響的實驗方法**）。 

## **B.1 問答生成消融實驗** 

我們隨機抽取了 100 個樣本，並使用不同規模的 Qwen2.5 指令微調模型（包含 0.5B、1.5B、3B 和 7B 版本）來從原始描述中生成合成問答對。接著，我們用人工方式檢查每個樣本中的問答對。 

|模型|空間相關性|問答對數量|
|---|---|---|
|0.5B|0.17|4.8|
|1.5B|0.93|13.6|
|3B|0.89|17|
|7B|0.86|14|

表 6：不同 Qwen2.5 指令微調模型在問答對生成上的消融實驗結果。 

實測下來，最小的 0.5B 模型表現相當慘烈，因此直接被我們淘汰出局。而在其他幾個模型中，最主要的差別在於「能生出多少問答對」。結果顯示，3B 模型生成的問答對數量最多，成為了我們的首選。雖然它生成的問答中，空間相關性的比例稍微低了一點點，但這並不是壞事——我們可以在後續流程中過濾掉非空間問題；而且在資料集中保留少部分非空間問答，其實有助於防止模型「讀書讀傻了」，避免它過度擬合（overfitting）在空間推理上而喪失了通用能力。考慮到運算資源的限制，加上較小規模的模型已經表現得有模有樣，我們實驗到 7B 模型就止步了。 

## **B.2 資料集篩選消融實驗** 

我們同樣測試了 0.5B、1.5B、3B 和 7B 的 Qwen2.5 指令微調模型，看看它們在「判斷原始影像描述是否包含空間資訊」這項分類任務上的表現。我們手動檢驗了 100 個分類後的樣本。 

|模型|運算時間|準確率 (Acc)|精確率 (P)|召回率 (R)|F1 值 (F1)|
|---|---|---|---|---|---|
|0.5B|1x|0.33|1|0.20|0.33|
|1.5B|1.26x|0.60|1|0.56|0.71|
|3B|1.42x|0.57|1|0.54|0.70|
|7B|1.49x|0.63|1|0.58|0.73|

表 7：不同 Qwen2.5 指令微調模型在資料集篩選任務上的消融實驗結果。其中 Acc 代表準確率，P 代表精確率，R 代表召回率，F1 代表 F1 值。 

同樣地，考慮到運算資源的上限，以及較小模型表現已達標，我們測試到 7B 之後就收工了。值得一提的是，在這項篩選任務中，「精確率 (Precision)」是我們最看重的指標。因為一旦出現「偽陽性」（**False Positive，指明明描述裡沒有空間關係，模型卻誤判為有**），就會將無效的描述送進問答生成流程，這會導致模型產生嚴重的幻覺，進而搞砸後續的訓練成果。 

## **C 定性分析** 

## **C.1 回答生成** 

我們在圖 4 中展示了更多 SpaRE 模型與同類視覺語言模型的實際回答對比案例。 

## **D 提示詞** 

我們展示了用於 VQA 資料集分析以及問答對生成的提示詞。 

## **D.1 資料集分析提示詞** 

在表 8 中，我們展示了用於分析 VQA 資料集以識別描述中空間關係的提示詞。該提示詞要求模型判斷給定的描述是否包含空間關係，從而幫助篩選出相關樣本以供進一步分析或生成問答對。 

根據下方詳細的影像描述，生成一個 JSON 格式的問答對清單。問題應完全聚焦於物體之間的空間關係，包括它們的位置、朝向、距離以及任何定義其相對位置的相關互動。請避免問答中出現空間細節之外的內容。 

輸出格式應如以下範例： [ {"question": <問題>, "answer": <回答>}, . . . ] 

- 關於空間關係，可以考慮詢問以下內容： - 位置與方向：物體所處的位置（例如：左、右、上、下）。 -相對距離與鄰近度：物體彼此之間的距離有多近或多遠。 - 朝向與角度：物體任何顯著的角度或朝向（例如：傾斜、旋轉）。 - 前景與背景層次：哪些元素處於前景、中景或背景。 - 邊界與邊緣：物體如何與邊緣對齊或融入背景。 - 陰影與反射的互動：陰影相對於物體的位置，或物體在表面上的反射。 

- 重疊與分層：如果物體重疊或分層，哪些物體在上方或後方。 - 比例與尺寸對比：基於空間線索的物體相對尺寸。 

僅輸出 JSON 內容，並以 ‘[’ 開頭和 ‘]’ 結尾。 

判斷下方提供的描述是否包含空間關係： **{description}** 

表 8：用於識別描述中空間關係的提示詞。 

影像描述： **{description}** 

表 9：基於聚焦空間關係的描述生成問答對的提示詞。 

## **E 人工評估** 

研究團隊的一名成員手動驗證了資料集中 400 個條目的樣本，以評估其品質 and 準確性。具體的篩選過程如下。 

## **D.2 問答生成提示詞** 

## **E.1 樣本量** 

我們使用有限母體（**finite population，指研究對象的數量是有限且可以確定的總體**）公式來確定所需的樣本量： 

在表 9 中，我們展示了用於從聚焦於空間關係的影像描述中生成問答對 (QA pairs) 的提示詞。該提示詞指示模型生成一個問答對的 JSON 清單，其中每個問題都圍繞空間細節展開，例如物體的位置、朝向、距離和互動。提示詞中指定了輸出格式，並引導模型僅關注空間關係，同時排除無關的問題。 

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0013-19.png)

其中 _N_ = 455,494（資料集大小），_Z_ = 1.96（95% 信心水準），_p_ = 0.5（最大變異數），而 _E_ = 0.05（誤差範圍）。將這些數值代入公式後，我們得到 _n_ ≈ 384，為了讓評估結果更具穩健性，我們將其四捨五入至 400。 

## **F 結果來源** 

對於主實驗結果表（表 3），所有數值均使用多模態評估工具箱 VLMEvalKit (Duan et al., 2024) 以及我們針對未支援基準測試所撰寫的自訂評估程式碼計算得出。以下，我們將說明使用外部資料來源或需要特殊處理的具體情況。 

VSR (Liu et al., 2023a)、What’s Up (Kamath et al., 2023) 和 3DSRBench (Ma et al., 2024) 的隨機基準線（random baseline）數據均直接取自基準測試的原作者論文。對於 VSR 和 What's Up，我們使用自己開發的評估程式碼測試了所有模型。 

為了節省 API 呼叫成本，針對 GPT-4o-mini 和 GPT-4o，我們從 VSR、What’s Up A 和 What’s Up B 中各隨機抽樣了 100 個範例進行評估。而對於 3DSRBench，我們則直接採用了 Ma 等人 (2024) 論文中報告的這兩個模型的結果。 

我們並沒有在通用視覺語言基準測試中填寫 GPT-4o 和 GPT-4o-mini 的結果，因為這些基準測試的核心目的只是為了確認：進行空間推理微調後，模型的通用視覺語言任務效能並不會發生顯著退化。 

## **G 資料集** 

## **G.1 超詳細描述** 

我們在圖 5、圖 6 和圖 7 中，分別展示了來自 DOCCI (Onoe et al., 2024)、Localized Narratives (Pont-Tuset et al., 2020) 和 PixMo-Cap (Deitke et al., 2024) 三個資料集的影像描述對範例。
