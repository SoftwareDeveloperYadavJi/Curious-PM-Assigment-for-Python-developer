import openai
from config import OPENAI_GPT4O_API_KEY
# Make sure to set your OpenAI API key here
openai.api_key = OPENAI_GPT4O_API_KEY

def correct_transcription_gpt4o(transcription_text):
    # Update for new OpenAI API: using ChatCompletion
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use GPT-4 or GPT-3.5-turbo
        messages=[
            {"role": "system", "content": "You are an assistant that corrects transcriptions for accuracy."},
            {"role": "user", "content": transcription_text}
        ]
    )
    
    # Extract the response
    corrected_text = response['choices'][0]['message']['content']
    return corrected_text
