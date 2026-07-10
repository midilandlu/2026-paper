# Claude AI + Creo Parametric：第一個可運作的 MCP 整合 (逐步教學)

**原始影片連結：** [https://www.youtube.com/watch?v=ws6cdFytFNs](https://www.youtube.com/watch?v=ws6cdFytFNs)
**翻譯日期：** 2026-06-29

---

大家好，歡迎來到 Engineering Preetam (工程普里坦)。今天這段影片裡，我要給大家展示一些東西。這或許是關於這個主題的第一支影片，我將向你展示如何將 Creo 連接到 Claude。在右側，我打開了 Claude。讓我問一個問題：我的系統目前運行的是 Creo Parametric 嗎？

您可以看到它回答說正在系統上運行並且可以訪問。它接著問我是否想查看此會話中有哪些活動，像是當前模型和已載入的檔案。我會說「是，為什麼不呢？」。

現在 Creo Parametric 正在與 Claude 互動。接著，我對它說，這是一個夾具模型，我認為它的參數設定不正確（這個夾具可以進行彎曲）。我建議 Claude 自行正確設定所有必要的參數。讓我向您展示它現在有哪些參數，這樣您就知道目前確實沒有任何參數。

我們來看看。首先，它會載入現有參數，但似乎沒有任何設定。而這正是我們剛才在檢查參數時看到的情況。現在，Claude 將自動為我們寫入參數。好的，看起來參數現在已經寫入 Creo Parametric 中了，我們在介面裡也能看到。

太棒了，各位。我的意思是，這正是我想要達到的效果。

現在，假設我想創建一個 BOM（物料清單）並將其匯出為 Excel 檔案，我也可以這樣做。我輸入要求：『請產生一個 BOM 模型清單，並以 Excel 格式匯出。』Claude 成功解讀了這是一個 BOM 需求。好的，那我現在就試試，看看效果如何。

好的，我現在在 Excel 中打開了這個 BOM 檔案。它確實以一種大多數公司都能輕鬆閱讀的格式創建了 BOM，這真是太棒了，各位。

---

**現在，讓我來談談它的運作原理。**

如果我進入文件設置，然後在開發工具中，你會看到 **Creoson** 正在運行。所以，我們在這裡所做的基本上是透過 **MCP (Model Context Protocol)** 連接埠與 PTC Creo Parametric 進行通訊。

讓這一切如此特別的原因在於，Creo 官方自己也還沒有正式發表這款整合功能。所以，我非常確定這支影片是第一個向你展示如何使用 MCP 協議將 Claude 連接到 PTC Creo Parametric 的示範。

問題是，你無法直接將 Claude 連接到 PTC Creo，因為 PTC Creo 目前原生還不支援 MCP 協議。但是有一款名為 **Creoson** 的開源外掛程式，它可在網路上完全免費取得，你只需要下載這個。

要使用 Creoson，需要安裝 **J-Link**，這是 PTC Creo Parametric 安裝過程的一部分。所以，在安裝 Creo 時我們需要確保已經勾選了 J-Link。當我們啟動 Creoson 會話後，Creoson 就可以透過 J-Link 與 PTC Creo 進行通訊。

我們在這裡所做的，就是在 **Creoson 和 Claude 之間建造了一座橋樑**。我們採用的方法是使用 Python（如果有人需要這個腳本，我可以提供給你）。這基本上在 Creoson（它只理解 JSON）和 Claude 之間建立了一座中介橋樑。

- **Claude** 只理解 MCP（模型上下文協定）。
- **Creoson** 只理解 JSON。

所以，實際上發生的情況是：**Claude 桌面版透過 MCP 連接到這台橋接伺服器，該橋接伺服器將 MCP 請求轉換為 HTTP JSON 請求，然後 Creoson 接收到 JSON 請求後，透過 J-Link 真正去與 Creo Parametric 通訊。**

各位，希望這段影片的總結能對你們有所幫助。如果是這樣的話，請務必訂閱 Engineering Preetam 頻道，我很快就會為您帶來另一個類似的教學影片。在此之前，請多保重，再見。
