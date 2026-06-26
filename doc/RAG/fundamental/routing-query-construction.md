---
title: "Routing and Query Construction"
url: "https://div.beehiiv.com/p/routing-query-construction"
requestedUrl: "https://div.beehiiv.com/p/routing-query-construction"
author: "Divyanshu Dixit"
coverImage: "imgs/img-001-RAG_-_QC_and_Routing.jpg"
siteName: "Latest and Greatest"
publishedAt: "2024-02-22T17:00:00.000Z"
summary: "Speak the language of your database"
adapter: "generic"
capturedAt: "2026-06-20T06:00:39.740Z"
conversionMethod: "defuddle"
kind: "generic/article"
language: "zh-TW"
---

# 路由與查詢建構 (Routing and Query Construction)

說你資料庫的語言 (Speak the language of your database)

![](imgs/routing-query-construction/img-001-RAG_-_QC_and_Routing.jpg)

接續 [RAG - 你說什麼？](https://app.beehiiv.com/posts/110f398a-8ce2-4d4f-a4dc-102e453404ab)

今天我們進入路由 (routing) 和查詢建構 (query construction)，這應該能完成進階 RAG 流程的第一部分。所以，讓我們開始吧！

## 路由 (Routing)：

一旦我們充分理解了問題，接下來就要決定將該問題導向何處。你的資料可能有多個資料庫和向量儲存庫，而答案可能在其中任何一個裡面。這就是路由發揮作用的地方。基於使用者查詢和預先定義的選項，LLM 可以決定：

a) 正確的資料來源
b) 要執行什麼動作：例如，進行摘要還是語意搜尋
c) 是否同時執行多個選項並彙整結果 [(「多重路由功能」)](https://docs.llamaindex.ai/en/stable/module_guides/querying/router/root.html)

以下是幾種「路由」查詢的方法：

**a) 邏輯路由 (Logical routing)：** 在這種情況下，我們讓 LLM 使用預先定義的路線來決定參考知識庫的哪一部分。這對於建立非確定性鏈 (non-deterministic chains) 很有用，其中一個步驟的輸出會引導到下一個步驟。

**b) 語意路由 (Semantic routing)：** 一種根據上下文透過提示詞來增強使用者查詢的強大方式。這有助於 LLM 快速、具成本效益地做出決策，以選擇要採取的路線（選項可以是預先定義的或自訂的），從而產生確定性的輸出。

![](imgs/routing-query-construction/img-002.png)[

來源：Codegpt.co

](https://blog.codegpt.co/semantic-router-enhancing-control-in-llm-conversations-68ce905c8d33)

## 查詢建構 (Query Construction)：

好的，現在我們已經有了路由器定義的路線，我們準備好發送查詢了嗎？答案是……看情況！

前面提到的查詢轉換技術對於完全非結構化的資料儲存庫效果很好，但大多數資料都存放在某種形式的結構化資料庫中。這意味著在思考查詢建構時，必須將資料庫的類型牢記在心。

![](imgs/routing-query-construction/img-003.png)[

來源：Langchain 部落格

](https://blog.langchain.dev/query-construction/)

我們很容易假設 LLM 會用自然語言與我們互動。這當然不是真的——與你互動的資料儲存庫決定了它所使用的語言。從使用 SQL 的關聯式資料庫，到具有相關結構化元數據 (metadata) 的非結構化資料，在建構查詢時都必須考慮資料庫的查詢語言。

![](imgs/routing-query-construction/img-004.png)[

來源：Langchain 部落格

](https://blog.langchain.dev/query-construction/)

**a.** [自我查詢檢索器 (Self-query retriever)](https://python.langchain.com/docs/modules/data_connection/retrievers/self_query)（文字轉元數據過濾器）：存放在向量儲存庫中且具有清晰元數據文件的非結構化資料，就可以使用這種檢索器。任何使用者問題（自然語言）都會被分解為一個查詢和一個過濾器（例如按年份、電影、藝術家）。透過提高發送給 LLM 以回答使用者查詢的資料品質，可以顯著提升問答流程的效能。

![](imgs/routing-query-construction/img-005.png)[

來源：Hard Kothari 於 X

](https://x.com/HardKothari/status/1717549379056275563?s=20)

**b. Text 2 SQL (文字轉 SQL)：** 人們普遍發現 LLM 在 Text2SQL 方面表現相當糟糕，過去一年有很多新創公司專注於解決這個問題。從創建虛構的資料表和欄位，到使用者查詢中的拼字錯誤，出錯的方式相當多。考慮到這些資料庫有多普遍，人們已經探索了許多方法來幫助 LLM 建立準確的 SQL 查詢。什麼方法最有效可能非常取決於你的知識庫，所以再次強調，沒有一個通用的規則。建立、迭代、修復！

- 建立資料表 (Create Table) + 選擇 3 筆資料 (Select 3)：在深入更進階的技術之前，這是建立模型在你的資料庫上表現基準的最直接方式。提示詞設計包含每個資料表的 CREATE TABLE 描述，接著是在 SELECT 語句中的三個範例資料列。

![](imgs/routing-query-construction/img-006.png)[

]
- 少樣本範例 (Few shot example)：提供幾個問答對作為範例，讓 LLM 了解如何建構查詢，你可以很快看到準確度提高 10-15%。根據範例的品質和所使用的模型，如果提供更多範例，準確度可能會更高。在後者有許多範例的情況下，將它們儲存在向量儲存庫中，並透過對輸入查詢進行語意搜尋來動態選擇幾個範例，可能是合理的作法。

![](imgs/routing-query-construction/img-007.png)[

來源：Arxiv

](https://arxiv.org/abs/2305.12586)

- anyscale 的優秀團隊也有一篇很棒的部落格文章，概述了從微調 (fine tuning) 帶來的顯著改善，連結如下供您閱讀：
	![](imgs/routing-query-construction/img-008.png)[
	來源：Anyscale
	](https://www.anyscale.com/blog/fine-tuning-llama-2-a-comprehensive-case-study-for-tailoring-models-to-unique-applications)
- RAG + 微調 (Fine-tuning)：如下文所述，使用 schema RAG 和 ICL 微調模型，與僅將整個 schema 添加到提示詞中並希望 LLM 能夠理解相比，準確度可提高 20% 以上。
	![](imgs/routing-query-construction/img-009.png)
	[來源：](https://scale.com/blog/text2sql-fine-tuning) [Scale.com](http://scale.com/)
- 使用者拼字錯誤：與包含正確拼字的向量儲存庫對比搜尋專有名詞，可以成為減少特定使用者錯誤的好方法。在 Text2SQL 的早期，這是一個特別令人討厭的問題。

**c. Text 2 Cypher (文字轉 Cypher)：** 這是圖形資料庫 (graph databases) 專用的，圖形資料庫用於表達無法用表格形式表達的關係。Cypher 是這類資料庫的查詢語言。text-2-Cypher 是一項複雜的任務，因此建議在進行任何此類嘗試時使用 GPT4。

在檢索準確度方面，知識圖譜 (Knowledge Graphs) 是一個強而有力的案例，因此重要的是要著眼於表格和 2D schemas 之外的資料格式。

![](imgs/routing-query-construction/img-010.png)[

來源：Arxiv

](https://arxiv.org/abs/2311.07509)

到這裡，我們已經探索了各種查詢轉換、建構和路由的技術，這應該有助於我們說出使用者查詢應該導向的那個資料庫的語言。

接下來，我們將進入名為索引 (Indexing) 的流程部分，在那裡我們將更深入地探討分割 (splitting)、索引嵌入 (indexing embeddings) 以及如何將它們設定好以實現準確的檢索。