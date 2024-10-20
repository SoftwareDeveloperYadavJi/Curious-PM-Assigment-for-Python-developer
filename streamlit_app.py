import os
import streamlit as st
import assemblyai as aai
from utils.gpt4o import correct_transcription_gpt4o
from utils.text_to_speech import text_to_speech_elevenlabs
from utils.video_processing import extract_audio_from_video, replace_audio_in_video

from config import ASSEMBLYAI_API_KEY
# Set AssemblyAI API Key
aai.settings.api_key = ASSEMBLYAI_API_KEY

st.title("Video Audio Replacement with AI Voice")

# File uploader for video
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Create directory if it doesn't exist
    upload_folder = "uploaded_videos"
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    # Save uploaded video locally
    video_file_path = os.path.join(upload_folder, uploaded_file.name)
    with open(video_file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())

    st.write("Processing video...")
    st.write("Extracting audio...")  # Debug

    # Step 1: Extract audio from the video
    audio_file_path = "extracted_audio.wav"
    extract_audio_from_video(video_file_path, audio_file_path)
    st.write("Audio extracted successfully!")  # Debug

    # Step 2: Upload extracted audio to AssemblyAI and transcribe
    st.write("Uploading and transcribing audio...")  # Debug

    # Upload audio file to AssemblyAI
    with open(audio_file_path, 'rb') as audio_file:
        transcript = aai.Transcriber().transcribe(audio_file)

    if transcript.status == "completed":
        st.write("Transcription complete!")
        st.write("Transcription text: ", transcript.text)

        # Step 3: Correct transcription using GPT-4o
        st.write("Correcting transcription...")  # Debug
        corrected_transcription = correct_transcription_gpt4o(transcript.text)
        st.write("Corrected Transcription: ", corrected_transcription)

        # Step 4: Convert corrected transcription to speech using ElevenLabs
        st.write("Converting transcription to speech...")  # Debug
        corrected_audio_file = "corrected_audio.mp3"
        text_to_speech_elevenlabs(corrected_transcription, corrected_audio_file)
        st.write("Speech conversion complete!")  # Debug

        # Step 5: Replace the audio in the original video
        st.write("Replacing audio in the video...")  # Debug
        output_video_path = "output_video.mp4"
        replace_audio_in_video(video_file_path, corrected_audio_file, output_video_path)

        st.video(output_video_path)
        st.success("Video processing complete!")
    else:
        st.error(f"Transcription failed with status: {transcript.status}")
