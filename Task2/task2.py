from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__,
            static_folder="static")

@app.route("/")
def test():
    return render_template("index.html")
@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    if account == "test" and password == "test":
        return redirect("/success")
    elif account == "" or password == "":
        message_info = "empty"
        return redirect(url_for("error",message=message_info))
    else:
        message_info = "error"
        return redirect(url_for("error",message=message_info))
@app.route("/success") 
def loadin():
    return render_template("success.html")

@app.route("/error")
def error():
     data_receive = request.args.get("message")
     if data_receive == "empty":
         return render_template("fail.html",error = "Please enter username and password")
     else:
        return render_template("fail.html",error = "Username or password is not correct")

app.run(port = 3000)
