# VLM (Vision-Language Models) 論文導讀與全覽指南
> 本目錄 (`D:\2026 paper\doc\VLM`) 收錄了 **15 篇** 關於 **VLM 視覺語言模型** 的最新前沿論文，涵蓋 **LoRA 領域微調與表格/文件解析**、**視覺定位與分割 (Visual Grounding & Segmentation)**、**空間推理與 3D 定位 (Spatial Reasoning & 3D)** 以及 **模型自我修正機制 (Self-Correction)** 等關鍵主題。

---

## 📚 目錄與全覽對照表

| # | 論文編號 | 論文名稱 | 主要分類 | 本地檔案 | 推薦指數 |
| :-: | :--- | :--- | :--- | :--- | :-: |
| 1 | **2511.18306** | Table Comprehension in Building Codes using VLMs | 表格/工程文件 | `2511.18306_Building_Codes_Table_VLM.pdf` | 🌟🌟🌟🌟🌟 |
| 2 | **2508.05669** | Fine-Tuning VLMs for Markdown Conversion of Financial Tables | 表格/轉碼 | `2508.05669_Financial_Tables_Markdown.pdf` | 🌟🌟🌟🌟半 |
| 3 | **2603.28554** | Hydra: Unifying Document Retrieval and Generation in a Single VLM | 文件檢索與生成 | `2603.28554_Hydra_Doc_Retrieval_Generation.pdf` | 🌟🌟🌟🌟半 |
| 4 | **2604.03157** | Chart-RL: Policy Optimization RL for Chart QA | 2D圖表 / RL | `2604.03157_Chart_RL_VLM_Reasoning.pdf` | 🌟🌟🌟🌟 |
| 5 | **2605.11634** | Unlocking UML Class Diagram Understanding in VLMs | 2D圖表 / 架構圖 | `2605.11634_UML_Class_Diagram_VLM.pdf` | 🌟🌟🌟🌟 |
| 6 | **2604.11970** | INDOTABVQA: Benchmark for Cross-Lingual Table Understanding | 表格 / 跨語言 | `2604.11970_INDOTABVQA_Cross_Lingual_Table.pdf` | 🌟🌟🌟半 |
| 7 | **2605.07141** | Qwen3-VL-Seg: Unlocking Open-World Referring Segmentation | 像素級分割 | `2605.07141v1_Qwen3-VL-Seg...pdf` | 🌟🌟🌟🌟🌟 |
| 8 | **2507.05673** | R-VLM: Region-Aware VLM for Precise GUI Grounding | GUI自動化 / Grounding | `2507.05673v1_R-VLM...pdf` | 🌟🌟🌟🌟半 |
| 9 | **2601.13633** | EGM: Efficient Visual Grounding Language Models | 推理加速 / 定位 | `2601.13633v1_Scaling...pdf` | 🌟🌟🌟🌟 |
| 10 | **2404.19128** | Q-GroundCAM: Quantifying Grounding in VLMs via GradCAM | Grounding可解釋性 | `2404.19128v1_Q-GroundCAM...pdf` | 🌟🌟🌟半 |
| 11 | **2504.20648** | SpaRE: Enhancing Spatial Reasoning in VLMs with Synthetic Data | 空間推理 / 數據擴增 | `2504.20648v1_SpaRE...pdf` | 🌟🌟🌟🌟半 |
| 12 | **2505.21500** | ViewSpatial-Bench: Multi-perspective Spatial Localization | 空間推理 / 多視角 | `2505.21500v2_ViewSpatial-Bench...pdf` | 🌟🌟🌟🌟 |
| 13 | **2505.22429** | Zero-Shot 3D Visual Grounding from Vision-Language Models | 3D定位 / Zero-Shot | `2505.22429v1_Zero-Shot 3D...pdf` | 🌟🌟🌟🌟 |
| 14 | **2404.06510** | Can VLMs Correct Semantic Grounding Errors By Themselves? | 自我修正 (Self-Correction) | `2404.06510v2_Can Large...pdf` | 🌟🌟🌟🌟 |
| 15 | **2606.13156** | Iterative Visual Thinking and the Self-Correction Mirage | 自我修正 / 批判性思考 | `2606.13156v1_Iterative...pdf` | 🌟🌟🌟🌟🌟 |

---

## 📑 第一部分：LoRA 微調、表格與專業文件解析

