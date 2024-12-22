# **Meeting and Mail Crew**

Welcome to the Meeting and Mail Crew project


![flow](https://github.com/user-attachments/assets/8590f66d-a190-4fb0-b44b-8b3b206480c2)


Overview

This project aims to automate the process of generating meeting minutes, summarizing key discussions, and creating action plans. It utilizes a combination of AI agents and tools to analyze audio recordings, extract relevant information, and generate concise output.

Workflow

Audio file chunking:

Audio file is segmented into 1 minute segments for better audio to text conversion.

Audio to Text Conversion:

The project utilizes Whisper Turbo to transcribe audio recordings into text.

Meeting Minutes Generation:

Meeting of Minutes Crew analyzes the text chunks and generates a comprehensive summary of the meeting, including key discussions, decisions, and action items.

Action Planning:

Action analyzes the meeting summary and identifies specific action items that need to be completed.
Plan creates a structured plan for each action item, outlining the steps involved, timelines, and responsible individuals.
Sentiment Analysis:

Overall Sentiment analyzes the overall tone and sentiment of the meeting to provide insights into the team's mood and engagement.
Gmail Integration:

Gmail Agent  with the help of custom gmail api integration tool facilitate the automated sending of meeting minutes and action plans via Gmail.

Tools and Technologies

CrewAI
LangChain
Ollama
Llama 8b
Whisper Turbo
Gmail API
Benefits
