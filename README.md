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

The dataset used for this task contains 3,600 excerpts from IMPAQTS, divided in this way: 1,800 excerpts with questionable implicit contents and 1,800 without them; half of the excerpts with implicit contents (900) contain implicatures and the other 900 contain presuppositions; in turn, implicatures are subdivided into three classes: particularized conversational, generalized conversational, and conventional implicatures, each one consisting of 300 elements. 

Data are extracted from public speeches freely available on YouTube. Labels used in the tasks refer exclusively to implicit content that is not *bona-fide* true, namely, persuasive and manipulative linguistic strategies. For each excerpt, we provide the speech (as an audio file), the manually revised transcription, and the speech metadata.

## Subtask 1. Implicit content detection
The implicit content detection task consists of identifying the presence of questionable implicit content in speech excerpts. It is applied the full dataset of 3,600 excerpts split into training, development, and test sets. Predictions will be evaluated through the F1-score.

|classes  | total | train | dev | test |
|:---------|-------|-------|-----|------|
| implicit | 1800  | 1200  | 200 | 400  |
| no_implicit | 1800  | 1200  | 200 | 400  |
| **total** | **3600** | **2400** | **400** | **800** |

### Examples

Excerpt with implicit content:

> Recuperiamo, recuperiamo ciascuna componente con la sua identità, il meglio delle nostre tradizioni, di quella socialista e comunista, di quella cattolico-popolare, di quella laica e repubblicana. **I nostri partiti sono altra cosa rispetto ai loro antecedenti storici, le forze schierate da questa parte rappresentano la rottura più conseguente col vecchio sistema politico e di potere.**
> (Giorgio Napolitano, 1996)
>
> *Implica che le attuali forze di centro-sinistra siano migliori rispetto ai propri antecedenti.}\footnote{Explanations are reported in these examples for a better task understanding, but will not be provided in the challenge.*

Excerpt without implicit content:
---
Resterò vicino al cimento e agli sforzi dell’ Italia e degli italiani, con infinita gratitudine per quel che ho ricevuto in questi quasi 9 anni non soltanto di riconoscimenti legati al mio ruolo, non soltanto di straordinarie occasioni di allargamento delle mie esperienze, anche internazionali, **ma per quel che ho ricevuto soprattutto di espressioni di generosa fiducia e costante sostegno, di personale affetto, direi, da parte di tantissimi italiani che ho incontrato o comunque sentito vicini**.    
(Giorgio Napolitano, 2014)
---

## Subtask 2. Implicit classification

The implicits classification task involves a binary distinction between implicature and presupposition. These two labels can be briefly defined as follows:
- **Implicature** refers to the mechanism through which a meaning not explicitly stated or expressed is suggested. As the content is inferred by the recipients themselves, they are often less aware that it has been conveyed to them, and they are less likely to question it. As an instance of content implicitness, implicatures induce the addressee to extract further, unexpressed meanings from what is said.
- **Presupposition** refers to the mechanism by which a piece of information is presented as if the recipients were already familiar with it. Because it is framed as shared knowledge, recipients are led to take it for granted and are therefore less likely to critically evaluate it. As an instance of responsibility implicitness, presuppositions attribute responsibility for the content also to the addressee.

This subtask is applied to the subset of 1,800 excerpts containing implicit content and is split into training, development, and test sets. Predictions will be evaluated through the F1-score.

|classes | total | train | dev | test |
|:-----|-------|-------|-----|------|
| implicatures | 900   | 600   | 100 | 200  |
| presuppositions  | 900   | 600   | 100 | 200  |
| **total** | **1800** | **1200** | **200** | **400** |

## Subtask 3. Implicatures classification

The implicatures classification task is applied to a subset of 900 excerpts, which must be categorized into one of three types: particularized conversational, generalized conversational, or conventional implicatures.
- **Particularized Conversational Implicatures**: In line with Grice’s theoretical framework, conversational implicatures are defined as those arising when the speaker deliberately (or seemingly deliberately) challenges one of the four conversational maxims derived from the Cooperative Principle. More specifically, in this type of implicature, the intended inference depends on particular features of the specific context of the utterance, which occur as one-off inferences and are not generalizable across different situations. 
- **Generalized Conversational Implicatures**: Like the previous category, these generalized implicatures are conversational. For these, the hearer assumes that the speaker is obeying the maxims; they only depend on what the speaker has said and on general assumptions regarding cooperative communication. They do not require specific contextual knowledge for interpretation.
- **Conventional Implicatures**: They do not depend on the context of utterance (e.g., communicative situation, conversational goals, or adherence to the Cooperative Principle) but are rather stably associated with the conventional meaning of certain expressions. Their interpretation requires knowledge of the lexical or grammatical item from which they arise. 

Data are split into training, development, and test sets. Predictions will be evaluated through the macro F1-score.

|classes | total | train | dev | test |
|:-----|-------|-------|-----|------|
| particularized conversational impl. | 300   | 150   | 50  | 100  |
| generalized conversational impl.  | 300   | 150   | 50  | 100  |
| conventional impl. | 300   | 150   | 50  | 100  |
| **total** | **900** | **450** | **150** | **300** |
