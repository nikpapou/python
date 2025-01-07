import pandas as pd
import plotly.graph_objects as go


data = {
    "Product": [
        "Product A",
        "Product B",
        "Product C",
        "Product D",
        "Product E",
    ],
    "Sales": [1200, 1500, 900, 1800, 1600],
}

df = pd.DataFrame(data)

trace = go.Histogram(
    x=df["Sales"],  # Sales data
    nbinsx=5,  # Number of bins
    name="Product Sales",  # Name of the trace
    marker=dict(color="#ff7f0e"),  # Color of the bars
)

layout = go.Layout(title="Product Sales Distribution")
fig = go.Figure(data=[trace], layout=layout)
fig.show()