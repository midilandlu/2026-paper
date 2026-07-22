# VLM 結合 LoRA 微調之論文精選與解析指南
> 本目錄收錄了針對 **複雜表格 (Complex Tables)**、**2D 圖表/圖檔 (2D Charts & Diagrams)** 與 **工程/專業文件 (Engineering & Specialized Documents)** 透過 LoRA 進行 VLM 微調與優化的最新高價值論文。

---

## 📚 論文目錄列表

| 論文編號 | 論文名稱 | 主題領域 | 下載檔名 | 推薦指數 |
| :--- | :--- | :--- | :--- | :---: |
| **2511.18306** | Table Comprehension in Building Codes using Vision Language Models and Domain-Specific Fine-Tuning | 工程法規 / 複雜表格 | `2511.18306_Building_Codes_Table_VLM.pdf` | 🌟🌟🌟🌟🌟 (5/5) |
| **2508.05669** | Fine-Tuning Vision-Language Models for Markdown Conversion of Financial Tables in Malaysian Audited Financial Reports | 財報表格 / Markdown轉碼 | `2508.05669_Financial_Tables_Markdown.pdf` | 🌟🌟🌟🌟半 (4.5/5) |
| **2603.28554** | Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model | 文件檢索與生成 / 系統架構 | `2603.28554_Hydra_Doc_Retrieval_Generation.pdf` | 🌟🌟🌟🌟半 (4.5/5) |
| **2604.03157** | Chart-RL: Policy Optimization Reinforcement Learning for Enhanced Visual Reasoning in Chart Question Answering | 2D 統計圖表 / RL + LoRA | `2604.03157_Chart_RL_VLM_Reasoning.pdf` | 🌟🌟🌟🌟 (4.0/5) |
| **2605.11634** | Unlocking UML Class Diagram Understanding in Vision Language Models | 2D 工程圖 / UML架構圖 | `2605.11634_UML_Class_Diagram_VLM.pdf` | 🌟🌟🌟🌟 (4.0/5) |
| **2604.11970** | INDOTABVQA: A Benchmark for Cross-Lingual Table Understanding in Bahasa Indonesia Documents | 跨語言表格 / 視覺問答 | `2604.11970_INDOTABVQA_Cross_Lingual_Table.pdf` | 🌟🌟🌟半 (3.5/5) |

---

## 📑 各文章詳細摘要與導讀

### 1. Table Comprehension in Building Codes using Vision Language Models and Domain-Specific Fine-Tuning
* **ArXiv ID**: `2511.18306`
* **本地檔案**: [2511.18306_Building_Codes_Table_VLM.pdf](./2511.18306_Building_Codes_Table_VLM.pdf)
* **摘要內容**: 建築規範與工程標準文件包含大量用於確保安全與合規的表格。然而，傳統 NLP 與一般通用 VLM 在面對複雜排版、跨行標題（Multi-row headers）及跨儲存格（Merged cells）時常出現理解偏差。本研究對比了「圖像直輸入 (Direct)」與「轉 LaTeX 後輸入 (Indirect)」兩種管道，並利用 LoRA 對主流開源 VLM 進行領域特定微調。
* **應用場景**: 建築法規、工程圖紙/規範文件、合規審查自動化系統與專業領域 RAG。
* **方法與亮點**:
  * 證實「直接將表格圖像餵給 VLM」相比「間接轉化為 LaTeX 代碼」表現出更高的資訊提取準確率。
  * 採用 **LoRA (Low-Rank Adaptation)** 微調後，**Qwen2.5-VL-3B-Instruct** 的相對準確率提升高達 **100%+**。
  * 證明輕量化微調能在極低算力成本下，大幅適應高密度的專業結構化表格。
* **推薦閱讀指數**: 🌟🌟🌟🌟🌟 (5/5)
  * **推薦理由**: 最貼合「工程文件與複雜表格」的應用需求，對於實務上如何對輕量 VLM (3B) 進行領域適應具有極高的實驗參考價值。

---

### 2. Fine-Tuning Vision-Language Models for Markdown Conversion of Financial Tables...
* **ArXiv ID**: `2508.05669`
* **本地檔案**: [2508.05669_Financial_Tables_Markdown.pdf](./2508.05669_Financial_Tables_Markdown.pdf)
* **摘要內容**: 本論文針對審計財務報告中包含旋轉版面、多層表頭及隱含結構的複雜表格，提出將其精確轉換為 Markdown 格式的高保真 VLM 解決方案。
* **應用場景**: 財務報告解析、PDF/掃描件文檔結構化轉碼、自動化數據提取 Pipeline。
* **方法與亮點**:
  * 建構了包含 2,152 組高品質圖像-文本對的訓練集，並對 **Qwen2.5-VL-7B** 進行 LoRA SFT。
  * 提出全指標評估框架：LLM-as-a-judge 加上創新的 **Markdown Tree-Edit-Distance-based Similarity (TEDS)**。
  * 微調後的模型達到 **92.20%** 的綜合準確率與 **96.53%** 的 Markdown TEDS 分數，表現擊敗了 GPT-4o、Gemini 2.5 Flash 等大型閉源模型，且大幅降低推論延遲。
