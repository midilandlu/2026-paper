# The LLM Fallacy: Misattribution in AI-Assisted Cognitive Workflows 

Hyunwoo Kim Harin Yu Hanau Yi ddai Inc. hw.kim@ai-dda.com 

## **Abstract** 

The rapid integration of large language models (LLMs) into everyday workflows has transformed how individuals perform cognitive tasks such as writing, programming, analysis, and multilingual communication. While prior research has focused on model reliability, hallucination, and user trust calibration, less attention has been given to how LLM usage reshapes users’ perceptions of their own capabilities. This paper introduces the LLM fallacy, a cognitive attribution error in which individuals misinterpret LLM-assisted outputs as evidence of their own independent competence, producing a systematic divergence between perceived and actual capability. We argue that the opacity, fluency, and low-friction interaction patterns of LLMs obscure the boundary between human and machine contribution, leading users to infer competence from outputs rather than from the processes that generate them. We situate the LLM fallacy within existing literature on automation bias, cognitive offloading, and human–AI collaboration, while distinguishing it as a form of attributional distortion specific to AI-mediated workflows. We propose a conceptual framework of its underlying mechanisms and a typology of manifestations across computational, linguistic, analytical, and creative domains. Finally, we examine implications for education, hiring, and AI literacy, and outline directions for empirical validation. We also provide a transparent account of human–AI collaborative methodology. This work establishes a foundation for understanding how generative AI systems not only augment cognitive performance but also reshape self-perception and perceived expertise. 

## **1 Introduction** 

The rapid integration of large language models (LLMs) into everyday workflows has reshaped how individuals perform cognitive tasks, including writing, programming, analysis, and multilingual communication (Achiam et al., 2023). Beyond incremental productivity gains, this shift reflects a structural change in how cognitive labor is organized, with generative systems functioning as embedded components of knowledge work rather than external tools (Brynjolfsson et al., 2025). LLMs do not merely augment isolated tasks but alter the conditions under which problem solving and content generation occur. 

Existing research has primarily focused on systemlevel concerns such as model reliability, hallucination, and user trust calibration (Ji et al., 2023). Parallel work on alignment and human–AI interaction has emphasized improving system behavior through in- 

terpretability, controllability, and responsiveness to user intent (Ouyang et al., 2022). While these directions provide important insights into model performance and interaction design, they remain largely system-centered. Comparatively less attention has been given to how sustained interaction with LLMs reshapes users’ perceptions of their own capabilities, particularly in contexts where outputs are coproduced through iterative human–AI exchange. 

This paper introduces the concept of the LLM fallacy, defined as a cognitive attribution error in which individuals misinterpret LLM-assisted outputs as evidence of their own independent competence, producing a systematic divergence between perceived and actual capability. The phenomenon can be situated within a broader class of attributional distortions in which individuals misjudge the sources of their performance or knowledge (Kruger & Dunning, 1999). 

1 

However, unlike prior accounts that emphasize internal limitations in self-assessment, the LLM fallacy arises from the integration of external generative systems into cognitive workflows, creating hybrid environments in which authorship and agency are not readily separable. 

As LLMs mediate an increasing share of cognitive processes, this misattribution produces a systematic divergence between perceived and actual capability. These divergences extend beyond individual misjudgment to affect institutional systems that rely on observable outputs as proxies for competence (Espeland & Sauder, 2007). When outputs can be produced through human–AI collaboration without corresponding internal expertise, evaluation frameworks risk conflating system-assisted performance with independently grounded skill. 

We argue that this phenomenon emerges from the interaction of several properties inherent to LLM systems, including output fluency, interactional immediacy, and the opacity of underlying computational processes (Burrell, 2016). High fluency can function as a metacognitive cue, leading users to infer competence from surface-level coherence rather than from the processes that generate it (Reber et al., 2004). At the same time, the abstraction of intermediate computational steps obscures the division of labor between human and system, limiting users’ ability to accurately attribute contributions. 

Taken together, these conditions produce a form of attributional ambiguity that is not incidental but structurally embedded within the interaction. The boundary between human contribution and machine generation is progressively reconstructed through repeated use, leading users to internalize system-assisted outputs as reflections of their own ability. 

