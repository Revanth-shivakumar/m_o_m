import streamlit as st
from app import MeetingMinutesFlow
import os

def main():
    st.title("Meeting Minutes Application")
    
    st.header("Upload Audio File")
    audio_file = st.file_uploader("Choose an audio file", type=["mp3", "wav"])
    
    if audio_file is not None:
        st.audio(audio_file, format='audio/wav')
        
        # Save the uploaded audio file as Meeting.wav
        with open("Meeting.wav", "wb") as f:
            f.write(audio_file.getbuffer())
        
        st.header("Meeting Minutes Flow")
        if st.button("Generate Meeting Minutes"):
            meeting_minutes_flow = MeetingMinutesFlow()
            meeting_minutes_flow.transcribe_meeting()
            meeting_minutes_flow.generate_meeting_minutes()
            st.text_area("Meeting Minutes", value=meeting_minutes_flow.state.meeting_minutes, height=300)
            
            # Access resultant text files from ./meeting_minutes folder
            st.header("Download Meeting Minutes Files")
            meeting_minutes_folder = './meeting_minutes'
            if os.path.exists(meeting_minutes_folder):
                for filename in os.listdir(meeting_minutes_folder):
                    file_path = os.path.join(meeting_minutes_folder, filename)
                    with open(file_path, 'r') as file:
                        st.download_button(
                            label=f"Download {filename}",
                            data=file,
                            file_name=filename,
                            mime='text/plain'
                        )

if __name__ == "__main__":
    main()