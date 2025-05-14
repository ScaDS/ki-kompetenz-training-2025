# Spickzettel für Lehrende: Verantwortungsvolle Nutzung von Generativer KI und Rechtlicher Rahmen

In dieser Übung diskutieren wir verschiedene rechtliche Rahmenbedingungen beim Einsatz von KI. Wir fokussieren uns insbesondere auf
* [Datenschutz](https://de.wikipedia.org/wiki/Datenschutz) ([Datenschutz-Grundverordnung](https://de.wikipedia.org/wiki/Datenschutz-Grundverordnung), [DSGVO](https://dejure.org/gesetze/DSGVO))
* [Urheberrecht](https://de.wikipedia.org/wiki/Urheberrecht) ([UrhG](https://www.gesetze-im-internet.de/urhg/))
* [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689)

Unsere ehemalige Kollegin Dr. Julia Möller-Lapperich hat das Thema KI-Kompetenzen sehr gut in [diesem Artikel zusammengefasst](https://www.nomos.de/wp-content/uploads/2025/04/Aufsatz_NJ_2025_05.pdf). 
Auch die AI-Abteilung der EU hat ein übersichtliches [FAQ-Dokument](https://digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers) veröffentlicht.

## Einordnung unserer Einrichtung

Beim Einordnen der Universität im Sinne des EU AI-Act sind wir:
* kein KI-Anbieter
* (noch kein) KI-Betreiber. Sobald das Rechenzentum ein LLM-basiertes KI-System zur internen Nutzung freigibt, sind wir es.
* Wir prozessieren Personenbezogene Daten und auch geheime Daten, insbesondere im Forschungkontext.
* Betroffene von Datenverarbeitung sind Studierdende, Mitarbeiter:innen und Wissenschaftler:innen.

Verschiedenste Anwendungen von KI im Universitätkontext sind denkbar:
* Beispiel KI mit inakzeptablen Risiko: Kameras in Seminarräumen (bspw. Online-Konferenz-Systeme) könnten benutzt werden, um Menschen zu überwachen, ihre Aufmerksamkeit zu messen und ggf. solche Informationen zu sammeln und an Lehrende oder Vorgesetzte weiterzugeben. Anwendungen dieser Art sind verboten.
* Hochrisiko-KI: KI-Systeme könnten eingesetzt werden, um Studienbewerber zu screenen und ggf. sogar Entscheidungen bzgl. Immatrikulation zu stellen. Die Anforderungen an solche Anwendungen sind sehr hoch. Die KI-Betreiber müssten das System und dessen Abläufe und Entscheidungen umfassend dokumentieren. Entscheidungen müssen von Menschen überwacht werden. Nutzende haben das Recht Einsicht in die Entscheidungsprozesse zu erhalten und ggf. KI-basierte, automatisierte Entscheidungen zu revidieren. Die Anforderungen sind so hoch, dass eine Einführung eines solchen Systems auf absehbare Zeit äußerst unwahrscheinlich ist.
* Hochrisiko-KI: Im mdeizinischen Umfeld, bspw. an Universitätskliniken, streben verschiedene KI-Systeme auf den Markt, die Abläufe optimieren. So kann man beispielse Arztbriefe automatisch generieren, wenn ein KI-Systen Zugang zu Patientendatenbanken hat. Hieraus ergeben sich zahlreiche Risiken, insbesondere im Kontext Datenschutz und hinsichtlich optimaler und ethischer Versorgung der Patienten. Die Tatsache, dass zahlreiche Firmen an Produkten für solche Anwendungen arbeiten, deutet darauf hin, dass Generative KI mittelfristig in Krankenhäusern einen Platz einnehmen wird. Auch hier ist es entscheident Abläufe zu implementieren bei der Menschen Entscheidungen selbst fällen und KI-unterstützte Prozesse transparent dokumentiert sind.
* Systematisches Risiko: Studierende und Forschende nutzen ChatGPT und andere ähnliche Anwendungen für Studium und Forschung. Die Konsequenzen sind mitunter schwer abzusehen. Offensichtlich lernen Studierende, die Zugang zu scheinbar allwissenden ChatApps haben anders, als Studierende die im Vor-Internetzeitalter in die Bibliothek gehen mussten um Antworten zu finden. Es besteht das Risiko, dass die Qualität des Wissenstransfers abnimmt, wenn beispielsweise die Lehrenden nicht im Umgang mit KI geschult werden.
* Minimales Risiko: Der Email-Spamfilter, der im Rechenzentrum dafür sorgt, dass automatisch Emails ausgefiltert oder als Spam markiert werden, birgt Risiken wie beispielsweise dass wir Email nicht bekommen. 
* Minimales Risiko: KI-Systeme sind auch in Fahrstühlen verbaut. Oft entscheidet ein [Fuzzy-Algorithmus](https://de.wikipedia.org/wiki/Fuzzylogik) ob der Fahrstuhl nach oben oder nach unten fährt, wenn gleichzeitig über und unter dem Fahrstuhl der Knopf gedrückt wird.

## Dürfen wir das?

Anhand einiger Beispiele wollen wir diskutieren, ob gegebene Beispielanwendungen und Szenarien machbar sind. Entscheidungen sind nicht Trivial und erfordern genaues abwägen.

### Review eines DFG-Proposals

Wir arbeiten als Reviewer für die DFG und würden gerne ein LLM einsetzen.

Pro:
* Schneller, effizienter Arbeiten, um bspw eine Zusammenfassung zu schreiben.
* Lokal ausgeführte KI-Systeme sorgen dafür dass der Proposal-Text mein vertrauliche IT-Umgebung nicht verläßt.

Kontra:
* DFG verbietet dies explizit in ihrer [Stellungnahme zum Einsatz generativer KI](https://www.dfg.de/resource/blob/289674/ff57cf46c5ca109cb18533b21fba49bd/230921-stellungnahme-praesidium-ki-ai-data.pdf).
* Online KI-Systeme erfüllen ggf. Datenschutzregeln nicht.
* Die Autoren haben der Nutzung ihrer Daten zu diesem Zweck nicht zugestimmt.
* Entscheidung sollte zwingend vom Menschen getroffen werden. Das ist es worum DFG Reviewer bittet.

### ChatBot für das Expert:innen Netzwerk der Uni Leipzig

Es scheint im Interesse der Universität dass potentielle Kollaborationspartner schnell die richtigen Experten finden, um beispielsweise ein neues Forschungsprojekt zu starten. Man könnte die Schwelle für eine solche Suche niedriger machen, indem man ein Forschungsinformationssystem mit einem ChatBot kombiniert.

Pro:
* Suche einfacher
* Ergebnisse potentiell besser
* Zeigt innovative Technik auf der Webseite der Uni
* Der Zweck der Verarbeitung dient einem höheren Ziel: Optimale Nutzung von Fördermitteln / öffentliche Förderung

Kontra:
* Die Datenbank enthält personenbezogene Daten
* Personen in der Datenbank haben dieser Art der Nutzung nicht zugestimmt
* Das System könnte benutzt werden, um irreführende Screenshots der Webseite der Uni zu machen

### ChatBot für Gute Wissenschaftliche Praxis beim Einsatz Generativer KI

Angenommen, wir wollen einen ChatBot implementieren, der eine Webseite der Graduiertenakademie [zur Nutzung Generativer KI](https://www.ga.uni-leipzig.de/qualitaetsentwicklung/nutzung-von-generativer-kuenstlicher-intelligenz) nutzt, um Studierende zu beraten.

Pro:
* Zeigt innovative Technik auf der Webseite der Uni, gerade in diesem Kontext
* Schult im Umgang mit generativer KI

Kontra:
* Auf der Webseite ist Copyright Uni Leipzig angegeben. Wir dürfen den Text nicht ohne Weiteres benutzen. Wir brauchen die Erlaubnis der Autorin.
* Das System, eingebettet in die Webseite, könnte benutzt werden, um irreführende Screenshots der Webseite der Uni zu machen.

## Was lernen wir in dieser Session?

Datenschutz, Risikomanagement und Urheberrecht sind wichtige Themen, die bei der Implementierung von KI-Systemen berücksichtigt werden müssen.
Die Teilnehmenden werden in die Lage versetzt bei konkreten Projekten Risiken zu beschreiben, beteiligte KI-Anbieter / Betreiber, Nutzenden und Betroffene zu identifizeren und die Risiken zu bewerten.
Eine solche Abwägung erlaubt es den Teilnehmenden Entscheidungen besser zu treffen und Risiken zu minimieren.

Ein wichtiger Anknüpfungspunkt ist der Gedanke "Wer ist verantwortlich?" bei der Nutzung von KI-Systemen. Es sind immer ausschließlich Menschen verantwortlich.