This paper makes the following contributions. First, it formally defines the LLM fallacy as a cognitive attribution error specific to AI-mediated environments. Second, it differentiates this phenomenon from adjacent constructs, including hallucination, automation bias, and cognitive offloading. Third, it proposes a mechanistic account explaining how LLM interaction produces attributional ambiguity. Fourth, it introduces a multi-domain typology of manifestations across computational, linguistic, analytical, creative, epistemic, and professional contexts. Fifth, it analyzes implications for evaluation systems, includ- 

ing hiring, education, and expertise signaling. Sixth, it provides a structured account of human–AI collaborative methodology to ensure transparency in research practice. Finally, it outlines testable hypotheses and directions for empirical validation. 

## **2 Background and Related Work** 

Research on human interaction with automated systems has long examined how reliance on machinegenerated outputs shapes human judgment and behavior (Parasuraman & Riley, 1997). A central concept in this literature is automation bias, which describes the tendency to over-rely on automated systems, often accepting outputs even when they are incorrect (Lee & See, 2004). This work shows that reliance is not purely functional but is mediated by perceived system authority and user trust, particularly under conditions of cognitive load. 

Closely related is the concept of cognitive offloading, in which individuals externalize mental processes by relying on external systems to perform tasks that would otherwise require internal effort (Risko & Gilbert, 2016). While offloading reduces cognitive burden, it also reshapes how knowledge is encoded and retained, often diminishing internalization (Hutchins, 1995). As cognitive responsibilities shift outward, the boundary between internal cognition and external support becomes increasingly fluid. 

The extended mind framework further develops this perspective by proposing that cognitive processes can be distributed across tools and environments rather than confined to the individual (Clark, 2010). Under this view, technologies do not merely assist cognition but participate in it, forming integrated systems in which reasoning and problem solving are coconstructed. This provides a theoretical basis for understanding LLMs as components within distributed cognitive architectures rather than as external aids. 

More recent work in human–AI collaboration examines how users engage with AI systems as partners in task execution (Amershi et al., 2019). These studies emphasize coordination, transparency, and the calibration of user expectations, showing that effective collaboration depends on an accurate understanding of system capabilities and limitations (Kocielnik et al., 2019). However, users often struggle to calibrate trust 

2 

appropriately, particularly when outputs are fluent or authoritative in presentation. 

Research in human-centered AI design further highlights the role of transparency and interpretability in shaping user understanding (Shneiderman, 2020). When system processes are opaque, users are more likely to form incomplete or inaccurate mental models of how outputs are generated, increasing the risk of misinterpretation. Opacity thus functions not only as a technical constraint but as a cognitive condition influencing how system contributions are perceived. 

While these frameworks provide important insights into reliance, delegation, and distributed cognition, they do not fully account for the attributional dynamics introduced by LLM-mediated workflows. Existing work focuses primarily on how users evaluate system outputs or integrate them into decisionmaking, rather than how such outputs are internalized as reflections of personal capability. The question of how externally generated content becomes incorporated into self-assessment remains underexplored. 

The LLM fallacy extends this body of work by introducing a distinct form of attributional distortion. Rather than focusing on over-reliance or trust in system correctness, it addresses how LLM-assisted outputs are misattributed as evidence of personal competence. This reframes the analytical focus from interaction and decision-making to self-perception and capability attribution, positioning the phenomenon as a complementary but distinct construct within the broader landscape of human–AI interaction. 

## **3 Conceptual Definition of the LLM Fallacy** 

The LLM fallacy is defined as a cognitive attribution error in which individuals misinterpret LLM-assisted outputs as evidence of their own independent competence. This occurs when system contributions are cognitively absorbed into the user’s self-assessment, producing a misalignment between actual and perceived capability (Kruger & Dunning, 1999). More broadly, the phenomenon can be understood as a failure of metacognitive monitoring, in which individuals are unable to accurately assess the sources and limits of their own knowledge (Wilson & Dunn, 2004). 

For the LLM fallacy to occur, several conditions 

must be met. First, the task must involve LLMmediated output generation, where the system produces content that would otherwise require domain expertise. Second, the interaction must be sufficiently seamless that the distinction between human input and system output is not salient. Third, the output must exhibit a level of fluency or coherence typically associated with skilled human performance (Alter & Oppenheimer, 2009). Under these conditions, users are more likely to rely on surface-level cues as proxies for competence rather than evaluating the underlying generative process (Reber et al., 2004). 

