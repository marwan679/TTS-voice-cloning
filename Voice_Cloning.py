import torch
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig, XttsAudioConfig, XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig
from torch.serialization import add_safe_globals

# Let PyTorch trust these classes during checkpoint loading
add_safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig, XttsArgs])

# Device setup
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Voice cloning to file
tts.tts_to_file(
    text="Hello, this is a voice cloning test. Nice to meet you!",
    file_path="output.wav",
    speaker_wav=["input.wav"],
    language="en",
    split_sentences=True
)
