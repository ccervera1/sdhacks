from flask import Flask, render_template, request

app = Flask(__name__, static_url_path="")



@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("homeFlask.html")



@app.route("/home", methods=['POST'])
def home_post():
    # text = request.form['text']
    processed_text = 'hello'
    # test_input(text)
    return processed_text


if __name__ == "__main__":
    app.run(debug=True)
