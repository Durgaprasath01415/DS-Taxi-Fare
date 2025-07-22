# 🚖 TripFare: Predicting Urban Taxi Fare with Machine Learning


### 📌 Overview

The TripFare project aims to predict the total fare for New York City taxi rides using machine learning models. The goal is to enhance fare transparency, help users estimate trip costs in real-time, and support ride-sharing and urban mobility systems with predictive analytics. We used a real-world dataset and built a complete pipeline — from data preprocessing to model deployment using Streamlit.


### 🧠 Problem Statement 

As a Data Analyst at an urban mobility analytics firm, your mission is to unlock insights from NYC taxi trip data to build a fare estimation system. 
This system helps:
  Users estimate fares before booking rides.
  Platforms offer price transparency.
  Cities understand urban travel trends.
  Tourists plan trip budgets more effectively.


### 🎯 Real-World Use Cases

🛺 Ride-Hailing Platforms – Live fare estimates before booking for better user trust.

🚖 Driver Incentive Systems – Help drivers know optimal locations and times for higher earnings.

🌆 Urban Mobility Analytics – Analyze trip trends for policy planning.

🧳 Travel Budgeting – Help travelers plan and predict estimated trip costs.

👥 Taxi Pooling & Sharing – Enable smarter dynamic pricing.


### 📂 Dataset

The dataset includes historical NYC taxi trip records with fields like pickup and dropoff timestamps, coordinates, passenger count, rate code, payment type, and fare components. 👉 Target variable: total_amount

| Column Name                                | Description |
-------------------------------------------- |--------------|
| VendorID                                   | Taxi vendor/provider ID |
| tpep_pickup_datetime 	                     | Trip start datetime |
| tpep_dropoff_datetime                      | Trip end datetime |
| passenger_count                            | Number of passengers |
| pickup_latitude/longitude                  | Pickup coordinates |
| dropoff_latitude/longitude                 | Dropoff coordinates |
| RatecodeID                                 | Type of rate applied (e.g., JFK, Newark, Standard) |
| payment_type                               | Type of payment (e.g., Card, Cash) |
| fare_amount, tip, taxes, tolls, surcharge	 | Fare components |
| total_amount 	                             | Final total amount paid (target variable) |


### 🛠️ Skills & Tools Used

Python, Pandas, NumPy

EDA & Visualization: Matplotlib, Seaborn

Preprocessing: Outlier Handling, Encoding, Transformation

Feature Engineering: Derived features like trip_distance, trip_duration, is_night, pickup_hour

Regression Models: Linear, Ridge, Lasso, Random Forest, Gradient Boosting

Model Deployment: Streamlit

Model Saving: Pickle


### 🔍 Workflow & Tasks

1️⃣ Data Understanding & Cleaning

Loaded and explored dataset using pandas

Checked data types, missing values, duplicates

2️⃣ Feature Engineering

trip_distance using Haversine Formula

trip_duration_minutes from pickup and dropoff datetime

pickup_hour, is_night, pickup_dayofweek extracted from timestamp

3️⃣ Exploratory Data Analysis

Distribution plots for fare, distance, duration

Correlation heatmap

Fare vs. distance, passenger count, time-of-day analysis

4️⃣ Data Transformation

Outlier removal (Z-score & IQR)

Skewness treatment

Categorical encoding (One-hot)

5️⃣ Model Building Built 5 regression models:

| Score | Linear Regression	| Ridge |	Lasso |	Random Forest Regressor |	✅GradientBoostingRegressor |
|-------|-------------------|-------|-------|-------------------------|---------------------------|
| MAE      | 1.123465 |	1.123471	| 1.376744	| 0.852733	| 0.831989 |
| MSE      | 4.098114 |	4.098297	| 5.747627	| 2.676619	| 2.325509 |
| RMSE     | 2.024380	| 2.024425	| 2.397421	| 1.636038	| 1.524962 |
| R2 Score | 0.926471	| 0.926468	| 0.896876	| 0.951976	| 0.958275 |

8️⃣ Model Deployment

Saved the best model (gb_model.pkl) using pickle

Built an interactive Streamlit app where users enter trip details

App predicts the estimated total fare


### 🚀 Streamlit App Demo User can input:

Trip distance (km)

Trip duration (minutes)

Is night ride?

Passenger count

Rate Code (one-hot encoded)

Payment Type

On submission, the app returns the predicted total fare instantly.
