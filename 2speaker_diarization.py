from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token="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")

# apply pretrained pipeline
diarization = pipeline(r"C:\\Users\\sohad\\OneDrive\\Desktop\\Python\\BacBon\\codes\\F_0101_10y4m_1.wav")
 # input audio file
# print the result
for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(turn)
    print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
    
    