import subprocess
from flask import Flask
import json
app = Flask(__name__)

@app.route("/",methods=["POST"])
def hello():
	subprocess.call('/home/pi/work/mbot/mes.sh')
	return json.dumps(dict(text="hello"))
