from click import style
import streamlit as st
import streamlit.components.v1 as stc
from streamlit_webrtc import webrtc_streamer
import time
import base64
# from video import VideoProcessor
from audio import AudioProcessor
import glob
import json
from PIL import Image
import random

def main():
    # css作成
    result_css = f"""
    <style>
    div.stButton {{
            text-align: center;
    }}
    div.stButton > button {{
            text-align: center;
            width: 500px;
            height: 40px;
            color: #5f6c7b; 
    }}
    /* ボタン色変更 */
    div.stButton > button:hover {{
        border-color: #90b4ce;
        color: #90b4ce;
        # border-color: #3da9fc;
        # color: #3da9fc;
    }}
    div.stButton > button:focus:not(:active) {{
        border-color: #90b4ce;
        color: #90b4ce;
    }}
    div.stButton > button.css-1cpxqw2:focus {{
        box-shadow: unset;
    }}
    div.stButton > button.css-1cpxqw2:focus {{
        border-color: #90b4ce;
        background-color: #90b4ce;
        color: #fffffe;
    }}
    /* ボタン色変更ここまで */
    </style>
    """
    # css適用
    st.markdown(result_css, unsafe_allow_html=True)
    
    st.session_state["question"]=0

    # st.markdown('# Interview-Practice')
    stc.html("""
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Yuji+Syuku&display=swap" rel="stylesheet">
    </head>
    <h1 class='title'>めんたつ</h1>
    <h1 class='subtitle'>あなたの<span>”オンライン面接力”</span>を測ってみよう。</h1>
    <h2 class='subtitle'>-How much <span>”Online-Interview-Skills”</span>do you have?-</h2>
    <style>
    .title {
        text-align: center;
        color: black;
        margin: 0;
        font-size: 70px;
    }
    .subtitle {
        text-align: center;
        color: #5f6c7b; 
    }
    h1.subtitle {
        font-size:30px;
        margin: 10px 0 0 0;
    }
    h2.subtitle {
        font-size:21px;
    }
    span {
        color: #3da9fc;
    }
    .title {
        font-family: 'Yuji Syuku', serif;
    }
    </style>
    """, height=225)


    st.button('質問１', on_click=question1)

    st.button('質問２', on_click=question2)

    st.button('質問３', on_click=question3)

    st.button('質問４', on_click=question4)

    st.button('質問５', on_click=question5)

    # st.markdown(st.session_state["question"])

