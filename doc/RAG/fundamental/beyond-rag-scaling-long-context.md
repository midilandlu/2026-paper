---
title: "超越 RAG：擴展長文本上下文 (Beyond RAG: Scaling long context)"
url: "https://div.beehiiv.com/p/beyond-rag-scaling-long-context"
requestedUrl: "https://div.beehiiv.com/p/beyond-rag-scaling-long-context"
author: "Divyanshu Dixit"
coverImage: "imgs/beyond-rag-scaling-long-context/imgs/img-001-image.png"
siteName: "Latest and Greatest"
publishedAt: "2024-04-09T16:00:00.000Z"
summary: "替代架構：這才是未來的出路嗎？"
adapter: "generic"
capturedAt: "2026-06-20T06:36:44.127Z"
conversionMethod: "defuddle"
kind: "generic/article"
language: "zh-TW"
---

# 超越 RAG：擴展長文本上下文 (Beyond RAG: Scaling long context)

替代架構：這才是未來的出路嗎？

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/477899e2-4212-476c-8ea6-daba846157bb/image.png)[

資料來源：Latent Space blog

](https://www.latent.space/p/jan-2024?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

在我們先前的[進階 RAG](https://div.beehiiv.com/p/rag-say) 系列文章中，我們探討了各種建立高效率管道的方法，以克服 LLM 上下文視窗長度所帶來的限制。但這個限制真的是無法跨越的嗎？

在今日這個由 Transformer 架構主導的世界裡，很難想像會有另一種能高效率（以次二次方, subquadratically 的複雜度）擴展上下文的替代現實存在。因此，這篇文章將獻給那些「如果...會怎樣 (what if)」的替代架構 (alt architectures)——一個上下文長度不再是限制因素的平行時空。

注意力 (Attention) 「也」是你所需要的！

#### Transformer 架構：

讓我們先來回顧一下，為什麼 Transformers 會成為當今 LLM 的預設架構。這一切都始於 2017 年 Google 發表的那篇革命性論文——「[Attention is all you need](https://arxiv.org/pdf/1706.03762.pdf?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)」。其革命性在於能夠「平行」處理語言，而非「循序」處理（也就是過去 RNN 的做法，稍後會詳細說明）。

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/109b9b3e-aae0-41ff-8493-9f2ac0517624/image.png)[

資料來源：Arxiv, Vaswani et al

](https://arxiv.org/pdf/1706.03762.pdf?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

這個架構最大的優勢之一在於其通用的多模態性質，該論文的共同作者 Ashish Vaswani 為此做出了精闢的總結：

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/0da82482-2071-45e4-a75c-0b6b344e7dfb/image.png)[

資料來源：Financial Times

](https://www.ft.com/content/37bb01af-ee46-4483-982f-ef3921436a50?accessToken=zwAGASoZXEbgkc83uwGv7kZEg9OYL-85IUNqUA.MEUCIGAX418D_QPFvxq-QLYReJE4g1m7wcZRXGk6pf1HqVQQAiEAn53oHV1zcVD3MYxeTbCWsSf_BIiSf_E_JcvZfhzlScw&sharetype=gift&token=4178b09d-f17c-4285-a18c-446dce2bdb54&utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

透過「自注意力模組 (self attention module)」實現的平行化，帶來了運算效率、可擴展性與準確度的提升，這相較於過去盛行的循序 RNN 架構是一大躍進，而它們的發展也正好與 GPU 的崛起不謀而合！於是，一場為了打造更強大 LLM 而在更大資料集上訓練更多參數的軍備競賽就此展開。

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/93271f65-7d06-41c2-9cab-7c79db02de14/image.png)[

資料來源：Jay Alammar’s blog

](https://jalammar.github.io/illustrated-transformer/?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

那麼，我們為什麼還要討論替代架構呢？看起來注意力機制就是我們需要的一切啊！嗯，可能未必。對 Transformer 架構最大的批評之一，就是它的運算量與記憶體需求會隨著序列長度呈「二次方 (quadratically)」成長，這意味著在訓練（注意力計算）與生成（完整的歷史回顧）上需要花費更多的金錢 ($$$)。

這引發了人們對下面將探討的「次二次方 (sub-quadratic)」LLM 的熱烈關注。不過，我要為這個關於二次方擴展的批評加上一個但書：雖然在預訓練階段確實如此，但當進入推論 (inference) 階段時，注意力機制在整體運算中只佔了很小一部分，所以對於這些炒作，還是要持保留態度。

#### RNN 架構：

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/ae586d5c-7651-4ac4-a01e-33b902f8f1da/image.png)[

資料來源：Andrej Karpathy’s blog

](https://karpathy.github.io/2015/05/21/rnn-effectiveness/?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

RNN 的最大缺點在於它們難以處理過長的序列，原因是所謂的「[梯度消失問題 (vanishing gradient problem)](https://www.superdatascience.com/blogs/recurrent-neural-networks-rnn-the-vanishing-gradient-problem?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)」。長短期記憶模型 (LSTM) 和門控循環單元 (GRU) 等架構曾被寄予厚望能克服這個問題，但就目前而言，Transformer 架構已經有效地解決了這個難題，因而成為生成式模型的業界標準。

## RWKV：

你說要重新發明 RNN？那就來看看 RWKV 吧，它是一個隸屬於 Linux 基金會底下的開源、非營利專案。RWKV 聲稱結合了 RNN 與 Transformer 兩者的優點，其基礎是 [Apple 的無注意力 Transformer (Attention Free Transformer)](https://machinelearning.apple.com/research/attention-free-transformer?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)。

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/878ba36c-2bc2-49c4-868d-438f73283585/image.png)[

資料來源：RWKV docs

](https://wiki.rwkv.com/?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

這意味著什麼？這代表它在訓練和推論上的擴展性都比 Transformers 更好（成本隨序列長度呈線性成長，而非二次方成長），也就是說成本更低，支援的上下文長度更長。基於這個架構的 Eagle 7b 模型，在多語言基準測試中擊敗了所有其他 70 億參數規模的模型，不僅能與 Llama 家族和 Mistral 互別苗頭，其推論成本和延遲更只有對手的一小部分！它也是每個 token 運算效率最高的模型。

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/df71c6a5-cbc4-4243-affe-fa9fa083f0dd/image.png)[

資料來源：RWKV docs

](https://blog.rwkv.com/p/eagle-7b-soaring-past-transformers?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

然而，能夠有一個基於 RNN 的模型在基準測試中一較高下，這讓 RWKV 成為有機會把現任霸主 Transformer 趕下王座的最強候選人之一！

## MonarchMixer：

考量到其背後由史丹佛大學 Hazy Research 團隊這個強大陣容所推動，MonarchMixer 是另一個令人興奮的潛力股。這個架構的目的是克服 Transformers 呈二次方成長的限制，並鎖定兩個軸向：「序列長度」（注意力）與「模型維度」（MLP 層）。

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/78845923-90db-446d-94ad-8816358af097/image.png)[

資料來源：Stanford Hazy Research

](https://hazyresearch.stanford.edu/blog/2024-01-11-m2-bert-retrieval?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

解決方案是什麼？使用「Monarch 矩陣」作為「高硬體效率且具表現力的次二次方原語 (subquadratic-primitive)」來取代注意力和 MLP。對於技術細節感興趣的讀者，可以在[這裡](https://arxiv.org/pdf/2310.12109.pdf?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)了解更多。正如作者在論文中所指出的，這目前仍是一個研究領域，且由於 M2 層尚未針對推論進行最佳化，現在要將其與 Transformers 或 SSM（稍後討論）進行比較還言之過早。但隨著它的發展，絕對值得持續關注其進展。

## 狀態空間模型 (State Space Models, SSMs)：

要詳細解釋 SSM 的運作原理足以寫成另一篇文章，但從高層次來看，它們是基於輸入、輸出與狀態變數隨時間演進的動態系統。這裡的「狀態 (state)」可以定義為描述系統在任何時間點所需資訊的表徵。這與本文相關的原因在於，過去的資訊可以被總結為一個狀態，進而用來預測下一個狀態。SSM 可以用以下兩個方程式來解釋。

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/1d41bbf4-693e-4204-9e4a-8d267a670f39/image.png)[

資料來源：Maarten Grootendorst’s blog

](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

**狀態方程式 (state equation)** 描述了 a) 當前狀態隨時間如何演進（忘掉不相關的東西），以及 b) 輸入如何影響狀態（從輸入中記住什麼）。

**輸出方程式 (output equation)** 描述了 a) 當前狀態如何轉換為輸出（即如何預測下一個狀態），以及 b) 輸入如何直接影響輸出（如何使用輸入來做出預測）。

SSM 最大的問題在哪？它們對所有的輸入一視同仁。這讓它們非常有效率（狀態很小），但效果不是很好（像 RNN 一樣很容易遺忘）。相較之下，Transformers 因為具備注意力機制能進行完整的歷史回顧，剛好與之相反。

## Mamba：

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/2bf89f90-18f9-49ae-bc58-c69fcd9ec9d7/image.png)[

資料來源：Kola Ayonrinde’s blog

](https://www.kolaayonrinde.com/blog/2024/02/11/mamba.html?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

這正是 Mamba 令人感興趣的地方，它標榜自己是這兩者之間良好的折衷方案，透過成為一個「選擇性 (Selective)」的狀態空間模型。

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/8502eca8-894c-4047-b1c6-0f0be62a62e2/image.png)[

資料來源：Mamba paper, Arxiv

](https://arxiv.org/pdf/2312.00752.pdf?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

將上圖與 Transformer 架構進行比較，你注意到了什麼？注意力機制（「多頭注意力, Multi-Head Attention」）被選擇機制（SSM）取代了。因此，現在在推論時不再需要回顧所有歷史資料的語料庫，關於哪些內容應該保留在記憶中的「選擇」，是在建立「壓縮狀態」時就完成了。據報導，這造就了一個比 RNN 與 Transformers 更強大且更有效率的架構。同樣值得注意的是，該架構應用了一些技巧來針對 GPU 硬體進行最佳化（參考 Tri Dao 的 [Flash Attention 論文](https://arxiv.org/abs/2205.14135?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)）。

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/797d77dd-57f3-4c4e-afee-edf57c1bcc98/image.png)[

資料來源：Maarten Grootendorst’s blog

](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

藉由將內建的上下文視為長期記憶，現在可以以非常低的成本與延遲來參照這些狀態。這讓它在擴展上下文和儲存空間時非常實用，也是令人興奮的原因。最終定論尚未出爐，同時我們已經看到 JAMBA 的發表，它利用了混合專家 (mixture-of-experts) 技術將這個概念進一步推進。這部分我們將在未來的文章中詳細討論。

## Striped Hyena：

這裡簡單提一下來自 Together AI 的 [Striped Hyena](https://www.together.ai/blog/stripedhyena-7b?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)，它是一個基於 SSM 架構的開源專案。根據作者的說法，*「它是一個混合架構，由旋轉（分組）注意力與排列在 [Hyena](https://arxiv.org/abs/2302.10866?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com) 區塊中的門控卷積 (gated convolutions) 所組成。」* 結果呢？在 32k、64k 和 128k 序列長度的訓練中，它的速度分別提升了 >30%、>50% 和 >100%，這使它非常適合在長上下文的應用場景中進行微調。

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/af827d2e-23ce-4d0e-b9df-0000da31b242/image.png)[

資料來源：Together AI

](https://www.together.ai/blog/stripedhyena-7b?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

Striped Hyena 身為一個專注於真實世界應用場景的開源專案，它選在 Mamba 之後發表，且聲稱能擊敗 Llama-2 和 Yi-7b，這立刻引起了眾人的目光。他們確實分享了一份充滿希望的藍圖，因此希望我們能獲得更多關於訓練資料的細節，並進一步驗證這些混合架構可能帶來的前景。

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/09e7cd9d-57ae-4e3f-b953-31f56df0951d/image.png)[

資料來源：Together AI

](https://www.together.ai/blog/stripedhyena-7b?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

## 擴散模型 (Diffusion Models)：

在討論替代架構的領域時，如果不提到擴散模型（尤其是目前在文字轉圖像 Text to Image 的領域），那我就太失職了。由 [Deeplearning.ai](http://deeplearning.ai/?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com) 提供的這門[免費短期課程](https://www.deeplearning.ai/short-courses/how-diffusion-models-work/?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)，對於想了解擴散模型的初學者來說是個很好的起點。

擴散模型內部也有幾種架構上的變形，例如基於 CNN、基於 Transformer、狀態空間模型等等。更進一步來說，這些架構的擴展方式也有所不同。其中，潛在擴散 (Latent Diffusion) 已成為擴展高解析度影像合成的主要方式（例如 Stable Diffusion 就是基於這種架構）。

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/d241e611-3c9f-47e6-9563-d084865a7b23/image.png)[

資料來源：Arxiv, Rombach et al

](https://arxiv.org/pdf/2112.10752.pdf?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

潛在擴散模型 (Latent Diffusion Models, LDMs) 的突破性在於「潛在空間 (Latent Space)」的概念，*一個具有運算效率、低維度的空間，在其中，高頻、難以察覺的細節被抽象化。* LDM 主要基於卷積骨幹（U-Net CNN），並藉由引入[擴散 Transformer (Diffusion Transformers, DiT)](https://arxiv.org/abs/2212.09748?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz-8Nb-a1BUHkAvW21WlcuyZuAvv0TS4IQoGggo5bTi1WwYUuEFH4RunaPClPpQPx7iBhn-BH) 而得到改良。

#### 沙漏擴散 (Hourglass Diffusion)：

隆重介紹沙漏擴散 (Hourglass Diffusion)！SOTA (State of the Art) 在 AI 領域是一個不斷移動的目標，而*沙漏擴散 Transformer* (HDiT) 架構正是為了針對擴散模型達到這個目標而生。過去研究指出 LDM 不擅長表現精細的細節，這促使這篇論文的作者引入了*一種純粹的 Transformer 架構，用於高解析度像素空間的影像生成，其運算成本能隨解析度呈現次二次方的擴展。* 再見了，CNN/LDM！

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/1301484c-9e98-4182-bbb1-8e694b6083a6/image.png)[

資料來源：Arxiv, Crowson et al

](https://arxiv.org/pdf/2401.11605.pdf?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)

但 Transformers 的運算效率不是本來就很差嗎？如果你這麼做就不會了：

*這個架構不會一視同仁地處理影像，而是適應目標解析度：在高解析度下局部處理局部現象，並在階層中的低解析度部分獨立處理全域現象。*

這篇論文聲稱彌合了 Transformers 擴展特性與 U-nets 效率之間的差距，考慮到它出自 Katherine Crowson（參考 Stable Diffusion）之手，這絕對不容小覷。

## 環狀注意力 (Ring Attention，也就是 Gemini 1.5?)：

最後，既然我們在討論長上下文的擴展，怎麼能不提到房間裡的大象——擁有 1000 萬 token 上下文視窗的 Gemini 1.5 Pro。它聲稱（並在某種程度上獲得社群驗證）在多模態的大海撈針測試中，高達 100 萬 token 都能達到近乎完美的召回率。

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/007efadb-96e1-407d-b2c1-e311f6202237/image.png)[

資料來源：Gemini release post

](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com#architecture)

這究竟是怎麼辦到的？RAG 死定了嗎？Gemini 的發布再次改變了遊戲規則，讓人們不禁開始想像無限的上下文能解鎖哪些應用場景。對於這篇部落格文章的主題而言，更重要的是：除了身為一個基於 Transformer 的混合專家 (MoE) 模型之外，Deepmind 究竟採用了哪些基礎架構上的改變，才能在不嚴重犧牲運算或效率的情況下達到這種規模？

一個合理的推測是基於 [Ring Attention 論文](https://arxiv.org/pdf/2310.01889.pdf?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com)，*它利用區塊式 (blockwise) 運算的自注意力與前饋機制 (feedforward)，將長序列分散到多個裝置上，同時讓鍵-值 (key-value) 區塊的通訊與區塊式注意力的運算完全重疊。*

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,%20https://div.beehiiv.com/p/quality=80,%20https://div.beehiiv.com/p/format=auto,%20https://div.beehiiv.com/p/width=720,%20https://div.beehiiv.com/p/onerror=redirect/uploads/asset/file/0f2ee851-3446-49b8-992b-797b08c168fb/image.png)[

資料來源：Andreas Kopf’s slides

](https://docs.google.com/presentation/d/180lS8XbeR1_bTMaldg21LKYQkjXftHuh9VnZ3xk27qQ/edit?utm_campaign=beyond-rag-scaling-long-context&utm_medium=referral&utm_source=div.beehiiv.com#slide=id.g2c992d5a0ef_0_106)

Ring Attention 之所以重要，是因為它讓上下文長度能隨著裝置數量呈線性擴展，同時還能保持極佳的召回率，這使得「近乎無限的上下文」成為非常真實的可能性。缺點是什麼？這是為「擁有大量 GPU 資源的玩家 (GPU rich)」準備的，這可能是我們這些凡人的限制，而不是 Google 的。

只有時間能證明 Transformers 是否會繼續稱霸，但隨著我們從展示 (demos) 邁入 AI 實際投入生產的時代，了解替代架構是有價值的。在我們擴展上下文的過程中，記憶體效率將是至關重要的；雖然目前已經有一些領先者，但還沒有明確的贏家……目前還沒有！讓我們交叉手指祈禱，期待在不同架構中能出現多個贏家。

下次見，祝您閱讀愉快！