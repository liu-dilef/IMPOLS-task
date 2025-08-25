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

The dataset used for this task is derived from the {IMPAQTS corpus}[https://impaqts.dilef.unifi.it], a large-scale, multimodal collection of Italian political speeches systematically annotated for pragmatic implicitness.

The IMPAQTS corpus comprises 1,500 monological speeches delivered by approximately 150 prominent Italian political figures, spanning the entire period of the Italian Republic from 1946 to 2023. The size is approximately 2.36 million tokens, making it one of the most comprehensive resources for studying Italian political discourse to date. 
Each speech is manually annotated for various forms of non-explicit persuasion, including presuppositions, implicatures, vague expressions, and topicalizations. 
Speech transcriptions are manually revised and time-aligned to the original audio/video source, making IMPAQTS a fully multimodal resource for the analysis of political speech.

The dataset used for this task contains 3,600 excerpts from IMPAQTS, divided in this way: 1,800 excerpts with questionable implicit contents and 1,800 without them; half of the excerpts with implicit contents (900) contain implicatures and the other 900 contain presuppositions; in turn, implicatures are subdivided into three classes: particularized conversational, generalized conversational, and conventional implicatures, each one consisting of 300 elements. 

Data are extracted from public speeches freely available on YouTube.

Labels used in the tasks refer exclusively to implicit content that is not \textit{bona-fide} true, namely, persuasive and manipulative linguistic strategies.

For each excerpt, we provide the speech (as an audio file), the manually revised transcription, and the speech metadata.
