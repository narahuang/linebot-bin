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

handler = WebhookHandler('22df9152409a2adc584d29f9988ba6df') 
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

#def gf(query):
#    gf_company_name = get_company_name(query)
#    gf_company_summary = get_company_summary(query)
#    return gf_company_name + gf_company_summary

def handle_text_message(event):                  # default
    msg = event.message.text #message from user
    commandlist = msg.split()
    jobname = commandlist[0]
    result = commandlist[0] + commandlist[1]
    #if jobname == 'gf':
    #    result = gf(commandlist[1])
    #else:
    #    result = "gf 後面接股票代碼可以查詢 Google Finance 上面的公司資料唷！"

    # Google Finance 查詢公司名稱簡介
#    gf_company_name = get_company_name(msg)
#    gf_company_summary = get_company_summary(msg)
#    result = gf_company_name + gf_company_summary

    # 針對使用者各種訊息的回覆 Start =========
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=result))

    # 針對使用者各種訊息的回覆 End =========

# ================= 機器人區塊 End =================

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
