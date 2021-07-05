from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    try:
        if request.method == 'GET':
            ret = request.args.get('query', '')
            return jsonify({'result': str(ret)})
        elif request.method == 'POST':
            return jsonify({'result': str(request.form['query'])})
        else:
            return abort(400)
    except Exception as e:
        return jsonify({'result':'error'})
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
