from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("hielo/index.html")


@app.route('/generic')
def generic():  # put application's code here
    return render_template("hielo/generic.html")


@app.route('/elements')
def elements():  # put application's code here
    return render_template("hielo/elements.html")

@app.route('/test')
def test():  # put application's code here
    return render_template("hielo/test.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, ebug=True)