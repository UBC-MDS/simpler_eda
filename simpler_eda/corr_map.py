import pandas as pd
import altair as alt
import numpy as np


def corr_map(path, data_type, features, sep=",", color_theme='yellowgreenblue', plot_width=400, plot_height=300, title="Correlation Map"):
    """
    Plot a correlation map for the given list of feature and raw (the path and data type). 
    Users can also set multiple arugment regarding the data (e.g. the separator) and the setting for the correlation plot
    from color schemes, plot withh & height, title.

    Parameters
    ----------
    path: str
      A location path for the data file

    data: str
      The data type for the data. 
      It only supports CSV and Json at the moment.

    features: list
      A 1D list of numerical feature names in string with the feature names for correlation map plotting.
      It should contain at least 2 features.

    color_theme: str, default='yellowgreenblue'
      The color scheme
      Other color schemes can be "blues", "tealblues", "oranges", "greenblue", "redpurple", etc.
      Other proper color scheme reference can be found inhttps://vega.github.io/vega/docs/schemes/

    plot_width: int, default=400
      The width of the plot

    plot_height: int, default=300
      The heigh of the plot

    title: str, default="Correlation Map"
      The title of the correlation map

    Returns
    -------
    altair.vegalite.v4.api.Chart
      The altair correlation map plot

    Examples
    --------
    >>> import pandas as pd
    >>> import altair as alt
    >>> from corr_map import corr_map
    >>> corr_map.corr_map("data/abc.csv", "csv", ["age", "height", "income"])
    An altair.vegalite.v4.api.Chart object
    An correlation map with the correlation among the age, height and income

    """

    return corr_map
