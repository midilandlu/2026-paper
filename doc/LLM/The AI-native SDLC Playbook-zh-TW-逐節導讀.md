---
sourceTitle: The AI-native SDLC playbook
sourceUrl: https://claude.com/resources/articles/the-ai-native-sdlc-playbook
sourceAuthor: Louis Claxton（Anthropic）
sourceDate: 2026-08-21
sourceProducts: Claude Enterprise, Claude Code, Claude Tag
docType: 逐節導讀（繁體中文，依原文章節順序以自己的話整理，非翻譯）
compiledDate: 2026-11-01
---

# AI 原生 SDLC 實戰手冊 — 逐節導讀

> 本文依照〈The AI-native SDLC playbook〉的章節順序，用自己的話整理每一節的重點與名詞，**不是原文翻譯**。
>
> - **附圖**：直接引用原文託管的圖檔網址，版權屬 Anthropic。
> - **範例**：原文的範例檔、設定與提示詞都不轉載，只在出現的位置標出「原文範例」的內容與用途。要看全文請連到原文對應段落。
>
> 原文：<https://claude.com/resources/articles/the-ai-native-sdlc-playbook>（約 40 分鐘閱讀量，另有官方 PDF 版）
>
> 只想看架構與判準的話，請先讀同目錄的〈[精要導讀](The%20AI-native%20SDLC%20Playbook-zh-TW-精要導讀.md)〉。

---

## 程式碼不再是瓶頸

**重點**

- AI 讓寫程式快了很多，但審批、審查、交接和政策檢查仍然以人的速度運作。
- 傳統六階段 SDLC（Plan、Design、Build、Test、Deploy、Maintain）是在「寫程式最慢」的年代設計的。
- Build 縮短後會發生三件事：
  1. 瓶頸移到 Plan、審查與測試、Deploy。
  2. 逐行人工審查跟不上 agent 的產量。
  3. 治理上的例外仍要排進每週或每月的委員會。
- 作者以安全審查為例：安全團隊的人力是依人的產出配置的。agent 放大產量後，不是審查佇列爆掉，就是審查不足。檢查必須跟上產出的速度。

