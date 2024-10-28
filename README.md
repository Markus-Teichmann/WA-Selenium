## 1. Installation
  ### 1.1 Python
  Ein Tutorial zur installation von Python findet ihr hier: * <https://www.youtube.com/watch?v=bCY4D9n3Pew>
  (Wichtig ist aber wirklich nur, dass ihr wie in Minute 2:37 gezeigt wird den Hacken entsprechend setzt.)
  Ladet euch die aktuelle Version von Python runter: * <https://www.python.org>
  Für Windows ist das diese hier: * <https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe>
  Klick euch dann durch den Installer und setzt umbedingt das Häckchen bei "Python zum Pfad hinzufügen"
  Öffnet eine CMD (z.B. WIN + r drücken und dann cmd eingeben) und führt dort: "python --version" aus. Erscheint keine Fehlermeldung, so habt ihr Python erfolgreich installiert.
  ### 1.2 Librarys
      Nachdem ihr Python installiert habt müssen wir noch einige Abhängigkeiten installieren. Öffne dazu eine CMD und gebe ein:
         pip install selenium
      und
         pip install questionary
      Jetzt sind alle notwendingen Bedingugen abgeschlossen um WA-Selenium zu nutzen.
  ### 1.3 WA - Selenium
      Ladet euch WA-Selenium herunter: <https://github.com/Markus-Teichmann/WA-Selenium/archive/refs/heads/main.zip>
      Entpackt die Datei irgendwo auf eurem Computer. Dann fragt ihr bei passender Stelle nach den User-Data Ordner. Sobald ihr den habt plaziert ihr ihn unter den src Ordner, sodass sich folgende Ordnerstruktur ergibt:
      WA-Selenium/session-data/
      WA-Selenium/src/
      WA-Selenium/user-data/
      WA-Selenium/.gitignore
      WA-Selenium/chromedriver
      WA-Selenium/emojis
      WA-Selenium/README
      WA-Selenium/Selenium

## 2. WA-Selenium nutzen:
   Öffnet in dem WA-Selenium Ordner eine cmd und führt den Befehl:
      python Selenium.py
   aus. Erscheint hier keine Fehlermeldung, so habt ihr die Installation erfolgreich       
   abgeschlossen.