It is important to distinguish the LLM fallacy from related phenomena, particularly hallucination. Hallucination refers to cases in which a model produces incorrect or fabricated information, representing a failure at the level of system output (Ji et al., 2023). The LLM fallacy, by contrast, is independent of output correctness and instead concerns how outputs are cognitively interpreted. It persists regardless of whether generated content is accurate or erroneous, as it operates at the level of attribution rather than epistemic validity. 

The LLM fallacy is also distinct from automation bias and cognitive offloading. Automation bias involves over-reliance on system outputs, while cognitive offloading involves delegating mental effort to external systems (Risko & Gilbert, 2016). Both focus on task execution and decision-making processes. The LLM fallacy instead concerns how outputs are integrated into the user’s self-perception of competence, extending beyond reliance into the domain of capability attribution. 

At its core, the phenomenon reflects an attributional misalignment between human and system contributions. In LLM-mediated workflows, the boundary between user input and system-generated output becomes increasingly opaque, making their respective roles difficult to disentangle (Burrell, 2016). This opacity limits the user’s ability to construct accurate mental models of the generative process, increasing reliance on inferred rather than observed causality (Nisbett & Wilson, 1977). As a result, users may disproportionately attribute outputs to themselves, even when generation is largely system-driven. This misalignment defines the LLM fallacy and provides the foundation for the mechanisms and manifestations examined in subsequent sections. 

3 

## **4 Mechanism of Emergence** 

The LLM fallacy emerges from the interaction of multiple cognitive and system-level factors that jointly produce attributional ambiguity in LLM-mediated workflows. These factors reinforce one another, creating conditions under which users systematically misattribute system-generated outputs as reflections of their own competence (Sloman, 1996). From a dualprocess perspective, such misattributions arise when fast, intuitive judgments dominate reflective evaluation, allowing surface-level cues to guide inference. 

A primary mechanism is attribution ambiguity between human input and model output. In LLM interactions, users provide prompts that are often partial, underspecified, or iterative, while the system produces structured and coherent outputs. Because results emerge through a continuous interaction loop, the boundary between user contribution and system generation becomes difficult to delineate. This ambiguity increases the likelihood that users incorporate outputs into their sense of authorship, constructing post hoc accounts of their role despite limited introspective access to underlying processes (Nisbett & Wilson, 1977). Research on agency further shows that authorship is often inferred from outcomes rather than directly accessed, leading to systematic illusions of control and contribution (Aarts et al., 2005). In human–AI contexts, this dynamic is amplified: users may not fully experience ownership of generated content at a cognitive level yet still declare authorship at a reflective or social level, revealing a divergence between experienced and attributed authorship (Draxler et al., 2024). Similar dissociations appear in skilled action, where individuals attribute outcomes to themselves despite incomplete awareness of the processes that produced them (Logan & Crump, 2010). 

A second mechanism is the fluency illusion produced by high-quality natural language generation. LLM outputs are typically grammatically correct, contextually appropriate, and stylistically consistent, closely resembling skilled human performance. This surface-level fluency functions as a heuristic cue, leading users to infer competence from ease of processing rather than from the generative process (Reber et al., 2004). Fluency also biases judgments of credibility and expertise, increasing the likelihood that outputs are perceived as accurate and skillfully produced even 

in the absence of deeper evaluation (Metzger & Flanagin, 2013). 

Cognitive outsourcing further contributes to the phenomenon. LLMs allow users to externalize complex tasks, including reasoning, composition, and problem solving, with minimal effort. As the system assumes a greater share of cognitive workload, users engage less with the processes required to produce outputs, weakening their ability to assess their own understanding or skill (Kirsh, 2010). Repeated reliance reduces opportunities for self-generated reasoning, reinforcing the gap between perceived and actual competence. 

Another critical factor is pipeline opacity, referring to the invisibility of the processes that generate LLM outputs. Unlike traditional tools, where intermediate steps are observable or user-driven, LLMs abstract away retrieval, pattern matching, and synthesis. This opacity prevents users from tracing how outputs are produced and obscures the distinction between system-driven and user-driven contributions (Ananny & Crawford, 2018). In the absence of transparent intermediate steps, users rely on incomplete mental representations of the system, increasing the likelihood of attribution errors. 

Taken together, these mechanisms produce perceived competence inflation. Attribution ambiguity obscures authorship, fluency signals capability, cognitive outsourcing reduces reflective engagement, and pipeline opacity removes visibility into the generative process. Their interaction creates a structurally reinforced environment in which users are consistently inclined to overestimate their own independent competence, giving rise to the LLM fallacy. Formally, this relationship can be summarized as follows: capability divergence (∆ _C_ , defined as the gap between perceived and actual capability) emerges from the interaction of system-level properties, namely opacity, fluency, and immediacy, mediated by attribution ambiguity and cognitive outsourcing. 

