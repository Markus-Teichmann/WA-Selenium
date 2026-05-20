from src.menu import Menu
from src.messenger import Messenger

if __name__ == "__main__":
    messenger = Messenger()
    menu = Menu("Hauptmenü")
    menu.insert_option("CSV Datei auswählen", messenger.select_file)
    menu.insert_option("CSV Pfad anzeigen", messenger.display_csv_path)
    menu.insert_option("Kontakte auswählen", messenger.select_contacts)
    menu.insert_option("Kontakte anzeigen: ", messenger.display_contacts)
    menu.insert_option("Bild auswählen", messenger.select_image)
    menu.insert_option("Bild Pfad anzeigen", messenger.display_image_path)
    menu.insert_option("Dokument auswählen", messenger.select_document)
    menu.insert_option("Dokument Pfad anzeigen", messenger.display_document_path)
    menu.insert_option("Nachricht auswählen", messenger.select_message)
    menu.insert_option("Nachricht anzeigen", messenger.display_message)
    menu.insert_option("Nachricht abschicken", messenger.send_message)
    menu.display()