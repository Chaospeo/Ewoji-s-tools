from flask import Flask,render_template,Response,request
from api.google import google_api

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/google",methods=['POST','GET'])
def google():
    data = request.form
    if(data!={}):
        output = google_api(data)
    else:
        output = "请填写关键字"
    return render_template('google.html',output=output)

if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=23333)