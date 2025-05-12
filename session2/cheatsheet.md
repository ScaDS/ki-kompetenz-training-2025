# Spickzettel für Lehrende

In dieser Session werden Teilnehmende Dokumente und Daten analysieren. 

## Analyse von Zusammenhängen zwischen Forschungsdisziplinen

Diese Übung wird in der gesamten Gruppe durchgeführt. Wir betrachten einen Plot in dem jeder Datenpunkt einem Thema einer Doktorarbeit entspricht. 
Der Übungsleiter umrandet einige Punkte die nah beieinander liegen um eine Wordcloud aus den Forschungsthemen zu generieren. Die Teilnehmenden raten um welche Fachdisziplin es sich handelt. Beispiel: Sportwissenschaften:

![](plot_example_sport.png)

Nach einigen Wiederholungen sollte sich ein Gefühl einstellen, wie die Datenpunkte mit den dahinter liegenden Daten verknüpft sind. Es vermittelt ein intuitives Verständnis der Funktionsweise von Sprachmodellen. 

Hier noch die Auflösung für die Verteilung der Fakultäten:

![](faculties.png)


## Simuliertes Forschungsinformationssystem

Die Teilnehmenden bekommen Zugriff auf drei simulierte Forschungsinformationssysteme, in denen mit LLM-Technologie gesucht werden kann. Ihre Aufgabe ist es, zu ermitteln, welches System zufällige Antworten liefert, welches ein LLM benutzt und welches mit Embeddings arbeitet. Das zufällige System lässt sich einfach ermitteln, da es bei wiederholten Anfragen stark unterschiedliche Antworten liefern wird. Die Relevanz jener Antworten sollte auch sehr klein sein. Die anderen beiden System lassen sich schwieriger unterscheiden. Theoretisch sollte das Embedding-basierte System besser funktionieren und auch schneller antworten. Das LLM-basierte System baut aus der gesamten Datenbank einen sehr langen Prompt und diesen zu verarbeiten dauert mitunter lange.

Hinweis: Das dahinter liegende Sprachmodell ist OpenAI's GPT-4o-mini. Daher sollten keine Personen-bezogenen oder geheimen Daten in das Suchfeld eingegeben werden. 

## Analyse von Fördermittelanträgen

Eine häufige Anwendung von Sprachmodellen ist eine Kombination mit indizierten Dokumenten. Die zugrundeliegende Technik ([Retrieval Augmented Generation, RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation))

