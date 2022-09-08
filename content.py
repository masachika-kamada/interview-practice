# import json
# import random


# title = """
#     <head>
#         <link rel="preconnect" href="https://fonts.googleapis.com">
#         <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
#         <link href="https://fonts.googleapis.com/css2?family=Yuji+Syuku&display=swap" rel="stylesheet">
#     </head>
#     <h1 class='title'>めんたつ</h1>
#     <h1 class='subtitle'>あなたの<span> ”オンライン面接力” </span>を測ってみよう。</h1>
#     <h2 class='subtitle'>-How much <span> ”Online-Interview-Skills” </span>do you have?-</h2>
#     <style>
#     .title {
#         text-align: center;
#         color: black;
#         margin: 0;
#         font-size: 70px;
#     }
#     .subtitle {
#         text-align: center;
#         color: #5f6c7b;
#     }
#     h1.subtitle {
#         font-size:30px;
#         margin: 10px 0 0 0;
#     }
#     h2.subtitle {
#         font-size:21px;
#     }
#     span {
#         color: #3da9fc;
#     }
#     .title {
#         font-family: 'Yuji Syuku', serif;
#     }
#     </style>
#     """

# loading_animation = """
#     <div class="loader">Loading...</div>
#     <style>
#     .loader,
#     .loader:before,
#     .loader:after {
#         background: #3da9fc;
#         -webkit-animation: load1 1s infinite ease-in-out;
#         animation: load1 1s infinite ease-in-out;
#         width: 1em;
#         height: 4em;
#     }
#     .loader {
#         color: #3da9fc;
#         text-indent: -9999em;
#         margin: 44px auto;
#         position: relative;
#         font-size: 22px;
#         -webkit-transform: translateZ(0);
#         -ms-transform: translateZ(0);
#         transform: translateZ(0);
#         -webkit-animation-delay: -0.16s;
#         animation-delay: -0.16s;
#     }
#     .loader:before,
#     .loader:after {
#         position: absolute;
#         top: 0;
#         content: '';
#     }
#     .loader:before {
#         left: -1.5em;
#         -webkit-animation-delay: -0.32s;
#         animation-delay: -0.32s;
#     }
#     .loader:after {
#         left: 1.5em;
#     }
#     @-webkit-keyframes load1 {
#         0%,
#         80%,
#         100% {
#             box-shadow: 0 0;
#             height: 4em;
#         }
#         40% {
#             box-shadow: 0 -2em;
#             height: 5em;
#         }
#     }
#     @keyframes load1 {
#         0%,
#         80%,
#         100% {
#             box-shadow: 0 0;
#             height: 4em;
#         }
#         40% {
#             box-shadow: 0 -2em;
#             height: 5em;
#         }
#     }
#     </style>
#     """

# def result_upper(idx):
#     questions = [
#         "自己紹介をお願いします",
#         "志望動機は何ですか？",
#         "学生時代に頑張ったことはなんですか？",
#         "長所と短所を教えてください",
#         "将来のキャリア像について教えてください"]

#     content = """
#         <head>
#             <link rel="preconnect" href="https://fonts.googleapis.com">
#             <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
#             <link href="https://fonts.googleapis.com/css2?family=Yuji+Syuku&display=swap" rel="stylesheet">
#         </head>
#         <h1>分析結果</h1>
#         <p>質問内容: """ + questions[idx] + """</p>
#         <style>
#         h1 {
#             font-family: 'Yuji Syuku', serif;
#             font-size: 60px;
#             color: black;
#         }
#         h1, p {
#             text-align: center;
#             margin: 10px 0 30px 0;
#         }
#         p {
#             color: #5f6c7b;
#         }
#         </style>
#         """
#     return content

# def result_lower():
#     with open('./results/eye_track.json') as f:
#         eye_track = json.load(f)

#     with open('./results/voice_analyze.json') as f:
#         voice_analyze = json.load(f)

#     randomi = random.randrange(0, 4)
#     img_paths = [
#         "https://user-images.githubusercontent.com/63488322/188748819-3b49bf32-a860-4864-b5e2-ce7db8f214fb.jpg",
#         "https://user-images.githubusercontent.com/63488322/188748809-06f71abc-31e9-4b93-92a2-e634d49e260d.jpg",
#         "https://user-images.githubusercontent.com/63488322/188748816-f25bed0c-8cb6-4772-9032-a8fce86168c8.jpg",
#         "https://user-images.githubusercontent.com/63488322/188748818-c5598617-1b19-4b91-b637-fd4883382cef.jpg"
#     ]

#     content = """
#     <div class='wrapper'>
#         <div class='first'>
#             <p>カメラ目線率<span class='camera_coma'>：</span><span class='point camera_span'>""" + str(round(eye_track['eye_center_ratio']*100)) + """</span>%</p>
#             <p>無言の時間率<span class='mute_coma'>：</span><span class='point mute_span'>""" + str(round(voice_analyze['mic_off_ratio']*100)) + """</span>%</p>
#         </div>
#         <div class='second'>
#             <p>笑顔率<span class='smile_coma'>：</span><span class='point smile_span'>""" + str(round(eye_track['face_smile_ratio']*100)) +  """</span>%</p>
#             <p>声量<span class='volume_coma'>：</span><span class='point volume_span'>""" + "volume" +  """</span></p>
#         </div>
#     </div>
#     <div class='under_wrapper'>
#         <p>面接官からの印象<span class='impression_coma'>：</span><span class='point impression_span'>""" + "calc_score" + """</span></p>
#     </div>
#     <div class="img_div">
#         <img src=""" + img_paths[randomi] + """>
#     </div>
#     <style>
#     .wrapper {
#         display: flex;
#         flex-wrap: wrap;
#     }
#     .first {
#         margin: 0 0 0 23%;
#     }
#     .second {
#         margin: 0 0 0 4%;
#     }
#     .under_wrapper {
#         text-align: center;
#     }
#     .point {
#         font-size: 30px;
#         color: #3da9fc;
#         margin: 0 4px;
#         }
#     p {
#         color:#5f6c7b;
#         margin:5px 0;
#     }
#     .camera_coma {
#         margin:0 0 0 0px;
#     }
#     .muite_coma {
#         margin:0 0 0 31px;
#     }
#     .muite_coma {
#         margin:0 0 0 16px;
#     }
#     img {
#         width: 400px;
#         height: auto;
#     }
#     .img_div {
#         text-align: center;
#         margin: 30px;
#     }
#     </style>
#     """
#     return content

# def calc_score(eye, smile, volume, mic_off):
#     score = eye + smile - mic_off
#     # 全部均一に換算してるが、優先順位とか考えてもいいかも
#     # volumeを計算式に追加する必要あり

#     if score >= 300:
#         return "good"
#     elif score >= 200:
#         return "normal"
#     elif score >= 100:
#         return "not good"
#     else:
#         return "Bad"
