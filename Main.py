from flask import Flask, render_template, request

app: Flask = Flask(__name__)

@app.route("/", methods=['GET'])
def Index() -> str:
    return render_template('home.html')

@app.errorhandler(404)
def NotFound(e: Exception) -> tuple[str, int]:
    return render_template("notFound.html"), 404

@app.route("/404.html")
def NotFoundPage() -> str:
    return render_template("notFound.html")

if __name__ == "__main__":
    app.run()
