import pandas as pd
import altair as alt
import numpy as np


def corr_map(data, features, color_schme='yellowgreenblue', plot_width=400, plot_height=300, title="Correlation Map"):
  """
  Plot a correlation map with the given dataframe object and a list of numerical features. 
  Users are allowed to set multiple arguments regarding the setting of the correlation plot 
  including color schemes, plot width, height, and plot title.

  Parameters
  ----------
  data: pandas.core.frame.DataFrame
    The input dataframe ojbect   

  features: list
    A 1D list with names of numerical feature in str for correlation map plotting.
    It should contain at least 2 features.

  color_scheme: str, optional
    The color scheme
    Other color schemes can be "blues", "tealblues", "oranges", "greenblue", "redpurple", etc.
    Other proper color scheme reference can be found in https://vega.github.io/vega/docs/schemes/

  plot_width: int, optional
    The width of the plot

  plot_height: int, optional
    The heigh of the plot

  title: str, optional
    The title of the correlation map

  Returns
  -------
  `altair`
    The altair correlation map plot

  Examples
  --------
  >>> import pandas as pd
  >>> import altair as alt
  >>> import numpy as np
  >>> from simpler_eda.corr_map import corr_map
  >>> from vega_datasets import data
  >>> df = data.cars()
  >>> corr_map(df, ["age", "height", "income"])
  """

  return corr_map
