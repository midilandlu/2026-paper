# **SpaRE: Enhancing Spatial Reasoning in Vision-Language Models with Synthetic Data** 

**Michael Ogezi** University of Waterloo Vector Institute mogezi@uwaterloo.ca 

## **Freda Shi** 

University of Waterloo Vector Institute fhs@uwaterloo.ca 

## **Abstract** 

Vision-language models (VLMs) work well in tasks ranging from image captioning to visual question answering (VQA), yet they struggle with spatial reasoning, a key skill for understanding our physical world that humans excel at. We find that spatial relations are generally rare in widely used VL datasets, with only a few being well represented while most form a long tail of underrepresented relations. This gap leaves VLMs ill-equipped to handle diverse spatial relationships. To bridge it, we construct a synthetic VQA dataset focused on spatial reasoning generated from hyperdetailed image descriptions in Localized Narratives, DOCCI, and PixMo-Cap. Our dataset consists of 455k samples containing 3.4 million QA pairs. Trained on this dataset, our Spatial-Reasoning Enhanced (SpaRE) VLMs show strong improvements on spatial reasoning benchmarks, achieving up to a 49% performance gain on the What’s Up benchmark, while maintaining strong results on general tasks. Our work narrows the gap between human and VLM spatial reasoning and makes VLMs more capable in real-world tasks such as robotics and navigation. We look to share our code and dataset in due course. 

## **1 Introduction** 

Spatial reasoning—the ability to understand and interpret spatial relationships between objects—is a critical component of intelligent systems that interact with the physical world (Newcombe et al., 2000). Applications such as robotics, autonomous navigation, and extended reality rely heavily on precise spatial understanding to function effectively (Landsiedel et al., 2017; Balakrishnan et al., 2021). Without robust spatial reasoning, these systems risk misinterpreting their environments, leading to failures that could compromise safety and efficiency. 

Despite impressive advancements in visionlanguage models (VLMs) for tasks like image cap- 

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0001-10.png)

**----- Start of picture text -----**<br>
A front view of a small gray<br>elephant figurine on the  left ;<br>in the  middle , there is an<br>orange and black tiger; and on<br>the  right , there is a papier-<br>mâché rhino head. They are<br>all positioned  side by side ,<br>with space  between  them...<br>LLM:  Given the  description ,<br>extract spatial  QA  pairs...<br>What is to the  right  of the orange tiger? The rhino head<br>Which animal figurine is located on the<br>leftmost  side? The elephant<br>What animal is in the  middle  of the<br>The tiger<br>arrangement?<br>What is in the  background ? A floral wallpaper<br>...<br>**----- End of picture text -----**<br>

Figure 1: Our synthetic data generation pipeline: Hyperdetailed image descriptions are fed to an LLM that extracts spatial-reasoning question-answer (QA) pairs. 

tioning, visual question answering (VQA), imagetext retrieval, and zero-shot image classification, these models consistently struggle with spatial reasoning (Kamath et al., 2023; Liu et al., 2023a; Zhang et al., 2024). For instance, VLMs may correctly identify objects in an image but fail to comprehend their spatial arrangement, which is crucial for tasks like scene understanding and navigation. 

Spatial relations are rare in existing visionlanguage datasets (see Table 2). Common relations (like on, left, and under) dominate, while less frequent ones (like facing, opposite, and surrounding) are severely underrepresented. In fact, the top 17% of relations make up over 90% of all spatial relation examples (see Table 10 in the appendix). This imbalance leaves VLMs poorly equipped to handle the full range of spatial relations. 

Previous efforts to address this gap have fallen short. Synthetic datasets (Johnson et al., 2017; Agrawal et al., 2023), while providing structured and controlled environments, rely on simplistic geometric shapes and synthetically generated images, which fail to generalize to real-world data. On the other hand, human-curated datasets (Liu et al., 2023a; Kamath et al., 2023) are limited in both quantity and diversity of spatial relations, leading to continued subpar performance. 

To bridge this gap, we present a novel approach that leverages the untapped potential of hyper-detailed captions from recent long-form image-captioning datasets. Datasets such as DOCCI (Onoe et al., 2024), PixMo-Cap (Deitke et al., 2024), and Localized Narratives (Pont-Tuset et al., 2020) contain rich, detailed descriptions of images, often including explicit descriptions of spatial relationships and object interactions (see Figure 5 in the appendix). 

