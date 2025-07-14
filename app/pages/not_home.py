import dash
import dash_bootstrap_components as dbc  # Importa Dash Bootstrap Components
from dash import html, dcc, callback, Input, Output
from app import anios_nh
dash.register_page(
    __name__,
    path='/Indicadores_de_Calidad_del_Agua',
    title='Indicadores de Calidad del Agua',
    name='Otro nombre'
)

map_icon_I = html.I(id="map_icon", className="bi bi-map", style={'margin': '0', 'paddin': '0'})
botton_map_I= dbc.Button(
    [map_icon_I],
    id="navigate-button2",
    color="primary",
    n_clicks=0,
    size="sm",
    outline=True,
    className="button-custom-map",
    style={'width': '70%', 'height': '6vh', 'margin': '1vh 10% 1vh 10%'}
)

tooltip_map_I = dbc.Tooltip(
    "Abre el mapa de Acciones de desinfección en una nueva ventana",  # Texto que se muestra
    target="navigate-button2",   # Debe coincidir con el id del botón
    placement="top"           
)

slider_periodo_nh = dcc.Slider(
    id="slider_periodo_nh",
    step=None,
    marks=anios_nh,
    value=list(anios_nh.keys())[-1],
    className="slider-custom-R"
)
encabezado_nh =  dbc.Row([
        dbc.Col(
            html.H2("Indicadores de Calidad del Agua", style={'color': 'white', 'margin':'0', 'padding': '2vh 0 0 10px'}), # paddin arriba, derecha abajo izquierda
            width = 6,
            xxl = 6, xl = 6, lg = 6, md = 6, sm = 12,  xs = 12, 
            style = {'backgroundColor': '#9C2448', 'padding': '0','margin':'0'} 
        ),
        dbc.Col(
            #html.H2("Barra", style={'color': 'white', 'margin':'0', 'padding': '0'}),
            html.A(
                html.Img(src="./assets/Imagenes/Planeacion_dorado.png", style={'width': '100%', 'height': '70%', 'padding': '1vh 0 0 10px'}),
                href = "https://sigeh.hidalgo.gob.mx/", 
                target= "_blank"
            ),
            width = 3,
            xxl = 3, xl = 3, lg = 3, md = 3, sm = 6,  xs = 6, 
            style = {'backgroundColor': '#9C2448', 'padding': '0', 'margin':'0'}
        ),
        dbc.Col(
            html.A(
                html.Img(src="./assets/Imagenes/CEAA_dorado.png", style={'width': '75%', 'height': '75%', 'padding': '1vh 0 0 10px'}),
                href = "https://ceaa.hidalgo.gob.mx/",
                target= "_blank" 
            ),
            width = 2,
            xxl = 2, xl = 2, lg = 2, md = 2, sm = 5,  xs = 5, 
            style = {'backgroundColor': '#9C2448', 'padding': '0', 'margin':'0'}
        ),
        dbc.Col(
            children= [botton_map_I,tooltip_map_I,
                       html.P("Explora otro mapa", style={'color': 'white', 'margin': '0', 'padding': '0vh 0 0vh 10%', 'fontSize': '11px'})],
            width = 1,
            xxl = 1, xl = 1, lg = 1, md = 1, sm = 1,  xs = 1, 
            style = {'backgroundColor': '#9C2448', 'padding': '0', 'margin':'0'}
        )
    ], 
    style={"height": "12vh", 'width': '100vw' , 'padding':'0', 'margin':'0'}
    )


enmedio_nh = dbc.Row([
    dbc.Col(
        children= slider_periodo_nh,
        width = 12,
        xxl = 12, xl = 12, lg = 12, md = 12, sm = 12,  xs = 12, 
        style = {'backgroundColor': '#BC955B', 'padding': '0','margin':'0'} 
    )
],
    style={"height": "8vh", 'width': '100vw' , 'padding':'0', 'margin':'0'}
)
mapa_nh = dbc.Row(
    dbc.Col(
        html.Iframe(src= "", 
                    id="mapa_nh",
                    style={'width': '100vw', 'height': '79vh', 'border': '0', 'padding': '0', 'margin': '0'}),
        width = 12,
        xxl = 12, xl = 12, lg = 12, md = 12, sm = 12,  xs = 12, 
        style = {'backgroundColor': '#9C2448', 'padding': '0','margin':'0'} 
    ),
    style={"height": "80vh", 'width': '100vw' , 'padding':'0', 'margin':'0'}
)



layout = html.Div([
    dcc.Location(id='url2', refresh=True),
    encabezado_nh,
    enmedio_nh,
    mapa_nh,
]
)
