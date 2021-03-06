# simpler_eda

![](https://github.com/UBC-MDS/simpler_eda/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/simpler_eda/branch/main/graph/badge.svg?token=ECSQE5SC2R)](https://codecov.io/gh/UBC-MDS/simpler_eda) [![Deploy](https://github.com/UBC-MDS/simpler_eda/actions/workflows/deploy.yml/badge.svg)](https://github.com/UBC-MDS/simpler_eda/actions/workflows/deploy.yml) [![Documentation Status](https://readthedocs.org/projects/simpler_eda/badge/?version=latest)](https://simpler_eda.readthedocs.io/en/latest/?badge=latest)

## Overview

Exploratory Data analysis (EDA) is an important step in any data analysis. However, carrying out EDA with the Altair package requires a lot of coding effort. Moreover, it assumes a basic knowledge of functions and grammar of graphics syntax that are appropriate for visualizing categorical and numerical variables. The simpler_eda package addresses this issue by providing functions that are tailored to produce categorical, numerical and correlation plots using a single line of code. Furthermore, the package provides customization capability for the plots based on specific user needs (theme, title, font, size and etc.). The users are able to spend more time on analyzing the data set and less time configuring Altair plot settings.

## Installation

``` {.bash}
$ pip install -i https://test.pypi.org/simple/ simpler_eda
```

## Functions

This package contains three functions, each that accepts a pandas `DataFrame` for EDA. The EDA functions can be used with a dataset with numerical and categorical features. Each functions will have it's own required and optional arguments to configure the properties of the plot.

1.  `corr_map:` Plot a correlation map with the given dataframe object and a list of numerical features. Users are allowed to set multiple arguments regarding the setting of the correlation plot including color schemes, plot width, height, and plot title.

2.  `numerical_eda:` This function takes in a data frame object, two numeric columns, and produces either a scatter or line plot to visualize the relationship between the two numerical features. Users can optionally change default arguments for plot-type, color, title, size of text, color-scheme, and toggle log transformation for the x and y axis.

3.  `categorical_eda:` This function takes in a data frame object and one categorical feature, to produce a histogram plot that visualizes the distribution of the feature. Users can also choose to plot the density graph of the feature by specifying in plot_type. The function also offers customization on color, plot title, font size, color-scheme, plot size, opacity level, and facet factor.

## How the simpler_eda package fits into the Python ecosystem

The simpler_eda package improves upon existing functions in the Altair packages library. Altair already includes many useful functions to visualize the relationship between numerical and categorical features with the use of grammar of graphics syntax. But often this is quite cumbersome and prone to errors, simpler_eda package provides convenience by allowing users to perform EDA with a single line of code. There are a number of packages that already provide similar functionality in the Python Ecosystem, such as [pandas profiling](https://github.com/pandas-profiling/pandas-profiling), [DataPrep](https://docs.dataprep.ai/index.html), [SweetViz](https://pypi.org/project/sweetviz/) and [Holoviwes](https://github.com/holoviz/holoviews). However, most of them are not easily customizable. Our simpler_eda package allows flexibility from plot types, color scheme, to plot titles.

## Dependencies

### Dependencies

-   [python = \^3.8](https://www.python.org/)
-   [pandas = \^1.2.3](https://pandas.pydata.org/)
-   [altair = \^4.1.0](https://altair-viz.github.io/)
-   [vega-datasets = \^0.9.0](https://github.com/altair-viz/vega_datasets)

## Usage

### Correlation Plot

``` {.python}
import pandas as pd
import altair as alt
import numpy as np
from simpler_eda.corr_map import corr_map
from vega_datasets import data
df = data.cars()
corr_map(df,
    ["Horsepower", "Displacement", "Cylinders", "Acceleration"])
```

<img src="img/corr_map_example.png" width="600"/>

### Numerical Plot

``` {.python}
import altair as alt
import pandas as pd
import numpy as np
from simpler_eda.numerical_eda import numerical_eda
from vega_datasets import data
numerical_eda(data.cars(), xval = "Horsepower", yval = "Acceleration",
    plot_type = "scatter",
                 color = "Origin",
                 title = " Horsepower vs Acceleration",
                 font_size = 10)
```

<img src="img/numerical_plot.png" width="100%"/>

### Categorical Plot

``` {.python}
import altair as alt
import numpy as np
import pandas as pd
from simpler_eda.categorical_eda import categorical_eda
from vega_datasets import data
cars = data.cars()
categorical_eda(data = cars,
                        xval = "Horsepower",
                        color = "Origin",
                        title = "Histogram of Horsepower in Different Origins",
                        plot_height = 200,
                        plot_width = 400,
                        color_scheme="tableau10"
                        )
```

<img src="img/categorical_plot.png" width="100%"/>

## Documentation

The official documentation is hosted on Read the Docs: <https://simpler_eda.readthedocs.io/en/latest/>

## Contributors

### Development Lead

| Contributor Name | GitHub Username                               |
|------------------|-----------------------------------------------|
| Cheuk (Chuck) Ho | [ChuckHo777](https://github.com/ChuckHo777)   |
| Deepak Sidhu     | [deepaksidhu](https://github.com/deepaksidhu) |
| Nicholas Wu      | [nichowu](https://github.com/nichowu)         |

We welcome and recognize all contributions. Please find the guide for contribution in [Contributing Document](https://github.com/UBC-MDS/simpler_eda/blob/main/CONTRIBUTING.rst).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
