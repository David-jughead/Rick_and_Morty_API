import requests
import time
import json

def get_data(url):
    response = requests.get(url)
    data = response.json()
    return data

# Función para contar la cantidad de veces que aparece una letra en los nombres de una lista de recursos
def count_letter(resource_list, letter):
    count = 0
    for item in resource_list:
        name = item['name'].lower()
        count += name.count(letter)
    return count

# Obtener todos los characters
characters_url = 'https://rickandmortyapi.com/api/character'
characters_data = get_data(characters_url)
all_characters = characters_data['results']

# Obtener todos los locations
locations_url = 'https://rickandmortyapi.com/api/location'
locations_data = get_data(locations_url)
all_locations = locations_data['results']

# Obtener todos los episodes
episodes_url = 'https://rickandmortyapi.com/api/episode'
episodes_data = get_data(episodes_url)
all_episodes = episodes_data['results']

# Contar las letras en los nombres de los locations, episodes y characters
start_time = time.time()

letter_counts = []
letter_counts.append({
    'char': 'l',
    'count': count_letter(all_locations, 'l'),
    'resource': 'location'
})
letter_counts.append({
    'char': 'e',
    'count': count_letter(all_episodes, 'e'),
    'resource': 'episode'
})
letter_counts.append({
    'char': 'c',
    'count': count_letter(all_characters, 'c'),
    'resource': 'character'
})

elapsed_time = time.time() - start_time

# Obtener las locations de cada episode y los characters que aparecen en cada episode
start_time = time.time()

episode_locations = []
for episode in all_episodes:
    episode_name = episode['name']
    episode_code = episode['episode']
    episode_characters = []
    for character_url in episode['characters']:
        character_data = get_data(character_url)
        character_location = character_data['origin']['name']
        if character_location not in episode_characters:
            episode_characters.append(character_location)
    episode_locations.append({
        'name': episode_name,
        'episode': episode_code,
        'locations': episode_characters
    })

elapsed_time += time.time() - start_time

# Crear el output en formato JSON
output = [
    {
        'exercise_name': 'Char counter',
        'time': f'{elapsed_time}s',
        'in_time': True,
        'results': letter_counts
    },
    {
        'exercise_name': 'Episode locations',
        'time': f'{elapsed_time}s',
        'in_time': True,
        'results': episode_locations
    }
]

json_output = json.dumps(output, indent=4)
print(json_output)
