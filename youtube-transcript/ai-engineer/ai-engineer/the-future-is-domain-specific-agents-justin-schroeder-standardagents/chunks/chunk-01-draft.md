# The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents
未來屬於「特定領域代理」 (Domain-Specific Agents) —— 賈斯汀·許洛德 (Justin Schroeder)，StandardAgents

“Composition over inheritance” has always been a good engineering rule. It may also be the unlock for useful AI. A Gmail agent is fundamentally more powerful than a Gmail skill — and when composed with Sheets, Notion, and GitHub agents, the system gets more capable, more reliable, and cheaper to run
「組合優於繼承」（Composition over inheritance）向來是軟體工程的黃金法則。如今，它可能也是解鎖實用 AI 的關鍵。一個 Gmail 代理（Agent）在本質上遠比單純的 Gmail 技能（Skill）還要強大——而當它與 Sheets（試算表）、Notion 和 GitHub 代理組合在一起時，整個系統不僅功能更強、更加可靠，運行成本也更低。

Okay, so I'm going to be talking about domain-specific agents and why I really think that they are going to play an unbelievably important role in the future of AI and in the future of how we build agents. To get started real quick, my name's Justin Schrader. Uh you can find me on X at JP Schrader. And um I work at a small company called Standard Agents, which nobody's heard of right now cuz we're still kind of in stealth mode. Um after this talk, if you're interested, feel free to reach out to me and uh I can let you know a little bit more. [00:00:02 → 00:00:39]
大家好，我今天要談談「特定領域代理」（domain-specific agents），以及為什麼我深信它們將在 AI 的未來、甚至在我們打造代理的方式上，扮演舉足輕重的角色。在開始之前，我先快速自我介紹一下。我叫賈斯汀·許洛德。你可以在 X（前身為 Twitter）上透過 JP Schrader 找到我。我目前在一家叫做 Standard Agents 的小公司工作，各位現在應該都沒聽過，因為我們還處於隱蔽模式（stealth mode，**指新創公司在正式發布產品前保持低調的階段**）。演講結束後，如果你有興趣，歡迎隨時聯絡我，我可以再多透露一點消息。[00:00:02 → 00:00:39]

Mostly, I'm known for doing a lot of different open-source projects. Uh Dmux, which is a great multiplexer for all of your coding agents. Uh ArrowJS, which is sort of like a UI framework, sort of like React for um the agentic era. A bunch more that I won't get into, but you know, maybe check them out if you're interested. Okay. [00:00:37 → 00:00:59]
我最為人所知的，應該是參與了許多不同的開源專案。像是 Dmux，這是一個非常棒的多工器（multiplexer），能用來管理你所有的程式代理。還有 ArrowJS，它有點像是一個使用者介面（UI）框架，可以想成是代理時代（agentic era）的 React。除此之外還有很多，我就不一一贅述了，有興趣的話可以去看看。好，我們進入正題。[00:00:37 → 00:00:59]

I think we can all agree that the moment in time that we are in is very similar to the Industrial Revolution. Um in fact, it might be like an accelerated Industrial Revolution. Maybe it's a bigger deal, but it's certainly not smaller. I probably don't need to convince you of that if you're listening to one of these talks. Um but that is the moment we find us find ourselves in. [00:00:57 → 00:01:18]
我想大家應該都同意，我們現在所處的時代，非常像是一場工業革命。事實上，它可能是一場「加速版」的工業革命。或許它的影響力更為深遠，但絕對不會比較小。如果你正在聽這場演講，我大概也不需要費力說服你這一點。但沒錯，這正是我們此刻所處的歷史節點。[00:00:57 → 00:01:18]

So, I actually think it's helpful to go back and sort of look at what was the key catalyst of the Industrial Revolution. And ultimately, it was that we learned how to harness energy with machines. We learned how to harness energy with machines. And what's interesting is that in this next era, we are essentially learning to harness intelligence with agents. And agents, I think, can be thought of a little bit like the machine of yesteryear. [00:01:17 → 00:01:47]
因此，我認為回顧歷史，看看什麼是推動工業革命的關鍵催化劑，其實是很有幫助的。說到底，關鍵在於我們學會了如何用機器來駕馭能源。我們學會了用機器來駕馭能源。而有趣的是，在接下來的這個新時代，我們本質上正在學習如何用代理來駕馭智慧。我認為，代理可以被看作是昔日的機器。[00:01:17 → 00:01:47]

It's the thing that is going to use the intelligence. Not so much us, but the agents. What's interesting about that is I bet if I was in an actual room with you guys and and we all put up our hands, I bet a lot of you when I say what is an agent instantly have examples that pop into mind, but also probably can't pull out a definition immediately. Some of you maybe can, um but the reality is that we haven't even coalesced on a definition of what an agent is, even though we're well into the agentic era at this point. And I think that's kind of interesting. [00:01:47 → 00:02:27]
代理將是運用這些智慧的主體。與其說是由我們人類來運用，不如說是由代理來發揮。這其中有趣的地方在於，如果我現在是在一個真正的會議室裡和你們面對面，請大家舉手，我敢打賭，當我問「什麼是代理？」時，你們很多人腦海中會立刻浮現一些例子，但可能無法立刻給出一個明確的定義。或許有些人可以，但現實是，儘管我們現在已經深入了代理時代，我們甚至還沒有對「什麼是代理」達成一個統一的定義。我覺得這滿有意思的。[00:01:47 → 00:02:27]

