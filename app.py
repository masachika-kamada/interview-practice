import streamlit as st
import streamlit.components.v1 as stc
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

    # 値の受け渡し
    st.session_state["results"]='hoge'
    st.button("結果へ", on_click=show_result)


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
    st.markdown(st.session_state["results"])

    st.button('ホームへ', on_click=show_home)
    
def show_home():
    # homeへ切り替え
    st.session_state["page_control"]=0

def show_result():
    # resultへ切り替え
    st.session_state["page_control"]=1

# 状態保持する変数を作成して確認
if ("page_control" in st.session_state and
    st.session_state["page_control"] == 1):
    result_page()
else:
    st.session_state["page_control"] = 0
    main()