## **4.6 Qualitative Analysis** 

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0008-04.png)

|Question|Models<br>Answers|
|---|---|
|If I stand at the<br>person’s position<br>facing where it is<br>facing, is the table<br>on the left or right<br>of me?|SpaRE-7B<br>Right<br>✔<br>Qwen2-VL-7B<br>Left<br>✘<br>Qwen2-VL-72B<br>Left<br>✘<br>InternVL2-76B<br>Left<br>✘<br>GPT-4o<br>Left<br>✘|

Figure 2: Comparison of answers provided by different VLMs to a spatial reasoning question. 

In Figure 2, when asked, _“...is the table on the left or right of me?”_ , SpaRE-7B correctly answers _“Right”_ , while the compared VLMs provide incorrect responses. This question is difficult because while the table is on the left, in the viewer’s and thus VLM’s perspective, it is to the right from the perspective of the person shown. This example demonstrates the practical improvements achieved with our method. While questions like this remain challenging for SpaRE VLMs, as discussed shortly, they significantly outperform existing alternatives. We show more examples in Figure 4 in the ap- 

pendix. 

## **4.7 Error Analysis** 

While our performance on VSR and What’s Up is strong, we see relatively weaker performance on 3DSRBench. We observe, consistent with Zhang et al. (2024), that VLMs struggle with _empathetic_ spatial reasoning. That means that they fail to adopt the perspectives of others when reasoning about spatial relations. This egocentric bias, originating from source datasets, is also present in our synthetic dataset. Addressing this will likely require datasets that capture manually annotated information about different frames of reference in a scene. 

## **5 Conclusion** 

In this work, we tackled the lack of spatial reasoning data in VL datasets by generating synthetic QA pairs from hyper-detailed image captions using LLMs. Our approach greatly improves the spatial reasoning of VLMs, as shown by strong gains across benchmarks, without hurting general VL performance. By using rich spatial descriptions to create diverse and accurate QA pairs, we provided the data needed for VLMs to learn and apply spatial reasoning effectively. Our results emphasize the importance of data quality and diversity in training robust VLMs and open new directions for research in robotics, navigation, and extended reality. We hope this work encourages further exploration of synthetic data to address VLM limitations, helping build more capable and versatile multi-modal AI systems. 

## **6 Limitations** 

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0008-14.png)

Figure 3: Ambiguity of spatial relations without an explicit frame of reference: is the plant to the _right_ or _left_ of the bench from the _viewer’s_ or _woman’s_ perspective? 

While our approach significantly improves the spatial reasoning abilities of VLMs, we recognize some limitations. For instance, spatial descriptions 

can be ambiguous without clear frames of reference (FOR) (Levinson, 2003; Liu et al., 2023a). Moreover, we and Zhang et al. (2024) observe that current VLMs fall short in capturing different FORs during spatial reasoning. As shown in Figure 3, whether the plant is to the _right_ or _left_ of the bench depends on whether a viewer-centric or object-centric perspective is used—without specifying the FOR, it is hard to determine the intended meaning. 

In future work, we plan to address this challenge by incorporating explicit FOR annotations into our synthetic data generation pipeline. We also intend to explore more efficient methods for generating synthetic data with large language models and to adapt our approach to other languages with richer morphology. 

## **7 Ethics Statement** 

Our work uses synthetic data generated from hyperdetailed image descriptions to improve spatial reasoning in VLMs. The source data is publicly available and does not contain sensitive information. However, since improved spatial reasoning can affect applications like robotics or navigation, it is important to test these models thoroughly before deployment. We also note that the language models used to generate synthetic data may exhibit biases from their training data. To help the community verify and build on this work, we plan to release our code and data under open-access terms. 

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

## **A Experiments** 

## **A.1 Hyperparameter Tuning** 

To achieve the reported batch sizes, we employed gradient accumulation. Tables 4 and 5 summarize the hyperparameter search and the selected values for training the SpaRE-2B and SpaRE-7B models respectively. The search includes variations in learning rate (LR), batch size, epochs, optimizer, warm-up steps, dropout rate, and learning rate schedule. For both models, the optimal values were chosen based on performance on a held-out subset. 

|Hyperparameter|Tried|Selected|
|---|---|---|
|Learning rate|1_×_10_−_5,3_×_10_−_5|3_×_10_−_5|
|Batch size|32, 64|64|
|Epochs|1, 2, 3|2|
|Optimizer|AdamW, AdamW8bit|AdamW8bit|
|Warm-up steps|500, 1000, 1500|1000|
|Dropout|0, 0.1|0.1|
|Schedule|Linear, Cos, Fixed|Cos|

Table 4: Summary of hyperparameter search and the values selected for SpaRE-2B training. 

|Hyperparameter|Tried|Selected|
|---|---|---|
|Learning rate|3_×_10_−_4,1_×_10_−_4|1_×_10_−_4|
|Batch size|32, 64|64|
|Epochs|1, 2, 3|2|
|Optimizer|AdamW, AdamW8bit|AdamW|
|Warm-up steps|500, 1000, 1500|1000|
|Dropout|0, 0.1|0.1|
|Schedule|Linear, Cos, Fixed|Cos|

Table 5: Summary of hyperparameter search and the values selected for SpaRE-7B training. 

## **B Pipeline Ablations** 

We subsequently describe the ablations that we carried out for QA-pair generation and source dataset filtering. 

## **B.1 QA Generation Ablations** 

We perform ablations on 100 samples using the following Qwen2.5 instruct models to generate synthetic datasets from source descriptions: 0.5B, 1.5B, 3B, and 7B. We manually check the QA pairs in each sample. 