Um here's my definition. You can feel free to agree with it or not, but agents are deterministic software that harness the non-deterministic results produced by models in pursuit of some desired objective. Now, deterministic software might make you think more like a harness, and I actually think the distinction between an agent and a harness is really pedantic, not very helpful, um and for the most part, in most cases, you can just conflate the two. A harness is an agent and an agent is a harness, okay? And for the for the purposes of this talk, we're going to go ahead and just move forward with that. [00:02:25 → 00:03:04]
以下是我的定義。你可以同意或不同意，但我是這麼看的：代理是一種確定性的（deterministic）軟體，它駕馭模型所產生的非確定性結果，以追求某個期望的目標。「確定性的軟體」可能會讓你聯想到控制框架（harness，**指用來控制和管理其他程式或系統的軟體結構**），而我其實覺得，去區分「代理」和「控制框架」有點咬文嚼字，沒什麼實質幫助。在大多數情況下，你大可以把它們混為一談。控制框架就是代理，代理就是控制框架，好嗎？為了這場演講的順利進行，我們就先帶著這個共識繼續往下走。[00:02:25 → 00:03:04]

I think you could probably make some good arguments for why one is the other and vice versa, but really not important right now. Now, if you did have some examples pop to mind, they might have been like Claude or Codex, um you know, OpenClaude, Hermes. But you know what's interesting is I bet if you went out onto, you know, the the streets of corporate America in any city, maybe not San Francisco, but any city in America, and you asked somebody just in an office building, could you name an agent by name? I think some people are going to get Claude. Some people might get Codex. [00:03:04 → 00:03:46]
我想你或許能提出一些很好的論點來解釋為什麼這兩者是一樣的，反之亦然，但現在這真的不重要。剛才如果你的腦海中確實浮現了一些代理的例子，那可能是 Claude 或是 Codex，也可能是 OpenClaude、Hermes。但有趣的是，我敢打賭，如果你走到美國企業界的街頭——隨便哪個城市，也許不包括舊金山，但美國任何一個城市的辦公大樓裡——隨便問一個人：「你能說出一個代理的名字嗎？」我想有些人會說出 Claude，有些人可能會說出 Codex。[00:03:04 → 00:03:46]

And that's about it. I don't think hardly anybody's going to be getting OpenClaude or Hermes. Uh Uh, and and really even Claude, I don't know that people would even know that that's an agent. These things are not well understood. And yet, what's so crazy is everybody is building agents. [00:03:45 → 00:04:04]
大概也就這樣了。我覺得幾乎沒人會說出 OpenClaude 或 Hermes。而且說真的，就算是 Claude，我也不確定人們是否知道它就是一個代理。大眾對這些東西的了解並不深。然而，瘋狂的是，現在每個人都在打造代理。[00:03:45 → 00:04:04]

I have a real estate agency down the street that's building agents. I know in like independent private insurance brokers building their own agents. I know Fortune 500 companies, lots of them, building their own custom agents. Everybody is trying to build their own custom agents. And I know people don't believe me, uh, but go talk to them. [00:04:04 → 00:04:26]
我住的街角有一家房地產仲介公司，他們在打造代理。我認識一些獨立的私人保險經紀人，他們也在打造自己的代理。我知道很多財星 500 大企業都在打造專屬的客製化代理。每個人都在嘗試建立屬於自己的客製化代理。我知道有些人可能不相信我，但不妨去跟他們聊聊看。[00:04:04 → 00:04:26]

Just go talk to people. They are trying to build custom agents. And I can't help but wonder why. Nobody seems to be asking this question, why? There's already AI everywhere. [00:04:26 → 00:04:38]
去和業界的人聊聊吧。他們真的都在嘗試打造客製化代理。我不禁納悶：為什麼？似乎沒有人問過這個問題：為什麼？現在到處都是 AI 了啊。[00:04:26 → 00:04:38]

You can get on ChatGPT all the way down to some open-source model from China on some, you know, rickety website. There's everything in between, but still people want to build custom agents. And ultimately, it comes down to integration. Businesses want their data properly integrated into AI. They They believe, and are probably right, that if they appropriately leverage AI, they're going to have these dramatic gains in their business and so on and so forth. [00:04:38 → 00:05:06]
你可以用 ChatGPT，也可以去一些簡陋的網站上用來自中國的開源模型。這之間有著各種各樣的選擇，但人們還是想要打造客製化代理。歸根究柢，這一切都跟「整合」有關。企業希望他們的數據能妥善地整合到 AI 之中。他們相信——而且這想法很可能是對的——如果能適當地利用 AI，將會為他們的業務帶來驚人的成長等等。[00:04:38 → 00:05:06]

So, they need to figure out how to get integrated. And building their own custom agents is obviously a way to do that. And it's one of the first ways that they discover, um, as a mechanism for doing it. The problem, though, is that agents are really hard. You have to take very, very careful care of the agentic loop and make sure that it's properly orchestrated. [00:05:04 → 00:05:28]
因此，他們必須找出整合的方法。而打造自己的客製化代理，顯然是達成這個目標的途徑之一。這也是他們最初發現可以用來實現整合的機制之一。然而，問題在於，打造代理真的非常困難。你必須非常非常小心地處理代理循環（agentic loop，**指代理接收輸入、思考並採取行動的反覆過程**），並確保它被正確地協調運作。[00:05:04 → 00:05:28]

There are a ton of different provider abstractions you need to think about. Um, fortunately, there's some good tools coming out around that, you know, like the the Vercel AI SDK is great. Um, durable execution, you need to make sure if there's faults, we can pick back up. These are relatively hard problems, um, especially if you're thinking about it at scale. And the reality is there's just tons more. [00:05:28 → 00:05:50]
你需要考慮一大堆不同的服務供應商抽象層（provider abstractions）。幸運的是，現在這方面開始出現了一些不錯的工具，像是 Vercel AI SDK 就非常棒。還有持久執行（durable execution）的問題，你必須確保系統在發生錯誤時能夠恢復運作。這些都是相對棘手的難題，特別是當你考慮到大規模運作時。而現實是，還有更多數不清的問題等著你。[00:05:28 → 00:05:50]