Armed with these resources, we use Qwen2.5-3B-Instruct (Yang et al., 2024)[1] to extract synthetic question-answer (QA) pairs focused on spatial relationships. Specifically, we extract spatial information from the hyper-detailed captions and formulate diverse and complex QA pairs that probe various aspects of spatial reasoning. Figure 1 illustrates our synthetic dataset generation method. By maintaining visual realism through the use of real-world images, our approach allows models to learn spatial reasoning skills in contexts they will encounter in practical applications, effectively addressing the domain gap introduced by synthetic visuals. 

We fine-tune VLMs on our synthesized dataset to produce **Spa** tial- **R** easoning **E** nhanced ( **SpaRE** ) VLMs. SpaRE VLMs significantly improve performance on spatial reasoning benchmarks, including VSR, What’s Up, 3DSRBench, and RealWorldQA. As shown in Table 3, we achieve up to a 49% gain on the A split of What’s Up (Kamath et al., 2023), a benchmark designed to test spatial understanding. Importantly, these enhancements do not come at the expense of general VL performance. SpaRE models maintain their performance on standard benchmarks such as MMMU (Yue et al., 2024), and MMBench (Liu et al., 2024b). This demonstrates that our method enhances spatial reasoning capabilities while preserving overall model effec- 

tiveness. 

By enhancing spatial reasoning in VLMs, our work supports systems that rely on accurate spatial understanding. This includes applications such as self-driving cars handling complex roads, robots operating alongside humans, and assistive technologies aiding visually impaired individuals in navigation. 

In summary, our contributions are threefold: 

1. **Quantifying Data Scarcity** : We analyze spatial relations in current datasets and find that the top 17% account for about 90% of the samples, revealing a significant gap in representation. 

2. **Synthetic Spatial Data Generation** : We develop a method to generate synthetic spatial reasoning QA pairs from hyper-detailed captions of over one million real-world images using advanced LLMs. 

3. **Enhancing VLM Spatial Reasoning** : Our approach significantly improves VLMs’ spatial reasoning capabilities—by up to 49%—without compromising general VL task performance. 

The rest of the paper is organized as follows. In Section 2, we review related work in spatial reasoning and VLMs. Section 3 details our approach to generating synthetic QA pairs and augmenting training data. We present our experiments and results, and a discussion in Section 4. Finally, we conclude and briefly outline possible future research directions in Section 5. 

## **2 Background and Related Work** 

## **2.1 Spatial Reasoning Abilities in VLMs** 

Spatial reasoning remains a challenge for VLMs. Liu et al. (2023a) introduced VSR, a dataset consisting of image-caption pairs where the binary task is to predict whether the caption accurately describes the spatial relations observed in the image. Their findings demonstrate that models consistently underperform on these tasks. Similarly, Kamath et al. (2023) highlighted that state-of-the-art VLMs struggle with basic spatial relations, performing near random on benchmarks designed to test understanding of concepts like _left_ , _right_ , _above_ , and _below_ . Furthermore, both Gokhale et al. (2023) and Cho et al. (2022) show that text-to-image generation models also struggle with producing images that faithfully represent spatial relations between 

1https://hf.co/Qwen/Qwen2. 5-3B-Instruct 

multiple objects. While Chen et al. (2024a) advanced quantitative spatial reasoning through their data generation pipeline (i.e., predicting approximate distances between objects), qualitative spatial understanding remained unexplored. These findings indicate a significant gap in current models’ abilities to process and reason about spatial information. 

## **2.2 Datasets for Spatial Reasoning** 

**Natural Data** Popular high-quality, supervisedfine-tuning datasets which we analyze, such as TextCaps (Sidorov et al., 2020), ShareGPT4o[2] , InternVL-SA-1B-Caption[3] , NewYorkerCaptionContest[4] , MMInstruct (Liu et al., 2024a), VQAv2 (Goyal et al., 2017), GQA (Hudson and Manning, 2019), OKVQA (Marino et al., 2019), Visual7W, FSC147 (Ranjan et al., 2021), Objects365-YorN (Shao et al., 2019), and HatefulMemes (Kiela et al., 2020) lack enough samples that probe spatial knowledge. They predominantly focus on object recognition, captioning, and general-purpose VQA, without detailed spatial annotations, leading to a significant data deficiency. 

