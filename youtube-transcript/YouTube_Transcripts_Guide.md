# 🎥 YouTube AI / Agent 影片精選與技術解析指南

> 本目錄收錄了針對 **AI Agent 工作流 (Agent Skills & Workflows)**、**AI 系統設計 (AI System Design)**、與 **Agent 測試與評測框架 (Harness & Benchmarks)** 等主題的精選 YouTube 影片逐字稿與雙語翻譯。

---

## 📚 影片目錄列表

| 影片編號 | 影片名稱 | 主題領域 | 講者 / 頻道 | 推薦指數 |
| :--- | :--- | :--- | :--- | :---: |
| **01** | New Skills! v1.1 brings /wayfinder, /research, /implement, /to-spec, /to-tickets | Agent Skills 工作流 | Matt Pocock | 🌟🌟🌟🌟🌟 (5/5) |
| **02** | Building Great Agent Skills: The Missing Manual | Agent Skill 撰寫規範 | Matt Pocock | 🌟🌟🌟🌟🌟 (5/5) |
| **03** | 9 Things People Get Wrong With My /grill-* skills | /grill 交互問答對齊 | Matt Pocock | 🌟🌟🌟🌟半 (4.5/5) |
| **04** | /handoff is my new favourite skill | 上下文接力與模組切換 | Matt Pocock | 🌟🌟🌟🌟半 (4.5/5) |
| **05** | Learn anything with the /teach skill | 互動式教學與技能提煉 | Matt Pocock | 🌟🌟🌟🌟 (4.0/5) |
| **06** | What if the harness mattered more than the model? | Agent 測試框架 / Evaluation | Aditya Bhargava (Etsy) | 🌟🌟🌟🌟🌟 (5/5) |
| **07** | AI System Design: From Idea to Production | AI 系統架構與生產落地 | Apoorva Joshi (MongoDB) | 🌟🌟🌟🌟半 (4.5/5) |
| **08** | Beyond the Harness: A Journey Towards Adaptive Engineering | 自適應工程 / Agent 演進 | Rajiv Chandegra (Annicha Labs) | 🌟🌟🌟🌟 (4.0/5) |
| **09** | The Future Is Domain-Specific Agents | 領域特定 Agent 趨勢 | Justin Schroeder (StandardAgents) | 🌟🌟🌟🌟 (4.0/5) |

---

## 📑 各影片詳細摘要與導讀

