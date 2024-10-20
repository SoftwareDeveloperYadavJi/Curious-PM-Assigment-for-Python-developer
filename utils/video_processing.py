
# utils/video_processing.py

from moviepy.editor import VideoFileClip, AudioFileClip

def extract_audio_from_video(video_file_path, audio_output_path):
    video = VideoFileClip(video_file_path)
    video.audio.write_audiofile(audio_output_path)




def replace_audio_in_video(video_file_path, new_audio_file_path, output_file_path, fps=24):
    # Load the video clip
    video_clip = VideoFileClip(video_file_path)
    
    # Load the new audio file
    new_audio = AudioFileClip(new_audio_file_path)
    
    # Set the audio of the video to the new audio
    video_clip = video_clip.set_audio(new_audio)
    
    # Write the result to a file with the given fps (default is 24)
    video_clip.write_videofile(output_file_path, fps=fps)


