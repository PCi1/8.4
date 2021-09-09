from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app=Flask(__name__)

@app.route("/mypage/me")
def mypage():
    return render_template("aboutme.html")

@app.route("/mypage/contact", methods=['GET', 'POST'])
def contact():
    if request.method=="GET":
        return render_template("kontakt.html")
    elif request.method=="POST":
        print(request.form)
        return redirect("/mypage/contact")