There's all kinds of validations and stop conditions and so on and so forth. And so what often happens is people do try to build their own custom agents, and they sort of work as a demo, but but not much more than that. Um, and really it turns out that it's an absolute nightmare for people. Um, building robust agents is just hard. And if you go talk to anybody in an IT department, they are pulling their hair out because there are so many different concerns. [00:05:50 → 00:06:20]
這裡面牽涉到各種驗證、停止條件等等。所以，經常發生的情況是：人們確實嘗試去打造自己的客製化代理，這些代理作為火力展示（demo）可能還算堪用，但也僅止於此了。實際上，這對大家來說簡直是一場惡夢。要打造出穩健的代理，真的太難了。如果你去問問 IT 部門的任何人，他們一定正為了這件事抓狂，因為要顧慮的地方實在太多了。[00:05:50 → 00:06:20]

Um, there's no defined way to build an agent right now. Like, actually no defined way. The closest thing maybe is, uh, Eve that just came out from Vercel is maybe like the closest thing. Um, but in reality, everybody's kind of coming up with their own way to do it. Um, telemetry and observability on these agents is unbelievably hard, especially at scale. [00:06:18 → 00:06:39]
目前，我們甚至還沒有一套打造代理的標準做法。是真的沒有。最接近標準的，大概是 Vercel 剛推出的 Eve 吧，這可能是最接近的東西了。但實際上，每個人都在摸索自己的做法。此外，要對這些代理進行遙測（telemetry）和可觀測性（observability）監控更是難如登天，尤其是在大規模部署時。[00:06:18 → 00:06:39]

Like, if you want to know exactly what is getting transmitted on every single step of every single turn of your agent, so that way you can diagnose it and fine-tune it and make sure things aren't going off the rails, that is very hard to do. Uh, agents are also not portable. So, if I do get a good agent working, if I've managed to climb to the top of, you know, this mountain and I've got a good agent that's finally working well, well, it works well on my machine. >> [laughter] >> But if I try to pass it off to somebody else, there's a very high likelihood that between all of the environment variable configurations and and system requirements and and runtimes, there's a good chance it's not going to run on that person's machine. And they're not composable. [00:06:39 → 00:07:23]
舉例來說，如果你想精確掌握代理在每一個回合的每一個步驟中到底傳輸了什麼資料，以便進行診斷、微調，並確保系統沒有失控，這是非常困難的。此外，代理也缺乏可攜性（portability）。所以，如果我真的成功打造出一個好用的代理——如果我好不容易爬到了這座山的頂端，終於有一個運作良好的代理了——嗯，它在我的電腦上運作得很好。 >> [笑聲] >> 但如果我試著把它交給其他人，在經歷了所有環境變數設定、系統需求和執行環境的差異後，它很有可能無法在那個人的電腦上執行。而且，它們還不具備可組合性（composable）。[00:06:39 → 00:07:23]

So, even if I get, you know, a really good chatbot working for my university, the chances that I'm going to then be able to reuse that for another thing is very, very low. I can't just easily share that. So, what often happens is after a short pursuit towards agents, people kind of back away and say, "Okay, fine. No more agents, no agents. Instead, we're going to do the MCP thing. [00:07:23 → 00:07:47]
因此，就算我成功為我的大學做了一個非常棒的聊天機器人，我要把它重複使用在其他專案上的機率也是微乎其微。我無法輕易地分享它。所以，通常的發展是：在短暫地追求打造代理之後，人們會打退堂鼓，然後說：「好吧，算了。不搞代理了，不搞了。我們改用 MCP（模型上下文協定）這套方法吧。」[00:07:23 → 00:07:47]

We've heard about this, it works. " And sure enough, Model Context Protocol, it does work. And really, it it works pretty well to take, you know, your corporate information like Zillow's information and then shove that into one of these really large pre-existing agents, something like Claude or ChatGPT, which I would consider a large general-purpose agent. Um and it and it sort of works like that. Uh and and it works okay. [00:07:47 → 00:08:15]
「我們聽說過這個，這方法行得通。」確實，模型上下文協定（Model Context Protocol）的確行得通。而且，要把你的企業資訊（比如房地產網站 Zillow 的資料）塞進像是 Claude 或 ChatGPT 這種現有的大型代理（我稱之為大型通用代理）中，MCP 確實運作得相當不錯。它差不多就是這樣運作的，效果也還可以。[00:07:47 → 00:08:15]

But if you take a look, this is actually from the MCP website, and if you take a look at what is supported in MCP clients around the world, you will notice that only one of these columns is actually filled out all the way down. And that, of course, is tools. So, MCP has become a de facto tool distribution mechanism for agents. So, if I need to get my company's tools into that other agent, then MCP's a good way to do that. It has not proven to be great at providing other value yet. [00:08:15 → 00:08:57]
但是如果你仔細看看這張圖，這是從 MCP 網站上擷取的，如果你看看全世界 MCP 客戶端所支援的功能，你會發現只有一欄是從頭到尾填滿的。那當然就是「工具」（tools）。因此，MCP 實質上已經成為了代理發布工具的一種標準機制。如果我需要把公司的工具整合到另一個代理中，MCP 是個好方法。但目前為止，它在提供其他價值方面的表現，還沒有被證明有多出色。[00:08:15 → 00:08:57]

And frankly, tools are just not enough. You know, I I I I like to joke that we didn't land a man on the moon by giving one guy a ton of tools. That's not a realistic way to get a really large project done. So, uh you know, maybe MCP's not the way, but aha, we have skills. We have skills, and skills are great. [00:08:55 → 00:09:20]
坦白說，光有工具是不夠的。我常開玩笑說，我們當年登陸月球，可不是靠著給一個人一大堆工具就辦到的。那不是完成大型專案的實際做法。所以，也許 MCP 不是最終解方。不過等等，我們還有「技能」（skills）。我們有技能，而且技能很棒。[00:08:55 → 00:09:20]

