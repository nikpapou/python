import plotly.graph_objects as go
import pandas as pd

data = {
    'Year': [2017, 2018, 2019, 2020],
    'Product A': [2000, 2500, 2700, 3000],
    'Product B': [1500, 1800, 2100, 2400]
}
df = pd.DataFrame(data)


fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Year'], y=df['Product A'], mode='lines+markers', name='Product A',
                         line=dict(color='blue', width=2), marker=dict(size=8)))

fig.add_trace(go.Scatter(x=df['Year'], y=df['Product B'], mode='lines+markers', name='Product B',
                         line=dict(color='red', width=2), marker=dict(size=8)))

fig.update_layout(title='Sales per Year',
                  xaxis_title='Year',
                  yaxis_title='Sales',
                  legend=dict(x=0, y=1, bgcolor='rgba(255, 255, 255, 0.5)'),
                  plot_bgcolor='rgba(0, 0, 0, 0)',
                  hovermode='x unified')
fig.show()