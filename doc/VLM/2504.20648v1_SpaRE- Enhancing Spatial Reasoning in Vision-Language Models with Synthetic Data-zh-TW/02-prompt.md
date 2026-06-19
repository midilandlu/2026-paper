# 翻譯任務提示 (Translation Prompt)

## 任務目標
請將這篇關於提升視覺語言模型 (VLMs) 空間推理能力的學術文章，翻譯成流暢、通俗易懂的繁體中文 (zh-TW)。

## 翻譯風格與目標受眾
- **目標受眾：** 一般讀者 (general)
- **翻譯風格：** 說故事風格 (storytelling)
請打破原文生硬的學術句型，將內容轉化為流暢、引人入勝的敘事風格。我們要像是在為一位對科技有興趣的朋友解釋一項酷炫的新技術一樣，將 SpaRE 的研發過程、遇到的空間推理長尾問題、以及如何藉由超詳細影像描述來生成合成問答對的過程，寫得像是一場克服萬難的探險。適時對較為艱澀的 AI 概念加上簡短註釋，讓讀者能輕鬆進入狀況。

## 術語表 (Glossary)
- Vision-Language Models (VLMs): 視覺語言模型
- Spatial Reasoning: 空間推理
- Synthetic Data: 合成資料
- What's Up benchmark: What's Up 基準測試
- Localized Narratives: 本地化敘事
- DOCCI: DOCCI
- PixMo-Cap: PixMo-Cap
- Spatial relations: 空間關係
- Question-Answer (QA) pairs: 問答對
- Hallucination: 幻覺
- Bounding box / bbox: 邊界框
- Supervised fine-tuning (SFT): 監督式微調
- Negative log-likelihood: 負對數似然
- Intersection-over-Union (IoU): 交併比
- Mean Intersection-over-Union (mIoU): 平均交併比
- What is to the right of the orange tiger?: 橘色老虎的右邊是什麼？
- Which animal figurine is located on the leftmost side?: 哪個動物公仔位於最左邊？
- What animal is in the middle of the arrangement?: 排在中間的是什麼動物？
- What is in the background?: 背景是什麼？

## 翻譯指引與挑戰
1. **重寫而非直譯 (Rewrite, not translate)：** 使用地道的繁體中文句型，勇敢拆解長句。將學術式的被動語態與長修飾語，改寫成口語化、主動的短句。品質測試：「讀起來像是一開始就用中文寫的文章嗎？」
2. **準確性至上 (Accuracy first)：** 演算法的步驟、事實、數據、邏輯必須與原文完全一致。
3. **適度解釋 (Proactive interpretation)：** 遇到專有名詞時，請在第一次出現時加上精簡註解，使用 `（**解釋**）` 的格式。例如：空間推理（**理解與解釋圖像中物體之間空間位置關係的能力**）。請保持克制，避免過多註解打斷閱讀節奏。
4. **保留格式與圖片 (Preserve format & images)：** 請保留所有的 Markdown 格式，包含標題、數學公式、代碼塊、清單等。特別是圖片標記如 `![](2504.20648v1_SpaRE-images/...)`，請原封不動保留，確保圖片正常顯示。
5. **語氣流暢：** 讓前後文銜接自然，使枯燥的數據與架構讀起來如同精彩的科技報導。
