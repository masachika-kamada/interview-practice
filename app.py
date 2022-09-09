import streamlit as st
import streamlit.components.v1 as stc
from streamlit_webrtc import webrtc_streamer
import time
import base64
from video import VideoProcessor
from audio import AudioProcessor
import layout, content


def main():
    st.markdown(layout.toppage_css, unsafe_allow_html=True)

    st.session_state["question"] = 0

    stc.html(content.title, height=225)

    st.button('質問１', on_click=question1)
    st.button('質問２', on_click=question2)
    st.button('質問３', on_click=question3)
    st.button('質問４', on_click=question4)
    st.button('質問５', on_click=question5)


def record_page():
    # ビデオ開始用変数 ボタンクリックでtrueにする
    playing = False
    
    if 'count' not in st.session_state:
        st.session_state["count"] = 0
    if 'end_button' not in st.session_state:
        st.session_state["end_button"] = 0

    container = st.container()
    start = container.button('開始する')
    if start:
        if st.session_state["count"] == 0:
            st.session_state["count"] += 1
        else :
            st.session_state["count"] == 0

    # 開始ボタンクリック時
    if st.session_state["count"] == 1:
        st.markdown(layout.rem_start_button_css, unsafe_allow_html=True)

        # ローディング表示
        stc.html(content.loading_animation)

        #入力する音声ファイル
        audio_path = f"questions/{st.session_state['question']}.mp3"
        with open(audio_path, "rb") as f:
            contents = f.read()
        audio_str = "data:audio/ogg;base64,%s"%(base64.b64encode(contents).decode())
        audio_html = f"""
            <audio autoplay=True>
            <source src="{audio_str}" type="audio/ogg" autoplay=True>
            Your browser does not support the audio element.
            </audio>"""

        audio_placeholder = st.empty()
        audio_placeholder.empty()
        time.sleep(0.5)
        audio_placeholder.markdown(audio_html, unsafe_allow_html=True)
        time.sleep(3)  # 音声再生時間
        st.session_state["count"] += 1

    if st.session_state["count"] == 2:
        st.markdown(layout.rem_stop_button_css, unsafe_allow_html=True)
        playing = True

    webrtc_streamer(
        key="",
        desired_playing_state=playing,
        video_processor_factory=VideoProcessor,
        audio_processor_factory=AudioProcessor,
        # デプロイ時にコメントアウト除去
        # rtc_configuration={
        #     "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        # }
    )

    st.markdown(layout.button_css, unsafe_allow_html=True)

    if st.session_state["count"] == 2:
        st.button('終了する', on_click=show_result)
        st.markdown(layout.stop_css, unsafe_allow_html=True)


def result_page():
    stc.html(content.result_upper(st.session_state['question'] - 1), height=145)
    stc.html(content.result_lower(), height=450)
    st.button('他の質問で分析してみる', on_click=show_home)
    st.markdown(layout.result_css, unsafe_allow_html=True)


def show_home():
    # homeへ切り替え
    st.session_state["page_control"] = 0

def question1():
    st.session_state["page_control"] = 1
    st.session_state["question"] = 1

def question2():
    st.session_state["page_control"] = 2
    st.session_state["question"] = 2

def question3():
    st.session_state["page_control"] = 3
    st.session_state["question"] = 3

def question4():
    st.session_state["page_control"] = 4
    st.session_state["question"] = 4

def question5():
    st.session_state["page_control"] = 5
    st.session_state["question"] = 5

def show_result():
    # resultへ切り替え
    st.session_state["page_control"] = 6


if __name__ == '__main__':
    # 状態保持する変数を作成して確認
    if ("page_control" in st.session_state and
        0 < st.session_state["page_control"] < 6):
        record_page()
    elif ("page_control" in st.session_state and
        st.session_state["page_control"] == 6):
        result_page()
    else:
        st.session_state["count"] = 0
        main()
