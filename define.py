import requests

def get_definitions(word):
    api = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(api)
    
    # Handle cases where the word is not found
    if response.status_code != 200:
        return {'error': 'Word not found or API request failed'}

    word_data = response.json()[0]
    definitions = []
    
    # Loop through meanings to get part of speech and definitions
    for meaning in word_data.get('meanings', []):
        part_of_speech = meaning.get('partOfSpeech', '')
        for definition_entry in meaning.get('definitions', []):
            definition = definition_entry.get('definition', '')
            formatted_definition = f"({part_of_speech}) {definition}"
            definitions.append(f"👉 {formatted_definition}")
    
    # Handle phonetic and audio data
    phonetic = word_data.get('phonetic', "Phonetic spelling not available")
    audio = 'No audio available'
    
    if 'phonetics' in word_data and word_data['phonetics']:
        audio = word_data['phonetics'][0].get('audio', 'No audio available')

    return {
        'definitions': definitions,
        'phonetic': phonetic,
        'audio': audio
    }
