import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '05699f107121e87c248a78023f472831'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "MAIL",
    "password": "PASSWORD"
}

response = requests.post(url=f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)

create_pokemons = {
    
    "name": "Бульбазавр",
    "photo_id": 1

}

response = requests.post(url=f'{URL}/pokemons', headers = HEADER, json = create_pokemons)
print(response.text)

change_pokemons = {
    "pokemon_id": "275820",
    "name": "Pikachu",
    "photo_id": 1
}

response = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = change_pokemons)
print(response.text)

add_pokeball = {
    "pokemon_id": "275820"
} 
response = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = add_pokeball)
print(response.text)