Um I I I actually do enjoy skills. I'm sure you do, too. We install them all the time for all kinds of things. And fundamentally, what a skill is is a markdown file, which basically works as documentation. Now, interestingly, there's lots of research out there that shows that if you use very many of these, it actually makes your agent substantially worse. [00:09:20 → 00:09:42]
我個人其實滿喜歡技能的。我相信你們也是。我們總是為了各種用途安裝它們。從根本上來說，技能就是一個 Markdown 檔案，基本上可以當作文件來使用。但有趣的是，現在有許多研究指出，如果你使用太多的技能，反而會讓你的代理表現大幅退步。[00:09:20 → 00:09:42]

But, they do work as documentation for various complex things. So, you know, back to the analogy of a man getting to the moon, it's a little bit like just giving this guy, you know, a ton of documentation. And the documentation's going to help, but it's not the fundamental problem. So, what's the fundamental problem? Okay. [00:09:38 → 00:10:02]
不過，它們確實可以作為處理各種複雜事務的說明文件。所以，回到登月的比喻，這就有點像是給那個人塞了一大堆的說明文件。這些文件雖然有幫助，但並沒有解決根本問題。那麼，根本問題究竟是什麼？好，讓我們來看看。[00:09:38 → 00:10:02]

Let's build up a basic agent stack here. Let's start with a model. All agents start with a model. Big one, small one, doesn't matter. They start with a model. [00:09:59 → 00:10:10]
讓我們在這裡建立一個基本的代理技術疊層（stack）。首先從模型（model）開始。所有的代理都是從模型開始的。不管模型是大是小，這都無所謂。它們都是從一個模型開始的。[00:09:59 → 00:10:10]

Then, you have something like a system prompt on top of that, which tells the model what its role in the grand universe is, sort of like its its life objective. Then, we have tools, the things that it can actually do, the effects it can take. And then, skills would be layered on top of that. And then, MCP would be layered on top of that. And then, finally, you have all the messages from the conversation. [00:10:08 → 00:10:34]
接著，在模型之上，你會加上像是「系統提示詞」（system prompt）這類的東西，它告訴模型它在這個浩瀚宇宙中的角色是什麼，有點像是它的人生目標。然後，我們有「工具」，也就是它實際能做的事情、能產生的作用。再往上疊加的是「技能」。然後是「MCP」疊在上面。最後，你擁有了對話中的所有「訊息」。[00:10:08 → 00:10:34]

That is roughly the stack of information that gets passed along within the runtime of an agent. And if you take a look here, almost all of it is context. Basically, everything. The system prompt, tools, skills, all of that is stuff that ends up in the context of the agent. And so, basically, people are trying to solve the integration problem by working on the context or the model. [00:10:34 → 00:11:07]
這大致上就是代理在執行期間（runtime）所傳遞的資訊疊層。如果你看看這個結構，會發現幾乎所有的東西都是「上下文脈絡」（context）。幾乎就是全部。系統提示詞、工具、技能，所有這些最終都會成為代理上下文的一部分。所以，基本上，人們都試圖透過調整上下文或模型，來解決整合的問題。[00:10:34 → 00:11:07]

These are the two areas where we constantly see new advances. We also see, you know, new new things come out like skills and and MCP, um new technologies, new protocols. They are all coming out in the in the area of the context and the model. So, how does it actually work then? Well, basically, you work at a company, you occasionally need to do some business travel, so you've got a couple travel MCPs installed. [00:11:07 → 00:11:36]
這也是我們不斷看到新進展的兩個領域。我們也看到一些新東西問世，像是技能、MCP，以及各種新技術、新協定。這些全都是圍繞著上下文和模型在發展。那麼，這到底是如何運作的呢？基本上，你在一家公司工作，偶爾需要出差，所以你安裝了幾個旅遊相關的 MCP。[00:11:07 → 00:11:36]

You've also got, you know, Figma and Playwright installed on yours. And all of these are building up in that context layer. And then you've got some, you know, Gmail MCPs to go check your mail for you and some Google Sheets to go fill out some other uh some other uh expense reports or something like that. And then you've got skills. You're a developer, so you've got some React fixers and linters. [00:11:36 → 00:11:59]
你的系統裡還裝了 Figma 和 Playwright（**一種自動化測試工具**）。所有這些東西都在那個上下文疊層中不斷累積。接著，你又安裝了一些 Gmail MCP 幫你收信，還有一些 Google Sheets MCP 幫你填寫出差的差旅報表之類的。然後，你還有各種技能。身為一個開發者，你擁有一些用來修復 React 程式碼和執行語法檢查（linters）的技能。[00:11:36 → 00:11:59]

This is actually, I think, like, the number one or the number two most popular MCP server that's out there. Um maybe you've got uh Matt's uh grill me skill or or maybe you've got the GitHub skill. And basically, what you're doing is you are inflating that context layer. And we have a term for this in engineering. It's called inheritance. [00:11:59 → 00:12:20]
順帶一提，我認為這可能是目前市面上數一數二受歡迎的 MCP 伺服器了。也許你還有 Matt 的 "grill me" 技能，或是 GitHub 技能。基本上，你正在做的，就是不斷膨脹那個上下文疊層。在軟體工程中，我們對此有個專有名詞，叫做「繼承」（inheritance）。[00:11:59 → 00:12:20]

The idea of inheritance is you take an object and then you add more attributes to it to allow that one object to have other properties. Right? And that's exactly what we are doing here with an agent. We're saying, "This agent is pretty good, but if we add all of these addish- additional extra layers, then the agent can do stuff that it previously couldn't do before. " That is exactly what inheritance is. [00:12:20 → 00:12:47]
繼承的概念是：你拿一個物件，然後為它加上更多的屬性，讓這個物件具備其他的特性，對吧？這正是我們在代理身上所做的事。我們是在說：「這個代理已經很不錯了，但如果我們加上所有這些額外的疊層，它就能做到以前做不到的事情。」這完完全全就是繼承的概念。[00:12:20 → 00:12:47]

