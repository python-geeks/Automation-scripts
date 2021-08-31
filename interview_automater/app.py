# The code uses dash library in Python for rendering the web-app.
# More information can be found at https://dash.plotly.com/
# Importing required libraries
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import webbrowser


# Initialisation
app = dash.Dash(__name__)
server = app.server


# Defining global variables
global name, score
score = 0


# Setting layout
app.layout = html.Div(
    style={'textAlign': "center", "marginLeft": "50px", "marginRight": "50px"},
    children=[
        html.H1(
            style={'color': "#1876D2", 'fontWeight': "bolder",
                   "marginBottom": "50px", 'fontSize': "50px"},
            children='Test your personality 😁'),
        html.H3('May I know your name?'),
        dcc.Input(id='name', type='text',
                  style={"height": "30px", "borderRadius": "20px",
                         "textIndent": "10px", "fontSize": "20px"}),
        html.Button('Submit',
                    style={'backgroundColor': "#1876D2", "border": "none",
                           "marginLeft": "10px", "outline": "none",
                           'fontWeight': "bolder", "padding": "10px",
                           "borderRadius": "20px", 'color': "white"},
                    id='submit', n_clicks=0),
        html.Div(id='init'),
        html.Div(id='q1'),
        html.Div(id='q2'),
        html.Div(id='q3'),
        html.Div(id='q4'),
        html.Div(id='q5'),
        html.Div(id='q6'),
        html.Div(id='q7'),
        html.Div(id='q8'),
        html.Div(id='q9'),
        html.Div(id='q10'),
        html.Div(id='result')
    ]
)


# Using callbacks to handle questions and answers,
# along with keeping a track of score
@app.callback(
    Output('init', 'children'),
    [Input('name', 'value'), Input('submit', 'n_clicks')]
)
def update_name(name, n_clicks):
    if n_clicks == 0:
        raise PreventUpdate
    else:
        return [html.Br(),
                html.H3(
                    style={'color': "#1876D2"}, children='''You like to spend
                    your free time exploring something new or do you follow
                    same routine'''),
                dcc.RadioItems(
                    id='a2', options=[{'label': 'New 💯',
                                       'value': 'new'},
                                      {'label': 'Same as always',
                                       'value': 'same'}],
                    value=None)]


@app.callback(
    Output('q1', 'children'),
    [Input('a1', 'value')]
)
def q1(a1):
    global score
    if a1 is None:
        raise PreventUpdate
    else:
        if a1 == 'yes':
            score = score + 1
        elif a1 == 'maybe':
            score = score + 0.5
        return [html.Br(),
                html.H3(
                    style={'color': "#1876D2"}, children='''You like to spend
                    your free time exploring something new or do you follow
                    same routine'''),
                dcc.RadioItems(
                    id='a2', options=[{'label': 'New 💯',
                                       'value': 'new'},
                                      {'label': 'Same as always',
                                       'value': 'same'}],
                    value=None)]


@app.callback(
    Output('q2', 'children'),
    [Input('a2', 'value')]
)
def q2(a2):
    global score
    if a2 is None:
        raise PreventUpdate
    else:
        if a2 == 'new':
            score = score + 1
        return [html.Br(),
                html.H3(
                    style={'color': "#1876D2"}, children=''''How comfortable
                    are you while talking to new people?'''),
                dcc.Slider(
                    id='a3',
                    min=0,
                    max=10,
                    marks={
                        0: 'Not at all',
                        10: 'Absolutely comfortable'
                    },
                    step=1,
                    value=None
        )]


@app.callback(
    Output('q3', 'children'),
    [Input('a3', 'value')]
)
def q3(a3):
    global score
    if a3 is None:
        raise PreventUpdate
    else:
        if a3 == 1:
            score = score + 0.1
        elif a3 == 2:
            score = score + 0.2
        elif a3 == 3:
            score = score + 0.3
        elif a3 == 4:
            score = score + 0.4
        elif a3 == 5:
            score = score + 0.5
        elif a3 == 6:
            score = score + 0.6
        elif a3 == 7:
            score = score + 0.7
        elif a3 == 8:
            score = score + 0.8
        elif a3 == 9:
            score = score + 0.9
        elif a3 == 10:
            score = score + 1
        return [html.Br(),
                html.H3(
                    style={'color': "#1876D2"}, children='''What do you prefer-
                    hard work or smart work?'''),
                dcc.RadioItems(
                    id='a4',
                    options=[{'label': 'Hard work', 'value': 'hard'},
                             {'label': 'Smart work', 'value': 'smart'},
                             {'label': 'It depends on the situation',
                              'value': 'both'}],
                    value=None)]


