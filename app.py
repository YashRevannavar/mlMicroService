from flask import Flask, render_template, request
from algorithm import predict_fucn


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    data = []
    if request.method == "POST":
        label = predict_fucn()
        return render_template("index.html", label=label)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)