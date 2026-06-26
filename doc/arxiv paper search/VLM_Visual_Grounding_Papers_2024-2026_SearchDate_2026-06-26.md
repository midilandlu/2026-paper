# 提升 VLM 視覺定位 (Visual Grounding) 精度：近兩年核心論文推薦清單

本清單整理了 20 篇近兩年 (2024-2026) 關於提升視覺語言模型 (VLM) 視覺定位精度的精選論文。依照**核心痛點解決度**、**作者權威性**與**研究通用性**，將論文分為五個優先級別 (Tier 1 ~ Tier 5)，幫助您由淺入深、由核心到底層地掌握該領域最新進展。

---

## 🥇 Tier 1: 底層機制改良與免訓練方案 (最高優先度)
本梯次論文直接探討 VLM 為何定位不準，並從訓練動態、內部神經元拆解與空間提示等層面給出通用且極具啟發性的解法。

### 1. Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradients for Visual Grounding
* **發布日期**：2026-05-30
* **作者**：Hee Suk Yoon, Eunseop Yoon, Jaehyun Jang, SooHwan Eom, Ji Woo Hong, Mark Hasegawa-Johnson, Qi Dai, Chong Luo, Chang D. Yoo
* **連結**：[arxiv://2606.00564](https://arxiv.org/pdf/2606.00564v1)
* **摘要**：本研究挑戰了 VLM 蒸餾的標準視角，將損失在數學上分解為「語言先驗」與「視覺定位」。分析發現這兩者的梯度向量幾乎正交，導致常規優化在隱式平衡兩者時走上局部最佳解。為了解決這導致定位能力受限的瓶頸，作者提出「視覺梯度轉向 (Visual Gradient Steering, VGS)」，動態重定向更新向量以優先考慮視覺子空間，大幅超越標準的蒸餾公式。

### 2. Your Large Vision-Language Model Only Needs A Few Attention Heads For Visual Grounding
* **發布日期**：2025-03-08
* **作者**：Seil Kang, Jinyeong Kim, Junhyeok Kim, Seong Jae Hwang
* **連結**：[arxiv://2503.06287](https://arxiv.org/pdf/2503.06287v1)
* **摘要**：本文發現凍結的 LVLM 中，只需依賴極少數的注意力頭（定位頭）即可展現強大的視覺定位能力。研究提出一種簡單有效的「免訓練 (Training-free)」框架，直接利用這三個注意力頭生成的文字到圖像注意力圖來識別目標。此方法無需微調便能達到與現有需微調模型相當的定位性能。

### 3. Visual Position Prompt for MLLM based Visual Grounding
* **發布日期**：2025-03-19
* **作者**：Wei Tang, Yanpeng Sun, Qinying Gu, Zechao Li
* **連結**：[arxiv://2503.15426](https://arxiv.org/pdf/2503.15426v4)
* **摘要**：MLLM 難以將文字描述與精確的圖像位置對齊，主因是缺乏顯式的空間參考。本文提出 VPP-LLaVA，引入「視覺位置提示詞 (Visual Position Prompt, VPP)」，在輸入圖像覆蓋一層可學習的座標軸特徵以提供結構化空間線索。同時發布了 60 萬筆的高品質微調資料集，大幅提升了模型在視覺定位上的表現。

### 4. Transcoders Trace Visual Grounding and Hallucinations in Vision-Language Models
* **發布日期**：2026-05-21
* **作者**：Dimitrios Damianos, Leon Voukoutis, Georgios Skyrianos, Vassilis Katsouros, Georgios Paraskevopoulos
* **連結**：[arxiv://2605.22902](https://arxiv.org/pdf/2605.22902v1)
* **摘要**：使用基於 Transcoders 的函數中心框架，拆解模型計算途徑以了解視覺輸入如何轉為文字。分析證實這些機制的因果途徑專屬於視覺語言互動，並成功提取出預測 VLM 幻覺 (Hallucinations) 的特徵。對於想從神經網路可解釋性 (Mechanistic Interpretability) 角度理解 Grounding 的研究者極具價值。

---

## 🥈 Tier 2: 基準測試、錯誤分析與複雜上下文 (高優先度)
這部分的論文揭示了現有模型在面對多目標、細粒度或醫療圖像時的失敗原因，並提出了評估指標或對比學習方法。

### 5. How Do Medical MLLMs Fail? A Study on Visual Grounding in Medical Images
* **發布日期**：2026-03-15
* **作者**：Guimeng Liu, Tianze Yu, Somayeh Ebrahimkhani, Lin Zhi Zheng Shawn, Kok Pin Ng, Ngai-Man Cheung
* **連結**：[arxiv://2603.14323](https://arxiv.org/pdf/2603.14323v1)
* **摘要**：針對醫療 MLLM 的定位能力進行系統性調查。發現模型常常無法將預測錨定在臨床相關的圖像區域。為此提出 VGRefine，一種在推理階段精煉注意力分佈的方法，完全不需額外訓練即可改善視覺定位。

### 6. Point-It-Out: Benchmarking Embodied Reasoning for Vision Language Models in Multi-Stage Visual Grounding
* **發布日期**：2025-09-30
* **作者**：Haotian Xue, Yunhao Ge, Yu Zeng, Zhaoshuo Li, Ming-Yu Liu, Yongxin Chen, Jiaojiao Fan
* **連結**：[arxiv://2509.25794](https://arxiv.org/pdf/2509.25794v1)
* **摘要**：NVIDIA 參與發表的 Point-It-Out (PIO) 基準測試，評估 VLM 在具身場景中精確視覺定位的能力。包含物件定位、指向與軌跡預測。實驗發現即使是 GPT-4o 這種強大通用模型，在精細視覺定位上也可能敗給特定開源模型。

### 7. MC-Bench: A Benchmark for Multi-Context Visual Grounding in the Era of MLLMs
* **發布日期**：2024-10-16
* **作者**：Yunqiu Xu, Linchao Zhu, Yi Yang
* **連結**：[arxiv://2410.12332](https://arxiv.org/pdf/2410.12332v2)
* **摘要**：提出多上下文視覺定位 (Multi-context visual grounding) 任務，要求模型在多張圖片中基於文字提示定位目標，挑戰了 MLLM 跨圖對比的能力，指出現有 MLLM 與人類之間的顯著落差。

### 8. EPIC-Bench: A Perception-Centric Benchmark for Fine-Grained Embodied Visual Grounding
* **發布日期**：2026-05-16
* **作者**：Haozhe Shan, Xiancong Ren, Han Dong, Haoyuan Shi, Yingji Zhang, Jiayu Hu, Yi Zhang, Yong Dai, Bin Shen, Lizhen Qu, Zenglin Xu, Xiaozhu Ju
* **連結**：[arxiv://2605.17070](https://arxiv.org/pdf/2605.17070v1)
* **摘要**：EPIC-Bench 專注於細粒度具身視覺定位，發現目前 VLM 普遍在物理互動的多目標計數、部分-整體關係理解及可供性區域 (affordance region) 檢測中遭遇瓶頸。

### 9. Multimodal Reference Visual Grounding
* **發布日期**：2025-04-02
* **作者**：Yangxiao Lu, Ruosen Li, Liqiang Jing, Jikai Wang, Xinya Du, Yunhui Guo, Nicholas Ruozzi, Yu Xiang
* **連結**：[arxiv://2504.02876](https://arxiv.org/pdf/2504.02876v2)
* **摘要**：當圖像中出現極度相似的物體時，VLM 常會定位失敗。本文提出引入「參考圖像 (Reference Images)」輔助 VLM，利用大語言模型進行物體比對，結合 Few-shot detection 大幅提升了在極相似物體間的定位精度。

---

## 🥉 Tier 3: 3D 空間與具身視覺定位 (中等優先度)
針對機器人、全景圖像等需要空間幾何理解的 3D 定位場景。

### 10. VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding
* **發布日期**：2024-10-17
* **作者**：Runsen Xu, Zhiwei Huang, Tai Wang, Yilun Chen, Jiangmiao Pang, Dahua Lin
* **連結**：[arxiv://2410.13860](https://arxiv.org/pdf/2410.13860v1)
* **摘要**：提出 VLM-Grounder 框架，動態拼接圖像序列並採用 Grounding-and-Feedback 機制，利用多視角投影在不依賴 3D 點雲與物體先驗的情況下，僅用 2D 圖片實現精確的 3D 零樣本視覺定位。

### 11. Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Models
* **發布日期**：2026-03-18
* **作者**：Kevin Qu, Haozhe Qi, Mihai Dusmanu, Mahdi Rad, Rui Wang, Marc Pollefeys
* **連結**：[arxiv://2603.18002](https://arxiv.org/pdf/2603.18002v1)
* **摘要**：為 2D VLM 提供空間監督，結合全局佈局重建與自我中心視角建模，引入預訓練 3D 模型的相機姿態先驗，強化了基於自然語言的定位與 3D 推理能力。

### 12. ScanReason: Empowering 3D Visual Grounding with Reasoning Capabilities
* **發布日期**：2024-07-01
* **作者**：Chenming Zhu, Tai Wang, Wenwei Zhang, Kai Chen, Xihui Liu
* **連結**：[arxiv://2407.01525](https://arxiv.org/pdf/2407.01525v3)
* **摘要**：提出 3D reasoning grounding 任務與 ScanReason 基準。其 ReGround3D 模型結合多模態大模型，通過推理模組與 3D 定位模組交錯推論，理解人類隱式意圖並找出目標 3D 位置。

### 13. Zero-Shot 3D Visual Grounding from Vision-Language Models
* **發布日期**：2025-05-28
* **作者**：Rong Li, Shijie Li, Lingdong Kong, Xulei Yang, Junwei Liang
* **連結**：[arxiv://2505.22429](https://arxiv.org/pdf/2505.22429v1)
* **摘要**：提出 SeeGround 零樣本框架，使用透視適應模組動態選擇最佳視角，並通過融合對齊模組整合視覺與空間訊號，彌合 2D 模型與 3D 場景間的模態差距。

### 14. PanoGrounder: Bridging 2D and 3D with Panoramic Scene Representations
* **發布日期**：2025-12-24
* **作者**：Seongmin Jung, Seongho Choi, Gunwoo Jeon, Minsu Cho, Jongwoo Lim
* **連結**：[arxiv://2512.20907](https://arxiv.org/pdf/2512.20907v1)
* **摘要**：透過全景圖像作為 2D 到 3D 間的橋樑。全景視圖能直接輸入 VLM 並保留長距離物體關係，並將多視角預測融合回 3D 邊界框，獲得更強的場景推理能力。

---

## 🎖️ Tier 4: 特定領域應用 (醫療與遙測)
特定領域圖像 (如衛星圖、醫療影像) 具有高密度、低對比等特性，需要專門架構。

### 15. GeoGround: A Unified Large Vision-Language Model for Remote Sensing
* **發布日期**：2024-11-16
* **作者**：Yue Zhou 等
* **連結**：[arxiv://2411.11904](https://arxiv.org/pdf/2411.11904v3)
* **摘要**：遙測視覺定位需要處理水平、定向邊界框及分割遮罩。本研究透過 Text-Mask 技術統一不同粒度的輸出，提升了 VLM 在處理高空遙測場景的定位一致性。

### 16. SATGround: A Spatially-Aware Approach for Visual Grounding in Remote Sensing
* **發布日期**：2025-12-09
* **作者**：Aysim Toker, Andreea-Maria Oncescu, Roy Miles, Ismail Elezi, Jiankang Deng
* **連結**：[arxiv://2512.08881](https://arxiv.org/pdf/2512.08881v2)
* **摘要**：透過特殊的控制 Token 介接專用的定位模組，讓 VLM 能同時對語言和空間資訊進行推理，大幅提高了衛星圖像的目標定位精度。

### 17. VividMed: Vision Language Model with Versatile Visual Grounding for Medicine
* **發布日期**：2024-10-16
* **作者**：Lingxiao Luo, Bingda Tang, Xuanzhong Chen, Rong Han, Ting Chen
* **連結**：[arxiv://2410.12694](https://arxiv.org/pdf/2410.12694v2)
* **摘要**：多數醫療影像為 3D，而 VLM 多為 2D。本文讓模型支援 2D 及 3D 影像，並能輸出分割遮罩和實例邊界框，改善了醫療領域的定位精確度。

### 18. Vision-Language Modeling in PET/CT for Visual Grounding of Positive Findings
* **發布日期**：2025-02-01
* **作者**：Zachary Huemann 等
* **連結**：[arxiv://2502.00528](https://arxiv.org/pdf/2502.00528v1)
* **摘要**：建構了自動化管道為 PET/CT 報告產生弱標籤，並訓練了 3D 視覺語言模型。模型整合了 LLM 嵌入與 3D nnU-Net，將文字精準對應至醫療影像位置。

---

## 🔒 Tier 5: 定位技術的安全性與穩健性 (Robustness)
探討目前 VLM 的視覺定位是否存在攻擊漏洞。

### 19. Adversarial Robustness for Visual Grounding of Multimodal Large Language Models
* **發布日期**：2024-05-16
* **作者**：Kuofeng Gao, Yang Bai, Jiawang Bai, Yong Yang, Shu-Tao Xia
* **連結**：[arxiv://2405.09981](https://arxiv.org/pdf/2405.09981v1)
* **摘要**：探討 MLLM 在視覺定位上的對抗穩健性。提出三種攻擊模式誘導模型生成錯誤邊界框，為提高 MLLM 的穩健性提供了 Baseline。

### 20. IAG: Input-aware Backdoor Attack on VLM-based Visual Grounding
* **發布日期**：2025-08-13
* **作者**：Junxian Li, Beining Xu, Simin Chen, Jiatong Li, Jingdi Lei, Haodong Zhao, Di Zhang
* **連結**：[arxiv://2508.09456](https://arxiv.org/pdf/2508.09456v5)
* **摘要**：揭示了 VLM 視覺定位任務中首個後門攻擊方法 IAG，能夠動態生成文字引導的觸發器。證明在維持原有性能的前提下，模型的定位結果可以被惡意操控。
