# import altair as alt
# import numpy as np
# import pandas as pd
# import pytest
from vega_datasets import data
from simpler_eda.corr_map import corr_map

df = data.cars()


def test_input_type():
    """
    Tests for exceptions handling.

    Returns
    -------
    None
        All test should pass and no asserts error should be displayed.
    """

    try:
        corr_map(
            ["a", "b", "c"],
            ["Horsepower", "Displacement", "Cylinders", "Acceleration"],
        )

    except Exception as err:
        assert str(err) == "The input data is not a panda dataframe"

    try:
        corr_map(df, "ab")

    except Exception as err:
        assert str(err) == "The input for feature should be a list"

    try:
        corr_map(df, ["Horsepower"])

    except Exception as err:
        assert str(err) == "There should be at least 2 features in the list"

    try:
        corr_map(df, ["Horsepower", [123, 456]])

    except Exception as err:
        assert (
            str(err)
            == "All the entries in the feature list should be a string"
        )

    # added a check to ensure the input list of features are all numeric
    try:
        corr_map(df, ["Horsepower", "Name"])

    except Exception as err:
        assert str(err) == "All features in the list should be numeric"

    try:
        corr_map(
            df,
            ["Horsepower", "Displacement", "Cylinders", "Acceleration"],
            corr_method="kvb",
        )

    except Exception as err:
        assert (
            str(err)
            == """The correlation method should be 'pearson', 'kendall',
            or 'spearman' """
        )

    try:
        corr_map(
            df,
            ["Horsepower", "Displacement", "Cylinders", "Acceleration"],
            color_scheme=["blueyellow"],
        )

    except Exception as err:
        assert str(err) == "The color scheme should be given as a string"

    try:
        corr_map(
            df,
            ["Horsepower", "Displacement", "Cylinders", "Acceleration"],
            plot_width="200",
        )

    except Exception as err:
        assert str(err) == "The plot_width should be given as an integer"

    try:
        corr_map(
            df,
            ["Horsepower", "Displacement", "Cylinders", "Acceleration"],
            plot_height="200",
        )

    except Exception as err:
        assert str(err) == "The plot_height should be given as an integer"

    try:
        corr_map(
            df,
            ["Horsepower", "Displacement", "Cylinders", "Acceleration"],
            title=200,
        )

    except Exception as err:
        assert str(err) == "The title should be given as a string"


out = corr_map(
    df,
    ["Horsepower", "Displacement", "Cylinders", "Acceleration"],
    corr_method="pearson",
    color_scheme="blueorange",
    plot_width=450,
    plot_height=450,
    title="Correlation Map",
)


def test_corr_map():
    """
    Tests the corr_map function to make sure the outputs are correct.

    Returns
    --------
    None
        All test should pass and no asserts should be displayed.s
    """
    assert (
        str(type(out)) == "<class 'altair.vegalite.v4.api.Chart'>"
    ), "The function should retrun an altair plot"
    assert (
        out.encoding.x.shorthand == "level_0"
    ), "The level_0 should be mapped to the x axis"
    assert (
        out.encoding.y.shorthand == "level_1"
    ), "The level 1 should be mapped to the y axis"
    assert (
        out.mark.type == "rect"
    ), "the plot type (mark) should be a rect plot (heatmap)"
    assert out.encoding.color.scale.scheme == "blueorange", (
        "the color scheme should blueorange (default) or the inputted color"
        " scheme"
    )
    assert (
        out.title == "Correlation Map"
    ), "The title should be Correlation Map or the given value"
