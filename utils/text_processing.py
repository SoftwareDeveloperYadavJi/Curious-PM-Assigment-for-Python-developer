import openai
from config import AZURE_GPT4O_API_KEY

openai.api_key = AZURE_GPT4O_API_KEY

def correct_transcription(transcription):
    prompt = f"Please correct the following transcription by removing any grammatical errors and unnecessary filler words like umm, hmm, etc.:\n\n{transcription}"
    
    response = openai.Completion.create(
        engine="gpt-4o",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5
    )
    
    corrected_text = response.choices[0].text.strip()
    return corrected_text