### 1. Table Comprehension in Building Codes using Vision Language Models and Domain-Specific Fine-Tuning
* **ArXiv ID**: `2511.18306`
* **本地檔案**: [2511.18306_Building_Codes_Table_VLM.pdf](./2511.18306_Building_Codes_Table_VLM.pdf)
* **摘要內容**: 建築法規與工程標準文件包含大量用於確保安全與合規的表格。本研究對比「圖像直輸入 (Direct)」與「轉 LaTeX 後輸入 (Indirect)」兩種管道，並利用 LoRA 對主流開源 VLM 進行領域特定微調。
* **應用場景**: 建築法規、工程規範文件、合規審查自動化系統與專業領域 RAG。
* **方法與亮點**:
  * 證實「直接將表格圖像餵給 VLM」比「間接轉化為 LaTeX」表現更佳。
  * 採用 LoRA 微調後，**Qwen2.5-VL-3B-Instruct** 的相對準確率提升高達 **100%+**。
* **推薦閱讀指數**: 🌟🌟🌟🌟🌟 (5/5) — **極力推薦**。對工程文件、規範與複雜表格有直接實務參考價值。

---

### 2. Fine-Tuning Vision-Language Models for Markdown Conversion of Financial Tables...
* **ArXiv ID**: `2508.05669`
* **本地檔案**: [2508.05669_Financial_Tables_Markdown.pdf](./2508.05669_Financial_Tables_Markdown.pdf)
* **摘要內容**: 本論文針對審計財務報告中包含旋轉版面、多層表頭及隱含結構的複雜表格，提出將其精確轉換為 Markdown 格式的高保真 VLM 解決方案。
* **應用場景**: 財務報告解析、PDF/掃描件文檔結構化轉碼、自動化數據提取 Pipeline。
* **方法與亮點**:
  * 對 **Qwen2.5-VL-7B** 進行 LoRA 微調，提出 **Markdown Tree-Edit-Distance-based Similarity (TEDS)** 指標。
  * 達到 92.20% 綜合準確率與 96.53% Markdown TEDS 分數，表現超越 GPT-4o 與 Gemini 2.5 Flash。
* **推薦閱讀指數**: 🌟🌟🌟🌟半 (4.5/5) — **高度推薦**。極度適合表格 OCR/結構化轉碼 Markdown 的應用。

---

### 3. Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model
* **ArXiv ID**: `2603.28554`
* **本地檔案**: [2603.28554_Hydra_Doc_Retrieval_Generation.pdf](./2603.28554_Hydra_Doc_Retrieval_Generation.pdf)
* **摘要內容**: 視覺文件理解通常需要「檢索模型」與「生成模型」雙模型並存。Hydra 提出單一 VLM 兼具 Late-Interaction 向量檢索與自回歸生成雙重能力。
* **應用場景**: 海量文件/圖表庫檢索、Multi-modal Document RAG 系統架構。
* **方法與亮點**:
  * 設計**可開關的單一 LoRA Adapter**：開啟 LoRA 時產生多向量 Embedding 進行檢索；關閉時回復純生成模式。
  * 顯存佔用下降 59%~62%，擺脫雙模型部署的昂貴成本。
* **推薦閱讀指數**: 🌟🌟🌟🌟半 (4.5/5) — **高度推薦**。巧用 LoRA 作為功能開關，架構極具參考價值。

---

### 4. Chart-RL: Policy Optimization Reinforcement Learning for Enhanced Visual Reasoning in Chart QA...
* **ArXiv ID**: `2604.03157`
* **本地檔案**: [2604.03157_Chart_RL_VLM_Reasoning.pdf](./2604.03157_Chart_RL_VLM_Reasoning.pdf)
* **摘要內容**: VLM 在 2D 統計圖表問答 (CQA) 中常遇到數值提取不精確問題。Chart-RL 引入強化學習 (RL) 與策略優化（Policy Optimization）結合 LoRA 微調。
* **應用場景**: 2D 數據視覺化圖表（條形圖、折線圖、餅圖）分析與數據問答。
* **方法與亮點**:
  * 結合 Policy Optimization RL 與 LoRA (r=32, alpha=32)，微調後的 Qwen3-VL-4B 精確度達 63.4%（超越 8B 基礎模型的 58.0%），推理延遲由 31 秒降至 9 秒。
* **推薦閱讀指數**: 🌟🌟🌟🌟 (4.0/5) — **推薦**。結合 RL + LoRA 增強 VLM 推理能力的新嘗試。

