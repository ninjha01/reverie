from flask import Flask, render_template

import json
import plotly

import pandas as pd
import numpy as np
from sklearn.metrics import r2_score


app = Flask(__name__)
app.debug = True

from utils import get_assay_data


@app.route("/")
def index():

    # HACK: hardcoded
    assays = [
        "assay_0",
        "assay_1",
        "assay_2",
        "assay_3",
        "assay_4",
        "assay_5",
        "assay_6",
        "assay_7",
        "assay_8",
        "assay_9",
    ]

    graphs = []
    for a in assays:
        x, y = get_assay_data(a)
        _x = []
        _y = []
        for a, b in zip(x, y):
            if not pd.isna(a) and not pd.isna(b):
                _x.append(a)
                _y.append(b)
        x = _x
        y = _y
        graphs.append(
            dict(
                data=[dict(x=x, y=y, mode="markers", type="scatter", trendline="ols")],
                layout=dict(title="Measured vs Predicted"),
                r_squared=r2_score(x, y),
            )
        )
    ids = ["assay_{} | r2: {}".format(i, j["r_squared"]) for i, j in enumerate(graphs)]
    graph_json = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("layouts/index.html", ids=ids, graph_json=graph_json)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
