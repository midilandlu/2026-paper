---
sourceTitle: "How Cerebras Built Its Enterprise Knowledge Base"
sourceUrl: "https://www.cerebras.ai/blog/how-we-built-our-knowledge-base"
sourceRequestedUrl: "https://www.cerebras.ai/blog/how-we-built-our-knowledge-base"
sourceAuthor: "Isaac Tai, Daniel Kim, Mike Gao"
sourceCoverImage: "https://cdn.sanity.io/images/e4qjo92p/production/e16846d802e8869641cca284f224e49925584c38-1200x630.png?w=1200&h=630&fit=max&auto=format"
sourceSummary: "See how Cerebras built an enterprise AI knowledge base that connects Slack, code repositories, documentation, and custom data sources."
sourceAdapter: "generic"
sourceCapturedAt: "2026-07-22T04:19:07.034Z"
sourceConversionMethod: "defuddle"
sourceKind: "generic/article"
sourceLanguage: "en"
title: "Cerebras 如何構建其企業級 AI 知識庫：整合 Slack、程式碼與跨系統架構解析"
summary: "深入剖析 Cerebras 如何打造每日處理超過 15,000 次查詢的企業級 AI 知識庫。從多路混合檢索 (Hybrid Retrieval)、RRF 倒數排名融合、Slack 對話萃取 (Distillation & Bursting)，到 MCP 協定與端到端 Agent 系統架構的全方位實務經驗。"
language: "zh-TW"
---

# Cerebras 如何構建其企業級 AI 知識庫：整合 Slack、程式碼與跨系統架構解析