As illustrated in Figure 1, these interacting components collectively produce capability divergence through mediated attribution processes. 

4 

**LLM Interaction Properties** Opacity (hidden generation process) Fluency (surface-level coherence) Interactional Immediacy (rapid response cycle) 

**Cognitive Mediation** Attribution Ambiguity (unclear authorship) Cognitive Outsourcing (reduced self-processing) 

## **Misattribution Capability Divergence** (Perceived vs Actual) 

Figure 1: Mechanism of the LLM fallacy. LLM interaction properties (opacity, fluency, and interactional immediacy) shape cognitive mediation processes, including attribution ambiguity and cognitive outsourcing. These processes produce systematic misattribution of system-generated outputs, resulting in divergence between perceived and actual capability. 

## **5 Typology of LLM Fallacy Manifestations** 

The LLM fallacy manifests across multiple domains in which LLMs are used to perform cognitively demanding tasks. While the underlying attributional mechanism remains consistent, its form and visibility vary by task and output type. This section outlines key domains in which the phenomenon is most salient, illustrating how perceived competence inflation emerges across contexts (Dunning, 2011). Across domains, the common structure is a dissociation between externally supported performance and internally grounded understanding. 

In the computational domain, the LLM fallacy appears in coding and systems building, where users generate functional scripts or applications with LLM 

assistance. Users may produce working outputs without understanding underlying architecture, dependencies, or optimization strategies. Execution is thus misinterpreted as evidence of technical competence (Newell & Simon, 1976), reflecting a distinction between externally scaffolded performance and internally developed understanding. 

In the linguistic domain, the phenomenon emerges in multilingual production, where users generate fluent text in languages they do not independently command. Because LLM outputs are often grammatically accurate and contextually appropriate, users may conflate fluency with internalized language ability, overestimating their capacity to comprehend or produce language without assistance (Bender & Koller, 2020). This reflects a gap between surface form and semantic competence. 

In the analytical domain, the LLM fallacy mani- 

5 

fests in reasoning and problem-solving tasks. LLMs can generate structured explanations and step-by-step analyses, which users may adopt or reproduce. Exposure to such outputs can create the impression of possessing analytical skill, even when the underlying reasoning process is externally generated (Evans, 2008). Users may internalize the structure of reasoning without engaging in the processes required to produce it independently. 

In the creative domain, the phenomenon appears in writing, ideation, and content generation. LLMs assist in producing narratives, arguments, and stylistically refined text, which users may incorporate into their work. These outputs may be misattributed as evidence of personal creativity or authorship despite substantial system contribution (Latour, 1999), reflecting a redistribution of creative agency across human and machine. 

In the epistemic domain, the LLM fallacy is observed in knowledge acquisition and understanding. LLMs can summarize complex materials and generate accessible explanations, leading users to equate access to information with conceptual mastery. This aligns with the illusion of explanatory depth, in which individuals overestimate their understanding of complex systems (Rozenblit & Keil, 2002). 

In the domain of professional signaling, the phenomenon manifests in how individuals represent their capabilities in external contexts such as resumes or interviews. Users may report skills based on their ability to produce outputs with LLM assistance rather than independently acquired expertise, resulting in inflated representations of competence that may not transfer to unaided performance (Lamont, 2012). 

Together, these domains illustrate the breadth of the LLM fallacy across forms of cognitive work. Despite variation in task type, each domain reflects the same underlying pattern: the conflation of systemassisted output with internally grounded competence. 

## **6 Empirical Observations and Illustrative Cases** 

This section provides observational grounding for the LLM fallacy by identifying recurring patterns across real-world usage contexts. Rather than presenting anecdotal accounts or controlled experimental find- 

ings, it focuses on consistent, cross-domain observations that illustrate how the phenomenon manifests in practice (Rosenblat & Stark, 2016). Such approaches are particularly appropriate for early-stage conceptual work, where stable patterns across contexts can indicate an underlying cognitive structure. These observations are intended as conceptual and cross-contextual patterns rather than as controlled empirical validation. 

