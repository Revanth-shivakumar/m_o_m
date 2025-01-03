#!/usr/bin/env python

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start # type: ignore

import librosa

import whisper

from pydub import AudioSegment

from pydub.utils import make_chunks

from pathlib import Path

from crews.mom_crew.meeting_minutes_crew import MeetingMinutesCrew

from crews.gmail.gmail import Gmail

class MeetingMinutesState(BaseModel):
    transcript: str = ""
    meeting_minutes: str = ""


class MeetingMinutesFlow(Flow[MeetingMinutesState]):

    @start()
    def transcribe_meeting(self):
        print("Generating transcript")
        # implement whisper workflow
        SCRIPT_DIR=Path(__file__).parent
        #chunking audio files
        audio_path=str(SCRIPT_DIR/"Meeting.wav")
        audio=AudioSegment.from_file(audio_path,format="wav")

        chunk_length_ms=60000
        chunks=make_chunks(audio,chunk_length_ms)
        model=whisper.load_model('turbo')
        full_transcription = ""
        for i, chunk in enumerate(chunks):
            print(f"Transcribing chunk {i+1}/{len(chunks)}")
            chunk_path = f"chunk_{i}.wav"
            chunk.export(chunk_path, format="wav")
    
            # Load WAV file as NumPy array
            audio, sr = librosa.load(chunk_path, sr=None)

            # Pass the audio array to the model
            transcription = model.transcribe(audio)
            print(transcription)
            full_transcription += transcription['text'] + " "
        self.state.transcript = full_transcription
        meeting_minutes_folder = SCRIPT_DIR / "meeting_minutes"
        meeting_minutes_folder.mkdir(exist_ok=True)
        transcript_path = meeting_minutes_folder / "transcript.md"
        with open(transcript_path, "w") as f:
            f.write(self.state.transcript)
            
        
    @listen(transcribe_meeting)
    def generate_meeting_minutes(self):
        print("Generating meeting minutes")
        crew=MeetingMinutesCrew()
        inputs={
            "transcript":self.state.transcript
            }
        
        meeting_minutes=crew.crew().kickoff(inputs)
        self.state.meeting_minutes=meeting_minutes
    # @listen(generate_meeting_minutes)
    # def create_draft(self):
    #     crew=Gmail()
    #     inputs={
    #         "body":self.state.meeting_minutes
    #         }
    #     draft_crew=crew.crew().kickoff(inputs)
    #     print(draft_crew)
        
    def kickoff():
        meeting_minutes_flow = MeetingMinutesFlow()
        meeting_minutes_flow.plot()
        meeting_minutes_flow.kickoff()
   


if __name__ == "__main__":
    kickoff()
