## 1. Installation
  ### 1.1 Python
  Ein Tutorial zur installation von Python findet ihr hier: <br>
      <https://www.youtube.com/watch?v=bCY4D9n3Pew> <br>
  (Wichtig ist aber wirklich nur, dass ihr wie in Minute 2:37 gezeigt wird den Hacken entsprechend setzt.) <br>
  Ladet euch die aktuelle Version von Python runter: <br>
      <https://www.python.org> <br>
  Für Windows ist das diese hier: <br>
      <https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe> <br>
  Klick euch dann durch den Installer und setzt umbedingt das Häckchen bei "Python zum Pfad hinzufügen" <br>
  Öffnet eine CMD (z.B. WIN + r drücken und dann cmd eingeben) und führt dort: "python --version" aus. Erscheint keine Fehlermeldung, so habt ihr Python erfolgreich installiert.
  ### 1.2 Librarys
  Nachdem ihr Python installiert habt müssen wir noch einige Abhängigkeiten installieren. Öffne dazu eine CMD und gebe ein: <br>
    `pip install selenium`
  und <br>
    `pip install questionary`
  Jetzt sind alle notwendingen Bedingugen abgeschlossen um WA-Selenium zu nutzen.
  ### 1.3 WA - Selenium
  Ladet euch WA-Selenium herunter:<br>
    <https://github.com/Markus-Teichmann/WA-Selenium/archive/refs/heads/main.zip> <br>
  Entpackt die Datei irgendwo auf eurem Computer. Dann fragt ihr bei passender Stelle nach den User-Data Ordner. Sobald ihr den habt plaziert ihr ihn unter den src Ordner, sodass sich folgende Ordnerstruktur ergibt: <br>
      > WA-Selenium
      >> session-data/
      >> src/
      >> user-data/
      >> .gitignore
      >> chromedriver.exe
      >> emojis
      >> README.md
      >> Selenium.py

## 2. WA-Selenium nutzen:
   Öffnet in dem WA-Selenium Ordner eine cmd und führt den Befehl:
      python Selenium.py
   aus. Erscheint hier keine Fehlermeldung, so habt ihr die Installation erfolgreich       
   abgeschlossen.
