import altair as alt
import numpy as np
import pandas as pd
import pytest
from vega_datasets import data
from simpler_eda.corr_map import corr_map


df = data.cars()
out = corr_map(df, ["Horsepower", "Displacement", "Cylinders", "Acceleration"])

def test_corr_map():
    assert str(type(out)) == "<class 'altair.vegalite.v4.api.Chart'>", "The function should retrun an altair plot" 
    assert out.encoding.x.field == "level_0", 'The level_0 should be mapped to the x axis'
    assert out.encoding.y.field == "level_1", 'The level 1 should be mapped to the y axis'
    assert out.mark.type in ["rect"], 'the plot type (mark) should be a rect plot (heatmap)'
    assert out.encoding.color.scale.scheme == color_scheme, "the color scheme should blueorange (default) or the inputted color scheme"
    assert out.title in [title, "Correlation Map"], "The title should be Correlation Map or the given value"