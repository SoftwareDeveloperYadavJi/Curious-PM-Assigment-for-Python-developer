import os
import assemblyai as aai
from pydub import AudioSegment


def convert_audio_to_wav(audio_file_path):
    """
    Convert the audio file to a WAV format with appropriate settings.
    """
    audio = AudioSegment.from_file(audio_file_path)
    wav_path = "converted_audio.wav"
    audio = audio.set_frame_rate(16000).set_channels(1)  # Mono and 16kHz for better transcription
    audio.export(wav_path, format="wav")
    return wav_path

def transcribe_audio_assemblyai(audio_file_path):
    # Create a transcriber instance
    transcriber = aai.Transcriber()
    
    # Create a configuration for transcription
    config = aai.TranscriptionConfig(speaker_labels=True)

    # Transcribe the audio file
    transcript = transcriber.transcribe(audio_file_path, config)

    # Wait for the transcription to complete
    while transcript.status == aai.TranscriptStatus.processing:
        transcript = transcriber.get(transcript.id)  # Poll the status
        print(f"Transcription status: {transcript.status}")

    if transcript.status == aai.TranscriptStatus.error:
        print(f"Transcription failed: {transcript.error}")
        return None

    print("Transcription complete!")
    return transcript

# Main Execution
video_audio_path = 'extracted_audio.wav'

# Check if the audio file exists
if not os.path.exists(video_audio_path):
    print(f"Audio file not found: {video_audio_path}")
else:
    # Convert audio file to the correct format
    converted_audio_path = convert_audio_to_wav(video_audio_path)
    print(f"Converted audio file path: {converted_audio_path}")

    # Attempt to transcribe the converted audio
    transcript = transcribe_audio_assemblyai(converted_audio_path)
    if transcript:
        print("Transcription text:", transcript.text)

        # Print speaker utterances if speaker labels are enabled
        for utterance in transcript.utterances:
            print(f"Speaker {utterance.speaker}: {utterance.text}")
    else:
        print("Transcription failed.")