---

### 5. Unlocking UML Class Diagram Understanding in Vision Language Models
* **ArXiv ID**: `2605.11634`
* **本地檔案**: [2605.11634_UML_Class_Diagram_VLM.pdf](./2605.11634_UML_Class_Diagram_VLM.pdf)
* **摘要內容**: VLM 在工程類 2D 圖表（如 UML 類別圖、架構圖）理解上遠落後於自然照片。本研究建立了包含 16,000 組圖像-問答的三元組基準資料集。
* **應用場景**: 2D 工程架構圖、UML 類解圖、系統流程圖自動化理解與代碼生成。
* **方法與亮點**:
  * 證明僅透過 LoRA 輕量微調，小模型即可輕易超越未微調的大型模型 (如 Qwen 3.5 27B)。
* **推薦閱讀指數**: 🌟🌟🌟🌟 (4.0/5) — **推薦**。專攻 2D 結構圖/工程圖檔的理解痛點。

---

### 6. INDOTABVQA: Benchmark for Cross-Lingual Table Understanding in Bahasa Indonesia Documents
* **ArXiv ID**: `2604.11970`
* **本地檔案**: [2604.11970_INDOTABVQA_Cross_Lingual_Table.pdf](./2604.11970_INDOTABVQA_Cross_Lingual_Table.pdf)
* **摘要內容**: 評估 VLM 在包含有框、無框、彩色等不同視覺風格的文件表格上的單語與跨語言視覺表格問答表現。
* **應用場景**: 多語言文件表格問答、非典型/無邊框表格解析。
* **方法與亮點**:
  * 對 7B 級別 VLM 進行 LoRA 微調帶來 17.8% 準確率提升；加上表格空間座標 (Spatial Priors) 提示可額外增長 4~7%。
* **推薦閱讀指數**: 🌟🌟🌟半 (3.5/5) — **中度推薦**。揭示空間座標 Prompting 的效益。

---

## 👁️ 第二部分：視覺定位、像素級分割與 GUI 自動化 (Grounding & Segmentation)

### 7. Qwen3-VL-Seg: Unlocking Open-World Referring Segmentation with Vision-Language Grounding
* **ArXiv ID**: `2605.07141`
* **本地檔案**: [2605.07141v1_Qwen3-VL-Seg -Unlocking Open-World Referring Segmentation with Vision-Language Grounding.pdf](./2605.07141v1_Qwen3-VL-Seg%20-Unlocking%20Open-World%20Referring%20Segmentation%20with%20Vision-Language%20Grounding.pdf)
* **摘要內容**: 現有 MLLM 視覺定位多停留在 Bounding Box 框選階段，而結合 SAM 等外部分割模型又帶來龐大部署開銷。Qwen3-VL-Seg 提出無 SAM 的參數高效框架，直接將 Bounding Box 轉化為像素級 Referring Segmentation。
* **應用場景**: 像素級精確分割、機器人操作、圖像編輯、開放世界物件指稱分割。
* **方法與亮點**:
  * 設計輕量化 Box-Guided Mask Decoder，僅增加 17M 參數（僅佔 Base 模型 0.4%），完全不需外掛 SAM。
  * 構建包含 300 萬樣本的 SA1B-ORS 資料集與測試基準 ORS-Bench。
* **推薦閱讀指數**: 🌟🌟🌟🌟🌟 (5/5) — **極力推薦**。阿里通義實驗室最新力作，在端到端像素分割與開源生態上有突破性貢獻。

---

### 8. R-VLM: Region-Aware Vision Language Model for Precise GUI Grounding
* **ArXiv ID**: `2507.05673`
* **本地檔案**: [2507.05673v1_R-VLM-Region-Aware Vision Language Model for Precise GUI Grounding.pdf](./2507.05673v1_R-VLM-Region-Aware%20Vision%20Language%20Model%20for%20Precise%20GUI%20Grounding.pdf)
* **摘要內容**: GUI 自動化 Agent（如手機/電腦操作助手）的核心難點在於從混亂的螢幕截圖中精確定位按鈕與圖示。R-VLM 提出了區域感知 (Region-Aware) 框架與 IoU 感知目標函數。
* **應用場景**: UI/GUI 自動化操作 Agent、電腦/手機 Agent 指令執行（AITW、Mind2Web 任務）。
* **方法與亮點**:
  * 採用 Zoomed-in Region Proposal 機制，搭配 IoU-aware 損失函數替代傳統交叉熵損失。
  * 在 ScreenSpot 與 AgentStudio 測試集上，Grounding 準確率顯著提升 13%。