Efforts to tackle this issue include natural datasets such as VSR (Liu et al., 2023a), and What’s Up (Kamath et al., 2023) which manually curate training data specifically targeted at spatial reasoning. However, these datasets are typically small (e.g., the aforementioned ones total around 8k samples). 

**Synthetic Data** Synthetic data has been employed to augment training datasets for various language models (Gunasekar et al., 2023; Li et al., 2023; Abdin et al., 2024). The same has been the case for VLMs in tasks such as image captioning and text-to-image generation (Betker et al., 2023), as well as VQA and general visual instruction tuning (Liu et al., 2023b; Chen et al., 2025). In the specific case of spatial reasoning, datasets like CLEVR (Johnson et al., 2017) and STUPD (Agrawal et al., 2023) propose learning from images rendered from 3D synthetic environments with controlled spatial relationships. Unfortunately, these fail to capture the complexity, and nuance found in natural, real-world images. As a 

2https://sharegpt4o.github.io/ 

3https://hf.co/datasets/OpenGVLab/ InternVL-SA-1B-Caption 

4https://hf.co/datasets/jmhessel/ newyorker_caption_contest 

result, those models suffer from domain-shift issues and achieve poor generalization to practical applications (Agrawal et al., 2023). 

**Hyper-Detailed Image Descriptions** Recently, work toward curating datasets that describe images in extreme detail to address the shortcomings (Betker et al., 2023) of basic descriptions pulled from alt texts. Efforts such as DOCCI (Onoe et al., 2024), PixMo-Cap (Deitke et al., 2024), and to a lesser extent, Localized Narratives (Pont-Tuset et al., 2020) which total around 1 million imagedescription pairs, provide rich visual descriptions of natural images. In these rich descriptions, we find detailed descriptions of the spatial relationships between objects in the images. We show an example from DOCCI in Figure 5 in the appendix. We look to leverage these datasets to produce synthetic QA data in a manner similar to (Liu et al., 2023b; Chen et al., 2025). 

## **2.3 Our Contributions in Context** 

In summary, existing approaches to improving the spatial reasoning abilities of VLMs fall short in terms of diversity, performance, dataset size, and generalization. We quantify the data scarcity problem and leverage hyper-detailed captions to synthetically generate QA pairs that probe spatial reasoning in a manner that mirrors real-world complexities. 

## **3 Method** 

Our objective is to enhance the spatial reasoning capabilities of VLMs with our approach of generating synthetic QA pairs from hyper-detailed image descriptions using an LLM. In this section, we provide a comprehensive description of this approach. 

## **3.1 Data Sources and Analysis** 

## **3.1.1 Selection of Hyper-Detailed Datasets** 

To generate a substantial amount of spatial reasoning data, we selected the following three hyperdetailed image-description datasets: DOCCI (Onoe et al., 2024), Localized Narratives (Pont-Tuset et al., 2020), and PixMo-Cap (Deitke et al., 2024). We show dataset statistics in Table 1. 

**DOCCI** (Onoe et al., 2024) features long, human-annotated English descriptions originallycurated images, designed to address challenges such as spatial relations and world knowledge, with each description providing fine-grained detail for 

|**Source**|**Size**|**Filtered**|**Words**|**Gen. Pairs**|
|---|---|---|---|---|
|DOCCI|15k|10k|136|108k|
|LN|849k|232k|42|1,226k|
|Pixmo-Cap|717k|214k|196|2,038k|
|**Total**|1,581k|455k|113|3,372k|

Table 1: Details of selected image-description datasets. LN refers to Localized Narratives and Gen. Pairs refers the the number of generated QA pairs. 

improved model training. We show an example in Figure 5 in the appendix. 

**Localized Narratives** (Pont-Tuset et al., 2020) offers a unique form of multi-modal image annotation by synchronizing spoken descriptions (which are transcribed) with mouse traces across images from COCO (Lin et al., 2014), Flickr30k (Young et al., 2014), ADE20K (Zhou et al., 2019) and Open Images (Kuznetsova et al., 2020), to enhance applications such as controlled image captioning. We show an example in Figure 6 in the appendix. 

