---
title: "RAG - Say what?"
url: "https://div.beehiiv.com/p/rag-say"
requestedUrl: "https://div.beehiiv.com/p/rag-say"
author: "Divyanshu Dixit"
coverImage: "imgs/img-001-landscape_L_G.jpg"
siteName: "Latest and Greatest"
publishedAt: "2024-02-15T06:04:10.251Z"
summary: "Not the usual beginner RAG tutorial"
adapter: "generic"
capturedAt: "2026-06-20T04:58:11.829Z"
conversionMethod: "defuddle"
kind: "generic/article"
language: "zh-TW"
---

# RAG - 你說什麼？ (RAG - Say what?)

- [
	首頁
	](https://div.beehiiv.com/)
- [
	文章
	](https://div.beehiiv.com/archive)
- RAG - 你說什麼？

這不是一般的 RAG 新手教學

![RAG - Say what?](imgs/rag-say/img-001-landscape_L_G.jpg)

![](imgs/rag-say/img-002.png)[

來源：Langchain

](https://github.com/langchain-ai/rag-from-scratch)

你是否曾經好奇，當你向 ChatGPT 提問，或是「與你的 PDF 聊天」時，底層究竟發生了什麼事？聽過別人談論語意搜尋 (semantic search)、向量資料庫 (vector databases)、檢索 (retrieval)、索引 (indexing)，卻從未真正理解為什麼需要它們？

進入正題，也就是檢索增強生成 (Retrieval Augmented Generation, 簡稱 RAG)！如果你搜尋 RAG，會找到許多教學，但它們通常都在談論基礎知識。當我們想要在大型資料集上建立實際應用場景的生產級應用程式時，這些基礎教學可能不太夠用。這將是一個系列文章，我們會專注於 RAG 流程的每一個步驟，並深入探討進階技術，希望能幫助你打造生產級的應用程式。

所以，讓我們試著將流程一步步拆解。在這篇文章中，我們將只探討 RAG 流程的第一步，也就是「查詢轉換」(Query Translation)（如上方資訊圖表中的黑色方框所示）。如果你喜歡這裡的內容，請務必訂閱這份電子報，我們致力於為你帶來最新、最棒的資訊。

**[點此訂閱](https://div.beehiiv.com/)**

*我將會參考封面那張由 [LangChain](https://www.linkedin.com/article/edit/7163428941553233921/?utm_campaign=rag-say-what&utm_medium=referral&utm_source=div.beehiiv.com#) 優秀的 [Lance Martin](https://www.linkedin.com/article/edit/7163428941553233921/?utm_campaign=rag-say-what&utm_medium=referral&utm_source=div.beehiiv.com#) 所分享的詳細資訊圖表中的術語。如果你是初學者，想快速了解 RAG 的概念，我強烈建議在進入以下進階主題前，先看看他在 YouTube 上的[快速教學影片](https://www.youtube.com/watch?v=wd7TZ4w1mSw&utm_campaign=rag-say-what&utm_medium=referral&utm_source=div.beehiiv.com)。*

建立一個針對你的知識庫進行問答的最佳化解決方案，涉及許多環環相扣的元件。優化每一個元件的唯一方法就是不斷實驗和迭代，因為當涉及到 LLM 的底層運作時，並沒有一本萬用的手冊（也就是說，*「我求你不要再胡說八道了」*）。

那麼，我們從一個顯而易見的問題開始：為什麼要用 RAG，難道 LLM 還不夠好嗎？

**問題 1**：LLM 不了解你的資料，甚至不了解任何最新的資料。它們是在網路上公開（*咳咳*）的資訊上進行預先訓練的，所以它們既不是你專屬資料庫的專家，也無法掌握最新資訊，而這些資料庫通常是特定領域的。

![](https://media.licdn.com/dms/image/D5612AQG9PksRLmA_hQ/article-inline_image-shrink_400_744/0/1707950075701?e=1713398400&v=beta&t=9gQeALZ6o2R4qcMFRxylVJ2YbfHIqXMoZqXbadxlAnE)[

來源：Langchain

](https://docs.google.com/presentation/d/1C9IaAwHoWcc4RSTqo-pCoN3h0nCgqV2JEYZUJunv_9Q/edit#slide=id.g26685277936_0_2)

**問題 2**：上下文視窗 (Context window) 的限制。計算資源的限制意味著每個 LLM 都有一次能攝入的最大標記 (token) 數量上限（經驗法則：平均 100 個 tokens 大約相當於 75 個單字）。一旦超出上下文視窗，就會導致上下文遺失，進而影響準確性、產生檢索問題和幻覺 (hallucination)。

![](https://media.licdn.com/dms/image/D5612AQHzwzbKk12LdA/article-inline_image-shrink_1000_1488/0/1707950100109?e=1713398400&v=beta&t=LG8ih8DP8gZiKSMb9Y9ar5Z_aQLMUu0hZuJcfaxa3ys)[

來源：Langchain 與 Karpathy 於 X

](https://docs.google.com/presentation/d/1C9IaAwHoWcc4RSTqo-pCoN3h0nCgqV2JEYZUJunv_9Q/edit#slide=id.g26685277936_0_2)

**問題 3**：[中間迷失問題 (Lost in the middle problem)](https://arxiv.org/abs/2307.03172?utm_campaign=rag-say-what&utm_medium=referral&utm_source=div.beehiiv.com)。即使 LLM 能夠一次攝入所有資料，還有一個問題是，LLM 檢索資訊的能力會取決於該資訊在文件中的位置。這裡參考的研究表明，舉例來說，如果相關資訊被埋在文件中間，而不是開頭或結尾，LLM 的效能會顯著下降。

![](https://media.licdn.com/dms/image/D5612AQF9K4MdpWMuuQ/article-inline_image-shrink_400_744/0/1707950134104?e=1713398400&v=beta&t=YahqIsMWF1fM9G_qzojwqwX0MZPLQTX2j4NrcRvK5gM)[

迷失在中間：語言模型如何使用長上下文

](https://arxiv.org/abs/2307.03172)

因此，我們需要 RAG！下一個顯而易見的問題是：如何進行？讓我們先從大家目前都熟悉的應用場景開始。上傳一份 PDF，然後跟它對話（想像一下 ChatGPT）。

當我們向一個基於大型資料來源的 AI 原生問答聊天機器人提問時，它的運作流程如下：

## 查詢轉換 (Query Translation)：

### a) 查詢拆解 (Query Decomposition)

你的問題對你來說可能很明顯，但對 LLM 來說可能並非如此。它可能太過模糊、太過具體，或是缺乏上下文。通常建議在將查詢發送到嵌入模型 (embedding model) 之前，先重新建構查詢（這部分稍後會詳細說明）。有誰比 LLM 自己更適合做這件事呢？以下是一些方法：

- [重寫-檢索-閱讀 (Rewrite-Retrieve-Read)](https://arxiv.org/abs/2305.14283?utm_campaign=rag-say-what&utm_medium=referral&utm_source=div.beehiiv.com)：這種方法側重於使用者輸入的查詢（即重寫它），而不僅僅是調整檢索器或閱讀器。它會提示 LLM 產生一個查詢，然後使用網路搜尋引擎來檢索上下文。透過使用小型語言模型的可訓練方案，可以進一步對齊流程。這個過程在下圖中總結得非常好：

![](https://media.licdn.com/dms/image/D5612AQHCus87scTRcg/article-inline_image-shrink_400_744/0/1707950259462?e=1713398400&v=beta&t=ukck2H2MV7hZrmdRBHKmBIjRg5fRWwgieJiaF8OztKo)[

來源：為檢索增強大型語言模型重寫查詢

](https://arxiv.org/abs/2305.14283)

- [將後續問題濃縮為獨立問題 (Follow-up question to condensed/standalone one)](https://smith.langchain.com/hub/langchain-ai/weblangchain-search-query?utm_campaign=rag-say-what&utm_medium=referral&utm_source=div.beehiiv.com)：這通常用於在對話中為聊天機器人提供上下文，方法是將對話重新表述為一個良好的獨立問題。Langchain 提供的這個提示詞模板就是一個很好的例子：
	*「給定以下對話和一個後續問題，請將後續問題重新表述為一個獨立的問題。*
	*對話歷史：{chat\_history}*
	*後續輸入：{question}*
	*獨立問題：」*
- [RAG 融合 (RAG Fusion)](https://github.com/langchain-ai/langchain/blob/master/cookbook/rag_fusion.ipynb?utm_campaign=rag-say-what&utm_medium=referral&utm_source=div.beehiiv.com)：這是 RAG 和倒數排名融合 (Reciprocal Rank Fusion, RRF) 的結合，透過產生多個查詢（從不同角度添加上下文），使用倒數分數對它們進行重新排序，然後融合文件和分數。這能帶來更全面和準確的答案。

![](https://media.licdn.com/dms/image/D5612AQFQXV63mM8lwQ/article-inline_image-shrink_400_744/0/1707950359169?e=1713398400&v=beta&t=9YmQYiyutaqJ1yncD_hmjV_VxuuU3uDjoT2Hu-tkgE4)[

來源：RAG-Fusion：檢索增強生成的新視角

](https://arxiv.org/abs/2402.03367)

- [退一步提示法 (Step-Back Prompting)](https://arxiv.org/abs/2310.06117?utm_campaign=rag-say-what&utm_medium=referral&utm_source=div.beehiiv.com)：這是一種更具技術性的提示技術，LLM 會進行抽象化，以推導出高層次的概念和第一原理。這是一個迭代過程，其中使用者的問題被用來產生一個退一步的問題。然後，退一步的答案會被用於推理，以產生最終答案。

![](https://media.licdn.com/dms/image/D5612AQE3KtLnq-sQqw/article-inline_image-shrink_1000_1488/0/1707950393528?e=1713398400&v=beta&t=lRYCVKfSw6ob61MzO396bXVBctFmdGJ7PJZxkUrWOtE)[

來源：退一步：透過大型語言模型中的抽象化喚起推理

](https://arxiv.org/abs/2310.06117)

- [查詢擴展 (Query Expansion)](https://arxiv.org/abs/2305.03653?utm_campaign=rag-say-what&utm_medium=referral&utm_source=div.beehiiv.com)：這是一個過程，其中 LLM 會根據提供的查詢，產生新的術語來擴展該查詢。這在文件檢索中非常強大，特別是應用於思維鏈 (Chain-of-Thought) 提示詞時。
	\- **使用生成的答案進行擴展**：在這種方法中，我們提示 LLM 根據我們的查詢產生一個假設性的答案。然後，我們將該答案附加到我們的查詢中，作為一個聯合查詢，再進行嵌入搜尋。透過使用假設性答案擴展我們的查詢，我們的查詢現在在進行嵌入搜尋時會落在不同的地方，從而提供更準確的答案。

![](https://media.licdn.com/dms/image/D5612AQGYSiGMHzzkXg/article-inline_image-shrink_400_744/0/1707950444874?e=1713398400&v=beta&t=sEsn6UokviFt6o_nXvfOWkZDnMRPgEY1odkaYRIpoGs)[

來源：深度學習

](https://www.deeplearning.ai/short-courses/advanced-retrieval-for-ai/)

\- **使用多個查詢進行擴展**：我們要求 LLM 根據我們的查詢產生額外的相似查詢。然後，我們將這些額外的查詢連同我們原始的查詢一起傳遞給向量資料庫進行檢索。與僅使用原始查詢相比，這顯著提高了準確性。反覆測試提示詞以評估哪種方式能帶來最佳結果，是至關重要的。

下面是一個表示影響的視圖，其中橘色十字表示產生的額外查詢，綠色圓圈表示檢索到的資訊。與僅使用原始查詢（紅色表示）相比，檢索到的資訊分散得多。好處是我們現在有更好的機會捕捉到所有相關的上下文，缺點是檢索到的結果數量更多（重新排序是解決這個問題的好方法——我們將在稍後關於檢索的文章中討論這一點）。

![](https://media.licdn.com/dms/image/D5612AQFedjd1UL4oUQ/article-inline_image-shrink_400_744/0/1707950483550?e=1713398400&v=beta&t=9Sb6hbnXR0UQh1M3T0r8nnD_kBnHnQnnbQD4W_dttmI)[

來源：深度學習

](https://www.deeplearning.ai/short-courses/advanced-retrieval-for-ai/)

### b) 偽文件 (Psuedo documents)：

- [假設性文件嵌入 (Hypothetical Document Embeddings, HyDE)](https://arxiv.org/abs/2212.10496?utm_campaign=rag-say-what&utm_medium=referral&utm_source=div.beehiiv.com)：有什麼比問錯問題更糟糕的？向一個相關性標籤可能標記不良的向量資料庫提問。因此，一種更好的方法是先創建一個假設性的答案，然後在嵌入中搜尋匹配項。需要注意的是，雖然這比「查詢到答案」的嵌入匹配更好，但對於與上下文高度不相關的問題，產生幻覺答案的可能性也更高。因此，在最佳化流程時，需要將這些邊緣情況 (edge cases) 考慮在內。

![](https://media.licdn.com/dms/image/D5612AQHTolPrkuOkJQ/article-inline_image-shrink_400_744/0/1707950508277?e=1713398400&v=beta&t=eUNwgxBoxLXuEOUnp2tfoMhZH66Dmvf3z4VFzozFMnQ)[

進階 RAG — 使用假設性文件嵌入 (HyDE) 改善檢索

](https://medium.aiplanet.com/advanced-rag-improving-retrieval-using-hypothetical-document-embeddings-hyde-1421a8ec075a)

我要再次強調，查詢轉換沒有絕對正確或錯誤的方法，這只是建立基於 RAG 流程的第一步。這是一個充滿實驗性的領域，了解什麼最適合你的使用場景的唯一方法，就是動手去建置。在 LLM 或向量資料庫方面，我們有非常多的選擇，所以去試試看吧，並請讓我知道進展如何，或者什麼方法最有效。

下一步：路由與查詢建構 (Routing and Query Construction)。