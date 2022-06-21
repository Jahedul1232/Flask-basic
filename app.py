from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")      #Decorator
def hello_world():
    return 'hello world'  #render_template('index.html')

@app.route("/admin")
def hello_admin():
    return 'hello admin'


@app.route("/guests/<guest>")
def hello_guest(guest):
    return 'hello %s as a guest'%guest

@app.route("/user/<name>")
def hello_user(name):
    if name =='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))



if __name__ == '__main__':
    app.run(debug=True)

