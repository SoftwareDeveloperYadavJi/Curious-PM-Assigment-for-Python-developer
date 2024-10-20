import requests
from config import ELEVENLABS_API_KEY

def list_voices():
    url = "https://api.elevenlabs.io/v1/voices"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        voices = response.json()
        print("Available voices:")
        for voice in voices['voices']:
            print(f"ID: {voice['id']}, Name: {voice['name']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")


def text_to_speech_elevenlabs(text, output_audio_path):
    valid_voice_id = "pNInz6obpgDQGcFmaJgB"  # Replace this with the correct voice ID
    # valid_voice_id = "XB0fDUnXU5powFXDhCwa"  # Replace this with the correct voice ID
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{valid_voice_id}"
    
    headers = {
        "accept": "audio/mpeg",
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        with open(output_audio_path, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Error: {response.status_code}, {response.text}")























