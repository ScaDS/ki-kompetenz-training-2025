# Wissensdestillation

Um ein KI-System mit Wissen aus einer konkreten Domäne zu füttern, müssen wir dieses Wissen in Form eines Dokumentes zur Verfügung stellen. Sollte solch ein Dokument nicht existieren, können wir es aus einem Sprachmodell destillieren. 

## Aufgabe

* Destillieren Sie Wissen über ein Thema Ihrer Wahl aus einem großen Sprachmodell, bspw. [ChatGPT](https://chat.openai.com/), [Claude](https://claude.ai/) oder [Gemini](https://gemini.google.com/app).
* Kuratieren Sie die generierte Wissensbasis (Tipp: setzen Sie sich ein Zeitlimit)
* Testen Sie ein Chat-System mit und ohne die Wissensbasis mit einem kleinen Sprachmodell, beispielsweise mit zwei Chat-Fenstern nebeneinander. Nutzen Sie hierfür Angebote wie [Blablador](https://helmholtz-blablador.fz-juelich.de/) und [ChatAI](chat-ai.academiccloud.de).

Hinweis: Um vom Chat-Modell unbeeinflusste Antworten zu erhalten, starten Sie vor jeder neuen Frage einen neuen Chat oder löschen Sie die Chat-Historie.

## Beispielthemen und -prompts

Im Folgenden erhalten Sie jeweils zwei Prompts. Der erste Prompt dient dazu, eine Wissensbasis zu generieren. 
Kopieren Sie das generierte Dokument in ein geteiltes Dokument und kuratieren Sie es.
Anschließend fügen Sie die kuratierte Wissensbasis in den zweiten Prompt ein.
Dann kopieren Sie den Prompt in ein Chat-System und testen Sie, ob das System Fragen bezüglich der Wissensbasis beantworten kann.
Testen Sie auch, ob das System Fragen außerhalb des Themas beantwortet.
Eigentlich sollte es das nicht.

### Forschungsförderung

Prompt zur Wissensdistillation:
```
Du bist eine Expertin in Forschungsförderung. 
Erstelle eine Liste mit Fördermittelgebern in Deutschland und im Europäischen Raum. 
Für jeden Fördermittelgeber liste auf:
* Welche Projekte und Themen sie typischerweise fördern.
* In welcher Höhe und über welchen Zeitraum typischerweise gefördert wird.
* Typische Rahmenbedingungen
```

Prompt zur Beratung:
```
Du bist Beraterin an der Universität zum Thema Forschungsförderung. 
Eine Wissenschaftlerin kommt zu Dir mit einer Frage bzgl. Forschungsförderung. 
Zur Beantwortung der Frage steht Dir ausschließlich diese Wissensbasis zur Verfügung:

<Wissensbasis>

Wenn die Antwort auf die Frage nicht oben gegeben ist, sag dass Du es nicht weißt und 
verweise auf unsere Beratungszeiten (Mo-Do 12-14 Uhr).
```

### Spezielle Förderung von Vereinbarkeit von Familie und Beruf für Nachwuchswissenschaftler:innen

Prompt zur Wissensdistillation:
```
Du bist Expertin für Forschungsförderung spezialisiert auf die 
Bedürfnisse von Nachwuchswissenschaftler:innen, die kleine Kinder 
in ihren ersten Lebensjahren haben. Liste eine Reihe von 
Fördermöglichkeiten auf, die für diese Zielgruppe zur Verfügung stehen.
```

Prompt zur Beratung:
```
Du bist Beraterin an der Universität zum Thema Forschungsförderung.
Eine Wissenschaftlerin kommt zu Dir mit einer Frage bzgl. Forschungsförderung.
Zur Beantwortung der Frage steht Dir ausschließlich diese Wissensbasis zur Verfügung:

<Wissensbasis>

Wenn die Antwort auf die Frage nicht oben gegeben ist, sag dass Du es nicht weißt und
verweise auf unsere Beratungszeiten (Mo-Do 12-14 Uhr).
```


### Projektmanagement

Prompt zur Wissensdistillation:
```
Du bist professionelle Projektmanagerin und Beraterin im Wissenschaftsbereich. 
Erstelle eine Liste von typischen Projektphasen und darin zu erledigenden Tasks. 
Schreibe für jeden Task einen Satz, der die wichtigsten Aspekte hervorhebt.
```

Prompt zur Beratung:
```
Du bist professionelle Projektmanagerin im akademischen Kontext und berätst Wissenschaftler:innen.
Eine Wissenschaftlerin kommt zu Dir mit einer Frage bzgl. Projektmanagement.
Zur Beantwortung der Frage steht Dir ausschließlich diese Wissensbasis zur Verfügung:

<Wissensbasis>

Wenn die Antwort auf die unten gegebene Frage nicht oben gegeben ist, sag dass Du es nicht 
weißt und verweise auf unsere Projektmanagementtraining vom 28.-29. Juni 2025: 
https://fortbildung.uni-leipzig.de/fortbildung.html?id=2306
```
