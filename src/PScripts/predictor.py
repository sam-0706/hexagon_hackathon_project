import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import gradio as gr

# Load the dataset
df = pd.read_csv("C://Users//sam//Downloads//re-generation-from-jan-2(NR).csv")

# Define the features and target variable
X = df[['Region', 'Month', 'Year']]
y = df['RE Generation Total']

# Map the categorical variables to numerical values
region_map = {'NR': 13,'SR':14,"ER":15,"WR":16,"NER":17}
month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
X['Region'] = X['Region'].map(region_map)
X['Month'] = X['Month'].map(month_map)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest regression model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Fit the model with the training data
model.fit(X_train, y_train)

# Define a function to predict the renewable energy generation total for a new set of attributes
def predict_re_gen(region, month, year):
    new_data = pd.DataFrame({'Region': [region], 'Month': [month], 'Year': [year]})
    new_data['Region'] = new_data['Region'].map(region_map)
    new_data['Month'] = new_data['Month'].map(month_map)
    prediction = model.predict(new_data)
    return prediction[0]

# Define the input and output interfaces using Gradio
inputs = [
    gr.inputs.Dropdown(choices=list(region_map.keys()), label="Region"),
    gr.inputs.Dropdown(choices=list(month_map.keys()), label="Month"),
    gr.inputs.Number(label="Year")
]
output = gr.outputs.Textbox(label="Predicted renewable energy generation total")

# Launch the web interface using Gradio
title = "Renewable Energy Generation Prediction"
description = "Enter the region, month, and year to predict the renewable energy generation total"
gr.Interface(predict_re_gen, inputs, output, title=title, description=description).launch()