And the truth about inheritance is it works. It does work. That's why these things are out there and they are working. But, there's an old saying, "Composition over inheritance. " And it turns out this this is as old as time. [00:12:47 → 00:13:06]
而關於繼承的真相是：它確實有效。它是真的有用。這就是為什麼這些東西存在於市場上，而且還能運作的原因。但是，有句老話說：「組合優於繼承。」事實證明，這是一個亙古不變的真理。[00:12:47 → 00:13:06]

Eventually, inheritance starts to break down. Imagine, like, you know, okay, I've got five skills on uh ChatGPT or on or on Claude, excuse me. And uh that works pretty well. Now, what if I have 100 skills? What if I have 1,000 skills? [00:13:04 → 00:13:21]
到最後，繼承的架構會開始崩潰。想像一下，好，我在 ChatGPT——抱歉，是在 Claude 上裝了五個技能。運作得還不錯。但是，如果我有 100 個技能呢？如果我有 1,000 個技能呢？[00:13:04 → 00:13:21]

There's some point at which I get diminishing returns from adding additional context. That's That's just obvious. We all kind of understand that implicitly. So, is there an alternative? Well, composition is the alternative to inheritance. [00:13:20 → 00:13:35]
到了一定程度後，添加額外的上下文會帶來「邊際效益遞減」（diminishing returns）。這是顯而易見的。我們大家心裡都清楚這點。那麼，有什麼替代方案嗎？有的，「組合」就是「繼承」的替代方案。[00:13:20 → 00:13:35]

It looks something like this. So, like imagine we have another little agent, and again, we're trying to provide Figma as an as a as a thing that can be done by our primary agent. Well, what we could do is have a tiny little agent where the actual system prompt of the agent is written specifically to be a Figma agent. It knows everything about Figma. It it knows all of its all of its context, all of its API, all of the right places to click and the things to do and mouse movements to make and everything like that. [00:13:35 → 00:14:08]
它看起來大概像這樣。想像一下，我們有另一個小型的代理，同樣地，我們希望我們的主代理能夠具備使用 Figma 的能力。我們可以怎麼做呢？我們可以建立一個非常迷你的代理，它的系統提示詞完全是專為成為一個「Figma 代理」而寫的。它對 Figma 瞭若指掌，知道所有相關的上下文、API，知道該點擊哪裡、該做什麼操作、滑鼠該怎麼移動，以及所有大大小小的細節。[00:13:35 → 00:14:08]

And then it has these precise tools that it needs to perform all of those actions, and nothing more. Just that. And then a very small message history, which just has to do with the Figma portion of this. And then you can have more of these. You can still have your Gmail and your travel and your Google Sheets and all that kind of stuff, but each of them is a separate isolated agent, a full agent. [00:14:08 → 00:14:33]
然後，它擁有執行這些操作所需的精確工具，僅此而已，沒有其他多餘的東西。就只有這些。接著是一段非常簡短的訊息紀錄，內容只跟 Figma 的操作有關。你可以擁有更多這樣的代理。你仍然可以有你的 Gmail 代理、旅遊代理、Google Sheets 代理等等，但它們每一個都是獨立、隔離的代理，都是一個完整的代理。[00:14:08 → 00:14:33]

Not just a little server with tools on it. It's a full agent with its own message history, its own agentic loop. And then above these, you have a coordinator. And the communication mechanism for all of these small agents speaking to the larger agent above it is just English. They just talk to each other the way a human does. [00:14:31 → 00:14:58]
不只是一個掛著工具的小型伺服器。這是一個擁有自己的訊息紀錄、自己的代理循環的完整代理。然後，在這些代理之上，你有一個協調者（coordinator）。而所有這些小型代理與上方較大型代理溝通的機制，就是使用英文。它們就像人類一樣，直接與彼此交談。[00:14:31 → 00:14:58]

So, if the primary agent is saying, "Oh, I should I should check my mail to see if there's anything about going on a trip. " Well, it knows to go ask Gmail for any new uh emails about a trip. Those funnel their way back up, says, "Oh, yeah, actually there's a trip coming up to Los Angeles this weekend. " And then it can go to our travel agent and start to make bookings. That's kind of a a rough idea of how something like this could work. [00:14:55 → 00:15:29]
所以，如果主代理說：「喔，我應該檢查一下信箱，看看有沒有關於出差的信件。」那麼，它就知道要去問 Gmail 代理，看看有沒有任何關於出差的新郵件。這些資訊會層層上報，Gmail 代理回覆：「喔，對，這個週末有一趟去洛杉磯的行程。」接著，主代理就可以去找旅遊代理開始訂票。這大概就是這種系統運作方式的初步構想。[00:14:55 → 00:15:29]

And the reality is it does work. And we know it works because this is actually how we got to the moon. There were teams of experts. Teams of experts with faces that looked like that and faces that looked like that. Each of them with different skills and capabilities. [00:15:27 → 00:15:46]
而現實是，這方法真的行得通。我們知道它行得通，因為我們當年就是這樣登上月球的。當時有一支支的專家團隊。這些專家長得像這樣，也長得像那樣。他們每個人都具備不同的技能和能力。[00:15:27 → 00:15:46]

And faces that looked like that. This is the Apollo 11 launch day. And look right here, there's an agent. I just found an agent sitting right there. >> [laughter] >> That brain of his is that's his LLM. [00:15:44 → 00:15:58]
還有長得像這樣的。這是阿波羅 11 號發射的那一天。你看看這裡，有一個代理。我剛剛發現那裡坐著一個代理。 >> [笑聲] >> 他的大腦就是他的 LLM（大型語言模型）。[00:15:44 → 00:15:58]

