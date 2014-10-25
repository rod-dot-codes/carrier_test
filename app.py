from flask import Flask
from flask import render_template
from flask import make_response
import etcd
import os
app = Flask(__name__)

@app.route("/")
def hello():
    """ Maybe I didn't need so many str()'s after it, it tended to work out.
        Etcd host of 172.17.42.1 is docker0 or the docker bridge to the CoreOS machine.
    """
    client = etcd.Client(host='172.17.42.1',port=4001)
    node_id = os.environ.get('node_id')
    leader = None
    try:
        result = client.read('/carrier_test/leader')
        if str(result.value) == str(node_id):
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