import requests

base_url = "https://pokeapi.co/api/v2"

def poke(name):
    url = f"{base_url}/pokemon/{name}"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()

        print("Name:", data["name"])
        print("Height:", data["height"])
        print("Weight:", data["weight"])
        print("Base Experience:", data["base_experience"])
    else:
        print("Pokémon not found!")

poke("pikachu")
#============================ Second Method use -->return repleace print return res.jsonaa()
# data=poke('pikachu')
# if data:
#     print(f"Name:{data['name']}")
#     print(f"Id :{data['id']}")