And here's his tools right there on the dashboard. Those are the tools. Now, he didn't have all the tools. He just had those tools. And he was really really really good at them. [00:15:58 → 00:16:08]
然後這是他的工具，就在控制台那邊。那些就是工具。當然，他並沒有掌握所有的工具。他只有那些工具。但他對那些工具非常、非常、非常在行。[00:15:58 → 00:16:08]

And then look at that mouth. That's the messages. Uh we are used to this. We can understand this. It implicitly works. [00:16:06 → 00:16:17]
然後看看那張嘴。那就是用來傳遞訊息的。我們對這種模式習以為常。我們完全能理解這種運作方式。它在無形中就是能順利運作。[00:16:06 → 00:16:17]

It's almost a form of biomimicry for the agentic world. Um it works. And I call them domain-specific agents. Um I don't think I was the first person to utter the words domain-specific agents. Certainly not the first person to have this idea. [00:16:14 → 00:16:31]
這幾乎可以說是代理世界的一種「仿生學」（biomimicry，**指模仿自然界生物系統的設計理念**）。它確實有效。我稱它們為「特定領域代理」。我想我大概不是第一個說出「特定領域代理」這個詞的人。當然也不是第一個想到這個點子的人。[00:16:14 → 00:16:31]

Um but that is what I want to talk to you about. Agents that are just targeted to very specific domain. And we over here at Standard Agents have been building this ecosystem for quite some time. So we've gotten to have a really good inside look at how they actually work. And I'm not ready to come out here and announce a product or anything like that. [00:16:29 → 00:16:51]
但這正是我今天想跟各位探討的主題：專注於非常特定領域的代理。我們在 Standard Agents 這裡，已經投入打造這個生態系統好一段時間了。因此，我們對它們實際的運作方式有了非常深入的了解。我今天不是來這裡發布什麼新產品的。[00:16:29 → 00:16:51]

Um but I can give you a little bit of a peek. First of all, they are far more token efficient. Far more token efficient. We regularly see over 80% token efficiency for any given task. Now, it's a little more complicated because you have to define those tasks a little bit more ahead of time. [00:16:51 → 00:17:12]
但我可以讓大家稍微窺探一下。首先，它們在 Token 的使用上要高效得多。效率高出非常多。我們經常在任何給定的任務中看到超過 80% 的 Token 效率。當然，這也會稍微複雜一些，因為你必須提前更詳細地定義這些任務。[00:16:51 → 00:17:12]

But if you can have an agent portability where I can take that Gmail agent, squeeze it up, and then send it to somebody else, we can create an ecosystem where we don't have to create every one of these skills and capabilities, but within that domain, you're going to get dramatic efficiency. Um and part of the reason is, if you think about the way that the context work works, I don't need to have the entire context of the conversation when I make a choice to do something. Instead, my primary coordinator level can just ask the Gmail uh hey, get that last email from Debbie. And that is the totality of the context. It literally just has the system message, its tools, and that message that came in. [00:17:10 → 00:17:57]
但是，如果你能擁有具備可攜性的代理，讓我可以把那個 Gmail 代理打包起來，然後傳送給其他人，我們就能創造一個生態系統，在裡面我們不需要重新發明每一種技能和能力；只要在這個特定領域內，你就能獲得驚人的效率。這其中一部分原因在於，如果你思考一下上下文運作的方式，當我要決定做某件事時，我並不需要整個對話的上下文。相反地，我主要的主協調器可以只告訴 Gmail 代理：「嘿，幫我找出 Debbie 寄來的那封最新郵件。」這就是全部的上下文了。它真的就只包含系統訊息、它的工具，以及剛收到的那條指令而已。[00:17:10 → 00:17:57]

And so, it is then able to perform this very targeted, very specialized, tiny little thing without all of the surrounding context. It's also far more practical with small language models. If you look at the difference in two models like DeepSeek uh V4 Flash and uh Fable 5, the cost difference is mind-boggling. It is 137 times cheaper than Fable per task. 137 and 37 times. [00:17:57 → 00:18:39]
因此，它就能夠在不需要所有周邊上下文的情況下，執行這個非常有針對性、非常專業、非常小巧的任務。此外，搭配小型語言模型使用時，這也實用得多。如果你看看像 DeepSeek V4 Flash 和 Fable 5 這兩個模型的差異，那成本的差距絕對會讓你瞠目結舌。以每次任務計算，前者比 Fable 便宜了 137 倍。足足 137 倍。[00:17:57 → 00:18:39]

Now, granted, if DeepSeek V4 Flash fails over and over and over again to do the job, then not only is it going to be, you know, not that much cheaper, it's also going to be much more annoying to use it. But that's why domain-specific agents are so great, because you don't need to have the V4 Flash do everything. Instead, it only needs to do the tasks that have been specifically picked for it to do. And with a very minimal context, it can execute those very faithfully. So, you get these dramatic cost reductions not only with the token efficiency, but also because you can use much smaller language models and even non-language models. [00:18:37 → 00:19:23]
當然，如果 DeepSeek V4 Flash 一次又一次地無法完成任務，那麼它不僅不會省多少錢，用起來還會讓人火冒三丈。但這正是特定領域代理之所以這麼棒的原因，因為你不需要讓 V4 Flash 做所有的事。相反地，它只需要去執行那些專門為它挑選的任務就好。而在極簡的上下文環境中，它可以非常忠實地完成這些任務。所以，你不僅能透過 Token 效率大幅降低成本，還能因為使用了更小的語言模型、甚至是非語言模型，而獲得驚人的成本優勢。[00:18:37 → 00:19:23]

