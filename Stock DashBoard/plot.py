import dash
from dash.dependencies import Input, Output
import dash_renderer as render
import dash_core_components as dcc
import dash_html_components as html
import plotly
import Datareader  as data

# stock = 'EURONEXT/FP'
# data.end = data.datetime.now()
# data.df = data.web.DataReader(stock, "quandl", data.start, data.end, api_key="bsFBSfJyyHzpcsZrjrBa")

app = dash.Dash()
app.layout = html.Div(children=[
    # html
    html.H1("Stocks Dash"),
    # # graph
    # dcc.Graph(
    #     id='example',
    #     figure={
    #         'data': [
    #             {'x': data.df.index, 'y': data.df.Last, 'type': 'line', 'name': stock},
    #         ],
    #         'layout': {
    #             'title': 'COVID-19 Deaths Statistics'
    #         }
    #     }
    # )

    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')
])


@app.callback(Output(component_id='output-graph', component_property='children'),
              [Input(component_id='input', component_property='value')])
def Update_graph(input_data):
    if input_data == '':
        input_data = 'AAPL'
    stock = input_data
    data.end_date = data.datetime.now()
    data.df2 = data.web.DataReader(stock, data_source='yahoo', start=data.start_date, end=data.end_date)

    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': data.df.index, 'y': data.df.Last, 'Close': 'line', 'name': stock},
            ],
            'layout': {
                'title': stock
            }
        }
    )
