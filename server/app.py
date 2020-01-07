from flask import Flask, jsonify, render_template
from flask_cors import CORS
import numpy as np

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping', methods=['GET'])
def ping_pong():
	return jsonify('pong!')


@app.route('/map', methods=['GET'])
def heatmap():
	x, y = np.linspace(-1,1,20).reshape(1,-1), np.linspace(-1,1,20).reshape(1,-1)
	hm = x.T @ y
	# test = ("\n".join([str(row) for row in hm]))
	return jsonify(list(map(list, hm)))

if __name__ == '__main__':
	app.run()