One prominent pattern appears in coding and system-building workflows. Users can generate functional scripts, applications, or system components through iterative interaction with LLMs, often without understanding the underlying logic, architecture, or debugging processes. While outputs may be operationally effective, users frequently lack the ability to independently reproduce, modify, or extend them. Empirical studies show that LLMs can improve task completion and scaffold code understanding, yet users often rely on generated solutions without internalizing the reasoning behind them (Nam et al., 2024). Moreover, evaluations of code generation systems demonstrate that surface-level correctness does not reliably indicate deeper correctness, as outputs may contain latent errors undetectable without domain expertise (Zhang et al., 2025). This pattern reflects a clear divergence between execution capability and underlying competence, consistent with the definition of the LLM fallacy (Brynjolfsson et al., 2025). 

A second pattern emerges in hiring and candidate evaluation contexts. Individuals may present high-quality outputs that reflect LLM-assisted production rather than independently developed skill. When evaluated under conditions requiring unaided performance or deeper understanding, discrepancies become apparent. This divergence is reinforced by evidence that AI assistance can improve observable task performance while increasing reliance on external systems, without corresponding gains in independent capability (Karny et al., 2024). As a result, both selfperception and external evaluation may be shaped by outputs that do not accurately reflect underlying competence, leading to systematic overestimation (Espeland & Sauder, 2007). 

In educational contexts, similar dynamics arise. AI assistance can reduce the need for sustained cognitive engagement, particularly in tasks involving explanation, synthesis, or problem solving. Studies indicate that when AI systems provide solutions or inter- 

6 

mediate reasoning, users engage less deeply with the material, limiting opportunities for incidental learning and knowledge internalization (Gajos & Mamykina, 2022). Although such assistance can improve short-term performance, it weakens the relationship between task completion and conceptual understanding, complicating the interpretation of performance as evidence of learning. 

Across domains, a consistent pattern emerges: the ability to produce outputs through LLM interaction is often interpreted as evidence of internalized skill. This aligns with broader findings in cognitive psychology showing that external assistance can induce overconfidence even when underlying understanding remains limited (Fisher & Oppenheimer, 2021). Such miscalibration reflects a general tendency to infer competence from outcomes rather than from the processes that generate them, a bias that persists even when individuals recognize the role of external aids (Sieck & Arkes, 2005). In this sense, the LLM fallacy can be understood as a specific instantiation of a broader cognitive bias, amplified by the fluency and immediacy of AI-generated outputs. 

More broadly, these observations indicate a shift in how task performance is distributed between human and system. In human–machine teaming, performance emerges from interaction rather than from the isolated capabilities of either component (Damacharla et al., 2018). However, evaluation practices often fail to account for this distribution, treating outputs as attributable to the individual. This misattribution is reinforced by reliance on decision aids, where users defer to system outputs and reduce independent verification and self-assessment (Van Dongen & Van Maanen, 2013). 

Together, these cases demonstrate how the LLM fallacy operates across applied contexts, providing an observational evidence layer that complements the conceptual and mechanistic framework established earlier. Rather than relying on controlled validation, these patterns highlight consistent discrepancies between output quality and underlying competence, bridging abstract definition and real-world manifestation and motivating the need for systematic empirical investigation. 

## **7 Implications for Evaluation Systems** 

The LLM fallacy has implications that extend beyond individual cognition, affecting institutional systems that rely on accurate assessment of human capability. As LLM-assisted workflows become more prevalent, existing evaluation frameworks risk becoming misaligned with the competencies they are intended to measure, particularly when observable outputs are used as primary indicators of skill (Muller, 2018). When outputs can be generated or substantially shaped through AI mediation, the relationship between performance and underlying capability becomes increasingly difficult to interpret, weakening the reliability of outcome-based evaluation as a proxy for competence. 

In hiring and candidate assessment, this misalignment introduces a divergence between demonstrated output and independently grounded expertise. Candidates may present work products or articulate solutions that reflect LLM-assisted generation rather than internalized knowledge or skill. Evaluation systems that rely on observable outputs may therefore overestimate competence, especially in contexts where system use is not visible or accounted for (Lamont, 2012). This problem is further compounded by the instability of evaluation itself under AI mediation. Recent work shows that LLM-based evaluation systems can be sensitive to surface-level linguistic features, such as expressions of uncertainty, leading to inconsistent or biased judgments that do not reliably reflect underlying quality (Lee et al., 2025). As a result, both human and automated evaluators may be influenced by features that are orthogonal to actual competence, amplifying the risk of misinterpretation. 

