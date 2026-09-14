import threading

from src.menu import Menu
from src.messenger import Messenger
from src.scheduler import Scheduler

if __name__ == "__main__":
    messenger = Messenger()
    scheduler = Scheduler(messenger)
    threading.Thread(target=scheduler.start, daemon=True).start()
    menu = Menu("Hauptmenü")
    menu.insert_option("CSV Datei auswählen", messenger.select_csv_file)
    menu.insert_option("CSV Pfad anzeigen", messenger.display_csv_path)
    menu.insert_option("Kontakte auswählen", messenger.select_contacts)
    menu.insert_option("Kontakte anzeigen: ", messenger.display_contacts)
    menu.insert_option("Datei auswählen", messenger.select_file)
    menu.insert_option("Datei Pfad anzeigen", messenger.display_file_path)
    menu.insert_option("Nachricht auswählen", messenger.select_message)
    menu.insert_option("Nachricht anzeigen", messenger.display_message)
    menu.insert_option("Nachricht abschicken", messenger.send_message)
    menu.display()