import torch
from TTS.utils.manage import ModelManager

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
ModelManager = ModelManager()
model_path = model_manager.download_model('tts_models/en/ljspeech/tacotron2-DDC')
tts = model_manager.load_model(model_path, device)


def tts(text, output_path="output.wav"):
    tts.tts_to_file(text=text, speaker='default', file_path=output_path)