You can use image generation and diffusion models. You can use all kinds of other models for smaller tasks. >> [snorts] >> You can also enforce really strict limits on the capabilities. And I think you know what I'm talking about. I'm talking about this. [00:19:23 → 00:19:38]
你可以使用影像生成和擴散模型（diffusion models）。你可以把各種其他的模型應用在較小的任務上。 >> [清了清嗓子] >> 你還可以對其功能施加非常嚴格的限制。我想你們知道我在說什麼。我指的就是這個。[00:19:23 → 00:19:38]

Uh we are all flying awfully close to the sun nowadays. We're everybody's just bypassing permissions left and right. And of course, you have to because a coding agent with a big model can do anything. And so, we use it to do everything. In a world that would be powered by smaller domain-specific agents, those agents can't do everything. [00:19:38 → 00:20:03]
我們現在大家都有點「太過大膽」了，就像飛得太靠近太陽的伊卡洛斯一樣。每個人都在到處繞過權限控制。當然，你必須這麼做，因為一個具備大型模型的程式碼代理，幾乎是無所不能的。所以，我們就用它來做所有的事情。但在一個由較小的特定領域代理所驅動的世界裡，這些代理可無法包辦一切。[00:19:38 → 00:20:03]

They can only do the things that are already explicitly approved for them to do. It doesn't mean that you still can't have permissions and permission dialogues, but you are opting into a much more controlled ecosystem. And I promise you, when you explain that to Doug in IT, he puts his heart at ease understanding the difference between those two. >> [snorts] >> And uh fourth, they these have excellent scaling characteristics. Because each of these agents is its own small little execution environment, you can parallelize them. [00:20:03 → 00:20:35]
它們只能做那些已經被明確批准去做的事情。這並不代表你就不能有權限機制或權限確認對話框了，而是你選擇進入了一個更加受控的生態系統。我向你保證，當你向 IT 部門的 Doug 解釋這一點時，一旦他明白這兩者的差異，他絕對會鬆一大口氣。 >> [清了清嗓子] >> 第四點，這些代理具有極佳的擴展特性（scaling characteristics）。因為每一個代理都是一個獨立的小型執行環境，所以你可以平行處理它們。[00:20:03 → 00:20:35]

You can put them on the cloud very easily without needing like a giant VPC up there. You can run thousands of instances all at the same time um in in all kinds of regions of the world. They don't actually need to be uh you know, geographically co-located or anything like that. Um so, they have very, very good scaling characteristics. Unfortunately, they don't exist. [00:20:35 → 00:21:02]
你可以非常輕易地把它們放到雲端上，不需要建立一個龐大的虛擬私有雲（VPC）。你可以同時執行數千個實例（instances），而且可以分散在世界各地。它們實際上不需要地理位置上的集中。所以，它們的擴展性非常、非常好。不幸的是，它們現在還不存在。[00:20:35 → 00:21:02]

That's the downside. >> [laughter] >> These domain-specific agents don't really exist. Um not in a big public way. Like I said, here at Standard Agents, we have them. We are working with them on a daily basis, but they are not out there in public very much yet. [00:21:00 → 00:21:22]
這就是缺點。 >> [笑聲] >> 這些特定領域代理其實還不存在。至少在廣泛公開的層面上還沒有。就像我說的，在 Standard Agents，我們有。我們每天都在使用它們工作，但它們還沒有真正走入大眾視野。[00:21:00 → 00:21:22]

However, that's changing. That is going to change very quickly. We're about halfway through 2026, and and I'm here to make a public prediction that I think as we roll on from from this point to the end of 2026, we are going to see a dramatic uptick in people talking about building domain-specific agents, frameworks around them. All kinds of things are coming down the pipe. And it's not going to be a small trickle. [00:21:19 → 00:21:50]
然而，情況正在改變。而且改變的速度會非常快。現在是 2026 年的年中左右，我要在這裡大膽預言：從現在到 2026 年底，我們將會看到越來越多人熱烈討論如何打造特定領域代理，以及圍繞它們建立的框架。各種相關的東西即將湧現。而且這絕不會只是涓涓細流。[00:21:19 → 00:21:50]

It's it's going to accelerate rapidly, and this will become a one of the main players in the agentic ecosystem. And 2027, I would say, is basically the year of multi-agent orchestration. That's another word you'll start to hear a lot, I think. So, that's my big bold public prediction. I was really excited just a few days ago when Vercel released Eve. [00:21:50 → 00:22:17]
它會迅速加速發展，並成為代理生態系統中的關鍵角色。而我認為，2027 年基本上就會是「多代理協作」（multi-agent orchestration）爆發的一年。我想這會是另一個大家會開始常聽到的詞。這就是我大膽的公開預測。幾天前當 Vercel 發布 Eve 時，我真的非常興奮。[00:21:50 → 00:22:17]

This is the first time I actually saw the term that I had been blasting out into the void come back and hit me in my own face. The framework for building agents build a company brain, personal assistant, or domain-specific agent. So, there we go. About halfway through the year, we're going to start picking up steam. That's my prediction. [00:22:14 → 00:22:39]
這是我第一次看到我一直對著虛空吶喊的詞彙，終於得到了真實世界的回響，狠狠地撞擊了我。「這個打造代理的框架，可以建立公司的大腦、個人助理，或是特定領域代理。」看吧，就是這樣。大約在今年年中左右，這股浪潮就會開始蓄積動能。這就是我的預測。[00:22:14 → 00:22:39]

And there's a number of reasons. One of them is something that most people believe right now is that the cost of intelligence is going down. That trend reversed in 2026, actually. We track this on on a website. Tokens are not getting cheaper anymore. [00:22:37 → 00:22:57]
而這背後有幾個原因。其中一個是，現在大多數人都相信「智慧的成本正在下降」。事實上，這個趨勢在 2026 年逆轉了。我們在一個網站上追蹤了這個數據。Token 已經不再變便宜了。[00:22:37 → 00:22:57]

