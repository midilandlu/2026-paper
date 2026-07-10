## **9 未來工作與研究方向 (Future Work and Research Directions)**

如同本文所介紹，LLM 謬誤（LLM fallacy）值得我們進行系統性的實證研究。未來的工作應聚焦於對照研究，比較在有 LLM 輔助與無輔助的情況下，人們所感受到的自身能力，從而讓我們能直接觀察到感知能力與實際能力之間的能力分歧（capability divergence）（Koriat, 1997）。此外，實驗設計可以進一步操弄系統輔助的透明度，藉此獨立分析在不同程度的透明度下，人們的歸因方式會如何轉變。

在這個框架下，提示詞（prompts）被設計成模組化、人類可讀的指令。這些指令將任務定義與評估條件具象化（**將內在思考轉化為外部明確指令**），確保在反覆的互動中能保持一致的應用標準。這呼應了當前廣泛的趨勢——將提示詞工程轉變為一種深思熟慮且以使用者為中心的實踐（Lo, 2023），並推動人類與 AI 之間走向更明確、協調的合作模式（Kraljic & Lahav, 2024）。在本研究中，運用這些特性是為了在人類與系統之間保持清晰的角色分工，而非試圖擴展或概括框架本身。

另一個核心研究方向，在於發展出能將這種分歧量化的測量框架。這包含設計一些指標，將使用者的自我能力評估與獨立的表現評估進行比較，同時建立特定任務的基準測試，將 LLM 輔助所帶來的貢獻獨立出來。透過這些方法，我們就能將 LLM 謬誤從一種推論而來的現象，轉化為可以具體測量的結構（Wilson & Dunn, 2004）。最關鍵的是，這些框架必須同時捕捉主觀的感知與客觀的表現，才能準確地呈現兩者之間的落差。

所有透過 LLM 互動產生的輸出，都必須經過系統性的人工審查、驗證以及選擇性的整合。這包含評估其概念的準確度、邏輯的一致性，以及是否與預期的理論框架契合。若輸出結果未達標準，就會在後續互動中被修改、捨棄或重新架構。這種反覆驗證的過程，反映了 AI 系統稽核與監督的既定實踐——在系統輔助的工作流程中，人為介入是確保可靠性與一致性的必要條件（Raji et al., 2020）。此過程也解決了系統生成的輸出與使用者理解程度之間潛在的落差，這與近期在人類與 LLM 互動中關於知識對齊（epistemic alignment）的討論不謀而合（Clark et al., 2025）。

縱向研究則提供了另一個探索的途徑。隨著 LLM 逐漸融入日常工作流程，我們有必要檢視這種反覆的互動，將如何隨著時間重塑使用者的自我認知。這類研究能夠評估長期使用 LLM 究竟是會放大、穩定，還是減弱歸因錯位（Dillon et al., 2025）；同時也能了解，使用者是否會對系統的貢獻建立更精確的心智模型，亦或在錯誤歸因（misattribution）中越陷越深。

這套工作流程體現了一種「人機迴圈（human-in-the-loop）」、「人類掌控（human-in-control）」以及「人類作為最終作者（human-as-final-author）」的協作模式。它不僅符合在 AI 輔助研究中對透明度的既定期待，也明確區分了輔助工具的使用與實質作者身分的差異，這與 AI 系統的報告標準是一致的（Mitchell et al., 2019）。在此背景下，結構化的提示方法便成為一種操作機制，用以強制執行限制、維持可解釋性，並維護知識的完整性（preserving epistemic...）。

我們也應該針對第 5 節提出的類型學，進行特定領域的研究。任務結構、評估標準與回饋機制的差異，都可能影響 LLM 謬誤的程度與形式。透過比較分析，我們能找出這種現象在哪裡最為明顯，並揭示特定領域的調節變數（**影響現象強弱的因素**），例如任務複雜度、回饋的取得容易度，以及中間推論過程的可見度（Gigerenzer & Gaissmaier, 2011）。

