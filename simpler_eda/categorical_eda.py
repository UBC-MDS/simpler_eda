import altair as alt
import numpy as np
import pandas as pd

def categorical_plot(
    data,
    xval = None,
    yval = "count",
    plot_type = "histogram",
    color = None,
    title = None,
    font_size = 10,
    color_scheme = "tableau20",
    plot_height = 150,
    plot_width = 200,
    opacity = 0.6,
    facet = None
    
):
    """
    This function takes in a data frame object and one categorical
    feature, to produce a histogram plot that visualizes the
    distribution of the feature. User can also choose to plot density
    graph of the feature by specifing in plot_type. 
    The function also offers customization on color, plot title, 
    font size, color-scheme, plot size, opacity level and facet 
    factor.

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
       Input dataframe object.
    xval : str
      Variable used to represent the x-axis.
    yval : str, optional
      Variable used to represent the y-axis.
    plot_type : str, optional
      Variable used to specify plot type. Options include "histogram" 
      and "density". When "density" is selected, the variable yval becomes obsolete.
    color : str, optional
      Variable used to set the color of the marks in the plot object.
    tilte : str, optional
      Variable used to set the title of the plot.
    font_size  : int, optional
      Variable used to set the size of the axis labels and title.
    color_scheme : str, optional
      Variable used to set the bar size.
    plot_height : int, optional
      Variable used to specify plot height
    plot_witdh : int, optional
      Variable used to specify plot width
    opacity : float, optional
      Variable used to specify density fill opacity for density plot
    facet : str, optional
      Variable used to specify facet factor

    Returns
    -------
    `altair`
        A histogram or density chart object based on user specifications.

    Examples
    --------
    >>> import altair as alt
    >>> import numpy as np
    >>> import pandas as pd
    >>> from simpler_eda.categorical_eda import categorical_plot
    >>> from vega_datasets import data
    >>> cars = data.cars()
    >>> categorical_plot(data = cars, 
                        xval = "Origin", 
                        yval = "count()",
                        color = "Horsepower",
                        title = "Histogram of Origin in Different Levels of Horsepower",
                        plot_height = 100,
                        plot_width = 200
                        )
    """

    return categorical_plot
