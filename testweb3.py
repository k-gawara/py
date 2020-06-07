import json
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    # mattermost -> bot へ送信される JSON データの取得
    post_dict = request.form

    # JSONから token と text (ユーザが入力したメッセージ) を取得
    token = post_dict['token']
    income_text = post_dict['text']

    # income_text は `bot_name COMMAND ARGUMENT` のような形式なので
    # 半角スペースで分割し、それぞれの要素を変数に格納する
    text_array = income_text.split(' ')
    bot_name = text_array[0]
    command = text_array[1]
    arg = " ".join(text_array[2:])

    payload_text = ""

    # command によって処理を分岐する
    if command == "echo":
        payload_text = echo(arg)
    elif command == "hoge":
        payload_text = hoge()
    elif command == "ping":
        payload_text = pong()
    elif command == "sushi":
        payload_text = sushi()

    # レスポンス用の JSON を組み立てる
    payload = {
        'username': bot_name,
        'icon_url': 'https://www.mattermost.org/wp-content/uploads/2016/04/icon.png',
        'text': payload_text,
        'MATTERMOST_TOKEN': token
    }
    json_payload = json.dumps(payload)

    return json_payload


# -------------------------------------------------------
# echo command
# -------------------------------------------------------
def echo(text):
    return text

# -------------------------------------------------------
# hoge command
# -------------------------------------------------------
def hoge():
    return "hoge"

# -------------------------------------------------------
# ping command
# -------------------------------------------------------
def pong():
    pong_msg = "pong :ping_pong:"
    return pong_msg

# -------------------------------------------------------
# sushi command
# -------------------------------------------------------
def sushi():
    return "（っ'-')╮ =͟͟͞͞ :sushi: ﾌﾞｫﾝ"

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port =5001)
