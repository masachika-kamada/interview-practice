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
    }}
    </style>
    """
    # css適用
    st.markdown(result_css, unsafe_allow_html=True)
    
    st.session_state["question"]=0

    # st.markdown('# Interview-Practice')
    stc.html(
    "<h1 style='text-align: center; color: black; font-size:30px;'>あなたの<span style='color: blue;'>”オンライン面接基礎力”</span>を測ってみよう。</h1>"
    "<h2 style='text-align: center; color: black; font-size:21px;'>-How much <span style='color: blue;'>”Online-Interview-Basic-Skills”</span> do you have?</h2>"
    )


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
        time.sleep(2.5)
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
        # 画面遷移用ボタン
        end = st.button('終了する', on_click=show_result)
        stop_css = f"""
        <style>
        div.element-container > div.stButton > button {{
                text-align: center;
                width: 91px;
                height: 40px;
                position: relative;
                right: 308px;
                bottom: -483px;
                z-index: 61;
                animation: fadeIn 5s ease 5s 1 normal;
        }}
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
    }}
    .css-1dm0a9e {{
        margin: 0 0 0 240px;
    }}
    div.MuiBox-root.css-0 {{
            display: flex;
    }}
    </style>
    """
    # css適用
    st.markdown(result_css, unsafe_allow_html=True)

def result_page():
    eye_track_json = glob.glob("./results/eye_track.json")
    with open('./results/eye_track.json') as f:
        eye_track = json.load(f)
        
    with open('./results/voice_analyze.json') as f:
        voice_analyze = json.load(f)

    # css作成
    result_css = f"""
    <style>
    div.stButton {{
            text-align: center;
            margin: 30px 0;
    }}
    </style>
    """
    # css適用
    st.markdown(result_css, unsafe_allow_html=True)

    # 質問割り当て
    question_dict = {1:"自己紹介をお願いします", 2:"志望動機は何ですか？", 3:"学生時代に頑張ったことはなんですか？", 4:"長所と短所を教えてください", 5:"将来のキャリア像について教えてください"}

    # st.markdown('# 分析結果')
    # st.markdown('# 質問内容:' + question_dict[st.session_state["question"]])
    stc.html(
        "<h1 style='text-align: center; color: black;'>分析結果</h1>"
        "<p style='text-align: center; color: black;'>質問内容: "+ question_dict[st.session_state['question']] + "</p>"
        )
    col1, col2 = st.columns(2)

    # 録画表示
    with col1:
        stc.html("<iframe width=’560’ height=’315’ src='https://www.youtube.com/embed/3QPp_DlcZpM' title=’YouTube video player’ frameborder=’0’ allow=’accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture’ allowfullscreen></iframe>")

    # 値受け取り
    with col2:
        stc.html("""
        <p>カメラ目線：<span class='point'>""" + str(round(eye_track['eye_center_ratio']*100)) + """</span>%</p>
        <p>笑顔：<span class='point'>""" + st.session_state['smile'] + """</span>秒 / 普通<span class='point'>""" + st.session_state['normal'] + """</span>秒</p>
        <p>面接官からの印象：<span class='point'>""" + st.session_state['interviwer'] + """</span></p>
        <p>声の大きさ：<span class='point'>""" + st.session_state['volume'] +  """</span></p>
        <p>無言の時間率：<span class='point'>""" + str(round(voice_analyze['mic_off_ratio']*100)) + """</span>%</p>
        <p>面接基礎力ランク：<span class='point'>""" + st.session_state['rank'] + """</span></p>
        <style>
        .point {
            font-size: 30px;
            color: rgb(255, 75, 75);
            margin: 0 4px;
            }
        p {
            margin:5px 0;
        }
        </style>
        """, height=300)
        # st.markdown('カメラ目線：**' + str(round(eye_track['eye_center_ratio']*100)) + '**%')
        # st.markdown('笑顔：**' + st.session_state['smile'] + '**秒 / 普通**' + st.session_state['normal'] + '**秒')
        # st.markdown('面接官からの印象：**' + st.session_state['interviwer'] + '**')
        # st.markdown('声の大きさ：**' + st.session_state['volume'] + '**')
        # st.markdown('無言の時間率：**' + st.session_state['silence'] + '**')
        # st.markdown('面接基礎力ランク：**' + st.session_state['rank'] + '**')

    st.button('他の質問で分析してみる', on_click=show_home)


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