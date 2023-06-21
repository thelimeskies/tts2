from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech
from datasets import load_dataset
import torch
from transformers import SpeechT5HifiGan
import soundfile as sf
import numpy as np


class MicrosoftT5TTS:
    def __init__(self):
        self.processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
        self.model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
        self.vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
        self.embeddings_dataset = load_dataset(
            "Matthijs/cmu-arctic-xvectors", split="validation"
        )

    def synthesize(self, text: str):
        inputs = self.processor(text=text, return_tensors="pt", padding=True)
        speaker_embeddings = torch.tensor(
            self.embeddings_dataset[7306]["xvector"]
        ).unsqueeze(0)
        spectrogram = self.model.generate_speech(
            inputs["input_ids"], speaker_embeddings
        )
        with torch.no_grad():
            speech = self.vocoder(spectrogram)

        return speech.numpy(), 16000

    def to_wav(self, text: str, path: str):
        try:
            speech, sample_rate = self.synthesize(text)
            sf.write(path, speech, samplerate=sample_rate)
            return True, None
        except Exception as e:
            return False, e

    def synthesize_in_chunks(self, text: str, chunk_size: int):
        """
        Synthesize text in chunks of chunk_size
        """

        speech = None

        for i in range(0, len(text), chunk_size):
            chunk = text[i : i + chunk_size]
            chunk_speech, sample_rate = self.synthesize(chunk)

            if speech is None:
                speech = chunk_speech
            else:
                speech = np.concatenate((speech, chunk_speech))

        return speech, sample_rate

    def to_wav_in_chunks(self, text: str, path: str, chunk_size: int):
        try:
            speech, sample_rate = self.synthesize_in_chunks(text, chunk_size)
            sf.write(path, speech, samplerate=sample_rate)
            return True, None
        except Exception as e:
            return False, e


if __name__ == "__main__":
    text = "This is a test"
    TTS = MicrosoftT5TTS()
    TTS.to_wav_in_chunks(text, "tts_example.wav", 100)
