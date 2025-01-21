import tkinter as tk
import requests
import ctypes #janela desfocada

try: #janela desfocada corrigida
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def get_races():
    url = "http://ergast.com/api/f1/2024.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        races = data['MRData']['RaceTable']['Races']
        results = "\n".join([f"{race['round']}: {race['raceName']} - {race['date']}" for race in races])
        label.config(text=results)
    else:
        label.config(text=f"Erro: {response.status_code}")

def get_dados():
    url = ""
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        races = data['MRData']['RaceTable']['Races']
        results = "\n".join([f"{race['round']}: {race['raceName']} - {race['date']}" for race in races])
        label.config(text=results)
    else:
        label.config(text=f"Erro: {response.status_code}") 
    return True

largura = 1000
altura = 800
root = tk.Tk()

root.geometry(f"{largura}x{altura}")
root.title("Corridas da F1 - 2024")

button = tk.Button(root, text="Buscar Corridas", command=get_races, font=("Arial", 14))
button.pack()

label = tk.Label(root, text="", justify="left", font=("Arial", 12))
label.pack()

root.mainloop()
