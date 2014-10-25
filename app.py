from flask import Flask
from flask import render_template
from flask import make_response
import etcd
import os
app = Flask(__name__)

@app.route("/")
def hello():
    client = etcd.Client(host='172.17.42.1',port=4001)
    node_id = os.environ.get('node_id')
    leader = None
    try:
        result = client.read('/carrier_test/leader')
        if result.value == node_id:
            leader = "ME"
        else:
            leader = result.value
    except:
        pass
    response = make_response(render_template('whoami.html', leader=leader))
    response.headers['proudly-served-by'] = str(node_id)
    return response

if __name__ == "__main__":
    app.run()