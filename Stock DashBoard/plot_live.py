import dash
from dash.dependencies import Output, Event
import dash_renderer as render
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objects as go
import random
from collections import deque  # container with size as list

X = deque(maxlen=20)
Y = deque(maxlen=20)
X.append(1)
Y.append(1)

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(id='graph-update', interval=1000)
    ]
)


@app.callback(Output('live-graph', 'figure'),
              events=[Event('graph-update', 'interval')])
def Update_graph():
    global X
    global Y
    X.append(X[-1] + 1)
    Y.append(Y[-1] + (Y[-1] * random.uniform(-0.1, 0.1)))

    data = go.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )

    return {'data': [data], 'layout': go.Layout(xaxis=list(range=[min(Y), max(Y)]),
                                                yaxis=list(range=[min(Y), max(Y)]))}
