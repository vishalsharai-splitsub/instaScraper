from flask import Flask

app = Flask(__name__)
import sys
import os

from thirdParty import instaloaderFunctions
import index


app.register_blueprint(index.profileAPI, url_prefix="/profiles")
app.register_blueprint(index.postAPI, url_prefix="/posts")

instaloaderFunctions.initializeInstaloder()


@app.route("/")
def index():
    return "Welcome To SecretX"


# Runs the flask app if this file is run
if __name__ == "__main__":
    app.run(threaded=True)
