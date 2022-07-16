import numpy as np


class AudioProcessor:
    def __init__(self):
        self.hoge = ""
        self.db_array = []  # 名前変更

    def recv(self, frame):
        raw_samples = frame.to_ndarray()[0]
        N = len(raw_samples)
        rms = np.sqrt((1 / N) * (np.sum(raw_samples)) ** 2)
        db = 20 * np.log10(rms)
        print(db)

        # TODO: データの蓄積
        self.db_array.append(db)

        # どの大きさだと最適なのか？声の大きさの基準を決める
        # 無言の時はいくつなのか
        # 大きすぎの時と小さすぎ（無言）の時のカウントとかをして
        # 最終的な評価に繋げる

    def on_ended(self):
        # videoが終わるときに呼び出されます
        # 最終的な結果をjsonファイルに出力
        # 参考：video.py
