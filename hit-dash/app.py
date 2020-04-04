import pandas as pd
import plotly .graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

app=dash.Dash()

data=pd.read_csv('gapminder.csv')

year_options=[]

for i in data['year'].unique():
    year_options.append({'label':i,'value':i})


print(data.head())


app.layout=html.Div([
    dcc.Dropdown(id='dropdown',
                 options=year_options,
                 value=1952),
    dcc.Graph(id='scatter')
])

@app.callback(Output('scatter','figure'),[Input('dropdown','value')])
def update_graph(year):
    filter=data[data['year']==year]
    trace=[]

    for i in filter['continent'].unique():
        continent=filter[filter['continent']==i]
        trace.append(go.Scatter(x=continent['gdpPercap'],y=continent['lifeExp'],mode='markers',name=i,text=continent['country']))

    return {'data':trace,
            'layout':go.Layout(title='Scatter Plot')}


if __name__=='__main__':
        app.run_server()

