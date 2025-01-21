import tkinter as tk
import requests

def get_races():
    url = "http://ergast.com/api/f1/2024.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        races = data['MRData']['RaceTable']['Races']
        results = "\n".join([f"{race['round']}: {race['raceName']} - {race['date']}" for race in races])
        return f"Estas são as corridas da F1 na temporada de 2024: \n" + results
    else:
        print(f"Erro ao ir buscar as corridas: {response.status_code}")

def get_seasons():
    url = "http://ergast.com/api/f1/seasons.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        seasons = data['MRData']['SeasonTable']['Seasons']
        results = "\n".join([f"{season['season']}" for season in seasons])
        return f"Estas são as temporadas da F1 de sempre\n" + results
    else:
        print(f"Erro ao ir buscar as temporadas: {response.status_code}")



def menu():
    print(f"1) Temporadas")
    print(f"2) Corridas")
    print(f"3) Sair")
    escolha = str(input("Seleciona uma opção: "))
    if (escolha == "1"):
        print(get_seasons())
    elif(escolha == "2"):
        print(get_races())
    elif(escolha == "3"):
        exit()
    else:
        print("Opção Inválida!")
        menu()

menu()
    