最後，未來的研究應著眼於探討如何介入以減少歸因的錯位。這可能包含：讓系統貢獻更加明確的介面設計；提升使用者對 LLM 能力與局限性認知的教育方法；以及能夠區別系統輔助表現與獨立表現的評估框架。這些介入措施將有助於將 LLM 謬誤從一個概念架構，轉變為一個具備實證基礎的研究領域（Doshi-Velez & Kim, 2017），同時也能推動人機系統的發展，使其在提升工作效能的同時，也能促進精準的自我評估。

## **10 結論 (Conclusion)**

本文介紹了「LLM 謬誤（LLM fallacy）」這個在人機互動中出現的現象：人們將 LLM 輔助的輸出結果錯誤歸因（misattribution）為自身獨立能力的證明，進而在感知能力與實際能力之間產生了系統性的分歧（Kruger & Dunning, 1999）。透過正式定義這個概念，本文為理解 LLM 介導（LLM-mediated）工作流程中歸因錯位的成因奠定了基礎，並將既有的自我評估錯誤理論，延伸至認知過程分散於人類與機器系統之間的新情境。

我們的分析找出了這個現象背後的運作機制，包括：歸因模糊性（attribution ambiguity）、受流暢度驅動的推論（fluency-driven inference）、認知外包（cognitive outsourcing），以及流程不透明性（pipeline opacity）。這些機制共同形塑出一種情境：即便使用者嚴重依賴系統生成的輸出，他們依然會高估自己的能力（Alter & Oppenheimer, 2009）。本文的類型學進一步證明，這種模式廣泛存在於運算、語言、分析、創意、知識及專業等多個領域。這顯示出 LLM 謬誤並非侷限於單一領域，而是在各種形式的認知工作中，都表現出結構上的一致性。

除了個人認知層面之外，LLM 謬誤對於那些依賴精確評估人類能力的機構系統，也帶來了深遠的影響。其效應延伸至招募、教育、技能認證以及 AI 素養框架——在這些領域中，可觀察到的輸出成果，已越來越無法真實反映出底層的實際能力（Muller, 2018）。隨著表現與能力之間的關聯性逐漸減弱，傳統那種「以輸出為基礎」的評估模式，也變得不再是衡量專業知識的可靠指標。

在生成式 AI 整合的廣闊發展軌跡中，LLM 謬誤反映出人們的關注焦點，正從「以系統為中心」轉移至「以使用者的認知動態為中心」。雖然過往的研究多半強調模型的行為、可靠性與對齊（alignment），但本文則特別凸顯了 LLM 是如何重塑人類的自我認知，以及對自身專業知識的感知能力膨脹（perceived competence inflation）（Bommasani et al., 2021）。因此，要真正理解 AI 所帶來的影響，我們不僅需要評估系統的表現，更必須深入探究人類認知在與 AI 持續互動的過程中，是如何進行調適的。

這項研究為 LLM 謬誤提供了一個概念框架，並指出了未來研究的方向。我們需要更多的實證研究來驗證這個現象、發展測量方法，並設計出能夠減輕歸因錯位的介入措施。隨著 LLM 逐漸深植於各種認知工作流程中，理解其對自我認知與能力評估的影響，將是不可或缺的課題。從更廣泛的角度來看，正視並解決 LLM 謬誤是絕對必要的——唯有如此，我們才能確保在混合認知系統中的人機協作，不僅能提升工作表現，更能促進自我評估的準確度。

## **參考文獻 (References)**

Aarts, H., Custers, R., & Wegner, D. M. (2005). On the inference of personal authorship: Enhancing experienced agency by priming effect information. _Consciousness and Cognition_ , 14(3), 439–458. 

Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F. L., ... & McGrew, B. (2023). GPT-4 technical report. _arXiv preprint arXiv:2303.08774_ . 