**PixMo-Cap** (Deitke et al., 2024) is a highquality pre-training dataset featuring a diverse array of images paired with detailed, dense captions created by transcribing and refining spoken descriptions from annotators across approximately 70 topics, to provide rich contextual information for model training. We show an example in Figure 7 in the appendix. 

## **3.1.2 Analysis of Spatial Relation Presence** 

To quantify spatial reasoning data in existing VLM datasets, we prompt Qwen2.5-3B-Instruct[5] (Yang et al., 2024) to identify spatial relations in given descriptions. This method performs well, and the prompt used is shown in Table 8 in the appendix. 

We applied this approach to several popular VLM datasets, as shown in Table 2, where the model predicted the presence of spatial relations in each caption. We then matched keywords in the text to compute frequencies for various spatial relations. The full statistics are provided in Table 10 in the appendix. 

||**Datasets**|**Total**|**%**|
|---|---|---|---|
||VQAv2|443.8k|1.44|
||GQA|943.0k|3.07|
||OKVQA|9.0k|0.03|
|VQA|Visual7W<br>**VSR**|327.9k<br>**7.7k**|1.07<br>**0.03**|
||FSC147|6.1k|0.02|
||Objects365-YorN|29,000.0k|94.35|
||Hateful-Memes|10.0k|0.03|
|||**30,747.5k**|**100**|

Table 2: VQA datasets in the supervised fine-tuning set used by InternVL2 (Chen et al., 2024b), a leading open-source VLM family. The spatial reasoning datasets are in **blue** . 

## **3.2 Synthetic Data Generation** 

## **3.2.1 Generation Pipeline** 

We use Qwen2.5-3B-Instruct (Yang et al., 2024)[6] to generate QA pairs focused on spatial reasoning from the image descriptions. The generation process involves the following: 

1. **Pre-Filtering** From each dataset, we filter for only descriptions containing explicit spatial information. We employ a setup similar to that described in our dataset analysis in Subsection 3.1.2 to classify viable descriptions. Filtering in this way trims our combined datasets by ~65%, as we show in Table 1. 

2. **Prompt Construction and QA Pair Generation** We construct a detailed prompt to guide the LLM in extracting relevant and diverse QA pairs, restricted to spatial reasoning. During generation, we decode with a temperature of 0, generating up to a maximum of 8 _,_ 192 new tokens. We also enforce the generation of structured output in the form of a JSON list of QA pairs for easy parsing. The generated pairs are guided to cover positions, orientations, and distances while excluding non-spatial details. The full prompt is shown in Table 9 in the appendix. 

3. **Post-Generation Quality Assurance** To ensure that we produce high-quality QA pairs that are relevant to spatial knowledge in the final dataset, we apply a set of automated verification techniques and drop pairs that fail them. We discuss these techniques in more detail in Subsection 3.3. 

6https://hf.co/Qwen/Qwen2. 

> 5-3B-Instruct 

5https://hf.co/Qwen/Qwen2. 5-3B-Instruct 

## **3.2.2 Dataset Composition** 

By applying this method across the selected datasets, we generated a substantial synthetic dataset of spatial reasoning QA pairs. Table 1 summarizes the number of QA pairs generated from each dataset. Figure 1 provides examples of generated QA pairs from a description corresponding to the show image. 

## **3.3 Quality Assurance** 

To ensure the quality and accuracy of the generated QA pairs, we implemented automated quality assurance measures. We employ the following criteria: 

requirements. We also filter out QA pairs tied to images that we were unable to download. This led us to drop around 50k samples mostly from PixMo-Cap. 

## **3.4 Human Evaluation** 

To further verify the quality of our dataset, we sample a representative subset of 400 samples from the dataset. We describe the process by which we arrive at this number in Section E.1 in the appendix. We observe an error rate of around 4% in the QA pairs, which we find reasonable for a synthetic dataset. 

## **3.5 Hallucination Mitigation** 

1. **Deduplication** We check for duplicates among the set of QA pairs generated for each sample and remove them. Specifically, we employ full-string matching on the questions. and CLIP (Radford et al., 2021) semantic similarity with a cutoff of 0 _._ 95 which we selected by manually testing a sample of QA pairs from 25 sample images. 

