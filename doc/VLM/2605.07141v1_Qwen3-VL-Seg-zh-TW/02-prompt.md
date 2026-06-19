# 翻譯任務提示 (Translation Prompt)

## 任務目標
請將這篇探討多模態大型語言模型 (MLLMs) 應用於「開放世界參照分割 (Open-world referring segmentation)」的學術文章，翻譯成流暢的繁體中文 (zh-TW)。

## 翻譯風格與目標受眾
- **目標受眾：** 一般讀者 (general)
- **翻譯風格：** 說故事風格 (storytelling)
請打破原文生硬的學術句型，將內容轉化為流暢、引人入勝的敘事風格。我們要像是在為一位對科技有興趣的朋友解釋一項酷炫的新技術一樣，將 Qwen3-VL-Seg 的誕生寫得像是一場克服萬難的探險，適時對較為艱澀的 AI 概念加上簡短註釋，讓讀者能輕鬆進入狀況。

## 術語表 (Glossary)
- Multimodal Large Language Models (MLLMs): 多模態大型語言模型
- Open-world referring segmentation: 開放世界參照分割
- Visual grounding: 視覺定位
- Bounding box / bbox: 邊界框
- Pixel-level mask: 像素級遮罩
- Box-guided mask decoder: 邊界框引導遮罩解碼器
- Multi-scale spatial feature injection: 多尺度空間特徵注入
- Spatial-semantic query construction: 空間語義查詢建構
- Box-guided high-resolution pixel fusion: 邊界框引導高解析度像素融合
- Iterative mask-aware query refinement: 疊代式遮罩感知查詢細化
- In-distribution (ID): 分佈內
- Out-of-distribution (OOD): 分佈外

## 翻譯指引與挑戰
1. **重寫而非直譯 (Rewrite, not translate)：** 使用地道的繁體中文句型，勇敢拆解長句。將學術式的被動語態與長修飾語，改寫成口語化、主動的短句。品質測試：「讀起來像是一開始就用中文寫的文章嗎？」
2. **準確性至上 (Accuracy first)：** 演算法的步驟、事實、數據、邏輯必須與原文完全一致。
3. **適度解釋 (Proactive interpretation)：** 遇到專有名詞時，請在第一次出現時加上精簡註解，使用 `（**解釋**）` 的格式。例如：開放世界參照分割（**能根據任意自然語言描述，精準描繪出圖像中對應物體輪廓的能力**）。請保持克制，避免過多註解打斷閱讀節奏。
4. **保留格式 (Preserve format)：** 請保留所有的 Markdown 格式，包含標題、數學公式、代碼塊、清單等。
5. **語氣流暢：** 讓前後文銜接自然，使枯燥的數據與架構讀起來如同精彩的科技報導。
