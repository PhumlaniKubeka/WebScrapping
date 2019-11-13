import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Launch the application:
app = dash.Dash()

# Create a DataFrame from the .csv file:
df = pd.read_csv('epl_stats.csv')

# Create a Dash layout that contains a Graph component:
app.layout = html.Div([
    dcc.Graph(
        id='number of wins',
        figure={
            'data': [
                go.Scatter(
                   x=df[df['team'] == i]['wins'],
                    y=df[df['team'] == i]['losses'],
                   fill='tonexty',
                    name=i,
                    mode = 'markers'
                )for i in df.team.unique()
            ],
            'layout': go.Layout(
                title = 'Number of wins',
                xaxis = {'title': 'Number of goals for'},
                yaxis = {'title': 'Number of goals against'},
                legend={'x': 0, 'y': -2},
                hovermode='closest'
            )
        }
    )
])

# Add the server clause:
if __name__ == '__main__':
    app.run_server(debug=True)