import streamlit as st
import streamlit.components.v1 as stc
from streamlit_webrtc import webrtc_streamer
import base64
import time


class VideoProcessor:
    def __init__(self):
        self.hoge = ""

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # return av.VideoFrame.from_ndarray(img, format="bgr24")


def main():

    st.session_state["question"]=0

    st.markdown('# Interview-Practice')

    st.button('質問１', on_click=question1)

    st.button('質問２', on_click=question2)

    st.button('質問３', on_click=question3)

    st.button('質問４', on_click=question4)

    st.button('質問５', on_click=question5)

    st.markdown(st.session_state["question"])

def record_page():
    st.markdown(st.session_state["question"])
    webrtc_streamer(
    key="",
    video_processor_factory=VideoProcessor,
    # デプロイ時にコメントアウト除去
    # rtc_configuration={
    #     "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    # }
    )

    #音声再生ボタン
    audio_path1 = './question/1intoro.mp3'
    audio_path2 = './question/2sibou.mp3'
    audio_path3 = './question/3gakuchika.mp3'
    audio_path4 = './question/4tyoutan.mp3'
    audio_path5 = './question/5vision.mp3'
    
    if st.button('質問文'):
        #入力する音声ファイル
        audio_placeholder = st.empty()
        if st.session_state["question"] == 1:
            audio_path = audio_path1
        elif st.session_state["question"] == 2:
            audio_path = audio_path2
        elif st.session_state["question"] == 3:
            audio_path = audio_path3
        elif st.session_state["question"] == 4:
            audio_path = audio_path4
        elif st.session_state["question"] == 5:
            audio_path = audio_path5

        file_ = open(audio_path, "rb")
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

    # 値の受け渡し
    st.button("結果へ", on_click=show_result)
    st.button("ホームへ", on_click=show_home)

def result_page(): 
    # css作成
    result_css = f"""
    <style>
    div.stButton > button:first-child  {{
        font-weight  : bold                ;
        border       :  5px solid #f36     ;
        border-radius: 10px 10px 10px 10px ;
        background   : #ddd                ;
    }}
    </style>
    """
    # css適用
    st.markdown(result_css, unsafe_allow_html=True)

    st.title("結果")
    # 値受け取り
    # st.markdown(st.session_state["results"])

    st.button('ホームへ', on_click=show_home)
    
def show_home():
    # homeへ切り替え
    st.session_state["page_control"]=0

def question1():
    # homeへ切り替え
    st.session_state["page_control"]=1
    st.session_state["question"]=1

def question2():
    # homeへ切り替え
    st.session_state["page_control"]=2
    st.session_state["question"]=2

def question3():
    # homeへ切り替え
    st.session_state["page_control"]=3
    st.session_state["question"]=3

def question4():
    # homeへ切り替え
    st.session_state["page_control"]=4
    st.session_state["question"]=4

def question5():
    # homeへ切り替え
    st.session_state["page_control"]=5
    st.session_state["question"]=5

def show_result():
    # resultへ切り替え
    st.session_state["page_control"]=6




# 状態保持する変数を作成して確認
if ("page_control" in st.session_state and
    st.session_state["page_control"] > 0 and 
    st.session_state["page_control"] < 6 ):
    record_page()
elif ("page_control" in st.session_state and
    st.session_state["page_control"] == 6):
    result_page()
else:
    main()