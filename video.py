class VideoProcessor:
    def __init__(self):
        self.hoge = ""

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # return av.VideoFrame.from_ndarray(img, format="bgr24")