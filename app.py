# import pandas as pd
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True)

recipes = dbc.Card([
    dbc.CardBody([
        html.H3("Opskrifter", className="card-title"),
        html.P("...", className="card-text")
    ])
])

groceries = dbc.Card([
    dbc.CardBody([
        html.H3("Indkøbsliste", className="card-title"),
        html.P("...", className="card-text")
    ])
])

app.layout = html.Div([
    # Header
    dbc.Col(html.H1("Madplanlægger", style={'text-align': 'center', 'padding-top': 20, 'padding-bottom': 20}), width={'size': 12}),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                recipes
            ], width={'size': '8'}),
            dbc.Col([
                groceries
            ], width={'size': '4'})
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)