import pandas as pd
import numpy as np
from pmdarima import auto_arima
import gradio as gr

# Load the dataset
df = pd.read_csv('C:\\Users\\sam\\Desktop\\projects\\Hexathon Project\\src\\PScripts\\Country_Consumption_TWH.csv')
df = df.set_index('Year')

# Fill NaN values with the mean
df = df.fillna(df.mean())

countries = df.columns.tolist()

def predict_energy_consumption(country, years_into_future):
    stepwise_model = auto_arima(df[country], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',
                           suppress_warnings=True,
                           stepwise=True)

    # Forecast
    n_periods = years_into_future
    future_forecast, confint = stepwise_model.predict(n_periods=n_periods, return_conf_int=True)

    # The forecast is a pandas Series, we return the last value (i.e., the prediction for the last year)
    return float(future_forecast.iloc[-1])



iface = gr.Interface(fn=predict_energy_consumption,
                     inputs=[gr.inputs.Dropdown(choices=countries, label="Country"),
                             gr.inputs.Slider(minimum=1, maximum=100, step =1, label="Years into future")],
                     outputs="number",
                     title="Energy Consumption Prediction",
                     description="Predicts a country's energy consumption for a number of years into the future.")
iface.launch(share=True)