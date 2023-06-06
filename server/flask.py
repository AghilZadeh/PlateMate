from flask import Flask, request, jsonify
import json
from surprise import SVD, Reader, Dataset
import pandas as pd
from sqlalchemy import text, create_engine

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def predict():
	# read data from UI
	input_data = request.get_data()
	input_data = input_data.decode('UTF-8')
	input_data = json.loads(input_data)

	# connecting to server
	host='food.c6y5zgbdkiga.us-east-2.rds.amazonaws.com'
	port=int(5432)
	user='agheal'
	passw='5DTQazR9nxPtEmb'
	database='postgres'
	mydb = create_engine('postgresql+psycopg2://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)

	# read data from database
	with mydb.connect() as connection:
		query = text("SELECT * FROM reviews")
		reviews = pd.DataFrame(connection.execute(query).fetchall())

	# creating the model
	svd = SVD()
	reader = Reader(rating_scale=(1,5))
	# Loads Pandas dataframe
	data = Dataset.load_from_df(all_data, reader)

	prediction = model.predict(input_data)
	return jsonify(prediction)

@app.route("/", methods=['GET'])
def hello_word():
    return 'Hello, World!'


@app.route("/data", methods=['GET'])
def get_data():
    return 'Get data'

if __name__ == '__main__':
     app.run()