* **推薦閱讀指數**: 🌟🌟🌟🌟半 (4.5/5)
  * **推薦理由**: 如果您的目標是將複雜表格「文字與結構轉碼」成 Markdown 供後續分析，本篇論文的微調策略與評估指標（Markdown TEDS）非常有實用價值。

---

### 3. Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model
* **ArXiv ID**: `2603.28554`
* **本地檔案**: [2603.28554_Hydra_Doc_Retrieval_Generation.pdf](./2603.28554_Hydra_Doc_Retrieval_Generation.pdf)
* **摘要內容**: 視覺文件理解（Visual Document Understanding）通常需要「檢索模型」與「生成模型」雙模型並存，導致顯存與維運成本加倍。Hydra 提出單一 VLM 兼具 ColBERT 式 Late-Interaction 向量檢索與自回歸生成雙重能力。
* **應用場景**: 海量文件/圖表庫檢索、Multi-modal Document RAG 系統架構。
* **方法與亮點**:
  * 設計了**可開關的單一 LoRA Adapter**：開啟 LoRA 時產生多向量 Embedding 進行檢索；關閉 LoRA 時精確恢復基礎模型的生成品質。
  * 顯存佔用從 28.85 GB 降至 10.77 GB（4B 模型下降 62.7%），解決雙模型部署昂貴問題。
* **推薦閱讀指數**: 🌟🌟🌟🌟半 (4.5/5)
  * **推薦理由**: 系統層面的巧妙設計！展示了如何巧妙運用 LoRA 作為「功能模組開關」，適合想建構高效能 Visual Document RAG 的架構師。

---

### 4. Chart-RL: Policy Optimization Reinforcement Learning for Enhanced Visual Reasoning in Chart Question Answering...
* **ArXiv ID**: `2604.03157`
* **本地檔案**: [2604.03157_Chart_RL_VLM_Reasoning.pdf](./2604.03157_Chart_RL_VLM_Reasoning.pdf)
* **摘要內容**: 當前 VLM 在 2D 統計圖表問答 (CQA) 中常遇到數值提取不精確、隱含空間關係理解困難等瓶頸。Chart-RL 引入強化學習 (RL) 與策略優化（Policy Optimization），強化模型的視覺感知與邏輯推理能力。
* **應用場景**: 2D 數據視覺化圖表（條形圖、折線圖、餅圖）分析與智慧數據問答。
* **方法與亮點**:
  * 將策略優化 RL 框架與 LoRA (r=32, alpha=32) 結合，僅需單張 GPU 即可進行高效訓練。
  * 微調後的 **Qwen3-VL-4B-Instruct** 在 ChartQAPro 數據集上精確度達 63.4%，超越未微調 8B 模型（58.0%），推論延遲從 31 秒降至 9 秒。
* **推薦閱讀指數**: 🌟🌟🌟🌟 (4.0/5)
  * **推薦理由**: 展示了除了 SFT 之外，結合 **RL + LoRA** 優化 VLM 視覺推理能力的新趨勢。

---

### 5. Unlocking UML Class Diagram Understanding in Vision Language Models
* **ArXiv ID**: `2605.11634`
* **本地檔案**: [2605.11634_UML_Class_Diagram_VLM.pdf](./2605.11634_UML_Class_Diagram_VLM.pdf)
* **摘要內容**: 雖然 VLM 在自然照片上表現優異，但在工程類 2D 圖表（如 UML 類別圖、架構圖）的理解上嚴重落後。本研究建立了包含 16,000 組圖像-問題-答案的三元組基準資料集。
* **應用場景**: 2D 工程架構圖、UML 類解圖、系統流程圖自動化理解與代碼生成。
* **方法與亮點**:
  * 構建專屬的工程圖表 VQA 數據集。
  * 證明僅透過 LoRA 輕量微調，較小的模型即可大幅超越大型基礎模型 (如 Qwen 3.5 27B)，有效補足 VLM 在符號化 2D 工程圖表的短板。
* **推薦閱讀指數**: 🌟🌟🌟🌟 (4.0/5)
  * **推薦理由**: 專門針對「2D 結構圖/工程圖檔」的理解痛點，對軟體工程與系統圖解分析很有幫助。

---

### 6. INDOTABVQA: A Benchmark for Cross-Lingual Table Understanding in Bahasa Indonesia Documents
* **ArXiv ID**: `2604.11970`
* **本地檔案**: [2604.11970_INDOTABVQA_Cross_Lingual_Table.pdf](./2604.11970_INDOTABVQA_Cross_Lingual_Table.pdf)
* **摘要內容**: 針對包含有框、無框、彩色等不同視覺風格的文件表格，評估 VLM 在單語及跨語言視覺表格問答上的表現落差。
* **應用場景**: 多語言文件表格問答、非典型/無邊框表格解析。
* **方法與亮點**:
  * 對 7B 級別 VLM 進行 LoRA 微調，帶來 17.8% 的顯著準確率提升。
  * 發現提供表格的**空間區域座標 (Spatial Priors)** 作為額外 Prompt 輸入，能額外帶來 4~7% 的效能增幅。
* **推薦閱讀指數**: 🌟🌟🌟半 (3.5/5)
  * **推薦理由**: 揭示了在表格問答中加入「空間邊界座標」引導（Spatial Prompting）對微調模型帶來的正向增益。

---
*文件建立時間: 2026-07-22*
