from flask import Flask
app=Flask(__name__, static_url_path='/static',static_folder='./static') # __name__ 代表目前執行的模組

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



@app.route('/pic')
def images():
    outStr = """
    <link href="/static/mycss.css" rel="stylesheet" type="text/css">
    <div class="pic">
    嘿嘿嘿~~~
    </div>
    <img src="/static/KtOrqGL.jpg">
    """
    return outStr
from flask import render_template
@app.route("/ceb101")
def home():
    return render_template("ceb101.html")




if __name__=="__main__": # 如果以主程式執行
    app.run() # 立刻啟動伺服器