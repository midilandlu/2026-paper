# 機構設計與 3D CAD 工作流程整合：AI Agent 與 VLM 核心論文推薦清單

針對「機構設計工作流程整合（2D工程圖 / 3D CAD 設計）」領域，為您檢索了近三年 (2024-2026) 最前沿的 AI 應用發展。

傳統生成式 AI（如 Midjourney 生成的 3D 網格）無法直接用於工業生產，因為它們缺乏尺寸參數且難以編輯。因此，近期的研究核心已轉向 **「Agent 自動編寫 CAD 腳本 (Procedural Modeling)」**、**「閉環式的迭代編輯 (Iterative Editing)」** 以及 **「符合製造與組裝規範 (B-Rep Assemblies)」**。

---

## 📊 核心技術發展趨勢與推薦優先順序

### 🥇 Tier 1: Agent 驅動的 CAD 迭代生成與編輯 (Iterative CAD Agent)
目前的突破在於讓 AI Agent 像工程師一樣，能看著 2D 工程圖或文字需求，一步步建構與修改 3D CAD。

**1. IterCAD: An Iterative Multimodal Agent for Visually-Grounded CAD Generation and Editing**
*   **推薦理由**：直接解決機構設計的真實工作流痛點：「修改與迭代」。它是一個多模態 Agent，能讀取 2D 工程圖 (Drawing-to-Code) 並與 CAD 軟體沙盒進行多輪互動。
*   **發布日期**：2026-06-11
*   **作者**：Tao Hu, Jiaxin Ai, Licheng Wen, et al.
*   **連結**：[http://arxiv.org/abs/2606.13368v1](http://arxiv.org/abs/2606.13368v1)
*   **摘要**：現有的自動化 CAD 方法多為開環的單次生成，這與真實世界迭代的設計實務不符。IterCAD 是一個統一的多模態 Agent 框架，支援閉環、互動式的 CAD 生成與編輯。透過幾何感知強化學習，大幅提升了腳本的可執行性與幾何精確度。

**2. LLM4CAD-Editor: An Intent-Aware Large Language Model Framework for Multi-Level Computer-Aided Design Editing**
*   **推薦理由**：放棄讓 LLM 去猜測 3D 空間座標，改為透過特徵名稱 (Feature names) 去定位與修改幾何體，極大提升了編輯的穩定性。
*   **發布日期**：2026-05-21
*   **作者**：Yuewan Sun, Zhenghui Sha
*   **連結**：[http://arxiv.org/abs/2606.20607v1](http://arxiv.org/abs/2606.20607v1)
*   **摘要**：LLM 已經能從文字生成參數化 CAD 程式，但真實工作流程需要的是可靠的「編輯」。本文提出基於特定領域語言 (DSL) 的 LLM4CAD-Editor 框架。其符號表示法允許模型透過特徵名稱而非座標來參照幾何體，將脆弱的座標推理轉化為自然語言推理。

### 🥈 Tier 2: 程式化 3D 建模與機制生成 (Procedural Modeling & Mechanism Synthesis)
讓 VLM 直接呼叫 CAD 軟體（如 SolidWorks, FreeCAD）的 API 寫程式來建構具備參數的幾何實體。

**3. 3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code**
*   **推薦理由**：評估 VLM Agent 是否有能力直接扮演「3D 建模師」，將設計參考圖轉換為能直接在引擎內使用的參數化程式碼。
*   **發布日期**：2026-05-31
*   **作者**：Yipeng Gao, Lei Shu, Genzhi Ye, et al.
*   **連結**：[http://arxiv.org/abs/2606.01057v1](http://arxiv.org/abs/2606.01057v1)
*   **摘要**：透過程式碼進行程序化 3D 建模能提供具備確定性、可精確編輯的資產（這是神經網路直接生成的 3D Mesh 辦不到的）。3DCodeBench 評估 12 款頂尖 VLM Agent 將圖文轉換為 3D 軟體程序化程式碼的能力，並發現給予 Agent 更多的「思考預算」與「多輪修復」能顯著提升品質。

**4. R-APS: Compositional Reasoning and In-Context Meta-Learning for Constrained Design via Reflective Adversarial Pareto Search**
*   **推薦理由**：針對機械連桿與機構合成設計。讓 LLM 串接真實的運動學求解器 (Kinematic solver) 進行驗證與修改，而非瞎猜。
*   **發布日期**：2026-06-03
*   **作者**：João Pedro Gandarela, Thiago Rios, Stefan Menzel, André Freitas
*   **連結**：[http://arxiv.org/abs/2606.04823v1](http://arxiv.org/abs/2606.04823v1)
*   **摘要**：針對平面機構合成（機器人、義肢、機械設計），在 Agent 工作流中引入反射式對抗帕雷托搜尋 (R-APS)。每一個由 LLM 生成的機構候選者都會被運動學求解器檢驗，並將失敗點回傳給 LLM 進行除錯與修正。

### 🥉 Tier 3: 面向製造的評估基準與創新設計
確保生成的 CAD 不是只有外觀好看，還要能夠真正被製造、組裝，甚至具備工程創新性。

**5. MUSE: Benchmarking Manufacturable, Functional, and Assemblable Text-to-CAD Generation**
*   **推薦理由**：這篇直指痛點：現在很多 AI 產出的 3D 根本不能拿去加工。它提出了一個檢驗 CAD 生成物是否符合製造與組裝規範的標準。
*   **發布日期**：2026-05-27
*   **作者**：Xiaoyu Dong, Zhi Li, Xiao-Ming Wu
*   **連結**：[http://arxiv.org/abs/2605.28579v2](http://arxiv.org/abs/2605.28579v2)
*   **摘要**：現有的 Text-to-CAD 基準只看幾何形狀相似度，忽略了功能性與可製造性。MUSE 專注於複雜、可編輯的邊界表示 (B-Rep) 組裝件，透過程式碼檢查、幾何檢查以及設計意圖對齊（功能性、可製造性、可組裝性）的三階段協議來評估生成的模型。

**6. Enhancing Creativity in 3D Generative Design via a TRIZ-Inspired Text-to-CAD Framework**
*   **推薦理由**：將傳統工程中的萃思理論 (TRIZ) 引入 LLM 的 CAD 生成工作流，讓 AI 成為能解決工程矛盾的創意夥伴。
*   **發布日期**：2026-06-19
*   **作者**：Dongeon Lee, Leekyo Jeong, Soyoung Yoo, et al.
*   **連結**：[http://arxiv.org/abs/2606.21378v1](http://arxiv.org/abs/2606.21378v1)
*   **摘要**：大多數 LLM 的 CAD 生成注重幾何精度，卻忽略了創意探索。本文提出受 TRIZ（萃思）啟發的 Text-to-CAD 框架，將人類專利的發明原則嵌入 LLM 提示策略中。例如在設計椅子時，自主應用分割、複合材料等原則生成創新變體，在保持結構完整性的同時實現輕量化。
