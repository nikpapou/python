import pandas as pd
import plotly.graph_objects as go
data = {
    "Subject": ['Physics', 'Chemistry', 'Biology', 'Maths', 'Computer Science',
                'History', 'Geography', 'Economics', 'Political Science', 'Psychology'],
    "Students": [47, 35, 42, 38, 50, 32, 37, 40, 36, 42],
    "Pass Percentage": [86, 74, 80, 83, 92, 75, 82, 78, 85, 87],
    "Department": ['Science', 'Science', 'Science', 'Science', 'Science',
                   'Arts', 'Arts', 'Arts', 'Arts', 'Arts']
}

df = pd.DataFrame(data)

fig = go.Figure()

for department in df["Department"].unique():
    fig.add_trace(
        go.Scatter(
            x=df[df["Department"] == department]["Students"],
            y=df[df["Department"] == department]["Pass Percentage"],
            mode="markers",
            name=department,
            text=df[df["Department"] == department]["Subject"],
            visible=False,
        )
    )
fig.data[0].visible = True

buttons = [
    dict(
        label=department,
        method="update",
        args=[
            {"visible": [department == dep for dep in df["Department"].unique()]},
            {"title": f"Department: {department}"},
        ],
    )
    for department in df["Department"].unique()
]

fig.update_layout(updatemenus=[dict(showactive=True, buttons=buttons)])

fig.show()