> **作者：** Isaac Tai, Daniel Kim, Mike Gao  
> **原文連結：** [How Cerebras Built Its Enterprise Knowledge Base](https://www.cerebras.ai/blog/how-we-built-our-knowledge-base)

我們的員工每天向內部 AI 知識庫提出超過 **15,000 個問題**。自 3 個月前上線以來，它已成為公司內部被最廣泛採用的工具之一，同時服務於人類員工、自動化腳本以及 AI 代理人 (Agents)。

在 Cerebras，我們的工程團隊涵蓋資料中心維運、晶片設計、硬體研發、模型訓練、推論最佳化、雲端平台等多個領域。隨著每年數百名新同仁加入，我們的通訊頻道總是充斥著相似的重複提問：

> *「請問在哪裡可以找到 X？」*  
> *「誰是負責 Y 領域的專家？」*  
> *「Z 的定義與用法是什麼？」*  

為此，我們建構了 **Cerebras Knowledge**，旨在將同仁與 AI 系統無縫連結至高價值的關鍵資訊。

![Cerebras 企業級 AI 知識庫垂直分層架構圖](diagrams/fig-001-architecture-stack.svg)

---

### 在資料存放的源頭直接對接 (Meeting Data Where It Lives)

在大型組織內部尋找資訊歷來是一大挑戰。資料高度散落在各個獨立工具中，幾乎每隔幾個季度，就會有人提出相同的理想化方案：「讓我們把所有資料都集中記錄到同一個平台上吧！」然而，建立「單一真實來源 (Single Source of Truth)」的夢想在現實實踐中極少成功。

資訊總是產生在最方便、最符合工作習慣的地方：文件的修訂註記、Slack 的討論串、GitHub 的代码 PR，以及 Jira 的任務狀態元資料。這些平台都是針對特定領域歷經多年產品工程最佳化的成果。要求工程師在 Google Docs 裡面討論代碼 Pull Request，體驗絕對會非常糟糕。

因此，我們設定的設計原則是：**盡可能不改變使用者現有的行為習慣**。在資料收集端，這意味著必須直接從各個原生平台進行資料擷取。

---

### 知識庫的架構剖析 (Anatomy of a Knowledge Base)

我們的企業知識庫主要提供三大核心能力：

1. **內部資料收集與儲存平台** (Data Collection & Storage)
2. **高效能資料查詢平台** (Query Platform)
3. **身分驗證、授權控管、稽核與分析層** (AuthZ/AuthN & Auditing)

系統的核心是一個單一的 **Postgres 資料表**，專門存放來自跨系統來源的嵌入向量 (Embeddings)、原始摘要以及元資料 (Metadata)。系統會持續即時攝取全公司的資料，並維護一個隨時可供查詢的資料儲存庫。

我們希望資料介面保持簡潔，又能通用於大多數資料型態，同時讓 Cerebras 的其他開發者能輕鬆擴充自訂連接器 (Connectors)。最終架構刻意維持極簡設計：從 Slack 討論串到晶片網表 (Netlists)，所有來源的資料最終都寫入同一張嵌入資料表中，且表中的任何內容都能立即透過統一介面查詢：

![多資料來源匯入單一可查詢嵌入資料表](diagrams/fig-002-data-sources-embeddings.svg)

每個資料來源只需定義資料內容、連線機制以及抓取頻率。無論資料來自 Slack、程式碼庫、文檔系統或自訂資料庫，產出的每一筆嵌入向量資料列都遵循完全相同的標準介面。

---

### Slack 對話資料處理

Slack 是我們系統中最關鍵的資料來源，因為全公司最新、最即時的工程討論與問題排解都發生在這裡。

![Slack Socket 模式即時處理與蒸餾流程](diagrams/fig-003-slack-ingestion-flow.svg)

#### 如何處理非結構化的 Slack 對話

起初我們測試了直接對原始 Slack 文字進行向量嵌入 (Embeddings) 的效果，但很快發現**單靠向量搜尋 (Vector Search) 並不足以精確比對所有相關資料**。

Slack 對話訊息面臨以下幾大挑戰：
* **資訊密度極度不均**：「好喔沒問題 (hey yeah sure mike)」與一段詳細的核心演算法解釋，在系統中都是一則獨立訊息。
* **訊息長度差異巨大**：在餘弦相似度 (Cosine Similarity) 計算中，較短的訊息經常意外打敗內容更豐富的長訊息。
* **語意嚴重依賴上下文**：單一訊息的完整含義高度依賴前後文對話脈絡。

為了解決這個難題，我們採用了**混合式檢索機制 (Hybrid Retrieval)**。Slack 攝取管道讓每個討論串 (Thread) 能同時透過多種檢索技術被搜尋，各種技術互相補足彼此的短板：

- **全文搜尋 (Full-Text Search)**：精確捕捉向量嵌入容易模糊化的特定 Token，如錯誤代碼字串、參數旗標 (Flag Names)、主機名稱等。當工程師貼上精確的 Error Message 時，字面詞彙比對是最佳證據。
- **向量嵌入搜尋 (Embedding Search)**：捕捉「換句話說 (Paraphrase)」的語意比對。例如詢問「清單載入後還原停滯」與解答「檢查點在 NFS 掛載上卡住」兩者詞彙完全不重疊，但向量相似度能將其精確關聯。(1)
- **逆向檔案頻率 (Inverse Document Frequency, IDF)**：過濾無意義的客套話。「聽起來不錯，謝謝！」在向量空間中可能靠近許多查詢，但因詞彙極其常見，IDF 評分會趨近於 0。
- **時間衰減 (Age Decay)**：對 Slack 答案設定時效性。若兩則討論串回答相同問題，半年前的討論串可能描述的是舊版架構；在相關性相當的情況下，較新的討論串將優先獲得高分。

> [!NOTE]
> **多訊號檢索與評分比對範例 (Search Scoring & Signal Penalization)**
> 
> **搜尋查詢 (Query)：** `“restore hangs after manifest load”` (清單載入後還原停滯)
> 
> 1. 🥇 **2 週前討論串 (Thread)** — **得分最高 (加權勝出)**
>    - *內容：* Checkpoint stalls on the NFS mount — set `CKPT_PREFETCH=4`. (檢查點在 NFS 掛載上卡住，請設定 CKPT_PREFETCH=4)
>    - *訊號評估：* 🟢 換句話說成功比對 (Paraphrase Match) | 🟢 包含罕見詞彙 (`CKPT_PREFETCH`) | 🟢 時效性較新打平勝出
> 
> 2. 🥈 **1 天前訊息 (Message)**
>    - *內容：* `ERR_MANIFEST_TIMEOUT`: restore hangs after manifest load.
>    - *訊號評估：* 🟢 精確字詞比對 (Exact Tokens) | 🟢 包含罕見錯誤碼 (`ERR_MANIFEST_TIMEOUT`)
> 
> 3. 🥉 **8 個月前討論串 (Thread)**
>    - *內容：* restore hangs after manifest load → use `LEGACY_FETCHER=1`.
>    - *訊號評估：* 🟢 字詞比對成功 | 🔴 **時間大幅衰減 (Age Decayed)**
> 
> 4. ❌ **3 小時前訊息 (Message)** — **懲罰剔除 (Penalized)**
>    - *內容：* sounds good, thanks! will try that (聽起來不錯，謝謝！我試試看)
>    - *訊號評估：* 🔴 虛假鄰居 (False Neighbor) | 🔴 無任何罕見詞彙 (No Rare Tokens)

沒有單一評分器是可以完全單獨信任的。每種技術都會產生自己獨立的排名視角，並在查詢時進行融合（詳見 [重新排名 Reranking](#重新排名-reranking)）。

#### Socket Mode 即時連線

為了即時收集資料，我們將 Slack Bot 以 **Socket Mode** 部署於工作區中。Slack 會透過持久化的 WebSocket 主動將所有訊息事件推播給我們，無需持續輪詢 (Polling) Web API，從而避免觸發 API 速率限制 (Rate Limits)。

當訊息事件到達時，系統會立即回應 ACK、利用穩定的 Event ID 進行去重 (Deduplication)，並將訊息放入攝取隊列中。

攝取工作者 (Ingest Consumer) 不會單獨儲存單一訊息，而是會解析該訊息所屬的**完整討論串 (Thread)**，並從 Slack API 重新拉取包含父訊息與所有回覆的完整對話，最終將整個對話串作為單一資料列寫回 Postgres。這確保了儲存的對話內容、參與同仁名單與最後活動時間戳記永遠保持最新。

#### 對話串萃取與結構化 (Threads Distillation)

雖然原始 Slack 文字落地後即可進行關鍵字全文檢索，但為了進行高品質的向量搜尋，我們導入了額外的蒸餾處理流程。(8)

在蒸餾階段，LLM 會分析整條對話串並提取結構化數據：
- 工程師實際會搜尋的**單句標準問題**
- 簡短的對話**內容摘要**
- 最終的**技術解決方案**
- 提及的**系統與程式碼組件名稱**

> [!TIP]
> **LLM 對話蒸餾結構化範例 (Distillation Pipeline)**
> 
> **原始 Slack 討論串 (`#CKPT-SUPPORT / THREAD_8F42`)：**
> * `09:14` **Maya:** Restore stalls after manifest load on the larger cluster. Small runs are fine. (較大叢集上載入 manifest 後還原停滯)
> * `09:17` **Owen:** I can reproduce with 128 shards. The logs stop before cache warmup. (在 128 個分片上記錄到重現)
> * `09:18` **Sam:** My laptop also stalls when it sees Monday. (閒聊客套話)
> * `09:21` **Maya:** Setting `CKPT_PREFETCH=4` makes it complete. The default is too high for the NFS mount. (設定 CKPT_PREFETCH=4 解決)
> 
> **蒸餾產出的結構化 JSON：**
> ```json
> {
>   "question": "Restore hangs after manifest load on large clusters with NFS mount",
>   "summary": "Restore stalls prior to cache warmup when sharded across 128+ nodes on NFS.",
>   "resolution": "Set environment variable CKPT_PREFETCH=4 to reduce NFS concurrency.",
>   "code_refs": ["CKPT_PREFETCH", "WarmShardCache", "Restore"]
> }
> ```

我們對這些提煉後的結構化數據進行向量嵌入並寫入資料庫。在我們的測試中，將非結構化對話標準化為一致格式後，**搜尋準確度獲得了顯著提升**。(7,9)

#### 突發段落過濾 (Bursting)

在實踐中我們遇到另一個問題：長討論串中某些關鍵細節，未必會被納入整體討論串摘要中。

為了強化個別關鍵訊息的訊號，我們引入了 **Bursting (突發對話塊)** 技術。一個 Burst 代表同一作者連續發送的一組訊息。我們會在訊息前加上討論串主題作為上下文脈絡 (Context) 後進行獨立嵌入 (2)，讓藏在角落的解答也能被搜尋到。

為防止低品質垃圾訊息干擾資料庫，每個 Burst 必須通過加權評分門檻才允許嵌入：
1. 包含全語料庫中的**罕見詞彙 (IDF ≥ 4.0)**
2. 合併後的 Burst 長度**至少達 200 個字元**
3. 包含同仁的**表情符號互動 (Reactions)**，提供社交訊號加權

---

### 程式碼儲存庫向量化

最初我們曾質疑是否有必要對程式碼庫進行向量嵌入。隨著 Claude Code 等 CLI 工具的普及，有人認為「grep 就足夠了」。但在參考 Cursor 在大型程式碼庫語意搜尋的實踐經驗後，我們決定進行嘗試。

Cerebras 擁有眾多內部儲存庫，部分儲存庫體積超過 **40 GB**。主要的挑戰在於如何高效保持嵌入向量的即時同步。

#### 使用 CocoIndex 維護程式碼向量

經過多次實驗，我們採用了開源的 **CocoIndex** 框架來處理程式碼庫的向量化。

對於每個儲存庫，我們使用特定程式語言的正則表達式邊界 (Regex Boundaries)，由粗到細進行程式碼切塊 (Chunking)。分割器優先嘗試類別 (Class) 邊界，若區塊過大則退回至方法 (Method) 或更小區塊。單一檔案會在不同細粒度層級產生多筆嵌入紀錄（如檔案級與函式級）。

```cpp
// CheckpointLoader.cc 語言感知邊界切分範例
class CheckpointLoader {
public:
  Status LoadManifest(Path p) {
    auto bytes = fs_.Read(p);
    if (!bytes.ok()) return bytes.status();
    manifest_ = ParseManifest(*bytes);
    return ValidateShards(manifest_);
  }
  
  Status WarmShardCache() {
    for (const auto& shard : manifest_.shards()) {
      cache_.Pin(shard.key());
      stats_.Record(shard.bytes());
    }
    return OkStatus();
  }
  
  Status Restore(RestoreOptions opts) {
    auto lease = coordinator_.Acquire(opts.cluster);
    if (!lease.ok()) return lease.status();
    for (auto id : manifest_.ordered_ids()) {
      RETURN_IF_ERROR(fetcher_.Fetch(id));
    }
    return coordinator_.Release(*lease);
  }
private:
  FileSystem fs_;
  Manifest manifest_;
  ShardCache cache_;
};
```

CocoIndex 將同步元資料維護於 Postgres 中。每次 Commit 提交時，它**僅對變更的程式碼區塊進行重新嵌入與更新**，無需重新計算整座儲存庫。由於同步狀態與向量儲存庫部位於同一 PostgreSQL 中，整體效能極高。

---

### 自訂資料來源擴充 (Custom Data Sources)

許多團隊已有現存的資料庫，不希望強迫將資料遷移至 Slack 或 Wiki。我們將自訂資料源設計為外掛腳本 (Plugin Scripts)。團隊只需提交一個小型 Python 模組，說明如何讀取其系統並輸出符合我們嵌入資料表 Schema 的數據列即可。

只要腳本寫入共用資料庫，其餘檢索與 Agent 堆疊完全無需修改，即可自動具備跨系統查詢能力。

---

### 查詢規劃與工具平行扇出 (Planning & Tool Fan-out)

針對使用者的每個查詢，系統首先執行輕量級的 **Planner (規劃器)** 流程，由 LLM 決定應呼叫哪些檢索工具：

![查詢規劃、工具平行扇出與答案合成流程](diagrams/fig-007-planner-tool-fanout.svg)

主要檢索工具包含：
- `subsystem_index`：各檔案的 LLM 高階摘要
- `search`：跨 Slack、Wiki、代碼與文檔的統一混合檢索向量管道
- `search_slack`：專用的 Slack 對話檢索
- `search_code`：基於 Ripgrep 的精確原始碼比對
- `recent_prs`：與問題相關的近期 GitHub Pull Requests
- `who_knows`：分析過往貢獻並比對特定主題的專家同仁

Planner 根據當前專案範圍與工具說明，發出工具呼叫指令，由 **Executor (執行器)** 平行扇出執行、將結果標準化為統一證據格式，最後交由 **Synthesis LLM** 合成最終解答與出處引用。(4)

---

### 重新排名 (Reranking)

為了防止僅共享字詞但解答不同問題的文件排在前面，我們採用 **倒數排名融合 (Reciprocal Rank Fusion, RRF)** 將各檢索器互不相容的結果進行整合。

RRF 評分公式如下：

$$\text{RRF Score}(d \in D) = \sum_{m \in M} \frac{w_m}{k + r_m(d)}$$

（其中預設權重 $w_m = 1.0$，平滑常數 $k = 60$，$r_m(d)$ 為文件在檢索器 $m$ 中的排名）

```
[多路檢索器原始排名結果]           [RRF 倒數排名融合分數計算]
- 檢索器 1 (Vector Search)   ──┐
- 檢索器 2 (Full-Text GIN)   ──┼─►  RRF 融合分數計算 (k=60)
- 檢索器 3 (Ripgrep Code)   ──┤     1. Class CheckpointLoader  [Score: 0.0792]
- 檢索器 4 (Slack Distill)  ──┘     2. INC-82: Slow Restore    [Score: 0.0776]
                                    3. Wiki: Checkpoint Format [Score: 0.0640]
```

平滑常數使「跨多個檢索器達成共識」的文件優先於「僅在單一檢索器拿第一」的文件。融合後進行去重與數量限制，選出 Top 20 候選項目。

隨後，我們將原始查詢與這 20 個候選項目送入精簡的 **Reranker 模型**進行二次打分 (0-10 分)，保留 Top 10。(6)

最後，我們進行**上下文擴展 (Context Expansion)**：例如若比對到 Wiki 某段落，會自動抓取前後相鄰段落，補齊被 Chunking 切碎的標題與先決條件，提供讀者完整的資訊脈絡。

---

### MCP 協定與 Web UI 架構對比

在檢索層之上，我們同時支援了 **MCP (Model Context Protocol)** 介面與 **Web UI** 兩類使用情境：

![MCP 客戶端與 Web UI 的架構對比](diagrams/fig-009-mcp-vs-webui.svg)

- **MCP 整合**：將檢索原語作為原子化工具 (Atomic Tools) 直接暴露（如 `search_slack`、`search_code`）。工具保持極簡且無 LLM 依賴，由 Client 端（如 Claude Code）擔任編排引擎，彈性高且呼叫成本低。(5)
- **Web UI 介面**：由系統封裝完整的端到端 Agent 流程，包含 Planner（規劃）、Executor（平行執行與標準化）與 Synthesis（答案合成），使用者只需簡單輸入問題即可獲得完整解答與引用。

---

### 專案分區與限定範圍搜尋 (Projects & Scoped Search)

隨著語料庫持續膨脹，「全局無差別搜尋」很快失去實用性。編譯器工程師不希望搜尋結果充斥雲端維運手冊。

我們引入 **Projects (專案)** 作為查詢的作用範圍。一個專案是相關 Slack 頻道、代碼庫、文檔與資料庫的邏輯集合。專案非常輕量，多個專案可彈性共享同一個資料來源（如事件處理頻道），無需重複儲存資料。

![專案分區與共享資料來源關聯架構](diagrams/fig-010-projects-scoped-search.svg)

在同一個專案範疇內，新進工程師無需事先了解複雜的頻道與文檔名稱，就能自動獲得高品質、精確對位的解答。

---

### 結語

Cerebras 內部 AI 知識庫之所以能夠成功，核心在於**「在資訊原生的地方與資料對接」**，而非強迫同仁遷就僵化的單一系統。透過結合多路混合檢索、語意蒸餾、RRF 排名融合與 Agent 靈活編排，我們打造出既能適應真實企業資料動態變化，又能在規模擴張中維持精準度與高效率的搜尋體驗。

---

### 參考文獻 (References)

1. Malkov and Yashunin, [*Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs*](https://arxiv.org/abs/1603.09320), arXiv:1603.09320 / IEEE TPAMI 2018.
2. Anthropic, [*Introducing Contextual Retrieval*](https://www.anthropic.com/news/contextual-retrieval), 2024.
3. Cormack, Clarke, and Büttcher, [*Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods*](https://dl.acm.org/doi/10.1145/1571941.1572114), SIGIR 2009.
4. Li et al., [*Search-o1: Agentic Search-Enhanced Large Reasoning Models*](https://arxiv.org/abs/2501.05366), arXiv:2501.05366, 2025.
5. Anthropic, [*Code Execution with MCP*](https://www.anthropic.com/engineering/code-execution-with-mcp), 2025.
6. Liu et al., [*Lost in the Middle: How Language Models Use Long Contexts*](https://arxiv.org/abs/2307.03172), arXiv:2307.03172, 2023.
7. Anthropic, [*Use XML Tags*](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags).
8. Salesforce/Slack Engineering, *How Slack AI Processes Billions of Messages*.
9. Improving Agents, *Best Nested Data Format*.
10. Cursor, [*Improving Agent with Semantic Search*](https://cursor.com/blog/semsearch), 2025.
