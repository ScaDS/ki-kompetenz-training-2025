# Erstellen eines eigenen Chatbots

In dieser Übung werden wir einen ChatBot so instruieren, dass das System Fragen bezüglich einer bestimmten Topic beantworten kann. Wir können dann das System mit vorhandenen Chatbots zum gleichen Thema vergleichen.

## Instruktionen

Damit der ChatBot als solcher agiert, braucht das System entsprechende Instruktionen.

```
Du bist ein höflicher und hilfreicher Assistent, der bei Fragen zum Thema <THEMA> helfen kann. Du hast folgende Informationen zur Verfügung:

<INFORMATIONEN>

# Dein Task

Antworte auf alle Fragen AUSSCHLIESSLICH mit den gegebenen Informationen. Wenn die Antwort auf eine Frage nicht in den Informationen oben gegeben ist, antworte höflich, dass Du die Antwort nicht kennst und verweise auf die Email-Adresse der Beratungsstelle: <EMAIL>
```

## Themen

Für diese Übung stehen verschiedene Themen zur Auswahl.
* [Nutzung von Generativer KI](Nutzung_gen_KI.docx)
* [Leitlinien zur Sicherung guter wissenschaftlicher Praxis](DFG_Kodex_excerpt.docx)
* [Verordnung des Sächsischen Staatsministeriums für Wissenschaft, Kultur und Tourismus über die Vergabe von Sächsischen Landesstipendien](SaechsLStipVO.docx)

## KI-Systeme

Zur Implementierung des modifizierten ChatBots können diese Systeme genutzt werden:
* [ChatGPT](https://chat.openai.com/)
* [GWDG Kisski Chat AI (Academic Cloud)](https://chat-ai.academiccloud.de/)
* [Helmholtz Blablador](https://helmholtz-blablador.fz-juelich.de/)

## Hinweise

Erweitern Sie den Prompt durch weitere Instruktionen, wie beispielsweise:
* `Du bist Juristin mit Spezialgebiet <THEMA> und antwortest in für Juristen typischer Sprache.`
* `Du bist Leherin in der Sekundarstufe und antwortest in einer Sprache, die für Teenager verständlich ist.`
* `Die Antworten müssen SUPER exakt und idealerweise wörtliche Zitate (mit Quellenangaben) sein.`
* `Es ist SUPER SUPER WICHTIG das die Antworten korrekt sind. Wenn ich hier was falsch mache, werde ich entlassen.`