import streamlit as st
from streamlit_webrtc import webrtc_streamer
from video import VideoProcessor
from audio import AudioProcessor


def main():
    st.markdown('# 面接練習')

    webrtc_streamer(
        key="",
        video_processor_factory=VideoProcessor,
        audio_processor_factory=AudioProcessor,
        # デプロイ時にコメントアウト除去
        # rtc_configuration={
        #     "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        # }
    )


if __name__ == '__main__':
    main()