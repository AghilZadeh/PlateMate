import os
from sqlalchemy import create_engine, text
import pandas as pd
import sqlalchemy as sa

# connecting to server
host = os.environ.get('AWS_RDS_HOST')
port = int(5432)
user = os.environ.get('AWS_RDS_USERNAME')
passw = os.environ.get('AWS_RDS_PASSWORD')
database = 'postgres'
engine = create_engine('postgresql+psycopg2://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)

# dumping data into server
#reviews_train = pd.read_csv('../data/reviews_train.csv', usecols=['RecipeId', 'AuthorId', 'Rating'])
#reviews_train.to_sql(name='reviews', con=mydb, if_exists = 'replace', index=False)

# reading files from database
with engine.connect() as con:
    query = text("SELECT * FROM reviews LIMIT 10")
    reviews = con.execute(query)

print(reviews.fetchall())