In educational contexts, LLM availability alters both learning processes and assessment validity. Students may rely on LLMs to generate explanations, complete assignments, or scaffold problem-solving, reducing the need to engage directly with underlying material. While such tools can enhance access and support learning, they also complicate the interpretation of performance outcomes. Assessment results may no longer reliably reflect conceptual understanding or skill acquisition, creating tension between accessibility and the accurate evaluation of learning progression (Kizilcec, 2016). This challenge is closely related to broader findings that proxy tasks and sub- 

7 

jective evaluation measures can produce misleading signals of system effectiveness or user competence, particularly when evaluators rely on superficial indicators rather than underlying processes (Buçinca et al., 2020). In this context, educational assessment faces the risk of conflating assisted performance with genuine understanding. 

Similar challenges arise in skill certification and expertise validation systems. Credentials are designed to signal verified competence, yet LLM-assisted workflows enable individuals to meet output-based criteria without possessing corresponding internalized expertise. This weakens the reliability of credentials as indicators of ability, particularly in domains where AI assistance is readily available (Porter, 1995). More broadly, the increasing integration of AI systems into task execution calls into question whether existing evaluation models, which are typically designed for individual performance, remain appropriate for hybrid human–machine settings. Research on human– machine teaming highlights the need for evaluation frameworks that explicitly account for the distribution of contribution between human and system, rather than treating outputs as solely attributable to one or the other (Damacharla et al., 2018). 

At a broader level, these shifts reflect a transformation in how knowledge and expertise are produced, interpreted, and validated. As LLMs become embedded within cognitive workflows, the boundary between individual cognition and system-assisted output becomes increasingly diffuse, challenging conventional assumptions about authorship, understanding, and knowledge ownership. This transformation extends beyond specific tasks, affecting how institutions define and evaluate competence in environments where human and machine contributions are inherently intertwined. 

These challenges highlight the need for updated AI literacy frameworks that explicitly account for the role of LLMs in shaping cognitive processes and outputs. Such frameworks must move beyond tool usage to address metacognitive awareness, enabling users and evaluators to distinguish between systemassisted performance and independently grounded competence (Liao et al., 2020). This includes developing shared norms around appropriate use, transparency, and interpretation of AI-mediated outputs, as well as clarifying when outputs can and cannot be 

treated as indicators of skill. 

Taken together, these implications indicate that the LLM fallacy operates not only at the level of individual perception but also at the level of institutional evaluation systems. Addressing this misalignment will require rethinking how competence is defined, measured, and communicated in AI-mediated environments, shifting from output-centric models toward process-aware evaluation frameworks that more accurately capture the distribution of human and machine contributions (Power, 1997). 

## **8 Human–AI Collaborative Methodology and Disclosure** 

This study was conducted using a human–AI collaborative workflow in which large language models (LLMs) were used as assistive tools for drafting support, structural refinement, language optimization, and iterative conceptual exploration. All interactions with the LLM were conducted through structured prompts and evaluated by the human author within a controlled interaction framework. In this context, LLMs were treated as systems whose outputs are shaped through interaction design rather than autonomous execution (Bommasani et al., 2021). Outputs were considered intermediate artifacts subject to human interpretation and validation, rather than authoritative contributions. 

All conceptual framing, theoretical claims, interpretations, and final decisions were made by the human author, who functioned as the primary investigator and retained full authority over the direction, validation, and integrity of the research. The LLM did not function as an independent author or co-author, nor as a generative authority, but as an assistive system operating under explicit human guidance. This distinction preserves the boundary between language generation and epistemic responsibility, ensuring that authorship remains grounded in human accountability (Huang et al., 2025). 

LLM interaction in this study was governed through a structured prompting methodology based on the Natural Language Declarative Prompting (NLD-P) framework (Kim et al., 2026), which was applied to enforce constraints on task structure, output scope, and revision criteria. Unlike conventional prompt en- 

8 

gineering approaches that rely on ad hoc instruction crafting or loosely structured interaction patterns (Sahoo et al., 2024), this framework was used here as a control mechanism to ensure that model behavior remained bounded, interpretable, and responsive to explicitly defined requirements. This approach aligns with established principles in human–AI interaction design, where system behavior is shaped through coordinated interaction between user intent and system response (Amershi et al., 2019). 

boundaries, ensuring that LLM-assisted outputs do not obscure the distinction between generated content and human-authored knowledge. 