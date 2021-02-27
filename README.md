# A package for Simpler Explanatory Data Analysis (simpler_eda)

![](https://github.com/nichowu/simpler_eda/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/nichowu/simpler_eda/branch/main/graph/badge.svg)](https://codecov.io/gh/nichowu/simpler_eda) ![Release](https://github.com/nichowu/simpler_eda/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/simpler_eda/badge/?version=latest)](https://simpler_eda.readthedocs.io/en/latest/?badge=latest)


## Overview

Exploratory Data analysis (EDA) is an important step in any data analysis.  However, carrying out EDA with the Altair package requires a lot of coding effort. Moreover, it assumes a basic knowledge of functions and grammar of graphics syntax that are appropriate for visualizing categorical and numerical variables. The simpler_eda package addresses this issue by providing functions that are tailored to produce categorical, numerical and correlation plots using a single line of code. Furthermore, the package provides customization capability for the plots based on specific user needs (theme, title, font, size and etc.). The users are able to spend more time on analyzing the data set and less time configuring Altair plot settings.

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ simpler_eda
```

## Functions

This package contains three functions, each that accepts a pandas `DataFrame` for EDA. The EDA functions can be used with a dataset with numerical and categorical features. Each functions will have it's own required and optional arguments to configure the properties of the plot. 

1. `correlation_eda_plot:`  Plot a correlation map with the given dataframe object and a list of numerical features. Users are allow to set multiple arguments regarding the setting of the correlation plot from color schemes, plot width, height and plot title.

2. `numerical_eda_plot:` This function takes in a data frame object, two numeric columns, and produces either a scatter or line plot to visualize the relationship between the two features. User can optionally change default arguments for plot-type, color, title, size of text, color-scheme, and toggle log transformation for the x and y axis.

3. `categorical_eda_plot:`  This function takes in a data frame object and one categorical feature, to produce a histogram plot that visualizes the distribution of the feature. User can also choose to plot density graph of the feature by specifing in plot_type. The function also offers customization on color, plot title, font size, color-scheme, plot size, opacity level and facet factor.

## How the simpler_eda package fits into the Python ecosystem

The simpler_eda package improves upon existing functions in the Altair packages library. Altair already includes many useful functions to visualize the relationship between numerical and categorical features with the use of grammar of graphics syntax. But often this is quite cumbersome and prone to errors, simpler_eda package provides convenience by allowing users to perform EDA with a single line of code. There are a number of packages that already provide similar functionality in the Python Ecosystem, such as [pandas profiling](https://github.com/pandas-profiling/pandas-profiling), [DataPrep](https://docs.dataprep.ai/index.html), [SweetViz](https://pypi.org/project/sweetviz/) and [Holoviwes](https://github.com/holoviz/holoviews). However, most of them are not easily customizable. Our simpler_eda package allows flexibility from plot types to plot titles.

## Dependencies

- TODO

## Usage

- TODO

## Documentation

The official documentation is hosted on Read the Docs: https://simpler_eda.readthedocs.io/en/latest/

## Contributors

### Development Lead

|Contributor Name     | GitHub Username|
|---------------------|-----------|
|Cheuk (Chuck) Ho  | [ChuckHo777](https://github.com/marvinmin)|
|Deepak Sidhu      | [Deepak](https://github.com/deepaksidhu)     |
|Nicholas Wu       | [Nicholas Wu](https://github.com/nichowu) |

We welcome and recognize all contributions. Please find the guide for contribution in [Contributing Document](https://github.com/UBC-MDS/simpler_eda/blob/main/CONTRIBUTING.rst).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
