# Video Audio Replacement Project

## Overview

This project provides a simple solution to replace the audio track of a video file with a new audio file. The tool extracts audio from the video, transcribes it, and corrects any inaccuracies before generating new audio with the desired text. Finally, it replaces the original audio with the newly created audio, ensuring that the audio duration matches the video's duration.

## Features

- Extracts audio from video files.
- Transcribes audio using an external API.
- Corrects transcriptions using natural language processing.
- Converts corrected text back into audio using text-to-speech services.
- Replaces audio in the original video with the new audio.
- Ensures audio and video duration matching, with options to adjust synchronization.

## Technologies Used

- [MoviePy](https://zulko.github.io/moviepy/) for video and audio processing.
- [Streamlit](https://streamlit.io/) for building the web application interface.
- [Speech Recognition API](https://pypi.org/project/SpeechRecognition/) for transcribing audio.
- [Text-to-Speech API](https://beta.elevenlabs.io/) for converting text to speech.

## Requirements

- Python 3.7 or higher
- Required Python packages:
  - moviepy
  - streamlit
  - pydub
  - requests
  - SpeechRecognition

You can install the required packages using pip:


## Usage
`
pip install moviepy streamlit pydub requests SpeechRecognition
`

## Start the Streamlit App
`
streamlit run streamlit_app.py
`


### Customization:

-  `https://github.com/SoftwareDeveloperYadavJi/Curious-PM-Assigment-for-Python-developer.git`  
- Add any additional sections you think are necessary, such as a changelog, FAQs, or troubleshooting tips.

Let me know if you need any further adjustments!


