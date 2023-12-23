from flask import Flask
from src.logger import logging
from src.exception import CustmeException
import os,sys


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    try:
        raise Exception('This is our second method of logging')
    except Exception as e:
        abc = CustmeException(e ,sys)
        logging.info(abc.error_message)
        return "Welcom to the machine learning pipeline project"

if __name__ == "__main__":
    app.run(debug=True)