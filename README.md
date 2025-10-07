

## Table of Contents
- [News](#news)
- [Task description](#task-description)
- [Goal](#goal)
- [Data](#data)
- [Subtask 1. Implicit content detection](#subtask-1-implicit-content-detection)
- [Subtask 2. Implicit classification](#subtask-1-implicit-classification)
- [Subtask 3. Implicatures classification](#subtask-3-implicatures-classification)
- [References](#references)
- [Organizers and Contacts](#organizers-and-contacts)

## News
Text data is available [here](https://github.com/liu-dilef/IMPOLS-task/tree/main/data).
Audio data can be accessed [here](https://drive.google.com/drive/folders/1FvA1Ij1wl2W5kvJ7hLAVv42zjaeKaqgX?usp=sharing).

## Task description
The task IMPOLS focuses on the automatic recognition of implicit content in political speech. Given an utterance in a context, we ask participants to develop a system capable of detecting and classifying the implicit contents that are non-*bona fide* true: these are implicit, questionable contents that are not conveyed in good faith but are still understood as true, albeit non-explicitly, within a given context. This kind of content is widely employed in political communication as a strategic tool to convey messages implicitly, thereby enabling the transmission of potentially manipulative content without overt expression.

We propose three subtasks: 
1. a **binary detection task**, in which the systems are asked to detect the presence of questionable implicit contents in speech excerpts;
2. a **binary classification task**, in which the systems are asked to discriminate between two types of implicit contents: implicatures and presuppositions;
3. a **multiclass classification task**, in which the systems have to identify if implicatures are particularized conversational, generalized conversational, or conventional.

IMPOLS is a monolingual (Italian) multimodal task: both the speech and the manually revised transcription will be provided to the participants in the three subtasks.

## Goal
IMPOLS aims to challenge machines to deal with complex, pragmatic phenomena that are difficult to disentangle, just as they are for humans. For this reason, the task is intriguing, allowing the development of systems that could help citizens to evaluate rhetorical communication strategies in politics critically.

Despite the wide amount of research on this topic, much existing work relies on English synthetic stimuli, limiting ecological validity and language variety. This challenge addresses the gap by using Italian semi-spontaneous political discourse, which captures the interplay of rhetoric, context, and speaker intent.

## Data

The dataset used for this task is derived from the [IMPAQTS corpus](https://impaqts.dilef.unifi.it), a large-scale, multimodal collection of Italian political speeches systematically annotated for pragmatic implicitness.
The IMPAQTS corpus is one of the most comprehensive resources for studying Italian political discourse to date: it includes speeches from prominent Italian political figures, spanning the entire period of the Italian Republic from 1946 to 2023. Each speech is manually annotated for various forms of non-explicit persuasion, including presuppositions, implicatures, vague expressions, and topicalizations. 
Speech transcriptions are manually revised and time-aligned to the original audio/video source, making IMPAQTS a fully multimodal resource for the analysis of political speech.

The dataset used for this task contains 2,637 excerpts from IMPAQTS, divided in this way: 1,332 excerpts with questionable implicit contents and 1,305 without them; half of the excerpts with implicit contents (666) contain implicatures and the other half contain presuppositions; in turn, implicatures are subdivided into three classes: particularized conversational, generalized conversational, and conventional implicatures, each one consisting of 222 elements. 

Data are extracted from public speeches freely available on YouTube. Labels used in the tasks refer exclusively to implicit content that is not *bona-fide* true, namely, persuasive and manipulative linguistic strategies. For each excerpt, we provide the speech (as an audio file), the manually revised transcription, and the speech metadata.

## Subtask 1. Implicit content detection
The implicit content detection task consists of identifying the presence of questionable implicit content in speech excerpts. It is applied the full dataset of 2,637 excerpts split into training and test sets. Predictions will be evaluated through the F1-score.

|classes  | total | train | test |
|:---------|-------|------|-------|
| implicit | 1332  | 912  | 420  |
| no_implicit | 1305  | 912  | 393  |
| **total** | **2637** | **1824** | **813** |

#### Examples

Example of an excerpt with implicit content:
> Recuperiamo, recuperiamo ciascuna componente con la sua identità, il meglio delle nostre tradizioni, di quella socialista e comunista, di quella cattolico-popolare, di quella laica e repubblicana. **I nostri partiti sono altra cosa rispetto ai loro antecedenti storici, le forze schierate da questa parte rappresentano la rottura più conseguente col vecchio sistema politico e di potere.**  
> (Giorgio Napolitano, 1996)
>
> *Implica che le attuali forze di centro-sinistra siano migliori rispetto ai propri antecedenti. (NOTE that explanations are reported in these examples for a better task understanding, but will not be provided in the challenge.)*

Example of an excerpt without implicit content:
> Resterò vicino al cimento e agli sforzi dell’ Italia e degli italiani, con infinita gratitudine per quel che ho ricevuto in questi quasi 9 anni non soltanto di riconoscimenti legati al mio ruolo, non soltanto di straordinarie occasioni di allargamento delle mie esperienze, anche internazionali, **ma per quel che ho ricevuto soprattutto di espressioni di generosa fiducia e costante sostegno, di personale affetto, direi, da parte di tantissimi italiani che ho incontrato o comunque sentito vicini**.  
> (Giorgio Napolitano, 2014)

## Subtask 2. Implicit classification

The implicits classification task involves a binary distinction between implicature and presupposition. These two labels can be briefly defined as follows:
- **Implicature** refers to the mechanism through which a meaning not explicitly stated or expressed is suggested. As the content is inferred by the recipients themselves, they are often less aware that it has been conveyed to them, and they are less likely to question it. As an instance of content implicitness, implicatures induce the addressee to extract further, unexpressed meanings from what is said.
- **Presupposition** refers to the mechanism by which a piece of information is presented as if the recipients were already familiar with it. Because it is framed as shared knowledge, recipients are led to take it for granted and are therefore less likely to critically evaluate it. As an instance of responsibility implicitness, presuppositions attribute responsibility for the content also to the addressee.

This subtask is applied to the subset of 1332 excerpts containing implicit content and is split into training and test sets. Predictions will be evaluated through the F1-score.

|classes | total | train | test |
|:-----|-------|-------|------|
| implicatures | 666   | 456 | 210  |
| presuppositions  | 666   | 456 | 210  |
| **total** | **1332** | **912** | **420** |

#### Examples

An example of implicature, along with its explanation:
> Questa non è una crisi qualsiasi, è la fine del grande imbroglio italiano che dura da ben 15 anni. È stato un imbroglio il golpe mediatico-giudiziario che ha portato al governo del Paese con la forza e la violenza **chi, dopo il crollo del muro di Berlino, è stato sconfitto dalla storia**.  
> (Stefania Craxi, 2007)
>
> *Implica che la sinistra sia stata sconfitta dalla storia*

An example of presupposition, along with its explanation:
> Queste sono le prime elezioni veramente libere di tutto il Dopoguerra, perché per la prima volta si vota liberi dalla paura del Comunismo che aveva condizionato tanta parte della vita politica italiana dal 45' in poi, e che aveva condizionato soprattutto le scelte del mondo cattolico.  Oggi si può votare dunque secondo coscienza, **non più turandosi il naso come tante volte aveva dovuto fare tanta parte dell' elettorato**, anche di sentimenti nazionali.  
> (Pino Rauti, 1990)
>
> *Presuppone che tanta parte dell'elettorato abbia dovuto votare turandosi il naso.*

## Subtask 3. Implicatures classification

The implicatures classification task is applied to a subset of 666 excerpts, which must be categorized into one of three types: particularized conversational, generalized conversational, or conventional implicatures.
- **Particularized Conversational Implicatures**: In line with Grice’s theoretical framework, conversational implicatures are defined as those arising when the speaker deliberately (or seemingly deliberately) challenges one of the four conversational maxims derived from the Cooperative Principle. More specifically, in this type of implicature, the intended inference depends on particular features of the specific context of the utterance, which occur as one-off inferences and are not generalizable across different situations. 
- **Generalized Conversational Implicatures**: Like the previous category, these generalized implicatures are conversational. For these, the hearer assumes that the speaker is obeying the maxims; they only depend on what the speaker has said and on general assumptions regarding cooperative communication. They do not require specific contextual knowledge for interpretation.
- **Conventional Implicatures**: They do not depend on the context of utterance (e.g., communicative situation, conversational goals, or adherence to the Cooperative Principle) but are rather stably associated with the conventional meaning of certain expressions. Their interpretation requires knowledge of the lexical or grammatical item from which they arise. 

Data are split into training and test sets. Predictions will be evaluated through the macro F1-score.

|classes | total | train | test |
|:-----|-------|-------|------|
| particularized conversational impl. | 222   | 152  | 70  |
| generalized conversational impl.  | 222   | 152  | 70  |
| conventional impl. | 222   | 152   | 70  |
| **total** | **666** | **456** | **210** |

#### Examples

An example of particularized conversational implicature, along with its explanation:
> Chi non la voleva capire non l'ha capita, eppure il significato è chiaro, non è la politica sottobanco che voglio fare, non è la politica sottobanco che appassiona le persone come voi, come noi. E nemmeno i patti dell'amministrazione con i poteri forti che innalzano quartieri in mezzo al nulla **invece di realizzare servizi e trasporti che rendono la vita più semplice ai nostri cittadini**.  
> (Ignazio Marino, 2013)
>
> *Implica che l'amministrazione Alemanno non abbia realizzato alcun servizio o trasporto che rendesse la vita più semplice ai cittadini.*

An example of generalized conversational implicature, along with its explanation:
> E allora, alla scelta di dire "no" all'eutanasia, si accompagna la scelta di dire "sì" alla medicina palliativa, "sì" ad una compagnia che aiuti ad affrontare in modo umano la morte. Ultima cosa, il paziente ha diritto alla protezione contro il dolore. **Molti credono di essere a favore dell'eutanasia** perché non sopportano l'idea di morire in mezzo a terribili sofferenze, o di veder morire tra terribili sofferenze una persona amata.  
> (Rocco Buttiglione, 2011)
>
> *Implica che molti di quelli che sostengono di essere a favore dell'eutanasia non lo siano veramente.*

An example of conventional implicature, along with its explanation:
> I partiti presentavano, con un programma, quello che volevano fare prima delle elezioni; poi, una volta al governo, facevano tutt'altro.  La Legge Fornero non era in nessun programma elettorale, nessun italiano l'ha mai votata. **Il Jobs Act non era in nessun programma, eppure l'hanno fatto**.  
> (Luigi Di Maio, 2018)
>
> *Implica che tutti i governi dovrebbero rispettare i programmi elettorali, che non dovrebbero fare niente che non sia scritto nel programma elettorale.*

## References

- Bianchi, C. (2011). *Pragmatica del linguaggio*. Bari: Gius. Laterza & Figli Spa.
- Cominetti, F., Gregori, L., Lombardi Vallauri, E., Panunzi, A., & altri. (2022). IMPAQTS: un corpus di discorsi politici italiani annotato per gli impliciti linguistici. In *Corpora e Studi linguistici. Atti del LIV Congresso della Società di Linguistica Italiana (Online, 8–10 settembre 2021), a cura di Emanuela Cresti e Massimo Moneglia*. Milano: Officinaventuno, 151–164.
- Cominetti, F., Gregori, L., Vallauri, E. L., & Panunzi, A. (2024). IMPAQTS: A multimodal corpus of parliamentary and other political speeches in Italy (1946–2023), annotated with implicit strategies. In *Proceedings of the IV Workshop on Creating, Analysing, and Increasing Accessibility of Parliamentary Corpora (ParlaCLARIN) @ LREC-COLING 2024*, 101–109.
- Garassino, D., Brocca, N., & Masia, V. (2022). Is implicit communication quantifiable? A corpus-based analysis of British and Italian political tweets. *Journal of Pragmatics, 194*, 9–22.
- Grice, H. P. (1975). *Logic and conversation*. London: University College London Press.
- Hu, J., Floyd, S., Jouravlev, O., Fedorenko, E., & Gibson, E. (2023, July). A fine-grained comparison of pragmatic language understanding in humans and language models. In A. Rogers, J. Boyd-Graber, & N. Okazaki (Eds.), *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)* (pp. 4194–4213). Toronto, Canada: Association for Computational Linguistics. https://doi.org/10.18653/v1/2023.acl-long.230
- Huguet Cabot, P.-L., Dankers, V., Abadi, D., Fischer, A., & Shutova, E. (2020, November). The pragmatics behind politics: Modelling metaphor, framing and emotion in political discourse. In T. Cohn, Y. He, & Y. Liu (Eds.), *Findings of the Association for Computational Linguistics: EMNLP 2020* (pp. 4479–4488). Online: Association for Computational Linguistics. https://doi.org/10.18653/v1/2020.findings-emnlp.402
- Jeretic, P., Warstadt, A., Bhooshan, S., & Williams, A. (2020). Are natural language inference models IMPPRESsive? Learning implicature and presupposition. *arXiv preprint arXiv:2004.03066*.
- Kim, Z. M., Taylor, D. E., & Kang, D. (2023). "Is the Pope Catholic?" Applying chain-of-thought reasoning to understanding conversational implicatures. *arXiv preprint arXiv:2305.13826*.
- Li, L., Li, J., Chen, C., Gui, F., Yang, H., Yu, C., Wang, Z., Cai, J., Zhou, J. A., Shen, B., & altri. (2024). Political-LLM: Large language models in political science. *arXiv preprint arXiv:2412.06864*.
- Lombardi Vallauri, E. (2016). The "exaptation" of linguistic implicit strategies. *SpringerPlus, 5*(1), 1106. https://doi.org/10.1186/s40064-016-2788-y
- Németh, R. (2023). A scoping review on the use of natural language processing in research on political polarization: Trends and research prospects. *Journal of Computational Social Science, 6*(1), 289–313.
- Paci, W., Panunzi, A., & Pezzelle, S. (2025, July). They want to pretend not to understand: The limits of current LLMs in interpreting implicit content of political discourse. In W. Che, J. Nabende, E. Shutova, & M. T. Pilehvar (Eds.), *Findings of the Association for Computational Linguistics: ACL 2025* (pp. 15569–15593). Vienna, Austria: Association for Computational Linguistics. https://aclanthology.org/2025.findings-acl.804/
- Sravanthi, S., Doshi, M., Tankala, P., Murthy, R., Dabre, R., & Bhattacharyya, P. (2024, August). PUB: A Pragmatics Understanding Benchmark for Assessing LLMs' Pragmatics Capabilities. In L.-W. Ku, A. Martins, & V. Srikumar (Eds.), *Findings of the Association for Computational Linguistics: ACL 2024* (pp. 12075–12097). Bangkok, Thailand: Association for Computational Linguistics. https://doi.org/10.18653/v1/2024.findings-acl.719
- Zheng, Z., Qiu, S., Fan, L., Zhu, Y., & Zhu, S.-C. (2021). Grice: A grammar-based dataset for recovering implicature and conversational reasoning. In *Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021* (pp. 2074–2085).

## Organizers and Contacts

- Lorenzo Gregori, University of Florence, lorenzo.gregori@unifi.it
- Walter Paci, University of Florence, walter.paci@unifi.it
- Valentina Saccone, University of Florence, valentina.saccone@unifi.it

