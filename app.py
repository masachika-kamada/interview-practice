import streamlit as st
from streamlit_webrtc import webrtc_streamer


class VideoProcessor:
    def __init__(self):
        self.hoge = ""

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # return av.VideoFrame.from_ndarray(img, format="bgr24")


def main():
    st.markdown('# 面接練習')

    webrtc_streamer(
        key="",
        video_processor_factory=VideoProcessor,
        # デプロイ時にコメントアウト除去
        # rtc_configuration={
        #     "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        # }
    )


if __name__ == '__main__':
    main()