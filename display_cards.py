from PIL import Image
import os

def display_cards(card_paths):
    images = []
    for path in card_paths:
        images.append(Image.open(path))

    # Calcola le dimensioni totali per la griglia
    max_width = max(image.width for image in images)
    total_height = sum(image.height for image in images)

    # Crea un'immagine vuota per disegnare le carte
    result = Image.new("RGB", (max_width, total_height), color=(255, 255, 255))

    # Disegna le carte sulla nuova immagine
    y_offset = 0
    for image in images:
        result.paste(image, (0, y_offset))
        y_offset += image.height

    # Mostra l'immagine
    result.show()

if __name__ == "__main__":
    # Assicurati di avere le immagini delle carte da poker nella stessa directory del tuo script
    card_paths = [f for f in os.listdir() if f.endswith('.jpg')]  # Modifica il filtro in base al formato delle tue immagini
    display_cards(card_paths)