They are actually going up even when adjusted for IQ. They're up 29% when you adjust for IQ just this year, halfway through the year, we're already up 30% and that can be caused by lots of different things. Of course, um we've got this memory crunch and and you know, probably the long-term trend over a 10-year cycle or something is that intelligence will go down, but that does not mean that we need to be paying 137 times the cost for something that can be done just as effectively. The problem is it's harder to break those things apart. Now, if you don't account for IQ, tokens are up 76% this year, almost 100% increase in tokens just this year. [00:22:54 → 00:23:43]
即使在考量了智商（IQ）的調整後，它們實際上還是上漲了。光是今年，經 IQ 調整後的價格就上漲了 29%。才過了半年的時間，我們就已經看到大約 30% 的漲幅。這背後可能有很多原因。當然，我們面臨著記憶體短缺的問題。你懂的，或許拉長到 10 年的週期來看，長期的趨勢仍是智慧成本會下降。但這並不代表我們就必須為了一件可以用同等效能完成的事情，去支付高達 137 倍的成本。問題在於，要把這些任務拆解開來變得更困難了。而且，如果你不把 IQ 因素算進去，今年 Token 的價格甚至飆升了 76%，光是今年幾乎就翻倍成長了。[00:22:54 → 00:23:43]

Um and we're we're not even halfway through it. So, we are really trending upwards on on token costs. So, anything we can do, especially with large businesses, to bring that down is going to be really important. Um the other the other use case to really consider is putting AI in front of customers. You can't put Fable in front of a customer, um unless that customer has a massive lifetime value. [00:23:41 → 00:24:06]
而今年甚至還沒過一半。所以，在 Token 成本上，我們真的處於一個上升的趨勢。因此，任何能幫忙降低成本的方法，尤其是對大企業來說，都會變得至關重要。另一個真正需要考慮的應用場景是，將 AI 直接推向客戶端。你不可能把 Fable 放到客戶面前，除非那個客戶能帶來極其龐大的終身價值（lifetime value）。[00:23:41 → 00:24:06]

It's just too expensive. So, you need to find a way to create great efficacy while being efficient. And domain-specific agents are going to be the way to do that. So, I'm going to leave you here in momentarily, um but before I do, let's just dream a little bit. Let me dig in a little bit deeper to how an agent could be orchestrated and what an ideal agent would actually look like. [00:24:06 → 00:24:32]
那實在太貴了。所以，你必須找到一個方法，在保持高效能的同時兼顧成本效益。而特定領域代理，將會是實現這個目標的關鍵。好，我等一下就講完了。但在結束之前，讓我們先來做個夢。讓我再稍微深入探討一下，一個代理可以如何被協調，以及一個理想的代理究竟會長什麼樣子。[00:24:06 → 00:24:32]

And then, I promise to leave you alone. Here we go. So, remember we got that model and we got the system prompt. And then, at the tool layer, let's break that apart a little bit. On one hand, we have these like functions. [00:24:32 → 00:24:45]
然後我就保證不煩大家了。開始吧。還記得嗎？我們有模型，還有系統提示詞。接著，在「工具層」，讓我們把它稍微拆解一下。一方面，我們有像是「函式」（functions）這樣的東西。[00:24:32 → 00:24:45]

This would be like an actual function that can get executed, like write a file to the file system. Then, we have prompts. Prompts are a lot like the system prompt, but they are smaller individual prompts that can get injected and and sub prompts that can you know, you can run a function that actually calls an LLM. So, let's say I have a main agent running, but I want to use Nano Banana just to generate an image when I'm using GLM you know, 5. 2 as my primary. [00:24:45 → 00:25:18]
這就像是可以實際執行的函式，比如說將檔案寫入檔案系統。然後，我們有「提示詞」（prompts）。這些提示詞很像系統提示詞，但它們是較小的、獨立的提示詞，可以被注入；還有一些子提示詞，你懂的，你可以執行一個實際呼叫 LLM 的函式。假設我有一個主代理正在運行中，但我目前主要使用的是 GLM 5.2，而我只希望用 Nano Banana 來生成一張圖片。[00:24:45 → 00:25:18]

Well, you can just have a tool that's a prompt. That would be really cool if you could do that. And then another type of tool could be another full-blown agent, like a complete other domain specific agent could just be one of the tools. So, that's the tool layer. And then you have hooks. [00:25:18 → 00:25:40]
那麼，你就可以有一個單純作為提示詞的工具。如果能做到這樣，那就太酷了。然後，另一種工具可能會是另一個完全獨立的代理。也就是說，一個完整的其他領域特定代理，可以只是其中的一個工具。這就是工具層。接著，我們還有「掛鉤」（hooks，**指在程式執行過程中攔截或修改其行為的機制**）。[00:25:18 → 00:25:40]

Uh what are hooks? Well, in this ideal world, a hook might be something that can kind of harness or change or mutate or perform side effects. So, let me give you an example. LLMs have no idea what time it is at any given point in time. Turns out a really great way to tell them what time it is is you inject an artificial message or an artificial tool call in the message history. [00:25:37 → 00:26:06]
什麼是掛鉤？嗯，在這個理想的世界裡，掛鉤可能是一種可以用來控制、改變、變異，或產生副作用的東西。讓我舉個例子。LLM 根本不知道現在是幾點。事實證明，要告訴它們現在時間的一個好方法，就是在訊息歷史紀錄中，注入一個人工的訊息或工具呼叫。[00:25:37 → 00:26:06]

So, [snorts] it looks like somebody just said, "Hey, what time it is? " and the other person replied, "Oh, it's 6:45 p. m. Pacific time. " Pretty simple. [00:26:06 → 00:26:17]
所以，[清了清嗓子] 這看起來就像是有人問：「嘿，現在幾點了？」然後另一個人回答：「喔，現在是太平洋時間下午 6 點 45 分。」就這麼簡單。[00:26:06 → 00:26:17]
