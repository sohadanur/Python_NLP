# instantiate the pipeline
from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained(
  "pyannote/speaker-diarization-3.1",
  use_auth_token="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")
# run the pipeline on an audio file
diarization = pipeline("C:\Users\sohad\Downloads\Speaker26_000.wav")
# dump the diarization output to disk using RTTM format
with open("audio.rttm", "w") as rttm:
    diarization.write_rttm(rttm)
import torch
pipeline.to(torch.device("cuda"))

waveform, sample_rate = torchaudio.load("C:\Users\sohad\Downloads\Speaker26_000.wav")
diarization = pipeline({"waveform": waveform, "sample_rate": sample_rate})
    
from pyannote.audio.pipelines.utils.hook import ProgressHook
with ProgressHook() as hook:
    diarization = pipeline("C:\Users\sohad\Downloads\Speaker26_000.wav", hook=hook)
    #diarization = pipeline("audio.wav", num_speakers=2)
    diarization = pipeline("C:\Users\sohad\Downloads\Speaker26_000.wav", min_speakers=2, max_speakers=5)
