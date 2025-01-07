import pandas as pd
import plotly.graph_objects as go

data = {
    "Customer ID": [
        "Cust1",
        "Cust2",
        "Cust3",
        "Cust4",
        "Cust5",
    ],
    "Spending": [200, 150, 350, 400, 250],
}
df = pd.DataFrame(data)


trace = go.Box(y=df["Spending"], name="Customer Spending", marker=dict(color="#d62728"))
layout = go.Layout(title="Customer Spending Distribution")
fig = go.Figure(data=[trace], layout=layout)
fig.show()