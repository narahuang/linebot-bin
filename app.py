# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from gfinance import get_company_name, get_company_summary

app = Flask(__name__)

handler = WebhookHandler('d0f949b59aab4a74f4b2fb460e3091c0') 
line_bot_api = LineBotApi('aMcIW96nybaqd7dJDM2Qfihat7kDeBrCa66hWY6dyMVyGJ1T3qyYaRRQ+b5DycEGKOgFQ+lT4F/48fQt06/ls4MPzp8342CSILFZYV1U7GPmtMk07Fo367SYf7r0c7W3wC4qcxW4MDvIK2mLAUcScwdB04t89/1O/w1cDnyilFU=') 


@app.route('/')
def index():
    return "<p>Hello World!</p>"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# ================= 機器人區塊 Start =================
@handler.add(MessageEvent, message=TextMessage)  # default


def handle_text_message(event):                  # default
    msg = event.message.text #message from user
# Add function switching for bot
# For now there is only Google Finance company info : gf
    commandlist = msg.split()
    jobname = commandlist[0]
    if jobname == 'gf':
        result = get_company_name(commandlist[1]) + '\n' + get_company_summary(commandlist[1])
    else:
        result = "gf 後面接股票代碼可以查詢 Google Finance 上面的公司資料唷！"

    # 針對使用者各種訊息的回覆 Start =========
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=result))

    # 針對使用者各種訊息的回覆 End =========

# ================= 機器人區塊 End =================

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
