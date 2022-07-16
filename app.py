import streamlit as st
from streamlit_webrtc import webrtc_streamer

import streamlit.components.v1 as stc
import base64
import time


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

    question_button = st.button('アプリ実行')
    if question_button:
        audio_path1 = './question/1intoro.mp3' #入力する音声ファイル
        audio_placeholder = st.empty()

        file_ = open(audio_path1, "rb")
        contents = file_.read()
        file_.close()
        audio_str = "data:audio/ogg;base64,%s"%(base64.b64encode(contents).decode())
        audio_html = """
                        <audio autoplay=True>
                        <source src="%s" type="audio/ogg" autoplay=True>
                        Your browser does not support the audio element.
                        </audio>
                    """ %audio_str

        audio_placeholder.empty()
        time.sleep(0.5)
        audio_placeholder.markdown(audio_html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()