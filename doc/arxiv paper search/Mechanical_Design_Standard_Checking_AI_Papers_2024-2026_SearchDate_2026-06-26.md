# 機構設計圖與 3D CAD：設計標準與可製造性檢查 (Design Rule Checking & DFM) AI 核心論文推薦清單

針對「機構設計標準檢查」、「可製造性評估 (DFM)」、「幾何干涉與組裝驗證」，為您檢索了近三年 (2024-2026) 運用 VLM、AI Agent 與機器學習進行輔助驗證的前沿文獻。

在設計標準檢查領域，業界發現純依賴神經網路的 VLM 容易產生「幻覺」，無法保證 100% 的物理正確性。因此，目前的最新趨勢是走向 **「神經符號系統 (Neuro-Symbolic)」**，也就是讓 AI 大腦與傳統物理/幾何驗證引擎（Solver / Prover）結對工作。

---

## 📊 核心技術發展趨勢與推薦優先順序

### 🥇 Tier 1: 神經符號系統與閉環自動修正 (Neuro-Symbolic Verification)
結合 LLM 的泛化推理能力與傳統求解器 (Solver) 的 100% 準確性。當設計不符標準時，系統會自動指出錯誤點，並要求 Agent 修正。

**1. Correct-by-Construction G-Code Generation: A Neuro-Symbolic Approach via Separation Logic**
*   **推薦理由**：完美展示了如何將「物理干涉與碰撞」轉化為 AI 可以理解並修正的邏輯錯誤。
*   **發布日期**：2026-05-11
*   **作者**：Yeonseok Lee
*   **連結**：[http://arxiv.org/abs/2605.10568v3](http://arxiv.org/abs/2605.10568v3)
*   **摘要**：提出一個神經符號 (Neuro-symbolic) 框架。系統會先從 3D CAD 模型 (STEP) 中提取邊界表示 (B-rep)。LLM 作為初始生成器，而分離邏輯證明器 (Separation Logic Prover) 則作為檢查器。系統將物理碰撞視為「空間資料競爭 (Spatial Data Races)」的邏輯違規，一旦驗證失敗，證明器會將失敗區域轉為邊界框 (Bounding boxes) 反饋給 LLM 進行自動迭代修正，確保最終輸出的設計與路徑 100% 安全且符合物理標準。

### 🥈 Tier 2: 導入 VLM 裁判與工程評分量表 (VLM as a Judge for Manufacturability)
過去評估 CAD 生成只看「形狀像不像」，現在的研究開始使用 VLM 根據工程量表來判斷「能不能製造」、「能不能組裝」。

**2. MUSE: Benchmarking Manufacturable, Functional, and Assemblable Text-to-CAD Generation**
*   **推薦理由**：提出了一套非常實用的三階段驗證協議，並證明了 VLM 有能力根據工程量表擔任設計圖的審查裁判。
*   **發布日期**：2026-05-27
*   **作者**：Xiaoyu Dong, Zhi Li, Xiao-Ming Wu
*   **連結**：[http://arxiv.org/abs/2605.28579v2](http://arxiv.org/abs/2605.28579v2)
*   **摘要**：MUSE 專注於複雜組裝件的 3D CAD。它提出三階段的設計標準檢查協議：(1) 代碼檢查、(2) 幾何檢查、(3) 設計意圖對齊。在第三階段，它引進了一個基於工程量表 (Rubric-based) 的 VLM 作為裁判，專門檢查生成的 CAD 是否具備「功能性、可製造性與可組裝性」。研究指出，目前的最強 LLM 雖然能寫出可執行的代碼，但在細粒度的工程標準驗證上仍面臨挑戰。

### 🥉 Tier 3: 結合圖神經網路的可製造性分析 (Graph-based Manufacturability Analysis)
直接讀取 3D CAD 的底層 B-rep (邊界表示法)，不轉換成圖片，用圖神經網路尋找違反製造規則的特徵。

**3. CAD-feature enhanced machine learning for manufacturing effort estimation on sheet metal bending parts**
*   **推薦理由**：針對板金折彎等特定製程的 DFM (Design for Manufacturing) 檢查，展現了如何結合 B-rep 與幾何特徵進行機器學習。
*   **發布日期**：2026-05-12
*   **作者**：Matteo Ballegeer, Toon Van Camp, Willem Jaspers, et al.
*   **連結**：[http://arxiv.org/abs/2605.12266v1](http://arxiv.org/abs/2605.12266v1)
*   **摘要**：單純的幾何表示缺乏精確製造性預測所需的語義。本文提出一種混合方法，利用基於規則的模組先識別製造特徵，再將這些特徵（如折彎特性、凸緣長度、表面角色）作為節點屬性，豐富了 B-rep 屬性鄰接圖。在實際的板金折彎工業數據測試中，這種結合領域知識與圖機器學習的方法能準確評估可製造性並估算製造工作量。

### 🎖️ Tier 4: 工程合約與約束驗證架構 (Contract-Bounded Architecture)
確保 AI 對機構進行任何修改前，必須通過前置的「操作合約」檢驗。

**4. Hylos: Operability Contracts for Model-Native Spatial Intelligence**
*   **推薦理由**：探討 3D 空間智能的底層系統架構，提出修改 3D 物件必須經過嚴格的「合約與約束檢查」，非常適合用於確保 AI 編輯 CAD 時不會破壞原有的機械拘束。
*   **發布日期**：2026-05-23
*   **作者**：Christopher Da Silva
*   **連結**：[http://arxiv.org/abs/2605.24728v1](http://arxiv.org/abs/2605.24728v1)
*   **摘要**：AI 生成的視覺 3D 模型往往無法直接操作。Hylos 提出「合約約束的空間智能 (Contract-bounded spatial intelligence)」。它將空間變更路由到 SpatialTransaction：這個檢查邊界會解析引用、檢查可接受性、保護幾何不變量 (Invariants)，並回傳提交或退回。這確保了 AI 生成或編輯的 3D 設計能夠成為 CAD、模擬與製造的可靠基礎，而不會發生不合理的干涉或機構解體。
