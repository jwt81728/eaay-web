from flask import Flask
app=Flask(__name__) # __name__ 代表目前執行的模組

@app.route("/") # 函式的裝飾 (Decorator) :以函式為基礎,提供附加的功能
def home():
    return "Hello 廢物! 今天吃什麼?!"
@app.route("/test")
def test():
    return "小威嫩嫩還在睡阿? 吃鍋貼好了!"
@app.route("/breakfast")
def breakfast():
    return "早餐店要嘛?"
@app.route("/drink")
def drink():
    return "要買飲料嗎?"
@app.route("/lay")
def lay():
    return "小威雷包!!"
@app.route("/shu")
def shu():
    return "             我是ㄎ一ㄤ妹, 劉緒緒!!!"

from flask import Response, Flask


@app.route("/pic")
def pic():
    with open("KtOrqGL.jpg", 'r') as image:
        resp = Response(image, mimetype="image/jpeg")
        return resp


if __name__=="__main__": # 如果以主程式執行
    app.run() # 立刻啟動伺服器