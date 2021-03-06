import altair as alt
import numpy as np
import pandas as pd
from vega_datasets import data
import warnings
import pytest
from pandas.api.types import is_numeric_dtype


cars = data.cars()


def numerical_eda(
    data,
    xval=None,
    yval=None,
    plot_type="scatter",
    color="red",
    title=None,
    font_size=10,
    color_scheme="tableau20",
    plot_width=400,
    plot_height=300,
    x_transform=False,
    y_transform=False,
):
    """
    This function takes in a data frame object, two numeric columns,
    and produces either a scatter or line plot to visualize the relationship
    between the two numerical features. Users can optionally change default
    arguments for plot-type, color, title, size of text, color-scheme, and
    toggle log transformation for the x and y axis.
    Parameters
    ----------
    data : pandas.core.frame.DataFrame
       Input dataframe object.
    xval : str
      Variable used to represent the x-axis.
    yval : str
      Variable used to represent the y-axis.
    plot_type : str
      Variable used to represent the graphical relationship between xval and yval, options are scatter or line plot.
    color : str, optional
      Variable used to group the data ponts in different colors.
    tilte : str, optional
      Variable used to set the title of the plot.
    font_size  : int, optional
      Variable used to set the size of the axis labels and title.
    color_scheme: str, optional
      The color scheme used for the plot.
      Other color schemes can be "accent", "category10", "category20", "category20b", "dark2", etc.
      Other proper color scheme reference can be found in https://vega.github.io/vega/docs/schemes/
    plot_width: int, optional
      The width of the plot.
    plot_height: int, optional
      The height of the plot.
    x_transform : bool, optional
      Determines whether a log transformation occurs on the x-axis.
    y_transform : bool, optional
      Determines whether a log transformation occurs on the y-axis.
    Returns
    -------
    `altair`
      Scatter plot or Line plot of user-specified variables.
    Examples
    --------
    >>> import altair as alt
    >>> import pandas as pd
    >>> import numpy as np
    >>> from simpler_eda.numerical_eda import numerical_plot
    >>> from vega_datasets import data
    >>> numerical_plot(data.cars(), xval = "Horsepower", yval = "Acceleration", plot_type = "line",
                 color = "Origin",
                 title = " Horsepower vs Acceleration",
                 font_size = 10)
    """
    # Defensive programming: Check if user provides valid inputs

    # Ensure title variable is specified by the user
    assert title is not None, "Variable title needs to be specified."

    error_one = "TypeError: Data must be entered as a pandas dataframe."
    assert isinstance(data, pd.DataFrame), error_one

    error_two = "Wrong type! X-axis variable must be entered as a String."
    assert isinstance(xval, str), error_two

    error_three = "Wrong type! Y-axis variable must be entered as a String."
    assert isinstance(yval, str), error_three

    error_four = "TypeError: x_transform must be of type boolean."
    assert isinstance(x_transform, bool), error_four

    error_five = "TypeError: y_transform must be of type boolean."
    assert isinstance(y_transform, bool), error_five

    error_six = "TypeError: plot_type must be either 'scatter' or 'line'."
    assert plot_type in ["scatter", "line"], error_six

    error_seven = "TypeError: plot_width must be an integer."
    assert isinstance(plot_width, int), error_seven

    error_eight = "TypeError: plot_height must be an integer."
    assert isinstance(plot_height, int), error_eight

    error_nine = "TypeError: font_size must be a positive integer."
    assert isinstance(font_size, int), error_nine

    error_ten = "Wrong type!: color must be a string."
    assert isinstance(color, str), error_ten

    error_eleven = "Wrong type!: title must be a string."
    assert isinstance(title, str), error_eleven

    error_twelve = "Wrong type!: color_scheme must be a string."
    assert isinstance(color_scheme, str), error_twelve

    # create a copy of the dataframe so that original dataframe
    #  remains unchanged
    df = data.copy(deep=True)

    # Ensure variable exists in the dataframe
    assert xval in df.columns, "Variable xval not found in input dataframe."

    assert yval in df.columns, "Variable yval not found in input dataframe."

    # Ensure variable is numeric
    error_msg_x = "Your x-variable needs to be numeric."
    assert pd.api.types.is_numeric_dtype(df[xval]), error_msg_x

    error_msg_y = "Your y-variable needs to be numeric."
    assert pd.api.types.is_numeric_dtype(df[yval]), error_msg_y

    # Toggle a log transformation on the x-axis
    warn_one = "Can't have negative x values with np.log"
    if x_transform:
        if any(df[xval] < 0):
            warnings.warn(warn_one)
        df[xval] = np.log(df[xval])
        xval = xval

    # Toggle a log transformation on the y-axis
    warn_two = "Can't have negative y values with np.log"
    if y_transform:
        if any(df[yval] < 0):
            warnings.warn(warn_two)
        df[yval] = np.log(df[yval])

    # Update scale bounds of the plots
    x_scale = alt.Scale(domain=(float(df[xval].min()), float(df[xval].max())))
    y_scale = alt.Scale(domain=(float(df[yval].min()), float(df[yval].max())))

    # Renaming column names, replacing underscores with space
    # Replacing underscores to whitespace
    df.columns = df.columns.str.replace("_", " ")
    xval = str(xval).replace("_", " ")
    yval = str(yval).replace("_", " ")
    color = str(color).replace("_", " ")

    # Plotting code for the function, code for either plot_type in ['line', 'scatter']
    # Code for the scatter plot
    if plot_type == "scatter":
        if color in df.columns:
            numerical_eda = (
                alt.Chart(df, title=alt.TitleParams(text=title))
                .mark_circle(size=30, opacity=0.8)
                .encode(
                    alt.X(xval, scale=x_scale),
                    alt.Y(yval, scale=y_scale),
                    alt.Color(color, scale=alt.Scale(scheme=color_scheme)),
                )
                .properties(width=plot_width, height=plot_height)
            ).configure_axis(
                titleFontSize=font_size, labelFontSize=font_size, labelAngle=0
            )
        else:
            numerical_eda = (
                alt.Chart(df, title=alt.TitleParams(text=title))
                .mark_circle(size=30, opacity=0.8, color=color)
                .encode(
                    alt.X(xval, scale=x_scale),
                    alt.Y(yval, scale=y_scale),
                )
                .properties(width=plot_width, height=plot_height)
            ).configure_axis(
                titleFontSize=font_size, labelFontSize=font_size, labelAngle=0
            )

    # Code for the line plot
    elif plot_type == "line":
        if color in df.columns:
            numerical_eda = (
                alt.Chart(df, title=alt.TitleParams(text=title))
                .mark_line(size=1, opacity=0.8)
                .encode(
                    alt.X(xval, scale=x_scale),
                    alt.Y(yval, scale=y_scale),
                    alt.Color(color, scale=alt.Scale(scheme=color_scheme)),
                )
                .properties(width=plot_width, height=plot_height)
                .configure_axis(
                    titleFontSize=font_size, labelFontSize=font_size, labelAngle=0
                )
            )
        else:
            numerical_eda = (
                alt.Chart(df, title=alt.TitleParams(text=title))
                .mark_line(size=1, opacity=0.8, color=color)
                .encode(
                    alt.X(xval, scale=x_scale),
                    alt.Y(yval, scale=y_scale),
                )
                .properties(width=plot_width, height=plot_height)
                .configure_axis(
                    titleFontSize=font_size, labelFontSize=font_size, labelAngle=0
                )
            )

    return numerical_eda
