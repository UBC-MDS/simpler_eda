import altair as alt
import numpy as np
import pandas as pd


def numerical_plot(
    data,
    xval=None,
    yval=None,
    plot_type="scatter",
    color=None,
    title=None,
    font_size=10,
    color_scheme="yellowgreenblue",
    plot_width=400,
    plot_height=300,
    x_transform=False,
    y_transform=False,
):
    """
    This function takes in a data frame object, two numeric columns,
    and produces either a scatter or line plot to visualize the
    relationship between the two features. User can optionally change
    default arguments for plot-type, color, title, size of text,
    color-scheme, and toggle log transformation for the x and y axis.

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
      Variable used to group the data ponts in different collors

    tilte : str, optional
      Variable used to set the title of the plot.

    font_size  : int, optional
      Variable used to set the size of the axis labels and title.

    color_scheme: str, optional
      The color scheme used for the plot.
      Other color schemes can be "blues", "tealblues", "oranges", "greenblue", "redpurple", etc.
      Other proper color scheme reference can be found in https://vega.github.io/vega/docs/schemes/

    plot_width: int, optional
      The width of the plot

    plot_height: int, optional
      The heigh of the plot

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

    return numerical_plot