Alter, A. L., & Oppenheimer, D. M. (2009). Uniting the tribes of fluency to form a metacognitive nation. _Personality and Social Psychology Review_ , 13(3), 219–235. 

Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P., ... & Horvitz, E. (2019). Guidelines for human-AI interaction. In _Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems_ (pp. 1–13). 

Ananny, M., & Crawford, K. (2018). Seeing without knowing: Limitations of the transparency ideal and its application to algorithmic accountability. _New Media & Society_ , 20(3), 973–989. 

Bender, E. M., & Koller, A. (2020). Climbing towards NLU: On meaning, form, and understanding in the age of data. In _Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics_ (pp. 5185–5198). 

Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., ... & Liang, P. (2021). On the opportunities and risks of foundation models. _arXiv preprint arXiv:2108.07258_ . 

Brynjolfsson, E., Li, D., & Raymond, L. R. (2025). Generative AI at work. _The Quarterly Journal of Economics_ , 140(2), 889–942. https://doi.org/10.1093/qje/qjae044. 

Buçinca, Z., Lin, P., Gajos, K. Z., & Glassman, E. L. (2020). Proxy tasks and subjective measures can be misleading in evaluating explainable AI systems. In _Proceedings of the 25th International Conference on Intelligent User Interfaces_ (pp. 454–464). 

Burrell, J. (2016). How the machine “thinks”: Understanding opacity in machine learning algorithms. _Big Data & Society_ , 3(1), 2053951715622512. https://doi.org/10.1177/2053951715622512. 

Clark, A. (2010). _Supersizing the Mind: Embodiment, Action, and Cognitive Extension_ . Oxford University Press. 

Clark, N., Shen, H., Howe, B., & Mitra, T. (2025). Epistemic alignment: A mediating framework for user–LLM knowledge delivery. _arXiv preprint arXiv:2504.01205_ . 

Damacharla, P., Javaid, A. Y., Gallimore, J. J., & Devabhaktuni, V. K. (2018). Common metrics to benchmark human-machine teams (HMT): A review. _IEEE Access_ , 6, 38637–38655. 

Dillon, E. W., Jaffe, S., Immorlica, N., & Stanton, C. T. (2025). Shifting work patterns with generative AI (No. w33795). _National Bureau of Economic Research_ . 

Doshi-Velez, F., & Kim, B. (2017). Towards a rigorous science of interpretable machine learning. _arXiv preprint arXiv:1702.08608_ . 

Draxler, F., Werner, A., Lehmann, F., Hoppe, M., Schmidt, A., Buschek, D., & Welsch, R. (2024). The AI ghostwriter effect. _ACM Transactions on Computer-Human Interaction_ , 31(2), 1–40. 

Dunning, D. (2011). The Dunning–Kruger effect. In _Advances in Experimental Social Psychology_ (Vol. 44, pp. 247–296). 

Espeland, W. N., & Sauder, M. (2007). Rankings and reactivity: How public measures recreate social worlds. _American Journal of Sociology_ , 113(1), 1–40. https://doi.org/10.1086/517897. 

Evans, J. S. B. (2008). Dual-processing accounts of reasoning, judgment, and social cognition. _Annual Review of Psychology_ , 59, 255–278. 

Fisher, M., & Oppenheimer, D. M. (2021). Harder than you think: How outside assistance leads to overconfidence. _Psychological Science_ , 32(4), 598–610. https://doi.org/10.1177/0956797620975779. 

Gajos, K. Z., & Mamykina, L. (2022). Do people engage cognitively with AI? Impact of AI assistance on incidental learning. In _Proceedings of the 27th International Conference on Intelligent User Interfaces_ (pp. 794–806). https://doi.org/10.1145/3490099.3511138. 

Gigerenzer, G., & Gaissmaier, W. (2011). Heuristic decision making. _Annual Review of Psychology_ , 62, 451–482. 