def record_page():
    #音声再生ボタン
    audio_path1 = './question/1intoro.mp3'
    audio_path2 = './question/2sibou.mp3'
    audio_path3 = './question/3gakuchika.mp3'
    audio_path4 = './question/4tyoutan.mp3'
    audio_path5 = './question/5vision.mp3'

    #ビデオ開始用変数 ボタンクリックでtrueにする 
    global playing
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

    #　開始ボタンクリック時
    if st.session_state["count"] == 1:
        playing_css = f"""
        <style>
        div.css-1n76uvr > div.element-container > div.stButton > button.edgvbvh9 {{
                display: none;
        }}
        </style>
        """
        # css適用
        st.markdown(playing_css, unsafe_allow_html=True)

        # ローディング表示 
        stc.html("""
            <div class="loader">Loading...</div>
            <style>
            .loader,
            .loader:before,
            .loader:after {
            background: #3da9fc;
            -webkit-animation: load1 1s infinite ease-in-out;
            animation: load1 1s infinite ease-in-out;
            width: 1em;
            height: 4em;
            }
            .loader {
            color: #3da9fc;
            text-indent: -9999em;
            margin: 44px auto;
            position: relative;
            font-size: 22px;
            -webkit-transform: translateZ(0);
            -ms-transform: translateZ(0);
            transform: translateZ(0);
            -webkit-animation-delay: -0.16s;
            animation-delay: -0.16s;
            }
            .loader:before,
            .loader:after {
            position: absolute;
            top: 0;
            content: '';
            }
            .loader:before {
            left: -1.5em;
            -webkit-animation-delay: -0.32s;
            animation-delay: -0.32s;
            }
            .loader:after {
            left: 1.5em;
            }
            @-webkit-keyframes load1 {
            0%,
            80%,
            100% {
                box-shadow: 0 0;
                height: 4em;
            }
            40% {
                box-shadow: 0 -2em;
                height: 5em;
            }
            }
            @keyframes load1 {
            0%,
            80%,
            100% {
                box-shadow: 0 0;
                height: 4em;
            }
            40% {
                box-shadow: 0 -2em;
                height: 5em;
            }
            }

            </style>
            """)

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
        time.sleep(3)
        st.session_state["count"] += 1
    if st.session_state["count"] == 2:
        # 開始ボタンを完全に消す
        playing_css = f"""
        <style>
        div.css-1n76uvr > div > div.css-1n76uvr > div.element-container > div.stButton > button.edgvbvh9 {{
            display:none;
        }}
        </style>
        """
        # css適用
        st.markdown(playing_css, unsafe_allow_html=True)
        
        # 再生用変数
        playing = True

    webrtc_streamer(
        key="",
        desired_playing_state=playing,
        # video_processor_factory=VideoProcessor,
        # audio_processor_factory=AudioProcessor,
        # デプロイ時にコメントアウト除去
        # rtc_configuration={
        #     "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        # }
    )

    result_css = f"""
    <style>
    div.stButton {{
            text-align: center;
    }}
    div.stButton > button {{
            text-align: center;
            width: 91px;
            height: 40px;
            position: relative;
            right: 308px;
            bottom: -170px;
            z-index: 61;
            color: #5f6c7b;
    }}
    /* ボタン色変更 */
    div.stButton > button:hover {{
        border-color: #90b4ce;
        color: #90b4ce;
        # border-color: #3da9fc;
        # color: #3da9fc;
    }}
    div.stButton > button:focus:not(:active) {{
        border-color: #90b4ce;
        color: #90b4ce;
    }}
    div.stButton > button.css-1cpxqw2:focus {{
        box-shadow: unset;
    }}
    div.stButton > button.css-1cpxqw2:focus {{
        border-color: #90b4ce;
        background-color: #90b4ce;
        color: #fffffe;
    }}
    /* ボタン色変更ここまで */
    </style>
    """
    # css適用
    st.markdown(result_css, unsafe_allow_html=True)

    if st.session_state["count"] == 2:
        # # 開始ボタンを完全に消す
        # playing_css = f"""
        # <style>
        # div.css-1n76uvr > div > div.css-1n76uvr > div.element-container > div.stButton > button.edgvbvh9 {{
        #     display:none;
        # }}
        # </style>
        # """
        # # css適用
        # st.markdown(playing_css, unsafe_allow_html=True)
        
        # # 再生用変数
        # playing = True
        # 画面遷移用ボタン
        end = st.button('終了する', on_click=show_result)
        stop_css = f"""
        <style>
        div.element-container > div.stButton > button {{
                text-align: center;
                width: 100px;
                height: 40px;
                position: relative;
                right: 302px;
                bottom: 78px;
                z-index: 61;
                # opacity:0;
                # animation-name: sample01; /*←@keyframesにも同じ名前を記述*/
                # animation-duration: 3s; 
                # animation-fill-mode: forwards;
                }}
        # @keyframes sample01 {{
        # 0% {{
        # opacity: 0;
        # color:#000;
        # }}
        # 100% {{
        # opacity: 1;
        # color:black;
        # }}
        # }}
        </style>
        """
        # css適用
        st.markdown(stop_css, unsafe_allow_html=True)
        # 値の受け渡し
    st.session_state['camera']='70'
    st.session_state['smile']='30'
    st.session_state['normal']='40'
    st.session_state['interviwer']='良'
    st.session_state['volume']='ちょうど良い'
    st.session_state['silence']='50'
    st.session_state['rank']='B'