* **推薦閱讀指數**: 🌟🌟🌟🌟半 (4.5/5) — **高度推薦**。GUI Agent 領域必讀，解決細微圖案與按鈕定位的關鍵論文。

---

### 9. EGM: Efficient Visual Grounding Language Models (Scaling Test-time Inference)
* **ArXiv ID**: `2601.13633`
* **本地檔案**: [2601.13633v1_Scaling Test-time Inference for Visual Grounding.pdf](./2601.13633v1_Scaling%20Test-time%20Inference%20for%20Visual%20Grounding.pdf)
* **摘要內容**: 分析發現小 VLM 在定位表現落後大 VLM 的主因在於語言理解而非視覺能力。EGM 提出「多個低成本 Token 匹配少數高成本 Token」的測試時推理加速方案。
* **應用場景**: 高即時性視覺定位、邊緣設備/端側 VLM 部署。
* **方法與亮點**:
  * EGM-Qwen3-VL-8B 在 RefCOCO 上達到 91.4 IoU，推論時間僅 737ms，比 Qwen3-VL-235B（4,320ms）快了 **5.9 倍** 且精確度更高。
* **推薦閱讀指數**: 🌟🌟🌟🌟 (4.0/5) — **推薦**。關注測試階段 (Test-time) 推理效率與模型加速的佳作。

---

### 10. Q-GroundCAM: Quantifying Grounding in Vision Language Models via GradCAM
* **ArXiv ID**: `2404.19128`
* **本地檔案**: [2404.19128v1_Q-GroundCAM- Quantifying Grounding in Vision Language Models via GradCAM.pdf](./2404.19128v1_Q-GroundCAM-%20Quantifying%20Grounding%20in%20Vision%20Language%20Models%20via%20GradCAM.pdf)
* **摘要內容**: 傳統 Pointing Game 指標僅給予 0/1 二元評價，無法反映 VLM 在視覺定位時的信心度與多部位混淆（Uncertainty）。本研究引入基於 GradCAM 的連續定量指標。
* **應用場景**: VLM 可解釋性評估、定位不確定性測量 (Grounding Uncertainty)。
* **方法與亮點**:
  * 提出 IO ratio 物理指標與 NMS 激活分析，量化模型的視覺關注焦點與幻覺偏差。
* **推薦閱讀指數**: 🌟🌟🌟半 (3.5/5) — **中度推薦**。著重於模型診斷與可解釋性評估。

---

## 🧭 第三部分：空間推理、3D 定位與視覺自我修正 (Spatial Reasoning & Self-Correction)

### 11. SpaRE: Enhancing Spatial Reasoning in Vision-Language Models with Synthetic Data
* **ArXiv ID**: `2504.20648`
* **本地檔案**: [2504.20648v1_SpaRE- Enhancing Spatial Reasoning in Vision-Language Models with Synthetic Data.pdf](./2504.20648v1_SpaRE-%20Enhancing%20Spatial%20Reasoning%20in%20Vision-Language%20Models%20with%20Synthetic%20Data.pdf)
* **摘要內容**: 現有 VLM 普遍缺乏空間推理能力（如「在...後面」、「圍繞」、「對立」等長尾空間關係）。本研究利用長文本圖像描述自動生成 45.5 萬組高質量的合成空間問答數據集。
* **應用場景**: 機器人導航、實體 AI (Embodied AI)、真實世界空間問答。
* **方法與亮點**:
  * SpaRE 微調後的模型在 What’s Up 空間基準測試上大幅提升高達 **49%**，且完全不損害通用 VLM 的基礎問答能力。
* **推薦閱讀指數**: 🌟🌟🌟🌟半 (4.5/5) — **高度推薦**。利用高質量數據合成解決空間推理盲點的代表作。

---

### 12. ViewSpatial-Bench: Evaluating Multi-perspective Spatial Localization in Vision-Language Models
* **ArXiv ID**: `2505.21500`
* **本地檔案**: [2505.21500v2_ViewSpatial-Bench Evaluating Multi-perspective Spatial Localization in Vision-Language Models.pdf](./2505.21500v2_ViewSpatial-Bench%20Evaluating%20Multi-perspective%20Spatial%20Localization%20in%20Vision-Language%20Models.pdf)
* **摘要內容**: 揭示現有 VLM 在「相機第一人稱視角 (Egocentric)」表現良好，但在切換到「第三人稱/他者視角 (Allocentric)」時表現暴跌的痛點。
* **應用場景**: 多視角空間定位、跨視角機器人控制。
* **方法與亮點**:
  * 打造 ViewSpatial-Bench 多視角基準，透過多視角數據微調使跨視角定位準確率提升 46.24%。
