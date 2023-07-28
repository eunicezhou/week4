from flask import Flask,render_template,request,redirect
from flask import session
app = Flask(__name__,
            static_folder="static")

app.secret_key = "shishi"

@app.route("/")
def test():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    session["account"] = account
    session["password"] = password
    if session["account"] == "test" and session["password"] == "test":
        return redirect("/success")
    elif session["account"] == "" or session["password"] == "":
        return redirect("/fail")
    else:
         return redirect("/error")

@app.route("/success") 
def loadin():
    return render_template("success.html")

@app.route("/fail") 
def empty():
        return render_template("fail.html",error = "Please enter username and password")

@app.route("/error")
def error():
     return render_template("fail.html",error = "Username or password is not correct")

@app.route("/signout")
def signout():
     del session["account"]
     return redirect("/")

app.run(port = 3000)
