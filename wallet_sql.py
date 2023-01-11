from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:@ip:port/database name'
db = SQLAlchemy(app)

@app.route('/')
def index():
    sql = """
    CREATE TABLE card_table (
    id serial NOT NULL,
    user_id character varying(50) NOT NULL,
    card_name character varying(50) NOT NULL,
    PRIMARY KEY (id))
    """
    db.engine.execute(sql)
    return "Successfully create database！"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)