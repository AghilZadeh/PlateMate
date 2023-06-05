from flask import Flask, request, jsonify
import json
app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def predict():
	input_data = request.get_data()
	input_data = input_data.decode('UTF-8')
	input_data = json.loads(input_data)
	prediction = model.predict(input_data)
	return jsonify(prediction)

if __name__ == '__main__':
     app.run()