2. **Reference Check** We filter out samples that make references to the description instead of directly asking about the image by matching for keywords such as “mention,” and “description.” 

3. **Answer-Description Consistency Check** We check that the answers are present in the original description to maximize groundedness. Specifically, we verify that subsets of the answer, such as key phrases, are present in the description, even if the entire answer is not matched exactly. 

4. **Image-Question Consistency Check** We compare the semantic similarity between images and questions in QA pairs to gauge alignment. Specifically, we employ CLIPScore (Hessel et al., 2021) with a 0 _._ 25 cutoff which we selected by manually testing a sample of 100 QA pairs. 

5. **Spatial Relation Verification** We filter out any QA pairs that do not consist of spatial-reasoning questions similarly to the approach described in Subsection 3.1.2. The difference here is that we classify based on the QA pair instead of the description. 

QA pairs were progressively filtered based on the aforementioned automated criteria, which are listed and applied in order of increasing computational 

In our initial studies, we identified the primary cause of hallucinations to be descriptions that did not contain any actual spatial relations. This insight led us to implement an aggressive filtering strategy for such descriptions. Following this refinement, hallucinations became manageable, with relation and object hallucination rates reduced to approximately 4% and 3%, respectively. 

## **3.6 Addressing Data Scarcity** 

Our pipeline generates 455k samples with 3.4 million QA pairs, helping to address the lack of spatial reasoning data in VLM datasets. By offering diverse examples across various spatial relations and contexts, we improve VLMs’ ability to learn and generalize spatial reasoning, leading to better performance on related tasks. 

## **3.7 Training Objective** 

We train our VLMs by optimizing the cross-entropy loss between the model’s predicted and the groundtruth text token probabilities, computing no loss on visual tokens. Specifically, given an input image _I_ and its corresponding text input _X_ (i.e., a question), along with the target output sequence (i.e., an answer), _Y_ = _{y_ 1 _, y_ 2 _, . . . , yT }_ , the model aims to minimize the negative log-likelihood of the target tokens given the inputs. 

The training objective is defined as: 

![](2504.20648v1_SpaRE-images/2504.20648v1_SpaRE-_Enhancing_Spatial_Reasoning_in_Vision-Language_Models_with_Synthetic_Data.pdf-0005-20.png)

where _θ_ represents the model parameters, _pθ_ ( _yt | I, X, y<t_ ) is the probability of generating the token _yt_ at position _t_ given the image _I_ , question _X_ , and previous tokens _y<t_ . 

We outline more training details in Subsection 4.1.2. 

## **4 Experiments and Results** 

In this section, we detail the experimental setup used to evaluate our method as well as present and discuss the results. Our experiments aim to evaluate the effectiveness of our approach and compare them to relevant baselines in enhancing VLMs’ spatial understanding while maintaining general VL capabilities. 

2. **What’s Up?** (Kamath et al., 2023): Focuses on evaluating models’ understanding of basic spatial relations, such as _left_ , _right_ , _above_ , _below_ , _in-front_ , and _behind_ . 

3. **3D Spatial Reasoning Benchmark (3DSRBench)** (Ma et al., 2024): Assesses models’ capabilities in understanding 3D spatial relations in complex scenes. 

4. **RealWorldQA**[8] : A dataset consisting of realworld images and questions requiring spatial reasoning to answer accurately. 

## **4.1 Experimental Setup** 

## **4.1.1 Base VLM Selection** 

We select Qwen2-VL-2B-Instruct and Qwen2-VL-7B-Instruct as our base VLMs for fine-tuning since they are leading open-source models in their respective size classes and thus provide strong foundations. We do not experiment with larger models due to computing resource constraints. 

## **4.1.2 Training Procedure** 

To select our hyperparameters, we conducted a search. We show our search and the selected hyperparameters for our 2B and 7B variants in Tables 4 and 5 respectively in the appendix. We train with bfloat16 precision for improved efficiency and a linear learning rate warm-up over the first 1 _,_ 000 steps, followed by a cosine decay schedule. To stabilize training, we clipped gradients with a maximum norm of 1 _._ 0. We train the models with 5 random seeds and report the mean results. 

The training was performed on 4 NVIDIA A40 GPUs with 48GB RAM. For the 2B model, all weights were trained, while for the 7B model, we used LoRA (Hu et al., 2021) to save memory. 

