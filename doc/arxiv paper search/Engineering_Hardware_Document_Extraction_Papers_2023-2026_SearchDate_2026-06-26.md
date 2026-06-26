# 專屬領域探討：機電設計、電路圖與電子規格書解析之核心論文推薦清單

針對您的特定領域（機構設計圖、機構規格、電路設計圖、電子產品規格書），為您搜尋並整理了近三年 (2023-2026) 專注於 **工程圖面解析 (Engineering Drawings)**、**電路圖理解 (Circuit Schematics)** 與 **資料表數據提取 (Datasheets)** 的核心論文。

工程領域的文件因為包含極端密集的視覺符號（如 GD&T 幾何公差、電路符號）與高度結構化的長表格，目前學界與業界最新的突破皆圍繞在**「混合式視覺檢測＋VLM」**以及**「多模態檢索與 Agent 生成」**。

---

## 📊 推薦閱讀優先順序與分類重點

### 🥇 Tier 1: 2D 機構工程圖面解析 (Mechanical Engineering Drawings)
針對工程製圖（包含尺寸標註、公差符號、標題圖框等）的自動化解析與結構化提取。

**1. From Drawings to Decisions: A Hybrid Vision-Language Framework for Parsing 2D Engineering Drawings into Structured Manufacturing Knowledge**
*   **推薦理由**：完美契合機構設計圖需求。結合了物體偵測與輕量級 VLM，專門提取圖面中的 GD&T（幾何公差）、尺寸標註與文字註解。
*   **發布日期**：2025-06-20
*   **作者**：Muhammad Tayyab Khan, Lequn Chen, Zane Yong, et al.
*   **連結**：[http://arxiv.org/abs/2506.17374v2](http://arxiv.org/abs/2506.17374v2)
*   **摘要**：傳統 OCR 在解析 2D 工程圖時，常因複雜排版與旋轉文字而失敗。本文提出一個混合視覺語言框架，先利用 YOLOv11-obb 定位並擷取傾斜的邊界框 (OBB) 圖像區塊，接著利用微調後的輕量級 VLM (Donut 與 Florence-2) 解析出結構化輸出。在包含 9 個關鍵類別的真實機械圖紙資料集上，該框架達到了 93.5% 的 F1 分數。

**2. BLUEPRINT Rebuilding a Legacy: Multimodal Retrieval for Complex Engineering Drawings and Documents**
*   **推薦理由**：針對巨量遺留工程圖庫的自動化元資料提取與檢索。
*   **發布日期**：2026-02-12
*   **作者**：Ethan Seefried, Ran Eldegaway, Sanjay Das, et al.
*   **連結**：[http://arxiv.org/abs/2602.13345v1](http://arxiv.org/abs/2602.13345v1)
*   **摘要**：數十年的工程圖面被鎖在缺乏元資料的遺留檔案庫中。Blueprint 是一個具備版面感知能力的多模態檢索系統。它偵測標準的圖紙區域，應用受區域限制的 VLM-OCR 來正規化識別碼（如 DWG、零件號），自動生成可用於跨廠區搜尋的結構化元資料。

### 🥈 Tier 2: 電路設計圖與網表重建 (Circuit Schematics & Netlists)
如何將 PDF/圖片格式的電路圖，精準轉換回可驗證的結構化數據或 Netlist。

**3. SINA: A Circuit Schematic Image-to-Netlist Generator Using Artificial Intelligence**
*   **推薦理由**：專門解決從「電路圖影像」反向生成機器可讀「網表 (Netlist)」的痛點。
*   **發布日期**：2026-01-29
*   **作者**：Saoud Aldowaish, Yashwanth Karumanchi, Kai-Chen Chiang, et al.
*   **連結**：[http://arxiv.org/abs/2601.22114v1](http://arxiv.org/abs/2601.22114v1)
*   **摘要**：SINA 是一個全自動的電路圖影像到網表的生成器。它結合了深度學習來偵測元件、連通組件標記 (CCL) 來提取連線、OCR 來擷取元件參考代號，並使用視覺語言模型 (VLM) 進行可靠的參考代號分配。實驗中達到了 96.47% 的網表生成準確率。

**4. VLM-CAD: VLM-Optimized Collaborative Agent Design Workflow for Analog Circuit Sizing**
*   **推薦理由**：探討 VLM 如何透過圖形拓樸結構，消除判讀複雜工程原理圖時的視覺幻覺。
*   **發布日期**：2026-01-12
*   **作者**：Guanyuan Pan, Shuai Wang, Yugui Lin, et al.
*   **連結**：[http://arxiv.org/abs/2601.07315v4](http://arxiv.org/abs/2601.07315v4)
*   **摘要**：為解決 VLM 判讀電路圖時的空間盲點與邏輯幻覺，提出 VLM-CAD 工作流。它整合了神經符號結構解析模組 (Image2Net)，將原始像素轉換為明確的拓樸圖與結構化 JSON，將 VLM 的決策錨定在確定性事實上，成功輔助類比電路的尺寸設計。

### 🥉 Tier 3: 電子規格書與高密度資料解析 (Datasheets & Visual-Dense Documents)
從極長且非結構化的規格書(Datasheet)中提取參數與邏輯表。

**5. DS2SC-Agent: A Multi-Agent Automated Pipeline for Rapid Chiplet Model Generation**
*   **推薦理由**：這篇精準擊中如何從「充滿未結構化表格與文字的 Datasheet」自動提取資料並轉換為工程代碼，極具參考價值。
*   **發布日期**：2026-03-22
*   **作者**：Yiwei Wu, Yifan Wu, Yunhao Xiong, et al.
*   **連結**：[http://arxiv.org/abs/2603.21190v1](http://arxiv.org/abs/2603.21190v1)
*   **摘要**：傳統工程中，從原始 Datasheet 手動建立行為模型耗時且易錯。本文提出首個端到端自動化管線 DS2SC-Agent，利用多 Agent 協作框架，將長篇非結構化文件解析、SystemC 核心程式碼建構、測試平台生成與自適應除錯整合，成功將複雜 Datasheet 轉換為功能正確的晶片模型。

**6. Index Light, Reason Deep: Deferred Visual Ingestion for Visual-Dense Document Question Answering**
*   **推薦理由**：當您有大量電子規格書需要建立知識庫時，此文提出了比傳統 RAG 更好的「視覺檢索策略」。
*   **發布日期**：2026-02-15
*   **作者**：Tao Xu
*   **連結**：[http://arxiv.org/abs/2602.14162v2](http://arxiv.org/abs/2602.14162v2)
*   **摘要**：在充滿視覺資訊的工程文件（如橋樑設計圖、電路問答）中，傳統的向量檢索會完全失效。本文提出「延遲視覺攝取 (DVI)」框架，在預處理階段不使用 VLM，僅靠文件目錄與圖號建立層級索引；推理時先用文字檢索定位，再將原始圖紙與問題送給 VLM 分析。這讓橋樑工程圖的 QA 準確率從 24.3% 大幅躍升至 65.6%。

### 🎖️ Tier 4: 工程文件多模態基準測試 (Benchmarks)
評估您的系統時可以參考的標準。

**7. AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding**
*   **發布日期**：2026-01-08
*   **摘要**：針對建築與工程 (AEC) 圖紙建立的多模態基準測試。結果發現，儘管現代 VLM 在 OCR 上表現極佳，但在涉及圖紙符號理解、空間推理與物件計數（如算有幾扇窗戶）時，準確率仍然很低（僅 40-55%），證明了在工程圖紙上仍需要特定領域的表徵與工具輔助。

**8. DRAGON: A Benchmark for Evidence-Grounded Visual Reasoning over Diagrams**
*   **發布日期**：2026-04-28
*   **摘要**：針對圖表、電路圖等進行視覺推理的基準測試。要求模型不僅要回答正確，還必須在地圖或電路圖上畫出「支撐其答案的視覺證據邊界框」，以防止 VLM 依賴幻覺盲目猜測。
