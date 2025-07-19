from gtts import gTTS
import tempfile

def synthesize_voice(text: str) -> str:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    gTTS(text=text, lang="en").save(tmp.name)
    return tmp.name