## **4.2 Evaluation Benchmarks** 

To evaluate the effectiveness of our approach, we assessed the fine-tuned model on a range of benchmarks covering both spatial reasoning and general VL tasks. 

## **4.2.1 Spatial Reasoning Benchmarks** 

We evaluate on these spatial reasoning benchmarks: 

1. **Visual Spatial Reasoning (VSR)** (Liu et al., 2023a): Tests models’ ability to a wide swath of understand 66 spatial relations in images through binary classification tasks. 

These benchmarks provide a comprehensive evaluation of spatial reasoning abilities across different types of spatial relationships and contexts. 

## **4.2.2 General VL Benchmarks** 

To ensure spatial reasoning improvements do not sacrifice general performance, we evaluate on general VL benchmarks: MMMU (Yue et al., 2024) for domain-specific multi-modal reasoning, MMBench (Liu et al., 2024b) for fine-grained vision–language skills, HallusionBench (Guan et al., 2024) for hallucinations, TextVQA (Singh et al., 2019) for text-in-image reasoning, and MME (Yin et al., 2023) for integrated multi-modal cognition. These benchmarks assess the SpaRE models’ general applicability and robustness relative to competing VLMs after spatial reasoning fine-tuning. 

## **4.3 Evaluation Metrics** 

We use accuracy as the primary metric for all spatial reasoning benchmarks. For multiple-choice tasks like What’s Up, 3DSRBench, and RealWorldQA, we prompt the VLM to predict the correct option, and then apply string matching to compare the output with the ground truth. For binary classification tasks like VSR, we evaluate binary accuracy by predicting _True_ or _False_ . 

Evaluations were conducted using VLMEvalKit (Duan et al., 2024) and our own code for unsupported benchmarks (VSR and What’s Up). Some results are sourced from other works, as we detail in Section F in the appendix. While most benchmarks use accuracy, MME uses a different scoring system. For MME, perception is scored out of 2,000, reasoning out of 800, and code, commonsense, and numerical tasks are scored out of 200 each. 

8https://x.ai/blog/grok-1.5v 

|Model|Spatial Reasoning Benchmarks<br>VSR<br>What’s Up A<br>What’s Up B<br>3DSRBench<br>RealWorldQA<br>Average|General Benchmarks<br>MMMU<br>MMBench<br>Hallusion<br>Bench<br>TextVQA<br>MME<br>perception<br>MME<br>reasoning<br>MME<br>code<br>MME<br>commonsense<br>MME<br>numerical|
|---|---|---|
|Random<br>Human Estimate|50.0<br>25.0<br>25.0<br>20.9<br>–<br>30.2<br>95.4<br>100.0<br>100.0<br>95.7<br>–<br>99.8|–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–|
|SpaRE-2B (Ours)<br>Qwen2VL-2B<br>InternVL2-2B|**80.8**<br>**93.4**<br>**95.1**<br>**54.4**<br>**63.5**<br>**77.6**<br>70.3<br>44.6<br>79.1<br>46.5<br>58.6<br>59.8<br>68.7<br>86.8<br>84.7<br>46.7<br>57.4<br>68.9|**40.0**<br>71.6<br>58.2<br>**79.2**<br>1467.9<br>432.4<br>108.5<br>**110.1**<br>39.5<br>34.0<br>**72.0**<br>**61.2**<br>**75.0**<br>**1490.7**<br>**441.8**<br>**112.5**<br>109.3<br>42.5<br>34.0<br>71.4<br>59.3<br>73.5<br>1442.2<br>423.6<br>92.5<br>108.6<br>**45.0**|
|SpaRE-7B (Ours)<br>Qwen2VL-7B<br>InternVL2-8B<br>LLaVA-NeXT-8B<br>SpaceLLaVa7|**85.4**<br>**100.0**<br>**100.0**<br>**57.5**<br>**68.8**<br>**82.3**<br>82.3<br>99.5<br>99.3<br>49.2<br>67.7<br>79.2<br>73.1<br>79.2<br>94.4<br>53.3<br>64.4<br>72.5<br>71.9<br>93.6<br>95.6<br>51.1<br>58.2<br>74.1<br>65.9<br>75.5<br>75.6<br>47.2<br>48.4<br>62.5|**51.0**<br>78.6<br>56.3<br>80.5<br>1661.4<br>**642.3**<br>145.5<br>**156.3**<br>127.5<br>**51.0**<br>79.9<br>59.9<br>**81.7**<br>**1667.3**<br>640.0<br>**152.5**<br>155.0<br>**132.5**<br>47.4<br>**80.9**<br>**64.7**<br>77.6<br>1649.6<br>572.1<br>**152.5**<br>147.1<br>87.5<br>46.7<br>72.5<br>39.0<br>65.6<br>1540.2<br>308.6<br>52.5<br>118.6<br>47.5<br>35.3<br>66.5<br>43.9<br>32.4<br>1411.8<br>295.0<br>47.5<br>125.0<br>72.5|
|GPT-4o-mini<br>GPT-4o|74.0<br>75.0<br>90.0<br>39.1<br>56.0<br>66.4<br>**79.0**<br>**100.0**<br>**100.0**<br>**45.3**<br>**61.0**<br>**77.9**|–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–<br>–|

