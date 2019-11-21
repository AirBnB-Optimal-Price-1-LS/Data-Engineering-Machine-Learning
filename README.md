
# Data Science Repo for AirBnB Optimal Price Predictor

The Data Science team for this project had two focuses, described below:<br>

## Data Engineering

Building and deploying a Flask API app to communicate price predictions to the back-end of the web app. Brainstorming with the back-end engineers, we settled on transmitting requests between their back-end server and our API via JSON object. This approach allowed our python-specific research and modeling to be ingested by their back-end servers and for us to unpack any requests coming through our API to be unpacked and read through our model using python.<br>

In addition to the repo, The API is also located [here](https://airbnb-prediction-api.herokuapp.com/)

## Machine Learning

Arriving at a machine learning technique that best suited the needs of the project. After thorough exploratory analysis, data wrangling and feature engineering, we developed preliminary models to use with sample data provided by back-end engineering. Constant communication with back-end engineers helped to narrow down which features were both necessary and expedient to include in model predictions. An important thing we kept in mind was that some data would have been unrealistic to have as fields that could be populated when someone was using the app (such as latitude and longitude of the property). Outliers were identified and removed, and our final model showed 28% improvement in its predictive power.<br>

Overall, our machine learning model achieved predictive accuracy of 90%.<br>

Our latest data analysis and machine learning methods can be found in this [notebook](https://github.com/AirBnB-Optimal-Price-1-LS/Data-Engineering-Machine-Learning/blob/master/Airbnb-price-estimation-28-feats.ipynb)
