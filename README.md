# IMPOLS task
IMPOLS - IMplicit contents in POLitical Speech task @ EVALITA2026

## Description
The task IMPOLS focuses on the automatic recognition of implicit content in political speech. Given an utterance in a context, we ask participants to develop a system capable of detecting and classifying the implicit contents that are non-*bona fide* true: these are implicit, questionable contents that are not conveyed in good faith but are still understood as true, albeit non-explicitly, within a given context. This kind of content is widely employed in political communication as a strategic tool to convey messages implicitly, thereby enabling the transmission of potentially manipulative content without overt expression.

We propose three subtasks: 
1. a **binary detection task**, in which the systems are asked to detect the presence of questionable implicit contents in speech excerpts;
2. a **binary classification task**, in which the systems are asked to discriminate between two types of implicit contents: implicatures and presuppositions;
3. a **multiclass classification task**, in which the systems have to identify if implicatures are particularized conversational, generalized conversational, or conventional.

IMPOLS is a monolingual (Italian) multimodal task: both the speech and the manually revised transcription will be provided to the participants in the three subtasks.

## Goal
IMPOLS aims to challenge machines to deal with complex, pragmatic phenomena that are difficult to disentangle, just as they are for humans. For this reason, the task is intriguing, allowing the development of systems that could help citizens to evaluate rhetorical communication strategies in politics critically.

Despite the wide amount of research on this topic, much existing work relies on English synthetic stimuli, limiting ecological validity and language variety. This challenge addresses the gap by using Italian semi-spontaneous political discourse, which captures the interplay of rhetoric, context, and speaker intent.

