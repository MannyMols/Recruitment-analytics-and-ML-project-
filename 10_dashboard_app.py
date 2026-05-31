import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output

# Load data
df = pd.read_csv('Recruitment_dashboard_ready.csv')

# Summary stats
total = len(df)
placed = int(df['was_placed'].sum())
placement_rate = round(placed / total * 100, 1)
at_risk = len(df[df['placement_risk_tier'].isin(['At Risk', 'Unlikely'])])

app = Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#1B2A4A', 'padding': '20px',
                              'fontFamily': 'Arial'}, children=[

    # Title
    html.H1('Recruiting Firm — Recruitment Analytics Dashboard',
            style={'color': 'white', 'textAlign': 'center', 'marginBottom': '5px'}),
    html.P('Powered by XGBoost Placement Prediction | May 2026',
           style={'color': '#90CAF9', 'textAlign': 'center', 'marginBottom': '30px'}),

    # KPI Row
    html.Div(style={'display': 'flex', 'justifyContent': 'space-around',
                    'marginBottom': '30px'}, children=[
        html.Div(style={'backgroundColor': '#263B5E', 'borderRadius': '10px',
                        'padding': '20px', 'textAlign': 'center', 'width': '20%'}, children=[
            html.H2(str(total), style={'color': '#90CAF9', 'margin': '0'}),
            html.P('Total Registered', style={'color': 'white', 'margin': '5px 0'})
        ]),
        html.Div(style={'backgroundColor': '#263B5E', 'borderRadius': '10px',
                        'padding': '20px', 'textAlign': 'center', 'width': '20%'}, children=[
            html.H2(str(placed), style={'color': '#4CAF50', 'margin': '0'}),
            html.P('Total Placed', style={'color': 'white', 'margin': '5px 0'})
        ]),
        html.Div(style={'backgroundColor': '#263B5E', 'borderRadius': '10px',
                        'padding': '20px', 'textAlign': 'center', 'width': '20%'}, children=[
            html.H2(f'{placement_rate}%', style={'color': '#FFD700', 'margin': '0'}),
            html.P('Placement Rate', style={'color': 'white', 'margin': '5px 0'})
        ]),
        html.Div(style={'backgroundColor': '#263B5E', 'borderRadius': '10px',
                        'padding': '20px', 'textAlign': 'center', 'width': '20%'}, children=[
            html.H2(str(at_risk), style={'color': '#F44336', 'margin': '0'}),
            html.P('At Risk / Unlikely', style={'color': 'white', 'margin': '5px 0'})
        ]),
    ]),

    # Slicers
    html.Div(style={'display': 'flex', 'gap': '20px', 'marginBottom': '20px'}, children=[
        html.Div([
            html.Label('Seniority Level', style={'color': 'white'}),
            dcc.Dropdown(
                id='seniority-filter',
                options=[{'label': 'All', 'value': 'All'}] +
                        [{'label': s, 'value': s} for s in sorted(df['seniority_level'].dropna().unique())],
                value='All', clearable=False,
                style={'width': '200px'}
            )
        ]),
        html.Div([
            html.Label('Risk Tier', style={'color': 'white'}),
            dcc.Dropdown(
                id='tier-filter',
                options=[{'label': 'All', 'value': 'All'}] +
                        [{'label': t, 'value': t} for t in
                         ['High Confidence', 'Likely', 'At Risk', 'Unlikely']],
                value='All', clearable=False,
                style={'width': '200px'}
            )
        ]),
    ]),

    # Charts Row 1
    html.Div(style={'display': 'flex', 'gap': '20px', 'marginBottom': '20px'}, children=[
        html.Div(style={'width': '50%'}, children=[dcc.Graph(id='donut-chart')]),
        html.Div(style={'width': '50%'}, children=[dcc.Graph(id='seniority-bar')]),
    ]),

    # Charts Row 2
    html.Div(style={'display': 'flex', 'gap': '20px', 'marginBottom': '20px'}, children=[
        html.Div(style={'width': '50%'}, children=[dcc.Graph(id='satisfaction-hist')]),
        html.Div(style={'width': '50%'}, children=[dcc.Graph(id='salary-scatter')]),
    ]),

    # At Risk Table
    html.H3('At Risk & Unlikely Candidates — Action Required',
            style={'color': '#F44336', 'marginTop': '10px'}),
    html.Div(id='at-risk-table')
])


