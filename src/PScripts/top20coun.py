import pandas as pd
import gradio as gr

# Load data from a CSV file
data = pd.read_csv('C:\\Users\\sam\\Desktop\\projects\\Hexathon Project\\src\\PScripts\\top20CountriesPowerGeneration.csv')

# Create a function to calculate the most used renewable resource and the amount of energy generated
def calculate_energy(country):
    # Filter data by the selected country
    country_data = data[data['Country'] == country]

    # Find the maximum value of the renewable energy sources and the corresponding column name
    max_renewable = country_data[['Hydro', 'Biofuel', 'Solar', 'Geothermal']].max().idxmax()

    # Calculate the total energy generated using renewable resources
    total_energy = country_data['Total'].sum()

    # Calculate the energy generated using the most used renewable resource
    energy_generated = country_data[max_renewable].sum()

    # Return the results
    return f"The most used renewable resource in {country} is {max_renewable} with {energy_generated:.2f} GWh out of a total of {total_energy:.2f} GWh generated."

# Create a Gradio interface
inputs = gr.inputs.Dropdown(choices=data['Country'].unique().tolist(), label="Select a country")
output = gr.outputs.Textbox()
gr.Interface(fn=calculate_energy, inputs=inputs, outputs=output, title="Renewable Energy Dashboard").launch(share=True)