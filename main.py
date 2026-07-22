import requests
import random
import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

def search_book(number):
    url = f"https://www.gutenberg.org/files/{number}/{number}-0.txt"

    response = requests.get(url)

    return response

def create_excerpts(text, size=200):

    words = text.split()

    excerpts = []

    for i in range(0, len(words), size):
        excerpt = " ".join(
            words[i:i+size]
        )

        excerpts.append(excerpt)

    return excerpts

def text_to_speach(excerpt):
    tts.tts_to_file(text=excerpt, speaker_wav="84-121123-0002.flac", language="en", file_path="/Users/sagebuilder09/Documents/GitHub/ProjectInsanity/audio/output.wav")



book = search_book(888)
excerpt = create_excerpts(book.text)
text_to_speach(excerpt[5])