import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

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
            id='recipe-dropdown',
            options=recipe_options,
            multi=True
        )
    ])
])

groceries = dbc.Card([
    dbc.CardBody([
        html.H3("Indkøbsliste", className="card-title"),
        html.P("Den generede indkøbsliste kan ses herunder.", className="card-text"),
        dbc.Table.from_dataframe(id='groceries-table', df=pd.DataFrame({'Type': ['N/A'], 'Antal': ['N/A'], 'Navn': ['N/A']}))
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



if __name__ == '__main__':
    app.run_server(debug=True)
