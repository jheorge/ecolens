import os
import pyttsx3
from gtts import gTTS
from io import BytesIO
import pyglet

temp_mp3_file_name = 'temp.mp3'

def delete_mp3(mp3_file_name: str):
    try:
        os.remove(mp3_file_name)
    except FileNotFoundError:
        pass


def get_text_to_speech():
    result = input("Write the text to speech (spanish): ")
    return result

def init_gtts(text: str):
    tts = gTTS(text=text, lang='es')
    tts.save(temp_mp3_file_name)
    mp3_fp = BytesIO()
    tts = gTTS(text=text, lang='es')
    tts.write_to_fp(mp3_fp)
    return mp3_fp

def play_gtts(mp3_fp: BytesIO):
    music = pyglet.media.load(temp_mp3_file_name, file=mp3_fp)
    player = pyglet.media.Player()
    player.queue(music)
    player.play()

    def on_eos():
        pyglet.app.exit()
        delete_mp3(temp_mp3_file_name)
    
    player.on_eos = on_eos

    pyglet.app.run()
    


def main():
     text = get_text_to_speech()
     audio = init_gtts(text)
     play_gtts(audio)
     

main()