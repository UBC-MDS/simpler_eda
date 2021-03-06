import altair as alt
import numpy as np
import pandas as pd

def categorical_eda(
    data,
    xval,
    plot_type = "histogram",
    color = None,
    title = None,
    font_size = 10,
    color_scheme = "tableau20",
    plot_height = 150,
    plot_width = 200,
    opacity = 1,
    facet_factor = None,
    facet_col = None
):
    """
    This function takes in a data frame object and one categorical
    feature, to produce a histogram plot that visualizes the
    distribution of the feature. User can also choose to plot density
    graph of the feature by specifing in plot_type. 
    The function also offers customization on color, plot title, 
    font size, color-scheme, plot size and other common configurations.

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
       Input dataframe object.
    xval : str
      Variable used to represent the x-axis.
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
    facet_factor : str, optional
      Variable used to specify facet factor
    facet_col : int, optional
      Variable used to specify number of facet columns

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
                        color = "Horsepower",
                        title = "Histogram of Origin in Different Levels of Horsepower",
                        plot_height = 100,
                        plot_width = 200
                        )
    """
    #Checking for valid inputs:
    if not isinstance(data, pd.DataFrame):
        raise Exception("the input data has to be a dataframe.")
    if facet_factor is None and facet_col is not None:
        raise Exception("facet_factor must be provided along with facet_col.")
    if facet_factor is not None and facet_col is None:
        raise Exception("Specify facet_col for facetting the plot")
    if plot_type not in ["histogram", "density"]:
        raise Exception("plot_type must be either 'histogram' or 'density'")
    if opacity <= 0 or opacity >1:
        raise Exception("opacity must be in range (0, 1)")
    if xval not in data.columns:
        raise Exception("xval must be a feature in the input dataframe")
    if color not in data.columns:
        raise Exception("color must be a feature in the input dataframe")

    
    if facet_factor == None:
        if plot_type == "histogram":
            categorical_plot = alt.Chart(data=data, title=title).mark_bar().encode(
                    x = alt.X(xval),
                    y = "count()",
                    color = alt.Color(color, scale=alt.Scale(scheme=color_scheme))
                ).properties(width=plot_width, height=plot_height
                ).configure_title(fontSize = font_size
                ).configure_axis(
                    labelFontSize=font_size,
                    titleFontSize=font_size
                )
        
        else:
            categorical_plot = alt.Chart(data=data, title=title).transform_density(
                    xval,
                    groupby=[color],
                    as_=[xval, "density"]
                ).mark_area(opacity=opacity).encode(
                    x = xval,
                    y = "density:Q",
                    color=alt.Color(color, scale=alt.Scale(scheme=color_scheme))
                ).properties(width=plot_width, height=plot_height
                ).configure_title(fontSize = font_size
                ).configure_axis(
                    labelFontSize=font_size,
                    titleFontSize=font_size
                )
    else:
        if plot_type == "histogram":
            categorical_plot = alt.Chart(data=data).mark_bar().encode(
                    x = alt.X(xval),
                    y = "count()",
                    color = alt.Color(color, scale=alt.Scale(scheme=color_scheme))
                ).properties(width=plot_width, height=plot_height
                ).facet(facet_factor, columns = facet_col, title=title
                ).configure_title(fontSize = font_size
                ).configure_axis(
                    labelFontSize=font_size,
                    titleFontSize=font_size
                )
        
        else:
            categorical_plot = alt.Chart(data=data).transform_density(
                    xval,
                    groupby=[color],
                    as_=[xval, "density"]
                ).mark_area(opacity=opacity).encode(
                    x = xval,
                    y = "density:Q",
                    color=alt.Color(color, scale=alt.Scale(scheme=color_scheme))
                ).properties(width=plot_width, height=plot_height
                ).facet(facet_factor, columns = facet_col, title=title
                ).configure_title(fontSize = font_size
                ).configure_axis(
                    labelFontSize=font_size,
                    titleFontSize=font_size)
        
    return categorical_plot
