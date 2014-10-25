from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
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
	return render_template('whoami.html', leader=leader)

if __name__ == "__main__":
    app.run()