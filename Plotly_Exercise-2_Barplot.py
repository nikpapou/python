import plotly.graph_objects as go
import pandas as pd

data = {
    "Product": ["Product A", "Product B", "Product C", "Product D"],
    "Sales": [2000, 2500, 1800, 2200],
}
df = pd.DataFrame(data)

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=df["Product"],
        y=df["Sales"],
        text=df["Sales"],
        textposition="auto",
        marker_color=["blue", "red", "green", "purple"],
    )
)

fig.update_layout(
    title="Sales in 2020",
    xaxis_title="Product",
    yaxis_title="Sales",
    plot_bgcolor="rgba(0, 0, 0, 0)",
    hovermode="x unified",
)
fig.show()