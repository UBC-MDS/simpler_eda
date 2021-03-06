import altair as alt
import numpy as np
import pandas as pd
from vega_datasets import data
import warnings
import pytest
from simpler_eda.numerical_eda import numerical_eda

cars = data.cars()


@pytest.fixture
def test_negative():
    negative_data = pd.DataFrame(
        {
            "x": [1, 2, 6, 7, 83, -1],
            "y": [1, 25, 6, -77, 2, 3],
            "Origin": [10, 11, 12, 12, 11, 19],
        }
    )
    return negative_data


def test_numerical_eda():

    """
    Tests the numerical eda function numerical_eda to make sure the outputs are
    correctly rendering.

    Returns:
    --------
    None
        The test should pass and no asserts should be displayed.
    """

    # Unit test for a scatter plot with no transformations and grouping by color
    plot1 = numerical_eda(
        cars,
        xval="Horsepower",
        yval="Acceleration",
        color="Origin",
        plot_type="scatter",
        font_size=10,
        color_scheme="tableau20",
        plot_height=100,
        plot_width=200,
    )

    assert (
        str(type(plot1)) == "<class 'altair.vegalite.v4.api.Chart'>"
    ), "The function should retrun an altair plot"
    assert (
        plot1.encoding.x.shorthand == "Horsepower"
    ), "Horsepower should be mapped to the x axis"
    assert (
        plot1.encoding.y.shorthand == "Acceleration"
    ), "Acceleration should be mapped to the y axis"
    assert plot1.mark["type"] in ["circle"], "the plot type (mark) should be a point"
    assert (
        plot1.title.text == "Horsepower vs Acceleration scatter plot"
    ), "The plot title should be Horsepower vs Acceleration scatter plot"
    assert (
        plot1.encoding.color.shorthand == "Origin"
    ), "The color of the mark should be based on Origin"

    # Unit test for a line plot with no transformations and grouping by color
    plot2 = numerical_eda(
        cars,
        xval="Acceleration",
        yval="Displacement",
        color="Origin",
        title="Line",
        plot_type="line",
        font_size=10,
        color_scheme="dark2",
        plot_height=100,
        plot_width=200,
    )

    assert (
        str(type(plot2)) == "<class 'altair.vegalite.v4.api.Chart'>"
    ), "The function should retrun an altair plot"
    assert (
        plot2.encoding.x.shorthand == "Acceleration"
    ), "Acceleration should be mapped to the x axis"
    assert (
        plot2.encoding.y.shorthand == "Displacement"
    ), "Displacement should be mapped to the y axis"
    assert plot2.mark["type"] in ["line"], "the plot type (mark) should be a line"
    assert plot2.title.text == "Line", "The plot title should be Line"
    assert (
        plot2.encoding.color.shorthand == "Origin"
    ), "The color of the mark should be based on Origin"

    # Unit test for a scatter plot with transformations and using color with categorical
    plot3 = numerical_eda(
        cars,
        xval="Displacement",
        yval="Acceleration",
        color="Origin",
        title="Scatterplot",
        plot_type="scatter",
        font_size=10,
        color_scheme="tableau20",
        plot_height=100,
        plot_width=200,
        x_transform=True,
        y_transform=True,
    )

    assert (
        str(type(plot3)) == "<class 'altair.vegalite.v4.api.Chart'>"
    ), "The function should retrun an altair plot"
    assert (
        plot3.encoding.x.shorthand == "Displacement"
    ), "Disolacement should be mapped to the x axis"
    assert (
        plot3.encoding.y.shorthand == "Acceleration"
    ), "Acceleration should be mapped to the y axis"
    assert plot3.mark["type"] in ["circle"], "the plot type (mark) should be a point"
    assert plot3.title.text == "Scatterplot", "The plot title should be Scatterplot"
    assert (
        plot3.encoding.color.shorthand == "Origin"
    ), "The color of the groupings should be origin"