Huang, B., Chen, C., & Shu, K. (2025). Authorship attribution in the era of LLMs. _ACM SIGKDD Explorations Newsletter_ , 26(2), 21–43. 

Hutchins, E. (1995). _Cognition in the Wild_ . MIT Press. 

Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., ... & Fung, P. (2023). Survey of hallucination in natural language generation. _ACM Computing Surveys_ , 55(12), 1–38. 

Karny, S., Mayer, L. W., Ayoub, J., Song, M., Su, H., Tian, D., ... & Steyvers, M. (2024). Learning with AI assistance. In _Proceedings of the ACM Collective Intelligence Conference_ . 

Kim, H., Yi, H., Bae, J., & Kim, Y. (2026). Natural Language Declarative Prompting (NLD-P): A Modular Governance Method for Prompt Design Under Model Drift. _arXiv preprint arXiv:2602.22790_ . https://doi.org/10.48550/arXiv.2602.22790. 

Kirsh, D. (2010). Thinking with external representations. _AI & Society_ , 25(4), 441–454. 

Kizilcec, R. F. (2016). How much information? Effects of transparency on trust in an algorithmic interface. In _Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems_ (pp. 2390–2395). https://doi.org/10.1145/2858036.2858402. 

Kocielnik, R., Amershi, S., & Bennett, P. N. (2019). Will you accept an imperfect AI? Exploring designs for adjusting end-user expectations of AI systems. In _Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems_ (pp. 1–14). https://doi.org/10.1145/3290605.3300641. 

Koriat, A. (1997). Monitoring one’s own knowledge during study: A cue-utilization approach to judgments of learning. _Journal of Experimental Psychology: General_ , 126(4), 349–370. https://doi.org/10.1037/0096-3445.126.4.349. 

Kraljic, T., & Lahav, M. (2024). From prompt engineering to collaborating. _Interactions_ , 31(3), 30–35. 

Kruger, J., & Dunning, D. (1999). Unskilled and unaware of it: How difficulties in recognizing one’s own incompetence lead to inflated selfassessments. _Journal of Personality and Social Psychology_ , 77(6), 1121–1134. https://doi.org/10.1037/0022-3514.77.6.1121. 

Lamont, M. (2012). Toward a comparative sociology of evaluation. _Annual Review of Sociology_ , 38, 201–221. 

Latour, B. (1999). _Pandora’s Hope_ . Harvard University Press. 

Lee, D., Hwang, Y., Kim, Y., Park, J., & Jung, K. (2025). Are LLM-judges robust to expressions of uncertainty? Investigating the effect of epistemic markers on LLM-based evaluation. In _Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)_ (pp. 8962–8984). https://aclanthology.org/2025.naacl-long.452/. 

Lee, J. D., & See, K. A. (2004). Trust in automation. _Human Factors_ , 46(1), 50–80. 

Liao, Q. V., Gruen, D., & Miller, S. (2020). Questioning the AI: Informing design practices for explainable AI user experiences. In _Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems_ (pp. 1–15). https://doi.org/10.1145/3313831.3376590. 

Lo, L. S. (2023). The CLEAR path. _Journal of Academic Librarianship_ , 49(4), 102720. 

Logan, G. D., & Crump, M. J. (2010). Cognitive illusions of authorship. _Science_ , 330(6004), 683–686. 

Metzger, M. J., & Flanagin, A. J. (2013). Credibility and trust of information in online environments: The use of cognitive heuristics. _Journal of Pragmatics_ , 59, 210–220. https://doi.org/10.1016/j.pragma.2013.07.012. 

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. In _Proceedings of the Conference on Fairness, Accountability, and Transparency_ (pp. 220–229). https://doi.org/10.1145/3287560.3287596. 

Muller, J. (2018). _The Tyranny of Metrics_ . Princeton University Press. 