def result_page():
    eye_track_json = glob.glob("./results/eye_track.json")
    with open('./results/eye_track.json') as f:
        eye_track = json.load(f)
        
    with open('./results/voice_analyze.json') as f:
        voice_analyze = json.load(f)

    i = random.randrange(1, 4)
    img_dict = {1:"https://images.unsplash.com/photo-1604488912264-dfed70450d76?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=922&q=80", 2:"https://images.unsplash.com/photo-1627199219038-e8263f729e3d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1031&q=80", 3:"https://images.unsplash.com/photo-1632144130358-6cfeed023e27?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80", 4:"https://images.unsplash.com/photo-1637855190680-5cbe1d870b46?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80"}

    # 質問割り当て
    question_dict = {1:"自己紹介をお願いします", 2:"志望動機は何ですか？", 3:"学生時代に頑張ったことはなんですか？", 4:"長所と短所を教えてください", 5:"将来のキャリア像について教えてください"}

    stc.html("""
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Yuji+Syuku&display=swap" rel="stylesheet">
        </head>
        <h1>分析結果</h1>
        <p>質問内容: """+ question_dict[st.session_state['question']] + """</p>
        <style>
        h1 {
            font-family: 'Yuji Syuku', serif;
            font-size: 60px;
            color: black;
        }
        h1, p {
            text-align: center;
            margin: 10px 0 0 0;
            }
        p {
            color: #5f6c7b;
        }
        </style>
        """, height=145
        )

    stc.html("""
    <div class='wrapper'>
        <div class='first'>
            <p>カメラ目線率<span class='camera_coma'>：</span><span class='point camera_span'>""" + str(round(eye_track['eye_center_ratio']*100)) + """</span>%</p>
            <p>無言の時間率<span class='mute_coma'>：</span><span class='point mute_span'>""" + str(round(voice_analyze['mic_off_ratio']*100)) + """</span>%</p>
        </div>
        <div class='second'>
            <p>笑顔率<span class='smile_coma'>：</span><span class='point smile_span'>""" + str(round(eye_track['eye_center_ratio']*100)) + """</span>%</p>
            <p>声量<span class='volume_coma'>：</span><span class='point volume_span'>""" + st.session_state['volume'] +  """</span></p>
        </div>
    </div>
    <div class='under_wrapper'>
        <p>面接官からの印象<span class='impression_coma'>：</span><span class='point impression_span'>""" + st.session_state['interviwer'] + """</span></p>
    </div>
    <div class="img_div">
        <img src=""" + img_dict[i]+ """>
    </div>
    <style>
    .wrapper {
        display: flex;
        flex-wrap: wrap;
    }
    .first {
        margin: 0 0 0 23%;
    }
    .second {
        margin: 0 0 0 4%;
    }
    .under_wrapper {
        text-align: center;
    }
    .point {
        font-size: 30px;
        color: #3da9fc;
        margin: 0 4px;
        }
    p {
        color:#5f6c7b;
        margin:5px 0;
    }
    .camera_coma {
        margin:0 0 0 0px;
    }
    .muite_coma {
        margin:0 0 0 31px;
    }
    .muite_coma {
        margin:0 0 0 16px;
    }
    img {
        width: 400px;
        height: auto;
    }
    .img_div {
        text-align: center;
        margin: 30px;
    }
    </style>
    """, height=450)

    st.button('他の質問で分析してみる', on_click=show_home)

    # css作成
    result_css = f"""
    <style>
    div.stButton {{
            text-align: center;
            margin: 0 0;
            color: #5f6c7b;
            }}

    .vsc-initialized {{
        margin: 0;
    }}
    /* ボタン色変更 */
    div.stButton > button:hover {{
        border-color: #90b4ce;
        color: #90b4ce;
        # border-color: #3da9fc;
        # color: #3da9fc;
    }}
    div.stButton > button:focus:not(:active) {{
        border-color: #90b4ce;
        color: #90b4ce;
    }}
    div.stButton > button.css-1cpxqw2:focus {{
        box-shadow: unset;
    }}
    div.stButton > button.css-1cpxqw2:focus {{
        border-color: #90b4ce;
        background-color: #90b4ce;
        color: #fffffe;
    }}
    /* ボタン色変更ここまで */
    </style>
    """
    # css適用
    st.markdown(result_css, unsafe_allow_html=True)


def show_home():
    # homeへ切り替え
    st.session_state["page_control"]=0

def question1():
    st.session_state["page_control"]=1
    st.session_state["question"]=1

def question2():
    st.session_state["page_control"]=2
    st.session_state["question"]=2

def question3():
    st.session_state["page_control"]=3
    st.session_state["question"]=3

def question4():
    st.session_state["page_control"]=4
    st.session_state["question"]=4

def question5():
    st.session_state["page_control"]=5
    st.session_state["question"]=5

def show_result():
    # resultへ切り替え
    st.session_state["page_control"]=6


if __name__ == '__main__':
    # 状態保持する変数を作成して確認
    if ("page_control" in st.session_state and
        0 < st.session_state["page_control"] < 6 ):
        record_page()
    elif ("page_control" in st.session_state and
        st.session_state["page_control"] == 6):
        result_page()
    else:
        main()