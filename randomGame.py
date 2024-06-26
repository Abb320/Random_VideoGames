import tkinter as tk
import random
from PIL import Image, ImageTk
import requests
from io import BytesIO

api_key = "4f6d2816e2f1498d86f851537a1f7062"

def ranGame():
    while True:
        thing = random.randint(1, 10000)
        url = f"https://api.rawg.io/api/games/{thing}?key={api_key}"
        response = requests.get(url)
        data = response.json()
        if 'name' in data:
            name = data['name']
            release = data.get('released', 'N/A')
            metacritic = data.get('metacritic', 'N/A')
            image_data = data.get('background_image')
            if image_data:
                return name, release, metacritic, image_data
        else:
            continue

def changeGame():
    name, release, metacritic, image_data = ranGame()
    label.config(text=name)
    released.config(text=release)
    metacriticscore.config(text=metacritic)

    response = requests.get(image_data)
    image_data_bytes = response.content
    image = Image.open(BytesIO(image_data_bytes))
    image = image.resize((300, 200))
    photo = ImageTk.PhotoImage(image)

    image_label.config(image=photo)
    image_label.image = photo

root = tk.Tk()
root.minsize(300, 200)
root.title("Random Game Generator")
entry = tk.Entry(root)

# Initial image setup
url = "https://media.rawg.io/media/games/f6b/f6bed028b02369d4cab548f4f9337e81.jpg"
response = requests.get(url)
image_data = response.content
image = Image.open(BytesIO(image_data))
image = image.resize((300, 200))
photo = ImageTk.PhotoImage(image)

button = tk.Button(root, text="Generate", command=changeGame)
image_label = tk.Label(root, image=photo)
label = tk.Label(root, text="Title")
released = tk.Label(root, text="Release Date")
metacriticscore = tk.Label(root, text="Metacritic Score")

button.pack()
image_label.pack()
label.pack()
released.pack()
metacriticscore.pack()

# Run the Tkinter event loop
root.mainloop()