@app.callback(
    Output('q4', 'children'),
    [Input('a4', 'value')]
)
def q4(a4):
    global score
    if a4 is None:
        raise PreventUpdate
    else:
        if a4 == 'hard':
            score = score + 0.5
        elif a4 == 'smart':
            score = score + 0.5
        elif a4 == 'both':
            score = score + 1
        return [html.Br(),
                html.H3(
                    style={'color': "#1876D2"}, children='''You and your peer
                    are working together. He/she is stuck in a task.
                    Will you?'''),
                dcc.RadioItems(
                    id='a5',
                    options=[{'label': 'Help them instantly',
                              'value': 'fast'},
                             {'label': '''Help after completing your current
                              work''',
                              'value': 'curr'},
                             {'label': '''Help after
                              completing all your work''',
                              'value': 'no'}],
                    value=None)]


@app.callback(
    Output('q5', 'children'),
    [Input('a5', 'value')]
)
def q5(a5):
    global score
    if a5 is None:
        raise PreventUpdate
    else:
        if a5 == 'fast':
            score = score + 0.5
        elif a5 == 'curr':
            score = score + 1
        return [html.Br(),
                html.H3(
                    style={'color': "#1876D2"}, children='''Which category do
                    you fit in?'''),
                dcc.RadioItems(
                    id='a6',
                    options=[{'label': 'Extrovert', 'value': 'ex'},
                             {'label': 'Introvert', 'value': 'in'},
                             {'label': 'Ambivert', 'value': 'am'}],
                    value=None)]


@app.callback(
    Output('q6', 'children'),
    [Input('a6', 'value')]
)
def q6(a6):
    global score
    if a6 is None:
        raise PreventUpdate
    else:
        if a6 == 'ex':
            score = score + 1
        elif a6 == 'am':
            score = score + 0.5
        return [html.Br(),
                html.H3(
                    style={'color': "#1876D2"}, children='''Are you willing to
                    work overtime if required?'''),
                dcc.RadioItems(
                    id='a7',
                    options=[{'label': 'Yes I would be happy',
                              'value': 'happy'},
                             {'label': 'Yes, if I get paid accordingly',
                              'value': 'pay'},
                             {'label': 'No, I am not comfortable doing this',
                              'value': 'no'}],
                    value=None)]


@app.callback(
    Output('q7', 'children'),
    [Input('a7', 'value')]
)
def q7(a7):
    global score
    if a7 is None:
        raise PreventUpdate
    else:
        if a7 == 'happy':
            score = score + 1
        elif a7 == 'no':
            score = score + 0.5
        return [html.Br(),
                html.H3(
                    style={'color': "#1876D2"}, children='''How comfortable
                    will you be if we ask you to travel for work?'''),
                dcc.RadioItems(
                    id='a8',
                    options=[{'label': 'No problem, I\'m ready',
                              'value': 'ready'},
                             {'label': 'Only if my safety is taken care of',
                              'value': 'safe'},
                             {'label': 'No, it is tiring for me',
                              'value': 'no'}],
                    value=None)]


@app.callback(
    Output('q8', 'children'),
    [Input('a8', 'value')]
)
def q8(a8):
    global score
    if a8 is None:
        raise PreventUpdate
    else:
        if a8 == 'ready':
            score = score + 1
        elif a8 == 'safe':
            score = score + 1
        elif a8 == 'no':
            score = score + 0.5
        return [html.Br(),
                html.H3(
                    style={'color': "#1876D2"}, children='''What is the salary
                    range you expect as a fresher?'''),
                dcc.RadioItems(
                    id='a9',
                    options=[{'label': '<= 4 lpa',
                              'value': 'less'},
                             {'label': '> 4 lpa till < 90 lpa',
                              'value': 'more'},
                             {'label': 'Best according to my talent',
                              'value': 'mid'}],
                    value=None)]


