import numpy as np
import json

class AudioProcessor:
    def __init__(self):
        self.hoge = ""
        self.db_array = []  # 名前変更

    def recv(self, frame):
        raw_samples = frame.to_ndarray()[0]
        N = len(raw_samples)
        rms = np.sqrt((1 / N) * (np.sum(raw_samples)) ** 2)
        self.db_array.append(rms)

    def on_ended(self):
        print(len(self.db_array),'+===============+')
        db_array = np.array(self.db_array)
        res = np.where(db_array < 200, False, True)
        mic_on_time, mic_off_time = 0, 0
        false_cnt = 0
        for r in res:
            if r is False:   
                false_cnt += 1
            else:
                
                if false_cnt < 40:  
                    mic_on_time += false_cnt
                else:  
                    mic_off_time += false_cnt
                mic_on_time += 1
                false_cnt = 0
        min_off_ratio = mic_off_time / (mic_on_time + mic_off_time)
        d = {
            "mic_off_ratio": min_off_ratio
        }
        with open('results/voice_analyze.json', 'w') as f:
            json.dump(d, f)