Table 3: The performance of original vs SpaRE VLMs, along with competitor models across a wide selection of datasets divided into spatial reasoning and general benchmarks. The **best** score is emboldened. 

## **4.4 Baselines and Compared VLMs** 

We compare our SpaRE models to multiple VLMs. For baselines, we include a random baseline for reference, which assigns answers uniformly at random, and a human estimate baseline from benchmark authors where available. We evaluate leading open-source models, including Qwen2VL (Wang et al., 2024), InternVL2 (Chen et al., 2024b), LLaVA-NeXT (Liu et al., 2023b), and SpaceLLaVa (Chen et al., 2024a), a model specifically optimized for quantitative spatial reasoning. We also compare against proprietary models: GPT-4o and GPT-4o-mini (Achiam et al., 2023). 

## **4.5 Results and Discussion** 

## **4.5.1 Spatial Reasoning Performance** 

Our fine-tuned models exhibit substantial improvements across the spatial reasoning benchmarks. Specifically, the average accuracy of the 2B and 7B variants increase by around **9%** and **3%** across these tasks. These gains demonstrate the effectiveness of our synthetic spatial reasoning data in enhancing the model’s spatial reasoning abilities. By incorporating explicit spatial relationships and diverse spatial contexts into the training data, the fine-tuned model developed a more robust understanding of spatial concepts. This suggests that the scarcity of spatial reasoning data in existing datasets was a key factor limiting the spatial capabilities of VLMs. 

## **4.5.2 General VL Performance** 

The results show that the fine-tuned model performs on par with the original models in general VL tasks, with minimal differences. This suggests that incorporating synthetic spatial reasoning data does not harm overall capabilities. During QA generation, we observe _benign_ hallucinations—QA pairs relevant to the image but unrelated to spatial reasoning. Including these in training helps prevent overfitting and preserves general performance. The ability to enhance spatial reasoning while maintaining broad VL competence highlights the effectiveness of our data augmentation approach. 

## **4.5.3 Impact of Synthetic Spatial Reasoning Data** 

The significant improvements in spatial reasoning tasks come from our effective use of synthetic data. By training on a wide range of spatial relations and situations, the model learns to understand and reason about space more accurately. We create QA pairs from detailed image captions, covering many types of spatial relationships. This variety helps the model apply spatial reasoning to new situations, even those not seen in training. However, the quality of the synthetic data is crucial for training a strong model. By carefully designing prompts and using a powerful, but fast LLM, we generate high-quality QA pairs that correctly reflect spatial relationships in images. Still, any shortcomings or biases in the LLM could affect the quality of the 

synthetic data. 

## **4.5.4 Generalization to Real-World Scenarios** 

SpaRE models improve by 4.9% and 1.1% on the original 2B and 7B models in RealWorldQA, showing that its spatial reasoning skills extend to realworld data, not just synthetic or controlled settings. The improvements on the RealWorldQA benchmark show that the model can apply spatial reasoning to real-world images and questions. RealWorldQA includes everyday scenes and tests the application of spatial reasoning to solve those tasks. This shows promise for our approach beyond academic settings. This is especially useful for applications like robotics, where models must understand complex spatial relationships in unpredictable environments. 