* **推薦閱讀指數**: 🌟🌟🌟🌟 (4.0/5) — **推薦**。深入剖析 VLM 視角轉換 (Perspective-taking) 能力缺陷。

---

### 13. Zero-Shot 3D Visual Grounding from Vision-Language Models (SeeGround)
* **ArXiv ID**: `2505.22429`
* **本地檔案**: [2505.22429v1_Zero-Shot 3D Visual Grounding from Vision-Language Models.pdf](./2505.22429v1_Zero-Shot%203D%20Visual%20Grounding%20from%20Vision-Language%20Models.pdf)
* **摘要內容**: 傳統 3D Visual Grounding 依賴昂貴的 3D 標註數據。SeeGround 透過 2D VLM 實現無須 3D 訓練的 Zero-Shot 3D 定位。
* **應用場景**: AR/VR 擴增實境、3D 空間物件定位、機器人 3D 視覺。
* **方法與亮點**:
  * 提出 Perspective Adaptation Module（動態選擇最佳渲染視角）與 Fusion Alignment Module。在 ScanRefer 上零樣本表現超越同類基準 7.7%。
* **推薦閱讀指數**: 🌟🌟🌟🌟 (4.0/5) — **推薦**。巧妙利用 2D VLM 升維解決 3D 定位難題。

---

### 14. Can Large Vision-Language Models Correct Semantic Grounding Errors By Themselves?
* **ArXiv ID**: `2404.06510`
* **本地檔案**: [2404.06510v2_Can Large Vision-Language Models Correct Semantic Grounding Errors By Themselvespdf.pdf](./2404.06510v2_Can%20Large%20Vision-Language%20Models%20Correct%20Semantic%20Grounding%20Errors%20By%20Themselvespdf.pdf)
* **摘要內容**: 探索 VLM 能否在不依賴外部工具、微調或 Oracle 反饋的情況下，僅憑多輪 Prompt 自我修正（Self-Correction）定位錯誤。
* **應用場景**: Test-time Prompting 最佳化、模型自我批判與檢驗。
* **方法與亮點**:
  * 將複雜的語意定位拆解為簡易的「二元驗證 (Binary Verification)」任務作為反饋機制，使 GPT-4V/GPT-4o 準確率提升高達 8.4 個百分點。
* **推薦閱讀指數**: 🌟🌟🌟🌟 (4.0/5) — **推薦**。早期探討 VLM 自我修正機制的代表性研討。

---

### 15. Iterative Visual Thinking and the Self-Correction Mirage in VLM Grounding
* **ArXiv ID**: `2606.13156`
* **本地檔案**: [2606.13156v1_Iterative Visual Thinking Teaching Vision-Language Models Spatial Self-Correction through Visual Feedback_.pdf](./2606.13156v1_Iterative%20Visual%20Thinking%20Teaching%20Vision-Language%20Models%20Spatial%20Self-Correction%20through%20Visual%20Feedback_.pdf)
* **摘要內容**: 對當前流行的「讓 VLM 迭代多思考 (Iterative Thinking) 以實現自我修正」給予批判性研析。
* **應用場景**: VLM 評估協議診斷、推理鏈 (Chain-of-Thought) 驗證真偽。
* **方法與亮點**:
  * 揭露許多自我修正論文宣稱的效能提升實為「測試蜃樓 (Measurement Mirage)」—即隱含使用了 Ground-Truth Oracle 來挑選 Trajectory 中的最佳 Step。
  * 證實一旦在無標籤部署規則下，最佳策略是不進行任何迭代（Step 0 即是最佳點）。原因在於 VLM 具備產生好結果的能力，但**缺乏正確自我驗證 (Verification Failure)** 的能力。
* **推薦閱讀指數**: 🌟🌟🌟🌟🌟 (5/5) — **極力推薦**。2026年最新的清流論文！直擊當前自修正/CoT狂熱中的實驗評估陷阱，極具批判思考價值。

---
*文件更新時間: 2026-07-22*
