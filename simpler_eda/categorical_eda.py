import altair as alt
import numpy as np
import pandas as pd

def categorical_plot(
    data,
    xval=None,
    yval=None,
    plot_type="bar",
    color=None,
    title=None,
    font_size=10,
    bar_size=5,
    color_scheme=None,
    sort_by=None,
    plot_height=None,
    plot_width=None,
    facet=None
):
    """
    This function takes in a data frame object, one categorical column,
    and one argument to specify count or percentage variable,
    to produce a bar plot that visualizes the
    count or percentage value of the feature. User can optionally change
    default arguements for color, plot title, size of text,
    color-schem, orientation, plot size and facet factor.

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
       Input dataframe object.
    xval : str
      Variable used to represent the x-axis.
    yval : str
      Variable used to represent the y-axis.
    plot_type : str, optional
      Variable used to represent the graphical relationship between xval and yval.
    color : str, optional
      Variable used to set the color of the marks in the plot object.
    tilte : str, optional
      Variable used to set the title of the plot.
    font_size  : int, optional
      Variable used to set the size of the axis labels and title.
    bar_size : int, optional
      Variable used to set the bar size.
    color_scheme : str, optional
      Variable used to set the bar size.
    sort_by : str, optional
      Variable used to specify sort argument
    plot_height : int, optional
      Variable used to specify plot height
    plot_witdh : int, optional
      Variable used to specify plot width
    facet : str, optional
      Variable used to specify facet factor

    Returns
    -------
    `altair`
        A bar chart according to user specification in the parameters.

    Examples
    --------
    >>> from simpler_eda.categorical_eda import categorical_plot
    >>> from vega_datasets import data
    >>> cars = data.cars()
    >>> categorical_plot(cars, xval = "Origin", 
                        yval = "count()",
                        color = "Horsepower",
                        title = "Histogram of Origin in Different Levels of Horsepower",
                        sort_by = '-y',
                        plot_height = 100,
                        plot_width = 200
                        )
    """