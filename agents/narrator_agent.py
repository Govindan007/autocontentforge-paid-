from gtts import gTTS

def run_narrator_agent(text, filename="output.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    return filename