Nam, D., Macvean, A., Hellendoorn, V. J., Vasilescu, B., & Myers, B. A. (2024). Using an LLM to help with code understanding. In _Proceedings of the IEEE/ACM 46th International Conference on Software Engineering_ (pp. 1–13). https://doi.org/10.1145/3597503.3639187. 

Newell, A., & Simon, H. A. (1976). Computer science as empirical inquiry: Symbols and search. _Communications of the ACM_ , 19(3), 113–126. https://doi.org/10.1145/360018.360022. 

Nisbett, R. E., & Wilson, T. D. (1977). Telling more than we can know: Verbal reports on mental processes. _Psychological Review_ , 84(3), 231–259. https://doi.org/10.1037/0033-295X.84.3.231. 

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., ... & Lowe, R. (2022). Training language models to follow instructions with human feedback. _Advances in Neural Information Processing Systems_ , 35, 27730–27744. https://doi.org/10.52202/068431-2011. 

Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. _Human Factors_ , 39(2), 230–253. https://doi.org/10.1518/001872097778543886. 

Porter, T. M. (1995). _Trust in Numbers: The Pursuit of Objectivity in Science and Public Life_ . Princeton University Press. 

Power, M. (1997). _The Audit Society_ . Oxford University Press. 

Raji, I. D., Smart, A., White, R. N., Mitchell, M., Gebru, T., Hutchinson, B., Smith-Loud, J., Theron, D., & Barnes, P. (2020). Closing the AI accountability gap: Defining an end-to-end framework for internal algorithmic auditing. In _Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency_ (pp. 33–44). https://doi.org/10.1145/3351095.3372873. 

Reber, R., Schwarz, N., & Winkielman, P. (2004). Processing fluency and aesthetic pleasure: Is beauty in the perceiver’s processing experience? _Personality and Social Psychology Review_ , 8(4), 364–382. https://doi.org/10.1207/s15327957pspr0804_3. 

Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. _Trends in Cognitive Sciences_ , 20(9), 676–688. 

Rosenblat, A., & Stark, L. (2016). Algorithmic labor. _International Journal of Communication_ , 10. 

Rozenblit, L., & Keil, F. (2002). The misunderstood limits of folk science: An illusion of explanatory depth. _Cognitive Science_ , 26(5), 521–562. https://doi.org/10.1207/s15516709cog2605_1. 

Sahoo, P., Singh, A. K., Saha, S., Jain, V., Mondal, S., & Chadha, A. (2024). Survey of prompt engineering. _arXiv_ . 

Shneiderman, B. (2020). Human-centered artificial intelligence: Three fresh ideas. _AIS Transactions on Human-Computer Interaction_ , 12(3), 109–124. https://doi.org/10.17705/1thci.00131. 

Sieck, W. R., & Arkes, H. R. (2005). The recalcitrance of overconfidence and its contribution to decision aid neglect. _Journal of Behavioral Decision Making_ , 18(1), 29–53. https://doi.org/10.1002/bdm.486. 

Sloman, S. A. (1996). The empirical case for two systems of reasoning. _Psychological Bulletin_ , 119(1), 3–22. https://doi.org/10.1037/0033-2909.119.1.3. 

Van Dongen, K., & Van Maanen, P. P. (2013). A framework for explaining reliance on decision aids. _International Journal of Human-Computer Studies_ , 71(4), 410–424. https://doi.org/10.1016/j.ijhcs.2012.10.018. 

Wilson, T. D., & Dunn, E. W. (2004). Selfknowledge: Its limits, value, and potential for improvement. _Annual Review of Psychology_ , 55, 493–518. https://doi.org/10.1146/annurev.psych.55.090902.141954. 

Zhang, Z., Wang, C., Wang, Y., Shi, E., Ma, Y., Zhong, W., Chen, J., Mao, M., & Zheng, Z. (2025). LLM hallucinations in practical code generation: Phenomena, mechanism, and mitigation. _Proceedings of the ACM on Software Engineering_ , 2(ISSTA), 481–503. https://doi.org/10.1145/3728894. 
