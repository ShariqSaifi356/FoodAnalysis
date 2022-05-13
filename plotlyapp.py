import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
import page2

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

search_bar = dbc.Row([
    dbc.Col(
        dbc.Button(
            "Home", color="dark", className="ms-2", n_clicks=0
        ), width="auto"
    ),
    dbc.Col(
        dbc.Button(
            "Dataset", color="dark", className="ms-2", n_clicks=0
        ), width="auto"
    ),
    dbc.Col(
        dbc.Button(
            "About", color="dark", className="ms-2", n_clicks=0
        ), width="auto"
    ),
    dbc.Col(
        dbc.Input(type="search", placeholder="Search")
    ),
    dbc.Col(
        dbc.Button(
            "Search", color="primary", className="ms-2", n_clicks=0
        ), width="auto"
    )
], className="g-0 ms-auto flex-nowrap mt-3 mt-md-0", align="center" )

navbar = dbc.Navbar([
    dbc.Container([
        html.A(
            dbc.Row([
                dbc.Col(
                    html.Img(
                        src=PLOTLY_LOGO, 
                        height="30px"
                    )
                ),
                dbc.Col(
                    dbc.NavbarBrand([
                        "Food Production Dashboard"
                    ], className="ms-2 dodgerblue")
                )
            ], align="center", className="g-0"),
            href="https://plotly.com", style={"textDecoration": "none"}),
        dbc.NavbarToggler(
            id="navbar-toggler", 
            n_clicks=0),
        dbc.Collapse(
            search_bar,
            id="navbar-collapse",
            is_open=False,
            navbar=True)
    ])
], color="dodgerblue", className="fixed-top")

card_img = dbc.Container([
    dbc.Card([
        dbc.CardImg(
            src="/static/images/ooter.jpg",
            top=True,
            style={"opacity": 0.2},
            className='shadow'
        ),
        dbc.CardImgOverlay(
            dbc.CardBody([
                html.H4("Feed All", className="title"),
                html.P([
                    "A Collective dashboard for food production"
                ], className="card-text1"),
                html.P([
                    "over the years"
                ], className="card-text1"),
            ])
        )
    ], className='shadow')
], className="pt-5")

cards = html.Div([
    html.Div([
        html.Div([
            dbc.Card([
                dbc.CardImg(
                    src="/static/images/analysis.jpg",
                    top=True,
                    style={"opacity": 0.4, "border":'rgb(245, 140, 101) solid 2px'},
                    className='shadow'
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody([
                        html.H4([
                            "Analysis"
                        ], className="font-medium card-title"),
                        html.B([
                            "Travel through various types of graphs and interpretations"
                        ], className="card-text"),
                    ]),
                )
            ]),
        ], className="col-4 mb-4" ),
                
        html.Div([
            dbc.Card([
                dbc.CardImg(
                    src="/static/images/info.png",
                    top=True,
                    style={"opacity": 0.4, "border":'rgb(27, 30, 205) solid 2px'},
                    className='shadow'
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody([
                        html.H4([
                            "Informative"
                        ], className="card-title"),
                        html.B([
                            "Discover past trends and predict the ones coming"
                        ], className="card-text"),
                    ]),
                )
            ]),
        ], className="col-4 mb-4" ),

        html.Div([
            dbc.Card([
                dbc.CardImg(
                    src="/static/images/access.jpg",
                    top=True,
                    style={"opacity": 0.4, "border":'rgb(97, 230, 230) solid 2px'},
                    className='shadow'
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody([
                        html.H4([
                            "Accessible"
                        ], className="card-title"),
                        html.B([
                            "Open for all - students, public, corporations, government"
                        ], className="card-text"),
                    ]),
                )
            ]),
        ], className="col-4 mb-4" )
    ], className="row"),
], className="container", style={"margin-top": "5rem"})

footer = html.Footer([
    html.Div([
        html.H5("Copyright")
    ], className="footer-copyright text-center pt-2 pb-1 shadow")],
    className="page-footer font-small blue down mt-5",
    style={"background-color": "white", "color": "dodgerblue"},
)

btn = html.Div([
    dbc.Button([
       "EXPLORE MORE"
], className = "bttn") 
], className="text-center")

card = html.Div([
    dbc.Col([
        dbc.Card([
            dbc.CardImg(
                src="/static/images/bar.jpg",
                top=True,
                className='shadow'
            ),
            dbc.CardBody(
                html.P([
                    "BAR CHARTS"
                ], className="text1")
            )
        ], style={"width": "18rem", "height": "18rem"})
    ], width="auto"),

    dbc.Col([
        dbc.Card([
            dbc.CardImg(
                src="/static/images/scatter2.png",
                top=True,
                className='shadow'
            ),
            dbc.CardBody(
                html.P([
                    "SCATTER CHARTS"
                ], className="text1")
            )
        ], style={"width": "18rem", "height": "18rem"})
    ], width="auto"),
], className='row')

card2 = dbc.Row([
    dbc.Col([
        dbc.Card([
            dbc.CardImg(
                src="/static/images/pie.png",
                top=True,
                className='shadow'
            ),
            dbc.CardBody(
                html.P([
                    "PIE CHART"
                ], className="text1")
            )
        ], style={"width": "18rem", "height": "18rem"})
    ], width="auto"),

    dbc.Col([
        dbc.Card([
            dbc.CardImg(
                src="/static/images/line.png",
                top=True,
                className='shadow'
            ),
            dbc.CardBody(
                html.P([
                    "LINE CHART"
                ], className="text1")
            )
        ], style={"width": "18rem", "height": "18rem"})
    ], width="auto")
], className='text-center')

app.layout = html.Div([
    navbar, 
    card_img, 
    cards, 
    html.Br(), 
    btn, 
    footer, 
    html.Br(), 
    card, 
    html.Br(), 
    card2
], className="pt-5")

@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
