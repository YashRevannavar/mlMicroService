from flask import Flask, render_template, request, url_for
from algorithm import predict_fucn


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Handles the home page of the web application.
    If the request method is POST, gets data from the form and passes it to 
    the prediction function, and then returns the rendered template with the predicted label.
    Otherwise, returns the rendered template of the home page.

    Returns:
    -------
    rendered template: str
    A string representing the rendered template of the home page.
    """
    if request.method == "POST":
        label = predict_fucn()
        return render_template("index.html", label=label)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
