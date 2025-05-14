# Spickzettel für Lehrende

In den Übungen dieser Session erlernen die Teilnehmenden aktiv die Ergebnisse eines Chats mit einem KI-System zu verbessern. Dabei spielen eine Reihe von [Prompt-Techniken](https://de.wikipedia.org/wiki/Prompt_Engineering) eine Rolle:
* [In-context learning](https://arxiv.org/abs/2301.00234)
* [Wissensdestillation](https://de.wikipedia.org/wiki/Wissensdestillation)
* Role-Prompting

## Generelle Vorgehensweise

Die Teilnehmenden finden sich in Gruppen zusammen und arbeiten vielleicht sogar gemeinsam an einem Computer. Generell wird empfohlen, an geteilten Dokumenten, bspw. in der [Speicherwolke](https://www.urz.uni-leipzig.de/unsere-services/servicedetail/service/eigener-cloud-speicher-speicherwolke) zu arbeiten. Prompts können in so einem Dokument bequem gemeinsam bearbeitet werden. Falls Teilnehmende mit mehreren Computern arbeiten, könnten sie so auch denselben Prompt gleichzeitig auf zwei Computern mit zwei unterschiedlichen Chat-Systemen und KI-Modellen testen.

Die angegebenen Zeiten sind nur als Richtschnur gedacht. Es gibt in der Regel Teilnehmende, die selbst ein gutes Timing haben. Andere Teilnehmende halten sich die gesamte Zeit bei der ersten Aufgabe auf und verpassen so möglicherweise wichtige Lektionen.

## Text-Generierung (10 Minuten)

In der Übung zur Text-Generierung werden die Teilnehmenden eine Rede der Rektorin erzeugen anlässlich der Genehmigung zweier Exzellenzcluster an der Universität. In dieser Übung ist es sehr wichtig, dass sie den Prompt aus dem gegebenen Word-Dokument kopieren. Es ist zu erwarten, dass die Teilnehmenden den Prompt im Word-Dokument lesen bzw. überfliegen werden, bevor sie ihn kopieren. Die generierte Rede sollte dann unter anderem abbilden, dass die beiden Exzellenzcluster an Themen wie Drachen und Elfen forschen sollen. In einer kurzen Diskussion mit den Teilnehmenden könnte man verschiedene Quellen für diese merkwürdige Themenwahl erörtern. Die Ursache ist tatsächlich eine [Prompt-Injektion](https://en.wikipedia.org/wiki/Prompt_injection), eine einfache Form eines Cyberangriffs. Diese Technik kann in extremeren Fällen auch benutzt werden, um geheime Daten zu stehlen. Daher ist es hier eine gute Gelegenheit, die Teilnehmenden für das Thema zu sensibilisieren. Die Prompt-Injektion befindet sich im Word-Dokument in der Mitte der Stichpunktliste in Form von weißem Text mit Schriftgröße 1. Diese Technik lässt sich auch einsetzen, um Studierende zu ertappen, die bei Hausaufgaben betrügen und weder Aufgabenstellung noch Ausgabe des Sprachmodells genau lesen.

## Wissensdestillation (20 Minuten)

Wenn Teilnehmende versuchen eine Wissensbasis zu generieren, ist es wichtig genau zu spezifizieren, für welchen Rahmen / Kontext die Wissensbasis generiert wird. Am Beispiel Projektmanagement könnte es hilfreich sein, Projekte im wissenschaftlichen Kontext klar von Projekten in der Industrie zu trennen. 

Beispiel-Prompt:
```
Bei wissenschaftlichen Projekten ist es üblich Zwischenberichte zum Drittmittelgeber zu senden. Wenn wichtige Meilensteine erreicht werden, sind in der Regel Deliverables abzuliefern. Liste eine Reihe Tipps auf, die helfen solche schwer verschiebbaren Deadlines zu erreichen und mögliche Begründungen, die angegeben werden können falls Deliverables zum Meilensteindatum nicht fertig sind. 
```

## Chat-Bot (30 Minuten)

Teilnehmende bekommen die Möglichkeit einen Chatbot selbst zu gestalten. Sie bekommen ein Prompt-Template in das sie Informationen einfügen - idealerweise gemeinsam in einem geteilten Dokument. Der komplette Prompt wird dann in die ChatApp kopiert. 
Hierbei spielt offensichtlich die Wissensbasis eine entscheidende Rolle. Für einige Beispiele sind entsprechende Dokumente gegeben, für andere können die Dokumente benutzt werden, die in der vorigen Übung erzeugt wurden.

Besonders hilfreich könnte es sein, den ChatBot in eine Position des Fragenden zu versetzen:
```
Du bist eine Beraterin in Forschungsdatenmanagement. Unser Job ist es einen Datenmanagementplan zu schreiben. Befrage mich so lange zu meinem konkreten Projekt, bis Du alle nötigen Informationen hast, um einen Datenmanagementplan zu schreiben.
```

## Bildgenerierung (Optional, 10 Minuten)

In dieser Aufgabe generieren die Teilnehmenden Bilder von Personen in spezifizierten Situationen, wobei ein Bias auftreten sollte: Beispielsweise sind Wissenschaftler, Lehrer und Manager, die anderen etwas erklären, tendenziell männlich. Eine Reinigungskraft ist tendenziell weiblich. Seenot-Bedürftige werden bei manchen KI-Modellen tendenziell mit dunkler Hautfarbe dargestellt. Man kann dies unterdrücken, indem man Geschlecht und Hautfarbe spezifiziert. 

Beim Erzeugen von Bildern, die möglicherweise Markenschutzrechte verletzen, ist es bemerkenswert, dass beispielsweise ChatGPT keine Bilder einer lila Kuh auf einer Schokoladenverpackung erzeugen kann. Es scheint dies zu unterdrücken. Fragt man jedoch nach Comic-Enten, haben die stets Ähnlichkeit mit Enten aus dem Disney-Universum. Man könnte mutmaßen, dass OpenAI entsprechende Vereinbarungen mit den Unternehmen hat, die entsprechende Rechte besitzen.

## Was lernen wir in dieser Session?

Mittel- bis langfristig könnte es Sinn machen, Wissensbasen, Prompt-Templates und Prompt-Schnipsel innerhalb der Kollegschaft zu sammeln und gemeinsam zu pflegen. Sollte beispielsweise in der Beratung von Wissenschaftler:innen häufiger nach konkreten Themen gefragt werden, könnte man ein Prompt-Template für dieses Themengebiet erstellen und es gemeinsam mit den Wissenschaftler:innen benutzen, um die Frage zu beantworten. So könnte man gleichzeitig Beratungssuchende bei konkreten Fragen bedienen, während man ihnen auch zeigt, wie sie ggf. selbst solche Fragen mittels Sprachmodellen beantworten können. Gerade hierfür wäre es wichtig, Grenzen aufzuzeigen. Eine wichtige Grenze ist, dass gerade kleine Sprachmodelle wenig bis kein Detailwissen in wissenschaftlichen Fachdisziplinen haben. Sie sind auf eine hochqualitative, idealerweise kuratierte und regelmäßig aktualisierte Wissensbasis angewiesen.
