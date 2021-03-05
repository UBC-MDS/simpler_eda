import pandas as pd
import altair as alt
import numpy as np
from vega_datasets import data
# need to have scipy as depencies to allow differen types of corr_method

def corr_map(data, features, corr_method='pearson', color_scheme='blueorange', plot_width=450, plot_height=450, title="Correlation Map"):
  """
  Plot a correlation map with the given dataframe object and a list of numerical features. 
  Users are allowed to set multiple arguments regarding the setting of the correlation plot 
  including method to calculate correlation, color schemes, plot width, height, and plot title.

  Parameters
  ----------
  data: pandas.core.frame.DataFrame
    The input dataframe ojbect   

  features: list
    A 1D list with names of numerical feature in str for correlation map plotting.
    It should contain at least 2 features.
  
  corr_method: str, optional
    The method to calculate correlation between features. The default is "Pearson", 
    two other supported methods are "'kendall' and 'spearman'.

  color_scheme: str, optional
    The color scheme
    Other diverging color schemes can be "blueorange, "redgrey", "purpleorange", etc.
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
  >>> corr_map(df, ["Horsepower", "Displacement", "Cylinders", "Acceleration"])
  """
  #Checking for valid inputs:
  if not isinstance(data, pd.DataFrame):
    raise Exception("the input data is not a panda dataframe.")
  if not isinstance(features, list):
    raise Exception("the features for  is not a list")
  if features not in list(data.columns):
  # if set(features)<=set(list(data.columns)): both not working not sure the reason..ss
    raise Exception("The features or one of the feature is not available the dataframe provided.")
  if not all(isinstance(f, str) for f in features):
    raise Exception("All the entries in the feature list should be a string")
  if corr_method not in ['pearson', 'kendall', 'spearman']:
    raise Exception("The correlation method should be 'pearson', 'kendall',  or'spearman'")
  if not isinstance(color_scheme, str):
    raise Exception("The color scheme should be given as a string")
  if not isinstance(plot_width, int):
    raise Exception("The plot_width should be given as an integer")
  if not isinstance(plot_height, int):
    raise Exception("The plot_height should be given as an integer")
  if not isinstance(title, str):
    raise Exception("The title should be given as a string")

  selected_cols = data[features]

  corr_df = selected_cols.corr(corr_method).stack().reset_index(name='corr')
    
  corr_map = alt.Chart(corr_df, title=title).mark_rect(opacity=0.45).encode(
    alt.X('level_0', title=""),
    alt.Y('level_1', title=""),
    alt.Size('corr', title="Correlation"),
    alt.Color('corr', scale=alt.Scale(scheme=color_scheme, reverse=True, domain=(-1,1)), title="Correlation"),
    alt.Tooltip(["level_0", "level_1"])
    ).configure_axis(labelFontSize=15
    ).configure_title(fontSize=20
    ).configure_legend(titleFontSize=14, titleAlign = "center", labelFontSize=13
    ).properties(width=plot_width, height=plot_height
    ).interactive()

# gradientOpacity=1 in configure_legend

  return corr_map

