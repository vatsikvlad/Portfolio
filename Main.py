from flask import Flask, render_template, request
import MyBio

app: Flask = Flask(__name__)
myBio: MyBio.MyBio = MyBio.MyBio()

@app.route("/", methods=['GET'])
def Index() -> str:
    return render_template('home.html', myBio = myBio)

@app.errorhandler(404)
def NotFound(e: Exception) -> str:
    return render_template("notFound.html"), 404

if __name__ == "__main__":
    app.run()
