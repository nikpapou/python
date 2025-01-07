import plotly.graph_objects as go
import pandas as pd

data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Market Share': [30, 20, 25, 25]
}
df = pd.DataFrame(data)

fig = go.Figure()
fig.add_trace(go.Pie(
    labels=df['Product'],
    values=df['Market Share'],
    textinfo='label+percent',
    marker=dict(
        colors=['blue', 'red', 'green', 'purple'],
        line=dict(color='#000000', width=1)
    )
))


fig.update_layout(
    title='Market Share of Products',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    hovermode='x unified'
)
fig.show()