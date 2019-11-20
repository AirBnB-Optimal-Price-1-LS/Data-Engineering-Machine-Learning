"""
App factory to create AirBnB price prediction API

__author__ = Patrick Dugovich, Xander Bennett, Andrew Archie, Luke Townsend
__license__ = MIT License
__version__ = 1.0

"""
from .data_cleaning import wrangle
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import pickle


def create_app():
    # app
    app = Flask(__name__)
    # CORS to try to prevent errors with web end
    CORS(app)
    # Loading model extracted from notebook
    model = pickle.load(open('model.pkl', 'rb'))
    parameters = [
        'neighbourhood_group_cleansed', 'bathrooms', 'bedrooms',
        'beds', 'bed_type', 'amenities', 'room_type', 'cleaning_fee',
        'security_deposit', 'minimum_nights'
    ]
    # routes
    @app.route('/', methods=['GET'])
    def predict():
        try:
            request_data = {}
            for param in parameters:
                request_data.update(param=request.args.get(param))
            print('request_data:', request_data)

            # Turning data into pandas DataFrame for use in model
            #request_data.update((x, [y]) for x, y in request_data.items())
            data_df = pd.DataFrame.from_dict(request_data)
            print('data_df:', data_df)

            # Adding individual columns for each amenity
            data_df = wrangle(data_df)

            # Make prediction based on created dataframe of user input data
            result = model.predict(data_df)

            # Creating dict to convert to json and return
            output = int(result[0])

            return jsonify(estimated_price=output)

        except Exception as e:
            return jsonify({'Error': e})
    return app
