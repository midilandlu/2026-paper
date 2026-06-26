# 從 PDF 與 PPT 中提取複雜表格：近兩年核心技術與論文推薦清單

為您搜尋並整理了近兩年 (2024-2026) 關於**從 PDF 與 PPT 檔案中讀取複雜表格內容**的重點論文。隨著多模態大型語言模型（MLLMs / VLMs）的崛起，焦點已從「依賴傳統 OCR 外掛程式」轉向了**「端到端（End-to-End）的文件影像直接理解」**以及**「跨頁面 / 複雜版面表格重建」**。

---

## 📊 核心技術發展趨勢與推薦優先順序

針對您的需求，以下整理了四大技術領域的重點論文，並依照**推薦優先度**進行排序：

### 🥇 Tier 1: 端到端多模態文件解析 (End-to-End Document Parsing)
這類技術放棄了傳統的破碎流程，直接讓視覺語言模型 (VLM) 讀取整張 PDF 或 PPT 影像，並輸出包含表格的 Markdown 或 HTML 結構。**對於充滿不規則排版的 PPT 最具潛力。**

**1. Qianfan-OCR: A Unified End-to-End Model for Document Intelligence**
*   **推薦理由**：將文件解析、版面分析與表格提取統一，能直接將複雜版面的 PDF 與截圖精準轉為 Markdown，是非常實用的企業級端到端方案。
*   **發布日期**：2026-03-11
*   **作者**：Daxiang Dong, Mingming Zheng, Dong Xu, et al.
*   **連結**：[http://arxiv.org/abs/2603.13398v1](http://arxiv.org/abs/2603.13398v1)
*   **摘要**：我們提出了 Qianfan-OCR，這是一個 4B 參數的端到端視覺語言模型，將文件解析、版面分析與文件理解統一在單一架構中。它執行直接的影像到 Markdown 轉換，並支援包括表格提取、圖表理解等任務。為了彌補端到端 OCR 中缺乏顯式版面分析的問題，我們提出了 Layout-as-Thought，這是一個可選的思考階段，在產生最終輸出之前生成結構化的版面表示（邊界框、元素類型與閱讀順序）。

**2. NVIDIA Nemotron Parse 1.1**
*   **推薦理由**：專為視覺密集的 PDF 與圖表截圖設計，輕量化且準確的 OCR 與表格提取方案。
*   **發布日期**：2025-11-25
*   **作者**：Kateryna Chumachenko, Amala Sanjay Deshmukh, Jarno Seppanen, et al.
*   **連結**：[http://arxiv.org/abs/2511.20478v1](http://arxiv.org/abs/2511.20478v1)
*   **摘要**：Nemotron-Parse-1.1 是一個輕量級的文件解析與 OCR 模型。它在一般 OCR、Markdown 格式化、結構化表格解析以及從圖片、圖表和圖解中提取文字等方面具備強大的能力，並支援視覺密集文件的長序列輸出。

**3. TableSeq: Unified Generation of Structure, Content, and Layout**
*   **推薦理由**：將表格「結構」、「內容」與「座標」融合為單一序列生成問題，大幅降低解析時間與複雜度。
*   **發布日期**：2026-04-17
*   **作者**：Laziz Hamdi, Amine Tamasna, Pascal Boisson, Thierry Paquet
*   **連結**：[http://arxiv.org/abs/2604.16070v1](http://arxiv.org/abs/2604.16070v1)
*   **摘要**：TableSeq 是一個純圖像、端到端的框架，用於聯合表格結構識別、內容識別與單元格定位。模型將這些任務表述為單一的序列生成問題：一個解碼器產生交錯的 HTML 標籤、單元格文字和離散座標 Token 流，從而在統一的自回歸序列中對齊邏輯結構、文本內容與單元格幾何形狀。

### 🥈 Tier 2: Agent 驅動與文件到表格 (Agentic & Document-to-Table)
處理極度複雜或非標準化的報告時，單次推論容易出錯。結合 Agent 多步驗證與抽絲剝繭是最新主流。

**4. AutoSAM: an Agentic Framework for Automating Input File Generation for the SAM Code with Multi-Modal Retrieval-Augmented Generation**
*   **推薦理由**：**強烈推薦於工程規格應用！** 該文專注於從充滿系統圖、設計報告與數據表的非結構化 PDF/PPT 中，使用 Agent 與多模態 RAG 準確提取結構化表格參數，防幻覺能力極佳。
*   **發布日期**：2026-03-25
*   **作者**：Zaid Abulawi, Zavier Ndum Ndum, Eric Cervi, Rui Hu, Yang Liu
*   **連結**：[http://arxiv.org/abs/2603.24736v1](http://arxiv.org/abs/2603.24736v1)
*   **摘要**：提出 AutoSAM，一個將大型語言模型代理與檢索增強生成（結合使用者指南與理論手冊）相結合的框架，並配有專門分析 PDF、圖像、試算表與文字檔的工具。它能攝取非結構化的工程文件（包含系統圖、設計報告與數據表），將與模擬相關的參數提取為人類可審核的中間表示，並合成驗證過、與求解器相容的輸入文件。

**5. DTBench: A Synthetic Benchmark for Document-to-Table Extraction**
*   **推薦理由**：探討從 PDF 提取表格後，LLM 如何解決資料衝突與推理問題。
*   **發布日期**：2026-02-14
*   **作者**：Yuxiang Guo, Zhuoran Du, Nan Tang, Kezheng Tang, Congcong Ge, Yunjun Gao
*   **連結**：[http://arxiv.org/abs/2602.13812v3](http://arxiv.org/abs/2602.13812v3)
*   **摘要**：Document-to-table (Doc2Table) 提取在目標綱要下從非結構化文件衍生結構化表格。我們提出了一個逆向的 Table2Doc 範式，設計了一個多 Agent 合成工作流，從真實表格生成文件，用以建立 DTBench 基準測試，藉此評估模型在推理、忠實度與衝突解決上的挑戰。

### 🥉 Tier 3: 跨頁表格與複雜版面處理
針對真實世界的 PDF 報告中「跨越數頁的表格」與「極端複雜結構」。

**6. Agentar-Fin-OCR**
*   **推薦理由**：針對長篇距、跨頁斷裂的 PDF 報告，提出「跨頁內容整合演算法」，能自動將切斷的表格無縫接合。
*   **發布日期**：2026-03-11
*   **作者**：Siyi Qian, Xiongfei Bai, Bingtao Fu, et al.
*   **連結**：[http://arxiv.org/abs/2603.11044v1](http://arxiv.org/abs/2603.11044v1)
*   **摘要**：針對金融領域的長 PDF 文件提出的解析系統。透過跨頁內容整合演算法恢復跨頁的連續性，並利用結構錨點 (Structural Anchor Tokens) 來定位表格單元格，有效應對極端版面與跨頁的表格解析難題。

**7. Dr. DocBench: A Comprehensive Benchmark for Expert-Level and Difficult Document Parsing**
*   **推薦理由**：專門針對「專家領域」的高難度文件建立測試基準，凸顯現有解析器在複雜專業圖表與跨頁佈局下的缺陷。
*   **發布日期**：2026-05-31
*   **作者**：Minglai Yang, Xinyan Velocity Yu, Pengyuan Li, et al.
*   **連結**：[http://arxiv.org/abs/2606.01393v1](http://arxiv.org/abs/2606.01393v1)
*   **摘要**：提出 Dr. DocBench，這是一個針對專家級文件解析的難度感知基準測試，重點針對化學方程式、樂譜、複雜表格與跨頁排版等現有解析器容易失敗的案例進行大規模評估與分析。

### 🎖️ Tier 4: 超越字串比對的語義評估機制
探討如何科學地衡量從 PDF 解析出來的表格是否真正具備「可用性」。

**8. Beyond String Matching: Semantic Evaluation of PDF Table Extraction**
*   **推薦理由**：捨棄傳統呆板的字串與樹編輯距離比對，利用 LLM 作為裁判進行表格「語義」評估。
*   **發布日期**：2026-03-19
*   **作者**：Pius Horn, Janis Keuper
*   **連結**：[http://arxiv.org/abs/2603.18652v2](http://arxiv.org/abs/2603.18652v2)
*   **摘要**：傳統基於規則的指標無法捕捉表格內容的語義等價性。本研究應用 LLM 作為裁判進行語義表格評估，發現基於 LLM 的評估與人類判斷的相關性（r=0.93）遠高於現行使用的 TEDS（r=0.68），為 PDF 解析工具的選擇提供了務實的指南。

**9. Semantic Triplet Restoration: A Novel Protocol for Hierarchical Table Understanding in Large Language Models**
*   **推薦理由**：有效降低處理深層合併儲存格的 token 消耗與複雜度。
*   **發布日期**：2026-05-29
*   **作者**：Yibin Zhao, Fangxin Shang, Dingrui Yang, Yuqi Wang
*   **連結**：[http://arxiv.org/abs/2605.31550v1](http://arxiv.org/abs/2605.31550v1)
*   **摘要**：提出語義三元組恢復 (STR) 協定，將表格中每一個儲存格改寫為 <行實體, 特徵路徑, 值> 的原子事實，取代冗長的 HTML/Markdown 中間表示法。這降低了模型推斷合併單元格與多層標頭的負擔，尤其在處理超長表格上下文時具有優勢。
