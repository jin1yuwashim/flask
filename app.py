from flask import Flask
app =    Flask(__name__)


@app.route("/")
def home():
    return 'hello 你好嗎~ 衷心感謝'

@app.route("/test")
def test():
    return 'test123'

if __name__ =='__main__':
    app.run()