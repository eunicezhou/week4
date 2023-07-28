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
    print(account,password)
    if account == "test" and password == "test":
        return redirect("/success")
    elif account == "" or password == "":
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

app.run(port = 3000)