@app.callback(
    Output('donut-chart', 'figure'),
    Output('seniority-bar', 'figure'),
    Output('satisfaction-hist', 'figure'),
    Output('salary-scatter', 'figure'),
    Output('at-risk-table', 'children'),
    Input('seniority-filter', 'value'),
    Input('tier-filter', 'value')
)
def update_charts(seniority, tier):
    filtered = df.copy()
    if seniority != 'All':
        filtered = filtered[filtered['seniority_level'] == seniority]
    if tier != 'All':
        filtered = filtered[filtered['placement_risk_tier'] == tier]

    # Donut
    tier_counts = filtered['placement_risk_tier'].value_counts().reset_index()
    tier_counts.columns = ['Tier', 'Count']
    color_map = {'High Confidence': '#4CAF50', 'Likely': '#2196F3',
                 'At Risk': '#FF9800', 'Unlikely': '#F44336'}
    donut = px.pie(tier_counts, names='Tier', values='Count', hole=0.5,
                   title='Pipeline Risk Distribution',
                   color='Tier', color_discrete_map=color_map)
    donut.update_layout(paper_bgcolor='#263B5E', font_color='white',
                        title_font_size=14)

    # Seniority bar
    sen = filtered.groupby('seniority_level')['was_placed'].mean().reset_index()
    sen.columns = ['Seniority', 'Placement Rate']
    sen['Placement Rate'] = (sen['Placement Rate'] * 100).round(1)
    bar = px.bar(sen, x='Placement Rate', y='Seniority', orientation='h',
                 title='Placement Rate by Seniority',
                 color='Placement Rate', color_continuous_scale='Blues')
    bar.update_layout(paper_bgcolor='#263B5E', plot_bgcolor='#263B5E',
                      font_color='white', title_font_size=14)

    # Satisfaction histogram
    placed_only = filtered[filtered['was_placed'] == 1]
    hist = px.histogram(placed_only, x='client_satisfaction_score', nbins=10,
                        title='Client Satisfaction Distribution (Placed Only)',
                        color_discrete_sequence=['#2196F3'])
    hist.update_layout(paper_bgcolor='#263B5E', plot_bgcolor='#263B5E',
                       font_color='white', title_font_size=14)

    # Salary scatter
    scatter = px.scatter(placed_only, x='salary_gap', y='client_satisfaction_score',
                         color='seniority_level', title='Salary Gap vs Client Satisfaction',
                         labels={'salary_gap': 'Salary Gap (£)', 
                                 'client_satisfaction_score': 'Satisfaction Score'})
    scatter.update_layout(paper_bgcolor='#263B5E', plot_bgcolor='#263B5E',
                          font_color='white', title_font_size=14)

    # At risk table
    at_risk_df = filtered[filtered['placement_risk_tier'].isin(['At Risk', 'Unlikely'])][
        ['first_name', 'last_name', 'seniority_level',
         'expected_salary_gbp', 'placement_probability', 'placement_risk_tier']
    ].sort_values('placement_probability')

    table = html.Table(
        style={'width': '100%', 'borderCollapse': 'collapse', 'color': 'white'},
        children=[
            html.Thead(html.Tr([
                html.Th(col, style={'padding': '10px', 'backgroundColor': '#263B5E',
                                    'borderBottom': '2px solid #90CAF9'})
                for col in ['First Name', 'Last Name', 'Seniority',
                            'Expected Salary', 'Placement Prob', 'Risk Tier']
            ])),
            html.Tbody([
                html.Tr([
                    html.Td(str(row[col]), style={'padding': '8px',
                            'borderBottom': '1px solid #263B5E',
                            'backgroundColor': '#1B2A4A'})
                    for col in at_risk_df.columns
                ]) for _, row in at_risk_df.iterrows()
            ])
        ]
    )

    return donut, bar, hist, scatter, table


if __name__ == '__main__':
    app.run(debug=True, port=8050)