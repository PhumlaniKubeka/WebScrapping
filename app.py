import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

app = dash.Dash()

# Creating DATA

df = pd.read_csv('epl_stats.csv')
labels = df.team
app.layout = html.Div([dcc.Graph(id='scatterplot',
                    figure = {'data':[
                            go.Scatter(
                            x=df.team,
                            y=df.attendance,
                            mode='markers',
                            marker = {
                                'size':12,
                                'color': 'rgb(51,204,153)',
                                'symbol':'pentagon',
                                'line':{'width':2}
                            }
                            )],
                    'layout':go.Layout(title='Attendance of EPL Teams',
                                        yaxis = {'title':'Attendance'})}
                    ),

                    dcc.Graph(id='scatterplot2',
                    figure = {'data':[
                            go.Scatter(
                            x=df.team,
                            y=df.goal_diff,
                            mode='markers',
                            marker = {
                                'size':12,
                                'color': 'rgb(51,204,153)',
                                'symbol':'pentagon',
                                'line':{'width':2}
                            }
                            )],
                    'layout':go.Layout(title='Goal Difference',
                                        yaxis = {'title':'Goal Difference'})}
                    ),
        dcc.Graph(id='Bar',
                     figure = {'data':[
                            go.Bar(
                            x=df.team,
                            y=df.wins,
                            name='wins',
                            ),
                            go.Bar(
                            x=df.team,
                            y=df.wins,
                            name='losses',
                            ),
                            go.Bar(
                            x=df.team,
                            y=df.draws,
                            name='Draws',
                            )
                     
                            
                            ],
                    'layout':go.Layout(title='Wins,Losses & Draws per team',
                                        yaxis = {'title':'Stats'})}
                    ),
    
                    dcc.Graph(id='scatterplot3',
                                        figure = {'data':[
                                                go.Pie(
                                                values = df.wins,
                                                labels= df.team
                                                )],
                                        'layout':go.Layout(title='Wins percentage of Teams',
                                         yaxis = {'title':'Wins'})}
                                        )])
                   

if __name__ == '__main__':
    app.run_server(debug=True)