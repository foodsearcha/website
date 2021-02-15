from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('/index.html')


if __name__ == '__main__':
<<<<<<< HEAD
    app.run()
=======
    app.run(host="0.0.0.0", port="28080")
>>>>>>> 5e1762368e1f0bbd33472d47d6cbc0e58a79732c