### 1. New Skills! v1.1 brings /wayfinder, /research, /implement, /to-spec, /to-tickets
* **影片 ID**: `A8mokin_YOs`
* **頻道 / 講者**: Matt Pocock
* **連結**: [YouTube 影片](https://www.youtube.com/watch?v=A8mokin_YOs)
* **本地檔名**: [transcript-zh-TW.md](./matt-pocock/new-skills-v11-brings-wayfinder-research-implement-to-spec-to-tickets/transcript-zh-TW.md)
* **摘要內容**: 介紹 Skills v1.1 版本的重大更新，包含流程技能重新命名（如 `/to-spec`、`/to-tickets`）、強化互動式問答考問 (`/grill`) 機制、提供完整開發生命週期，以及導入用於大型專案規劃與導航的新技能 `/wayfinder`。
* **應用場景**: 複雜軟體專案架構規劃、規格書拆解、需求 ticket 化、自動化程式實作。
* **方法與亮點**:
  * 引入 `/wayfinder` 協助 Agent 在大型專案中引導規劃與路徑搜尋。
  * 建立完整開發生命週期：從 `/research` -> `/to-spec` -> `/to-tickets` -> `/implement` 標準化流程。
  * 改進考問 (grilling) 機制，確保需求在寫 code 前完全對齊。
* **推薦閱讀指數**: 🌟🌟🌟🌟🌟 (5/5)
  * **推薦理由**: 了解現代 AI 輔助開發中，如何將軟體開發生命週期 (SDLC) 拆解為標準化 Agent Skills 的必看影片。

---

### 2. Building Great Agent Skills: The Missing Manual
* **影片 ID**: `UNzCG3lw6O0`
* **頻道 / 講者**: Matt Pocock (AI Engineer World's Fair)
* **連結**: [YouTube 影片](https://www.youtube.com/watch?v=UNzCG3lw6O0)
* **本地檔名**: [transcript-raw.json](./ai-engineer/ai-engineer/building-great-agent-skills-the-missing-manual/transcript-raw.json)
* **摘要內容**: 詳細解構如何撰寫高品質、可重用且高成功率的 Agent Skills，避免 Prompt 過度模糊或邏輯分歧。
* **應用場景**: 客製化 Agent Skill 撰寫、LLM Prompt 指令結構優化、開發團隊技能庫建立。
* **方法與亮點**:
  * 提出 Agent Skill 設計的三大關鍵要素：明確觸發條件、清晰步驟拆解、確定性產出格式。
  * 避免「大一統 Prompt」，將複雜任務化為專一模組化小技能。
* **推薦閱讀指數**: 🌟🌟🌟🌟🌟 (5/5)
  * **推薦理由**: 撰寫優質 Agent Skill 的權威指南，想要替助手開發 Skill 者的必備手冊。

---

### 3. 9 Things People Get Wrong With My /grill-* skills
* **影片 ID**: `UzMNBN6xLLA`
* **頻道 / 講者**: Matt Pocock
* **連結**: [YouTube 影片](https://www.youtube.com/watch?v=UzMNBN6xLLA)
* **本地檔名**: [transcript_zh-TW.md](./matt-pocock/9-things-people-get-wrong-with-my-grill-skills/transcript_zh-TW.md)
* **摘要內容**: 澄清使用者在執行 `/grill` (交互式考問對齊) 技能時常見的 9 個誤區，說明如何透過強烈的反覆提問與邊界案例對齊，在編寫程式碼前消除歧義。
* **應用場景**: 需求釐清、架構決策對齊、避免模型對盲目假設而寫出錯代碼。
* **方法與亮點**:
  * 強調 `/grill` 的本質不是幫你寫 Code，而是像資深架構師一樣「拷問」開發者以明確邏輯。
  * 指出常見錯誤：過早結束問答、忽略邊界條件、未明確指定技術選型。
* **推薦閱讀指數**: 🌟🌟🌟🌟半 (4.5/5)
  * **推薦理由**: 非常實用的互動技巧，能大幅提高模型一次性寫對程式碼的成功率。

---

### 4. /handoff is my new favourite skill
* **影片 ID**: `dtAJ2dOd3ko`
* **頻道 / 講者**: Matt Pocock
* **連結**: [YouTube 影片](https://www.youtube.com/watch?v=dtAJ2dOd3ko)
* **本地檔名**: [transcript-zh-TW.md](./matt-pocock/handoff-is-my-new-favourite-skill/transcript-zh-TW.md)
* **摘要內容**: 介紹 `/handoff` 技能，展示如何在上下文長度接近上限或階段任務完成時，精準打包當前狀態、決策紀錄與剩餘 Todo 移交給下一輪 Session。
* **應用場景**: 長時間跨 Session 開發、避免模型 Context window 爆滿導致幻覺與記憶遺失。
* **方法與亮點**:
  * 建立結構化的交接文件 (Handoff summary)，確保接棒的 Agent 能 100% 繼承背景。
  * 減少無效 Token 浪費，提高續接開發的準確率。
* **推薦閱讀指數**: 🌟🌟🌟🌟半 (4.5/5)
  * **推薦理由**: 解決 LLM 長上下文退化與跨對話傳承狀態的極佳實務方案。

---

### 5. Learn anything with the /teach skill
* **頻道 / 講者**: Matt Pocock
* **本地檔名**: [transcript-zh-TW.md](./matt-pocock/learn-anything-with-the-teach-skill/transcript-zh-TW.md)
* **摘要內容**: 示範如何使用 `/teach` 技能讓 AI 變成個人專屬導師，透過費曼學習法與步驟式引導協助學習複雜新概念。
* **應用場景**: 新技術快速上手、概念澄清、互動式學習體驗。
* **方法與亮點**:
  * 將學習流程分為「觀念解說 -> 實作演練 -> 檢討與反饋」三階段。
* **推薦閱讀指數**: 🌟🌟🌟🌟 (4.0/5)
  * **推薦理由**: 適合想利用 AI 自學任何程式庫或新技術開發者。

---

### 6. What if the harness mattered more than the model?
* **頻道 / 講者**: Aditya Bhargava (Etsy / AI Engineer World's Fair)
* **本地檔名**: [transcript-raw.json](./ai-engineer/ai-engineer/what-if-the-harness-mattered-more-than-the-model-aditya-bhargava-etsy/meta.json)
* **摘要內容**: Etsy 工程團隊分享在生產環境中部署 AI 時，外圍測試與控管框架 (Harness / Evaluation Framework) 對於最終品質的影響往往超過模型本身。
* **應用場景**: 生產級 Agent 架構設計、Eval 評測系統、企業級 LLM 整合。
* **方法與亮點**:
  * 重申「模型決定上限，但 Harness 決定下限」理念。
  * 展示如何建立重試、斷路器 (Circuit breaker) 與自動評測機制。
* **推薦閱讀指數**: 🌟🌟🌟🌟🌟 (5/5)
  * **推薦理由**: 企業端落地 AI 的精闢見解，適合架構師與 Tech Lead 參考。

---

### 7. AI System Design: From Idea to Production
* **頻道 / 講者**: Apoorva Joshi (MongoDB)
* **本地檔名**: [transcript-raw.json](./ai-engineer/ai-engineer/ai-system-design-from-idea-to-production-apoorva-joshi-mongodb/meta.json)
* **摘要內容**: 從概念原型到生產上線的全流程 AI 系統設計指南，涵蓋向量資料庫選型、RAG 檢索優化、快取與監控。
* **應用場景**: 企業 AI 系統架構、RAG / Vector DB 部署。
* **方法與亮點**:
  * 解析向量檢索與傳統全文檢索混合 (Hybrid Search) 的系統實作細節。
  * 強調 Observability（可觀測性）在 LLM 系統中的關鍵性。
* **推薦閱讀指數**: 🌟🌟🌟🌟半 (4.5/5)
  * **推薦理由**: 內容扎實的 AI 系統架構演講。

---

### 8. Beyond the Harness: A Journey Towards Adaptive Engineering
* **頻道 / 講者**: Rajiv Chandegra (Annicha Labs)
* **本地檔名**: [transcript-raw.json](./ai-engineer/ai-engineer/beyond-the-harness-a-journey-towards-adaptative-engineering-rajiv-chandegra-annicha-labs/meta.json)
* **摘要內容**: 探討當傳統軟體工程走向自適應工程 (Adaptive Engineering) 時，系統如何根據執行回饋動態調整 Agent 行為與流程。
* **應用場景**: 高級 Autonomous Agent 研發、自適應軟體系統。
* **推薦閱讀指數**: 🌟🌟🌟🌟 (4.0/5)

---

### 9. The Future Is Domain-Specific Agents
* **頻道 / 講者**: Justin Schroeder (StandardAgents)
* **本地檔名**: [transcript-raw.json](./ai-engineer/ai-engineer/the-future-is-domain-specific-agents-justin-schroeder-standardagents/meta.json)
* **摘要內容**: 分析通用 Agent 與特定領域 Agent (Domain-Specific Agents) 的消長，預測未來的垂直領域智能體發展模式。
* **應用場景**: 垂直領域 Agent 產品定位與技術選型。
* **推薦閱讀指數**: 🌟🌟🌟🌟 (4.0/5)

---
*文件建立時間: 2026-07-22*
