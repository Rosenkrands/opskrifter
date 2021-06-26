import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd

db = {}
for sheet_name in ['Retter', 'Ingredienser', 'Forbrug']:
    db[sheet_name] = pd.read_excel('recipes.xlsx', sheet_name=sheet_name)

recipe_options = []
for i in db['Retter'].index:
    option = {
        'label': db['Retter'].loc[i,'Navn'],
        'value': db['Retter'].loc[i,'ID']
    }
    recipe_options.append(option)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

recipes = dbc.Card([
    dbc.CardBody([
        html.H3("Opskrifter", className="card-title"),
        html.P("Vælg de opskrifter som du ønsker at generere indkøbslisten ud fra.", className="card-text"),
        dcc.Dropdown(
            id='recipes-dropdown',
            options=recipe_options,
            multi=True
        )
    ])
])

groceries = dbc.Card([
    dbc.CardBody([
        html.H3("Indkøbsliste", className="card-title"),
        html.P("Den generede indkøbsliste kan ses herunder.", className="card-text"),
        dbc.Table(id='groceries-table', children=[html.Thead(html.Tr([html.Th("Antal"), html.Th("Navn")]))], bordered=True)
    ])
])

app.layout = html.Div([
    # Header
    dbc.Col(html.H1("Madplanlægger", style={'text-align': 'center', 'padding-top': 20, 'padding-bottom': 20}), width={'size': 12}),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                recipes
            ], width={'size': '7'}),
            dbc.Col([
                groceries
            ], width={'size': '5'})
        ])
    ])
])

@app.callback(
    Output(component_id='groceries-table', component_property='children'),
    Input(component_id='recipes-dropdown', component_property='value')
)
def update_grocery_list(input_value):
    table_header = [
        html.Thead(html.Tr([html.Th("Antal"), html.Th("Ingrediens")]))
    ]
    if input_value is not None:
        grocieries1 = db['Forbrug'][db['Forbrug']['RetID'].isin(input_value)] \
            .groupby(['Ingrediens', 'Enhed'])['Antal'].sum().reset_index(drop=False)
        print(grocieries1)

        rows = []
        for i in grocieries1.index:
            rows.append(html.Tr([
                html.Td(str(grocieries1.loc[i,'Antal']) + ' ' + grocieries1.loc[i,'Enhed']),
                html.Td(grocieries1.loc[i,'Ingrediens'])
            ]))
        return table_header + [html.Tbody(rows)]
    return table_header

if __name__ == '__main__':
    app.run_server(debug=True)
