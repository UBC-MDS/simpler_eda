import altair as alt
import numpy as np
import pandas as pd
from vega_datasets import data
import warnings
import pytest
from simpler_eda.numerical_eda import numerical_plot

cars = data.cars()


def test_numerical_plot():

    # Unit test for a scatter plot with no transformations and using mark color
    plot1 = numerical_plot(
        cars,
        xval="Horsepower",
        yval="Acceleration",
        color="red",
        title="Scatter",
        plot_type="scatter",
        font_size=10,
        color_scheme="purpleorange",
        plot_height=100,
        plot_width=200,
    )
    plot1_dict = plot1.to_dict()

    assert (
        str(type(plot1)) == "<class 'altair.vegalite.v4.api.Chart'>"
    ), "The function should retrun an altair plot"
    assert (
        plot1.encoding.x.field == "Horsepower"
    ), "Horsepower should be mapped to the x axis"
    assert (
        plot1.encoding.y.field == "Acceleration"
    ), "Acceleration should be mapped to the y axis"
    assert plot1.mark["type"] in ["circle"], "the plot type (mark) should be a point"
    assert plot1.title.text == "Scatter", "The plot title should be Scatter"
    assert plot1.mark.color == "red", "The color of the mark should be red"

    # Unit test for a line plot with no transformations and using mark color
    plot2 = numerical_plot(
        cars,
        xval="Acceleration",
        yval="Displacement",
        color="blue",
        title="Line",
        plot_type="line",
        font_size=10,
        color_scheme="dark2",
        plot_height=100,
        plot_width=200,
    )
    plot2_dict = plot2.to_dict()

    assert (
        str(type(plot2)) == "<class 'altair.vegalite.v4.api.Chart'>"
    ), "The function should retrun an altair plot"
    assert (
        plot2.encoding.x.field == "Acceleration"
    ), "Acceleration should be mapped to the x axis"
    assert (
        plot2.encoding.y.field == "Displacement"
    ), "Displacement should be mapped to the y axis"
    assert plot2.mark["type"] in ["line"], "the plot type (mark) should be a line"
    assert plot2.title.text == "Line", "The plot title should be Line"
    assert plot2.mark.color == "blue", "The color of the mark should be blue"

    # Unit test for a scatter plot with transformations and using color with categorical
    plot3 = numerical_plot(
        cars,
        xval="Displacement",
        yval="Acceleration",
        color="Origin",
        title="Scatterplot",
        plot_type="scatter",
        font_size=10,
        color_scheme="purpleorange",
        plot_height=100,
        plot_width=200,
        x_transform=True,
        y_transform=True,
    )
    plot3_dict = plot3.to_dict()

    assert (
        str(type(plot3)) == "<class 'altair.vegalite.v4.api.Chart'>"
    ), "The function should retrun an altair plot"
    assert (
        plot3.encoding.x.field == "Displacement"
    ), "Disolacement should be mapped to the x axis"
    assert (
        plot3.encoding.y.field == "Acceleration"
    ), "Acceleration should be mapped to the y axis"
    assert plot3.mark["type"] in ["circle"], "the plot type (mark) should be a point"
    assert plot3.title.text == "Scatterplot", "The plot title should be Scatterplot"
    assert (
        plot3.encoding.color.field == "Origin"
    ), "The color of the groupings should be origin"

    # Unit test for a line plot with transformations and using color with numerical variable
    plot4 = numerical_plot(
        cars,
        xval="Displacement",
        yval="Acceleration",
        color="Horsepower",
        title="Lineplot",
        plot_type="line",
        font_size=10,
        color_scheme="purpleorange",
        plot_height=100,
        plot_width=200,
        x_transform=True,
        y_transform=True,
    )
    plot4_dict = plot4.to_dict()

    assert (
        str(type(plot4)) == "<class 'altair.vegalite.v4.api.Chart'>"
    ), "The function should retrun an altair plot"
    assert (
        plot4.encoding.x.field == "Displacement"
    ), "Displacement should be mapped to the x axis"
    assert (
        plot4.encoding.y.field == "Acceleration"
    ), "Acceleration should be mapped to the y axis"
    assert plot4.mark["type"] in ["line"], "the plot type (mark) should be a line"
    assert plot4.title.text == "Lineplot", "The plot title should be Scatterplot"
    assert (
        plot4.encoding.color.field == "Horsepower"
    ), "The color of the groupings should be Horsepower"