|Model|Spatial relevance|QA pairs|
|---|---|---|
|0.5B|0.17|4.8|
|1.5B|0.93|13.6|
|3B|0.89|17|
|7B|0.86|14|

Table 6: QA pair generation ablation study results for Qwen2.5 instruct models. 

The 0.5B model performs poorly and is discarded. Among the remaining models, the key difference is the number of QA pairs generated. The 3B model generates the most QA pairs, making it the preferred choice, as we can filter non-spatial questions later. While the spatial relevance rate isn’t the highest, the questions generated are still relevant, and including these samples in the dataset helps prevent overfitting to spatial reasoning. We stop at 7B due to computational resource limitations, as the smaller model sizes already perform decently. 

## **B.2 Dataset Filtering Ablations** 

We run ablations on the following Qwen2.5 instruct models for classifying source descriptions with spatial information present: 0.5B, 1.5B, 3B, 7B. We manually check 100 classified samples. 

|Model|Compute Time|Acc|P|R|F1|
|---|---|---|---|---|---|
|0.5B|1x|0.33|1|0.20|0.33|
|1.5B|1.26x|0.60|1|0.56|0.71|
|3B|1.42x|0.57|1|0.54|0.70|
|7B|1.49x|0.63|1|0.58|0.73|

Table 7: Dataset-filtering ablation study results for Qwen2.5 instruct models. Acc refers to accuracy, P refers to precision, R refers to recall, and F1 refers to F1-score. 

We stop at 7B due to computational resource limitations, as the smaller model sizes already perform well enough for our requirements. Additionally, we note that precision is the most important metric, as passing in sample descriptions without actual spatial relations—due to false positives—leads to severe hallucinations, negatively impacting downstream performance. 

## **C Qualitative Analysis** 

## **C.1 Response Generation** 

We show more examples of SpaRE models compared to similar VLMs in Figure 4. 

## **D Prompts** 

We show the prompts we used for the VQA dataset analysis and QA pair generation. 

## **D.1 Dataset Analysis Prompt** 

In Table 8, we present the prompt used for analyzing the VQA dataset to identify spatial relations within descriptions. The prompt asks the model to determine whether a given description contains a spatial relation, helping to filter relevant samples for further analysis or QA pair generation. 

Generate a JSON list of question-answer pairs based on the detailed image description below. The questions should exclusively focus on spatial relations between objects, including their positions, orientations, distances, and any relevant interactions that define their relative locations. Avoid questions outside of spatial details. 

The output should look like: [ {"question": <question>, "answer": <answer>}, . . . ] 

- For spatial relations, consider asking about: - Positions and Directions: Where objects are located (e.g., left, right, above, below). - Relative Distances and Proximity: How close or far objects are from each other. - Orientations and Angles: Any notable angles or orientations of objects (e.g., tilted, rotated). - Foreground and Background Layers: Which elements are in the foreground, middle ground, or background. - Boundaries and Edges: How objects align with edges or blend into the background. - Interaction of Shadows and Reflections: Shadow placement relative to objects, or how objects reflect on surfaces. 

- Overlapping and Layering: If objects overlap or are layered, which ones appear on top or behind. - Scale and Size Comparisons: Relative sizes between objects based on spatial cues. 

Output only the JSON, starting with ‘[’ and ending with ‘]’. 

Determine if the description provided below contains a spatial relation: **{description}** 

Table 8: Prompt for identifying spatial relations in descriptions. 

Image description: **{description}** 

Table 9: Prompt to generate QA pairs from a description focused on spatial relations. 

## **E Human Evaluation** 

A research team member manually validated a sample of 400 entries from the dataset to assess quality and accuracy. The selection process is detailed below. 

## **D.2 QA Generation Prompt** 

## **E.1 Sample Size** 

We determined the sample size to use with the finite population formula: 

In Table 9, we present the prompt used for generating question-answer (QA) pairs from image descriptions focused on spatial relations. The prompt instructs the model to generate a JSON list of QA pairs, with each question centered on spatial details such as object positions, orientations, distances, and interactions. The output format is specified, and the prompt guides the model to focus solely on spatial relationships while excluding non-relevant questions. 

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0013-19.png)

where _N_ = 455 _,_ 494 (dataset size), _Z_ = 1 _._ 96 (95% confidence level), _p_ = 0 _._ 5 (maximum variance), and _E_ = 0 _._ 05 (margin of error). Substituting these values, we obtain _n ≈_ 384, which we round up to 400 for robustness. 

## **F Sources of Results** 

For the main results table (Table 3), values are computed using VLMEvalKit (Duan et al., 2024) and our custom evaluation code for unsupported benchmarks. Below, we outline cases where external sources were used or special handling was required. 

Random baseline numbers for VSR (Liu et al., 2023a), What’s Up (Kamath et al., 2023), and 3DSRBench (Ma et al., 2024) were taken from the benchmark authors. For VSR and What’s Up, we used our evaluation code for all models. 

For GPT-4o-mini and GPT-4o, we sampled 100 examples from VSR, What’s Up A, and What’s Up B to manage costs. For 3DSRBench, we used the results reported in Ma et al. (2024) for these models. 

We did not fill in results for GPT-4o and GPT-4omini under general VL benchmarks, as the purpose of those benchmarks was to confirm that spatial reasoning fine-tuning does not significantly degrade general VL task performance. 

## **G Datasets** 

## **G.1 Hyper-Detailed Descriptions** 

We show examples of image-description pairs from DOCCI (Onoe et al., 2024), Localized Narratives (Pont-Tuset et al., 2020), and PixMoCap (Deitke et al., 2024) in Figures 5, 6, and 7. 