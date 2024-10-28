## 1. Installation
  ### 1.0 Git
  Den Installer zur installation Git findest du hier: <br>
    <https://git-scm.com/downloads/win>
  ### 1.1 Python
  Ein Tutorial zur installation von Python findest du hier: <br>
      <https://www.youtube.com/watch?v=bCY4D9n3Pew> <br>
  (Wichtig ist aber wirklich nur, dass ihr wie in Minute 2:37 gezeigt wird den Hacken entsprechend setzt.) <br>
  Ladet euch die aktuelle Version von Python runter: <br>
      <https://www.python.org> <br>
  Für Windows ist das diese hier: <br>
      <https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe> <br>
  Klick euch dann durch den Installer und setzt umbedingt das Häckchen bei "Python zum Pfad hinzufügen" <br>
  Öffnet eine CMD (z.B. WIN + r drücken und dann cmd eingeben) und führt dort: <br> 
      `python --version` <br>
  aus. Erscheint keine Fehlermeldung, so habt ihr Python erfolgreich installiert.
  ### 1.2 Librarys
  Nachdem ihr Python installiert habt müssen wir noch einige Abhängigkeiten installieren. Öffne dazu eine CMD und gebe ein: <br>
    `pip install selenium` <br>
  und <br>
    `pip install questionary` <br>
  Jetzt sind alle notwendingen Bedingugen abgeschlossen um WA-Selenium zu nutzen.
  ### 1.3 WA - Selenium
  Begebt euch mit dem Explorer in einen Beliebigen Ordner, öffnet dort eine CMD und führt folgenden Befehl aus: <br>
  `git clone https://github.com/Markus-Teichmann/WA-Selenium.git` <br>
  Dann fragt ihr bei euren Vorständen nach dem User-Data Ordner. Sobald ihr den habt plaziert ihr ihn in WA-Selenium Ordner, sodass sich folgende Ordnerstruktur ergibt: <br>
  > WA-Selenium
  >> session-data/ <br>
  >> src/ <br>
  >> user-data/ <br>
  >> .gitignore <br>
  >> chromedriver.exe <br>
  >> emojis <br>
  >> README.md <br>
  >> Selenium.py

## 2. WA-Selenium nutzen:
   Öffnet in dem WA-Selenium Ordner eine cmd und führt den Befehl:
      python Selenium.py
   aus. Erscheint hier keine Fehlermeldung, so habt ihr die Installation erfolgreich abgeschlossen.
