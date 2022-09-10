import numpy as np
import json
import pydub

class AudioProcessor:
    def __init__(self):
        self.hoge = ""
        self.db_array = []
        self.sound_chunk = pydub.AudioSegment.empty()
        self.mic_off_threshold = 500
        self.volume_threshold = 1200

    def recv(self, audio_frame):
        sound = pydub.AudioSegment(
            data=audio_frame.to_ndarray().tobytes(),
            sample_width=audio_frame.format.bytes,
            frame_rate=audio_frame.sample_rate,
            channels=len(audio_frame.layout.channels),
        )
        self.sound_chunk += sound

    def on_ended(self):
        sound = self.sound_chunk.set_channels(1)
        sample = np.array(sound.get_array_of_samples())
        if len(sample) < 16000:
            mic_off_ratio = 1
            volume = 0

        else:
            sample = abs(sample)[10000:-5000]

            speak_data = sample[sample > self.mic_off_threshold]
            if len(speak_data) == 0:
                mic_off_ratio = 1
                volume = 0
            else:
                volume = np.mean(speak_data) / self.volume_threshold

                speak_idx = np.where(sample > self.mic_off_threshold)
                prev_idx = 0
                for i in speak_idx[0]:
                    if i - prev_idx < 14000:
                        sample[prev_idx:i] = 5000
                    prev_idx = i

                mic_off_ratio = len(np.where(sample < self.mic_off_threshold)[0]) / len(sample)

        d = {
            "mic_off_ratio": mic_off_ratio,
            "volume": volume
        }
        with open("results/audio.json", "w") as f:
            json.dump(d, f)
        print("audio done")
