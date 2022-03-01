import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

titanic = pd.read_csv('./data/train.csv')

app = Dash(__name__)


isnull_heatmap = px.imshow(titanic.isnull(), aspect='16:9')

app.layout = html.Div(
  children=[
    html.H1(children='Exploratory Data Analysis'),
    
    html.Div(children='''
      Dash - abc
    '''),

    dcc.Graph(
      id='graph1',
      figure=isnull_heatmap
    )
  ]
)

if __name__ == '__main__':
  app.run_server(debug=True)
