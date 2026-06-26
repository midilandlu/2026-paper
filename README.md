# 2026 Paper 專案翻譯工作流指南

本專案配置了強大的 AI 代理（AI Agent）翻譯與文件解析技能（Skills），旨在幫助您快速、高品質地將各種外文素材（論文、網頁、Markdown）轉換為繁體中文（或其他指定語言）。

## 核心翻譯功能

本專案的翻譯功能基於 `baoyu-translate` 技能，並搭配其他文件解析技能聯動，以支援多種輸入格式。

### 1. 支援的輸入格式與使用方法

您可以直接在對話中對 AI 下達自然語言指令，AI 會自動選擇對應的處理技能：

* **PDF 文件翻譯 (如學術論文)**
  * **指令範例：** 「請幫我翻譯這份 `paper.pdf`」或「將這個 PDF 轉為中文並保留圖片」。
  * **背後運作：** 系統會先自動呼叫 `baoyu-pdf-to-markdown` 將 PDF 解析為乾淨的 Markdown 並自動提取所有圖片儲存到本地，接著交由 `baoyu-translate` 進行高品質翻譯，最終產出圖文並茂的 Markdown 譯文。

* **網頁/URL 翻譯**
  * **指令範例：** 「請翻譯這篇文章：`https://example.com/article`」。
  * **背後運作：** 系統會自動呼叫 `baoyu-url-to-markdown` 抓取網頁內容並轉為 Markdown，隨後傳遞給 `baoyu-translate` 進行翻譯。

* **純文字或 Markdown 檔案翻譯**
  * **指令範例：** 「翻譯 `doc/VLM/article.md`」或「將這段文字改成英文」。
  * **背後運作：** 系統直接使用 `baoyu-translate` 進行翻譯。針對長篇大論，系統會自動進行長文本切塊（Chunking），並保持術語的一致性。

### 2. 進階翻譯模式

`baoyu-translate` 提供了三種翻譯深度，您可以根據需求在提示詞中指定：

1. **快速翻譯 (Quick Mode)**：
   * **適用場景：** 內部參考、短文本、需要快速了解大意。
   * **指令範例：** 「幫我**快速翻譯**這篇文章」、「快翻」。
   * **特點：** 直接進行一次性翻譯，速度最快。

2. **一般翻譯 (Normal Mode - 預設)**：
   * **適用場景：** 部落格文章、一般文件、多數日常需求。
   * **指令範例：** 「翻譯這份文件」。
   * **特點：** 在翻譯前會先進行「內容分析」（分析領域、語氣、專有名詞），建立術語表後再進行翻譯，確保品質與一致性。

3. **精細翻譯 (Refined Mode)**：
   * **適用場景：** 準備發表、出版等級的文章、重要學術論文。
   * **指令範例：** 「請幫我**精翻**這篇論文」或「以出版品質翻譯」。
   * **特點：** 包含四個階段：內容分析 -> 初稿翻譯 -> 專家批評 (Critique) -> 最終潤飾 (Polish)。

### 3. 個人化設定與術語表

AI 在翻譯時會讀取您的偏好設定。您可以透過編輯位於您系統家目錄的設定檔來客製化翻譯風格：

* **設定檔路徑：** `C:\Users\您的使用者名稱\.baoyu-skills\baoyu-translate\EXTEND.md`（或專案內的對應位置）
* **可設定項目：** 預設目標語言（如 `zh-TW`）、預設風格（如 `storytelling`, `academic`）、目標受眾（如 `general`, `technical`），以及**自訂術語表 (Custom Glossary)**。

### 4. 翻譯後處理

當一般模式翻譯完成後，如果系統認為有進一步提升空間，可能會提示您：
> "Translation saved. To further review and polish, reply **繼續潤色** or **refine**."

您只需回覆「繼續潤色」，AI 就會啟動批評與潤飾流程，進一步提升文章的流暢度與專業感。

## ArXiv 論文檢索 (ArXiv MCP Server)

本專案整合了 [arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)，賦予 AI 代理直接在 ArXiv 上檢索與下載學術論文的能力。這讓文獻回顧和追蹤最新研究變得非常輕鬆！

### 支援的 ArXiv 功能
* **論文檢索 (`search_papers`)：** 根據關鍵字檢索 ArXiv 上的論文（例如：「幫我找最新關於 Vision-Language Model 空間推理的論文」）。
* **讀取論文 (`read_paper` / `download_paper`)：** 給定 ArXiv ID，直接讀取或下載論文內容，以便進行進階的翻譯或總結。
* **獲取摘要 (`get_abstract`)：** 快速取得論文摘要，幫助您判斷論文是否符合需求。
* **追蹤主題與通知 (`watch_topic` / `check_alerts`)：** 設定關注的特定研究領域，並定期檢查是否有最新發表的相關論文。
* **引用網路與語義檢索 (`citation_graph` / `semantic_search`)：** 探索文獻引用關係或使用語義搜尋找出相關文章。

**使用範例：**
「請幫我搜尋 ArXiv 上關於 RAG 架構的最新論文，並給我這幾篇的摘要，接著把最相關的下載並翻譯成繁體中文。」

## 文件目錄 (doc/) 結構說明

本專案的 `doc/` 目錄內收集並分類了透過本工作流處理的多種領域研究文獻與教學資料：

* **`doc/RAG/`**
  * 包含檢索增強生成（Retrieval-Augmented Generation, RAG）的相關教學筆記、架構圖和系列文章（如 Query Routing, Indexing, Retrieval, Generation 等進階 RAG 技巧）。
* **`doc/VLM/`**
  * 存放關於視覺語言模型（Vision-Language Models, VLM）的原始 PDF 論文、由 PDF 轉換出的 Markdown 檔案，以及經過翻譯處理的繁體中文版文章，主要側重於 VLM 在空間推理（Spatial Reasoning）、語意定位（Semantic Grounding）等領域的研究。
* **`doc/arxiv paper search/`**
  * 包含由 ArXiv 檢索任務自動產生的文獻彙整報告（Markdown 格式），涵蓋的主題包括硬體文件提取（Hardware Document Extraction）、複雜表格擷取（Complex Table Extraction）、VLM 表格理解以及 Visual Grounding 等最新研究的回顧。