def test_input_type():
    """
    Test for error if input is of a wrong type

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test should pass and no asserts should be displayed.
    """

    # Wrong dataframe input
    try:
        numerical_eda(
            list(cars),
            xval="Horsepower",
            yval="Displacement",
            color="Origin",
            title="Plot",
            plot_type="line",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=400,
        )
    except Exception as e:
        assert str(e) == "TypeError: Data must be entered as a pandas dataframe."

    # Wrong input for xval, must be string
    try:
        numerical_eda(
            cars,
            xval=10,
            yval="Displacement",
            color="Origin",
            title="Plot",
            plot_type="line",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=400,
        )
    except Exception as e:
        assert str(e) == "TypeError: X-axis variable must be entered as a String."

    # Wrong input for yval, must be string
    try:
        numerical_eda(
            cars,
            xval="Horsepower",
            yval=20,
            color="Origin",
            title="Plot",
            plot_type="line",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=400,
        )
    except Exception as e:
        assert str(e) == "TypeError: Y-axis variable must be entered as a String."

    # Wrong input type for x_transform, must be boolean
    try:
        numerical_eda(
            cars,
            xval="Horsepower",
            yval="Displacement",
            color="Origin",
            title="Plot",
            plot_type="line",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=400,
            x_transform="False",
        )
    except Exception as e:
        assert str(e) == "TypeError: x_transform must be of type boolean."

    # Wrong input type for y_transform, must be boolean
    try:
        numerical_eda(
            cars,
            xval="Horsepower",
            yval="Displacement",
            color="Origin",
            title="Plot",
            plot_type="line",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=400,
            y_transform="False",
        )
    except Exception as e:
        assert str(e) == "TypeError: y_transform must be of type boolean."

    # Wrong input type for plot_width, must be integer
    try:
        numerical_eda(
            cars,
            xval="Horsepower",
            yval="Displacement",
            color="Origin",
            title="Plot",
            plot_type="line",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width="Horse",
            x_transform=False,
        )
    except Exception as e:
        assert str(e) == "TypeError: plot_width must be an integer."

    # Wrong input type for plot_height, must be integer
    try:
        numerical_eda(
            cars,
            xval="Horsepower",
            yval="Displacement",
            color="Origin",
            title="Plot",
            plot_type="line",
            font_size=10,
            color_scheme="tableau20",
            plot_height="200",
            plot_width=100,
            x_transform=False,
        )
    except Exception as e:
        assert str(e) == "TypeError: plot_height must be an integer."

    # Wrong input type for font_size, must be integer
    try:
        numerical_eda(
            cars,
            xval="Horsepower",
            yval="Displacement",
            color="Origin",
            title="Plot",
            plot_type="line",
            font_size="10",
            color_scheme="tableau20",
            plot_height=200,
            plot_width=100,
            x_transform=False,
        )
    except Exception as e:
        assert str(e) == "TypeError: font_size must be a positive integer."

    # Wrong input type for color, must be string
    try:
        numerical_eda(
            cars,
            xval="Horsepower",
            yval="Displacement",
            color=50,
            title="Plot",
            plot_type="line",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=100,
            x_transform=False,
        )
    except Exception as e:
        assert str(e) == "TypeError: color must be a string."

    # Wrong input type for title, must be string
    try:
        numerical_eda(
            cars,
            xval="Horsepower",
            yval="Displacement",
            color="Origin",
            title=list("deep"),
            plot_type="line",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=100,
            x_transform=False,
        )
    except Exception as e:
        assert str(e) == "TypeError: title must be a string."

    # Wrong input type for color_scheme, must be string
    try:
        numerical_eda(
            cars,
            xval="Horsepower",
            yval="Displacement",
            color="Origin",
            title="Plot",
            plot_type="line",
            font_size=10,
            color_scheme=list("tableau20"),
            plot_height=200,
            plot_width=100,
            x_transform=False,
        )
    except Exception as e:
        assert str(e) == "TypeError: color_scheme must be a string."


def test_input_value():
    """
    Test for error if input is of a wrong value

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test should pass and no asserts should be displayed.
    """

    # Test for whether xval is in the dataframe
    try:
        numerical_eda(
            cars,
            xval="Horse",
            yval="Displacement",
            color="Origin",
            title="Plot",
            plot_type="line",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=400,
        )
    except Exception as e:
        assert str(e) == "Variable xval not found in input dataframe."

    # Test for whether yval is in the dataframe
    try:
        numerical_eda(
            cars,
            xval="Horsepower",
            yval="Displa",
            color="Origin",
            title="Plot",
            plot_type="line",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=400,
        )
    except Exception as e:
        assert str(e) == "Variable yval not found in input dataframe."

    # Test for whether color is in dataframe
    try:
        numerical_eda(
            cars,
            xval="Horsepower",
            yval="Displacement",
            color="Orig",
            title="Deepak",
            plot_type="line",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=400,
        )
    except Exception as e:
        assert str(e) == "Variable color not found in input dataframe."

    # Test for whether xval is  numeric
    try:
        numerical_eda(
            cars,
            xval="Origin",
            yval="Displacement",
            color="Origin",
            title="Deepak",
            plot_type="line",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=400,
        )
    except Exception as e:
        assert str(e) == "Your x-variable needs to be numeric."

    # Test for whether yval is  numeric
    try:
        numerical_eda(
            cars,
            xval="Horsepower",
            yval="Origin",
            color="Origin",
            title="Deepak",
            plot_type="line",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=400,
        )
    except Exception as e:
        assert str(e) == "Your y-variable needs to be numeric."

    # Test for whether plot_type is "scatter" or "line"
    try:
        numerical_eda(
            cars,
            xval="Horsepower",
            yval="Displacement",
            color="Origin",
            title="Deepak",
            plot_type="point",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=400,
        )
    except Exception as e:
        assert (
            str(e) == "InputValueError: plot_type must be either 'scatter' or 'line'."
        )


def test_negX(test_negative):
    """
    Test whether the function returns warning for negative values of xval for log transformation

    Parameters
    ----------
    test_negative: A pandas dataframe

    Returns
    -------
    None
        The test should pass and no asserts should be displayed.
    ----------
    """
    with pytest.warns(UserWarning):
        numerical_eda(
            test_negative,
            xval="x",
            yval="y",
            color="Origin",
            title="Plot",
            plot_type="scatter",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=400,
            x_transform=True,
            y_transform=False,
        )


def test_negY(test_negative):
    """
    Test whether the function returns warning for negative values of yval for log transformation

    Parameters
    ----------
    test_negative: A pandas dataframe

    Returns
    -------
    None
        The test should pass and no asserts should be displayed.
    ----------
    """
    with pytest.warns(UserWarning):
        numerical_eda(
            test_negative,
            xval="x",
            yval="y",
            color="Origin",
            title="Plot",
            plot_type="scatter",
            font_size=10,
            color_scheme="tableau20",
            plot_height=200,
            plot_width=400,
            x_transform=False,
            y_transform=True,
        )
