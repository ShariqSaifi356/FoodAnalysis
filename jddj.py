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