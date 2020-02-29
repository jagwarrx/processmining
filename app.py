from flask import Flask, Response, request, url_for
from main import Alphaminer
from main import Hueristics
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route("/",methods=['POST'])
def hello():
    file = request.files['file']
    filename = secure_filename(file.filename)
    function = request.form['select']
    print(function, filename)
    if function=='Alphaminer':
        link = Alphaminer(filename)
        image = link.split('/')[-1]
    else:
        link = Hueristics(filename)
        image = link.split('/')[-1]
    file.save(filename)
    resp = Response(image)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    #print(type(resp), resp)
    return resp

# @app.route("/image/<filename>")
# def render(filename):


if __name__ == "__main__":
    app.run(port=8080)
