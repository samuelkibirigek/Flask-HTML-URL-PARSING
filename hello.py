from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1 style='text-align: center'>This is the home page</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjE" \
           "xNmFiOTRkODUwNjYxN2Q5MzQ4MTZjMjI2OTcyZGU5NTE4Y2RiZjI1YiZjdD1n/fpXxIjftmkk9y/giphy.gif' width=200>"


if __name__ == "__main__":
    app.run(debug=True)