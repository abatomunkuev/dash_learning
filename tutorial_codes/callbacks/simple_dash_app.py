import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Define the layout 
# Heading 6 
# Text Input with id 'my-input'
# Div with id 'my-output'
app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])

# Register a Callback function
# Inputs and Outputs - arguments of Callback function
# Whenever the input changes, the callback function gets automatically called
# component_id and component_property are optional arguments
@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