@app.callback(
    Output('q9', 'children'),
    [Input('a9', 'value')]
)
def q9(a9):
    global score
    if a9 is None:
        raise PreventUpdate
    else:
        if a9 == 'more':
            score = score + 1
        elif a9 == 'mid':
            score = score + 1
        elif a9 == 'less':
            score = score + 0.5
        return [html.Br(),
                html.H3(
                    style={'color': "#1876D2"}, children='''How likely will
                    you reveal the company policies to an outsider, either
                    knowingly or unknowingly?'''),
                dcc.Slider(
                    id='a10',
                    min=1,
                    max=5,
                    marks={
                        1: 'Very unlikely',
                        2: 'Somewhat unlikely',
                        3: 'I don\'t know',
                        4: 'somewhat likely',
                        5: 'Very likely'
                    },
                    step=1,
                    value=None
        )]


@app.callback(
    Output('q10', 'children'),
    [Input('a10', 'value')]
)
def q10(a10):
    global score
    if a10 is None:
        raise PreventUpdate
    else:
        if a10 == 1:
            score = score + 1
        elif a10 == 2:
            score = score + 0.5
        elif a10 == 3:
            score = score + 0.5
        elif a10 == 4:
            score = score - 0.5
        elif a10 == 5:
            score = score - 1
        return [html.Br(), html.H3('Any feedback you want to provide?'),
                dcc.Input(id='res', type='text',
                          style={"height": "30px", "borderRadius": "20px",
                                 "textIndent": "10px", "fontSize": "20px"}),
                html.Button('Submit', id='feedback', n_clicks=0,
                            style={'backgroundColor': "#1876D2",
                                   "border": "none",
                                   "marginLeft": "10px",
                                   "outline": "none",
                                   'fontWeight': "bolder",
                                   "padding": "10px",
                                   "borderRadius": "20px",
                                   'color': "white"})
                ]


# Displaying result according to score
@app.callback(
    Output('result', 'children'),
    [Input('feedback', 'n_clicks')]
)
def result(n_clicks):
    if n_clicks == 0:
        raise PreventUpdate
    else:
        if score == 0:
            return [html.Br(),
                    html.H3("Score: " + str(score) + '''/10 --> I am sorry.
                            You are a poor fit.''',
                            style={"fontSize": "25px", "color": "#1876D2"}),
                    html.H3("😔"),
                    html.H3('Thanks for your time!')]
        elif score < 5:
            return [html.Br(),
                    html.H3("Score: " + str(score) + '''/10 --> You need to work
                            more upon your personality.''',
                            style={"fontSize": "25px", "color": "#1876D2"}),
                    html.H3("🙂"),
                    html.H3('Thanks for your time!')]
        elif score == 5:
            return [html.Br(),
                    html.H3("Score: " + str(score) + '''/10 --> You are average.
                            You can always improve.''',
                            style={"fontSize": "25px", "color": "#1876D2"}),
                    html.H3("😃"),
                    html.H3('Thanks for your time!')]
        elif score > 5 and score < 8.5:
            return [html.Br(),
                    html.H3("Score: " + str(score) + '''/10 --> You are a decent
                            fit for the company. Remember, practise makes a
                            man perfect!''',
                            style={"fontSize": "25px", "color": "#1876D2"}),
                    html.H3("💯💯"),
                    html.H3('Thanks for your time!')]
        elif score >= 8.5 and score <= 10:
            return [html.Br(),
                    html.H3("Score: " + str(score) + '''/10 --> Excellent🎉 We
                            are proud to have you in the workforce.
                            Congratulations!!''',
                            style={"fontSize": "25px", "color": "#1876D2"}),
                    html.H3("🔥🔥"),
                    html.H3('Thanks for your time!')]


def web():
    webbrowser.open_new('http://127.0.0.1:8050/')


# The main function
if __name__ == '__main__':
    web()
    app.title = 'yourPersonality'
    app.run_server()
