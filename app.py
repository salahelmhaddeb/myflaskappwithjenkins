from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)

#@app.route('/')

@app.route("/")
def index():
    return render_template("index.html")

def hello():
    return 'Hello World!\n'

@app.route('/hello/<username>')
def hello_user(username):
    return 'Salut %s! :) \n' % username

@app.route("/contact")
def page_contact():
    return render_template("contact.html")

@app.route("/a-propos")
def page_a_propos():
    return render_template("a-propos.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
