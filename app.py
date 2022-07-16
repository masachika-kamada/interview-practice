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
    st.session_state['camera']='70'
    st.session_state['smile']='30'
    st.session_state['normal']='40'
    st.session_state['interviwer']='良'
    st.session_state['volume']='ちょうど良い'
    st.session_state['silence']='50'
    st.session_state['rank']='B'
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
    div.main_container {{
        ext-align: center;
    }}
    </style>
    """
    # css適用
    st.markdown(result_css, unsafe_allow_html=True)
    main_container = st.container()
    main_container.title("分析結果")
    main_container.markdown("自己紹介をお願いします")
    # 録画表示 
    stc.html("<iframe width=’560’ height=’315’ src='https://www.youtube.com/embed/3QPp_DlcZpM' title=’YouTube video player’ frameborder=’0’ allow=’accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture’ allowfullscreen></iframe>")
    # 値受け取り
    container = st.container()
    container.markdown("カメラ目線" + st.session_state['camera'])
    container.markdown("笑顔：" + st.session_state['smile'] + '秒 / 普通' + st.session_state['normal'] + '秒')
    container.markdown("面接官からの印象" + st.session_state['interviwer'])
    container.markdown("声の大きさ" + st.session_state['volume'])
    container.markdown("無言の時間率" + st.session_state['silence'])
    container.markdown("面接基礎力ランク" + st.session_state['rank'])

    st.button('他の質問で分析してみる', on_click=show_home)

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