![原文圖 1：Build 縮短後，以人速運作的階段變成整體交期的主體](https://assets.claude.com/90fb4ed05417570c9d4ff95d33bef9502c765da4.png)

*原文圖 1（圖片來源：Anthropic）。圖意：Build 從數週縮短到數小時，但前後以人速運作的階段長度不變，所以它們成了新的限制。*

---

## 什麼是 AI 原生 SDLC？

**重點**

- 流程從線性的階段改成**迴圈**：每個節點都嵌入 AI，各個做法（play）之間的交接也自動化。
- 這個概念的其他叫法：agentic SDLC、AI SDLC、agentic software development。

![原文圖 2：AI 原生 SDLC 的迴圈示意](https://assets.claude.com/75c8e050ace91c2b288498fe45384469cfb00aa2.png)

*原文圖 2（圖片來源：Anthropic）。*

### 六個階段的轉變

> **原文範例：對照表**（三欄 × 六列）
> 逐一比較每個階段在傳統 SDLC 與 AI 原生 SDLC 中的做法。請見原文本節。

**核心機制：交付物鏈**

每個階段結束時，把一份交付物提交進版控，下一個階段從讀它開始。

| 階段 | 提交的交付物 |
|---|---|
| Plan | `intent.md` |
| Design | `spec.md` |
| Build | `plan.md`、diff 與測試 |
| Deploy | PR 審查發現 |
| Maintain | 事故紀錄，以及下一份 `intent.md` |

git 歷史因此同時是**稽核軌跡**：誰提出需求、agent 產出了什麼、誰核准，全都查得到。

---

## 做法（Plays）

**重點**

- 每個做法都用同一套結構說明：改變了什麼、如何起步、實施步驟、治理考量、如何衡量。
- 做法分屬六個階段，但不必依線性順序導入。導入的先後由一張相依圖決定。
- 階段之間的觸發條件：

  | 事件 | 觸發 |
  |---|---|
  | `intent.md` 被接受 | 進入 Design |
  | `spec.md` 被核准 | 啟動 plan mode |
  | PR 合併 | 啟動部署管線 |
  | production 指標突破控制帶 | 自動寫出下一份 `intent.md` |

- 導入節奏：先逐步手動提示每一關，確認每一關都可靠之後，才把「交付物被接受」接成下一關的自動觸發。

![原文圖 3：各做法的導入相依圖](https://assets.claude.com/4c40f7b7577eb3ddfc1cce14a11ac6667be05c8c.png)

*原文圖 3（圖片來源：Anthropic）。圖意：每個做法依所屬階段排列，箭頭表示前置關係，也就是建議的導入順序。*

---

## Plan（規劃）

### 把想法寫成 `intent.md`

**改變了什麼**

一個想法只需記錄一次，寫成 `intent.md`。來源可以是一個人、一張工單，或由告警觸發的事故。提出者和 Claude brainstorm，得到一份初步規格（proto-spec），再由產品負責人審閱、修正後提交。

**起步（一次性設定）**

- 建立共用的 intent 存放處，例如單一產品就開一個 `intent/` 資料夾。
- 團隊先講好一份模板。
- 接上連接器（例如 GitHub），讓非工程師也能提交。

**怎麼做**

1. 描述問題。
2. 和 Claude 來回討論，直到內容夠具體。
3. 依模板產生 `intent.md`。這一步可以包成 skill。
4. 自己修正內容。
5. 提交。

> **原文範例：`intent.md` 模板**（約 12 行）
> 含作者、狀態欄位，以及四個二級章節。請見原文 Plan 一節。

**治理與衡量**

- 產品負責人是這一關的把關者。
- 領先指標：從第一次對話到 `intent.md` 提交的時間。
- 落後指標：產品負責人接受進入 Design 的比例。

---

## Design（設計）

### 需求與設計合併處理

**改變了什麼**

需求和設計在同一個工作階段完成。agent 依組織的 skills（品牌、安全、合規、UX 等）撰寫 `spec.md`，並**主動標出**和政策衝突的地方。

**怎麼做**

- 前端功能可以先由產品負責人在 Claude Design（beta）做出原型，再匯出給 Claude Code。
- 產品負責人負責審閱，不負責撰寫。被標出的疑慮交給對應的政策負責人解決。
- 工程團隊要等這些都處理完，才會看到規格。

> **原文範例：提示詞**（一段，約 60 字）
> 要求 Claude 從 `intent.md` 產出需求與設計規格。請見原文 Design 一節。

**衡量**

- 從 `intent.md` 提交到 `spec.md` 提交的時間。
- `plan.md` 產生後，`spec.md` 還被改了幾次（返工）。

---

## Build（建置）

本階段的原則有三條：

1. 沒有被接受的計畫，就不開始實作。
2. 團隊知識放在 agent 會讀的檔案裡。
3. 防護機制寫成程式，不靠習慣。

### 預設從 Claude Code 的 plan mode 開始

**重點**

- 以 plan mode 開啟工作階段，餵入 `spec.md`，讓 Claude 反過來訪談工程師，直到計畫被核准。
- plan mode 在計畫被接受之前**不能改檔案**，所以設計審查一定發生在產生程式碼之前。
- 核准後的計畫提交為 `plan.md`。
- 追問計畫的幾個好問題：哪裡可能出錯？風險最高的是哪一步？哪些方案被否決了，原因是什麼？
- 實作偏離計畫時，就回頭更新 `plan.md`。

> **原文範例：`plan.md`**（約 15 行）
> 四個章節加一份編號步驟清單。請見原文對應段落。

**衡量**：第一次實作就合併的比例；返工次數。

### 改用 auto mode

**重點**

- 等防護機制成熟之後，例行工作可以不再逐次核准每個編輯。成熟的條件包括：調校過的 `CLAUDE.md`、政策 skills、hooks、可以直接執行的測試套件。
- 人的審查重心從「看著每個編輯」轉成「在較長的自主工作階段結束後審查交付物」。
- 適合搭配 worktree 平行作業。

### 側欄：既有系統與權威來源

**重點**

- Jira、需求管理工具、Figma、變更委員會這些既有系統很難換掉，新流程必須配合它們。
- 原則：**每種交付物只指定一個權威來源**。三種做法：
  1. 以 repo 為準。
  2. 以既有系統為準：Claude 在工作階段開始時讀取，再透過 MCP 寫回。
  3. 只做互連：在兩邊互相記錄紀錄 ID 與 commit SHA。

### `CLAUDE.md`

**重點**

- 納入版控的檔案，內容是指令、慣例、架構與常犯的錯誤。每個工作階段開始時都會讀取。
- **怎麼做**
  1. 用 `/init` 產生初稿。
  2. 刪到只剩第一天就需要的內容。
  3. 提交進 git。
  4. Claude 同一個錯犯兩次，才把修正寫進去。
  5. 控制在一頁以內。

> **原文範例：`CLAUDE.md`**（約 18 行）
> 以條列分區記錄指令、慣例與注意事項。請見原文對應段落。

**衡量**：`CLAUDE.md` 本該擋下卻仍重複發生的錯誤數；新人第一個 PR 被合併的時間。

### 把團隊知識寫成 skills

**重點**

- **必須一致套用的知識**才寫成 skill。其他內容放進 `CLAUDE.md` 或提示詞就夠了。
- skill 是一個含 `SKILL.md` 的資料夾。可以放在 `.claude/skills/<名稱>/`，或透過 plugin 發佈。
- 寫完要實測它會不會被觸發。
- skill 是**建議性**的。硬性規定必須有 hook 或 PR 時的檢查在後面兜底。

> **原文範例：`.claude/skills/secure-api-review/SKILL.md`**（約 16 行）
> 一份 API 安全審查 skill，含 YAML frontmatter 與編號檢查步驟。請見原文對應段落。

### 用 hooks 當建置期防護

**重點**

- hooks 提供**確定性**的強制執行。常見用途：擋下對受保護路徑的編輯、編輯後自動跑 formatter 和 linter、防止憑證進入 diff。
- build 期間的 hook 要快，而且只看被改動的檔案。完整測試套件留到 commit 或 PR 時再跑。
- 需要人核准的 hook 屬於 Deploy 階段。放在 build 期間，等於把人放回每個平行工作階段的關鍵路徑上。

### 平行工作階段與 subagents

**重點**

- 每個 Claude 工作階段各自用一個 git worktree，例如 `claude --worktree feature-auth`。
- 先開兩到三個。只有在審查跟得上的前提下，才再增加。
- subagent 定義在 `.claude/agents/`，有自己的 context window 和工具限制。原文舉的例子有程式簡化器、驗證器、研究員。

> **原文範例：`.claude/agents/verifier.md`**（約 6 行）
> 一個驗證用 subagent 的定義：frontmatter 加一小段說明。請見原文對應段落。

**衡量**

- 審查品質不下滑的前提下，每位工程師能同時跑幾個工作階段。
- 每週合併的變更數，搭配返工率一起看。

---

## Test（測試）

本階段的原則：每個工作階段在交給人之前，先自己驗證。駕駛 agent 的那些設定本身也要做回歸測試。

### 給 Claude 一個回饋迴路

**重點**

- Claude 自己跑測試、build 或截圖比對，反覆修改直到通過。最後可以再加一個 context 乾淨的驗證 subagent 做最終檢查（選用）。
- **怎麼做**
  - 把所有檢查包成一個指令，例如 `make test`、`npm test`。
  - 在 `CLAUDE.md` 列出這些指令，以及健康的輸出長什麼樣子。
  - 設定可量化的目標。
- **修 bug 的模式**
  1. 先寫一個會失敗的測試並提交。
  2. 再讓 agent 在**不改測試**的前提下修好它。可以用 hook 在修 bug 期間擋下對測試檔的編輯。
- **UI 的模式**：實作 → 截圖 → 比對 → 調整。跑兩到三輪很正常。
- **證據**：用工具實際輸出的測試或 build 結果，附在 PR 的檢查紀錄上，而不是採信 agent 的自述。

> **原文範例：`CLAUDE.md` 的驗證區塊**（約 7 行）
> 列出驗證指令與預期輸出。請見原文對應段落。

### 在 CI 持續跑 evals

**重點**

- evals 是 AI 原生版本的階段關卡式 QA。做法是準備 20 到 50 個真實任務，每個任務都有一段提示詞和一組檢查。
- 兩種時機要跑：在 CI 定期跑，以及 `CLAUDE.md`、skills、hooks 一有變更就跑。設定變更要以通過率作為合併門檻。
- 每一次 production 事故都要變成一個永久的 eval。

> **原文範例：`.github/workflows/agent-evals.yml`**（約 20 行）
> 一個 GitHub Actions workflow，以 shell 迴圈逐一執行 eval 任務。請見原文對應段落。

**衡量**：通過率隨時間的變化；在 CI 抓到和在 production 才發現的回歸，兩者的比例。

---

## Deploy（部署）

本階段的原則有三條：

1. 審查是雙向的。
2. 治理在 agent 動作的當下就強制執行。
3. agent 可以做到 production 關卡之前的所有事，但不越過那道關卡。

### 讓 AI 加入 PR 審查迴圈

**重點**

- Claude 依 `REVIEW.md` 審查進來的 PR，分成幾輪看：bug、安全、是否符合 spec／plan／設計原則。它也會回應 `@claude` 留言並推送修正。
- 兩種導入方式：使用託管的 Code Review 服務，或自架 `claude-code-action`。
- 分支保護仍然要求 code owner 核准。審查發現本身不會核准 PR，也不會擋下 PR。
- 審查發現要回饋進 `CLAUDE.md`。每月調整一次吹毛求疵類意見的數量與嚴重度評等。

> **原文範例：`REVIEW.md`**（約 15 行）
> 定義審查分幾輪、每輪看什麼。請見原文對應段落。

**衡量**：到第一次審查的時間；合併前抓到的缺陷數和漏到合併後的缺陷數。

### 用 hooks 當審批關卡

**重點**

- hook 有三種結果：allow（放行）、ask（要求人確認）、block（擋下）。production 部署這類發版關卡用 ask 或 block。
- 團隊層的 hooks 放在 `.claude/settings.json`。不可妥協的 hooks 放進 managed settings，工程師無法停用。
- block 時要說明原因，並指出該走哪條核准途徑。
- 每一次放行或擋下的決定，都要附時間戳記留下紀錄。

> **原文範例**
> - `.claude/settings.json`（約 12 行）：註冊部署前要執行的 hook。
> - `.claude/hooks/production-gate.sh`（約 10 行）：關卡腳本本身，判斷指令是否觸及 production。
>
> 請見原文對應段落。

### 實例：受監管企業的 managed settings

**重點**

由管理員部署的一份 JSON 設定，涵蓋：

- 禁止讀取機密、禁止使用網路工具的規則。
- 允許安全的 build、測試、lint 指令。
- 停用 bypass 模式。
- 作業系統層沙箱，搭配網域白名單。
- 封鎖憑證檔。
- hooks 與 MCP server 只能由管理端設定。
- 只允許核准的 plugin marketplace。
- 規定 Claude Code 的最低版本。

作者強調這只是**裁剪用的起點**，不是照抄的範本。

> **原文範例：managed settings JSON**（約 35 行）
> 後面附有逐一說明各設定鍵的條列。請見原文對應段落。

### CI/CD 整合與部署

**重點**

- 在 CI 以非互動模式執行 Claude，處理需要判斷的步驟，例如分流失敗原因、彙整不穩定的測試、撰寫 changelog。
- 先從唯讀開始，再把會寫入的步驟放到既有關卡後面。
- agent 的 job 要在沙箱中執行，使用短效、範圍受限的 token，預設不持有任何 production 憑證。
- 部署工具透過 MCP 開放，並依環境限定範圍。自主程度分級：

  | 環境 | agent 可以做的事 |
  |---|---|
  | dev | 自由操作 |
  | staging | 介於兩者之間 |
  | production | 只能準備，執行要由發版經理授權 |

- 回滾要做成一個演練過的單一指令。

> **原文範例：管線步驟**（約 6 行）
> 一段 YAML，示範在管線中呼叫 `claude -p`。請見原文對應段落。

---

## Maintain（維運）

迴圈在這個階段閉合。觸發來源可以是突破控制帶、工單、頻道訊息或排程。觸發後直接叫起 Claude，觸發路徑上沒有人。階段之間設有**信心關卡**，由確定性檢查或對抗式審查者擔任，決定要繼續還是升級給人處理。

### 維運與閉合迴圈

**重點**

- 傳統維運是被動的：告警可能被漏看，事後檢討的結論也可能永遠回不到程式碼。
- AI 原生的做法：觸發事件叫起 Claude，Claude 診斷後把結果寫成 `intent.md`，再走一遍前面的各個階段。

### 閉合迴圈的實作

**重點**

- **偵測不用模型**：由確定性腳本監看單一指標，例如 CI 測試失敗率、部署後的 5xx 比率、PR 週期時間。比較的基準是滾動基線（平均數與標準差），搭配 Western Electric 或類似的判定規則。
- 回應分級寫在納入版控的設定檔裡：

  | 偏離程度 | 回應 |
  |---|---|
  | 1σ | 腳本只記錄 |
  | 2σ | Claude 唯讀診斷 |
  | 3σ | Claude 可以提 PR，或執行事先核准的 runbook |

- Claude 以無狀態方式執行，可以是 CI 的一個步驟，或一個 Agent SDK 服務。
- 輸出是一份 `intent.md`，內容包括：異常、證據、結果、受影響的系統、待解問題。
- 每修好一個問題，就新增一個對應的事故 eval。
- 原文舉的例子：隔離不穩定的測試；部署後 5xx 突破 3σ 時觸發回滾。

> **原文範例：`bands.yaml`**（約 9 行）
> 以 CI 測試失敗率為例，定義 1σ、2σ、3σ 三級的回應。請見原文對應段落。

### 定期掃描程式碼庫

**重點**

- 安全掃描依排程執行，觸發路徑上沒有人。掃描結果和其他變更一樣，要走 PR 審查關卡。
- 託管版本是 Claude Security，目前以 public beta 提供給 Claude Enterprise 組織。它用 Claude Mythos 5 掃描，會逐筆驗證發現並附上信心評等。
- **怎麼做**
  1. 連接 repo。
  2. 跑一次基準掃描。
  3. 為每個專案設定排程，預設每週一次。
  4. 駁回的發現要記錄理由。
  5. 修補一律走 PR 審查。
  6. 把發現匯出到既有的追蹤系統。

**衡量**：已排程掃描的 repo 比例；從發現到開出 PR 的時間；每次掃描的漏洞數趨勢。

### 用 Claude Tag 讓 Claude 值班

**重點**

- Claude Tag（public beta，Slack）以應變者的身分加入事故頻道，頻道本身就是稽核軌跡。
- Claude 可以透過 MCP 確認指標已回到基線，並把事後檢討寫進納入版控的經驗教訓檔。
- 小修正以 PR 形式送出，較大的工作則寫成 `intent.md`。

![原文圖 4：Claude Tag 在事故頻道中值班](https://assets.claude.com/c84d83832da7d5dcc41d79cd919446480f7755a7.png)

*原文圖 4（圖片來源：Anthropic）。圖意：請求、診斷、人的授權與修正都留在處理事故的頻道裡，所以頻道就是稽核軌跡。*

---

## 結語

- 現在的模型與 harness 已經能讓組織改造整個 SDLC，同時讓人的判斷與治理留在核心位置。
- 作者的收尾大意：迴圈持續運轉，人的判斷始終位在迴圈之上。

### 資源與致謝

- 原文末依導入順序列出平台團隊需要的 Claude Code 官方文件：
  - 管理員設定、settings、伺服器端 managed settings
  - 權限、沙箱、hooks（指南與參考）
  - skills、plugin marketplace、managed MCP
  - 第三方部署（Bedrock、Vertex、Foundry）、網路設定
  - OpenTelemetry 監控、analytics、Compliance API、安全模型
- 致謝：Jim Blackhurst、Will Steuk、Jamal Arif。

---

## 延伸閱讀（原文內連結）

- [Securing an AI-native SDLC at Anthropic](https://claude.com/resources/articles/how-anthropic-secures-its-ai-native-software-development-lifecycle)
- [How Claude Tag runs on-call for CI/CD at Anthropic](https://claude.com/resources/articles/ai-ci-cd-on-call)
- [Claude Agent SDK 文件](https://platform.claude.com/docs/en/agent-sdk/overview)
- 產品頁：[Claude Code](https://claude.com/product/claude-code)・[Claude Design](https://claude.com/product/design)・[Claude Tag](https://claude.com/product/tag)・[Claude Security](https://claude.com/product/claude-security)
