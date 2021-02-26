# A package for Simpler Explanatory Data Analysis (simpler_eda)

![](https://github.com/nichowu/simpler_eda/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/nichowu/simpler_eda/branch/main/graph/badge.svg)](https://codecov.io/gh/nichowu/simpler_eda) ![Release](https://github.com/nichowu/simpler_eda/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/simpler_eda/badge/?version=latest)](https://simpler_eda.readthedocs.io/en/latest/?badge=latest)


## Overview

Exploratory Data analysis (EDA) is an important step in any data analysis.  However, carrying out EDA with the Altair package requires a lot of coding effort. Moreover, it assumes a basic knowledge of functions and grammar of graphics syntax that are appropriate for visualizing categorical and numerical variables. The simpler_eda package addresses this issue by providing functions that are tailored to produce categorical, numerical and correlation plots using a single line of code. Furthermore, the package provides customization capability for the plots based on specific user needs (theme, title, font, size and etc.). The users are able to spend more time on analyzing the data set and less time configuring Altair plot settings.

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ simpler_eda
```

## Functions

This package contains three functions, each that accepts a pandas `DataFrame` for EDA. No specific data set is required for the functions to work. Each functions will have it's own required and optional arguements to configure the properties of the plot. 

1. `correlation_eda_plot:` This function takes in a data frame object, a list of numerical features to be correlated (instead of all features) and outputs a correlation plot object. User can optionally change default arguements for color/fill, title, size of text and color-scheme.

2. `numerical_eda_plot:` This function takes in a data frame object, two numeric columns, and produces either a scatter or line plot to visualize the relationship of the two features. User can optionally change default arguements for plot-type, color/fill, title, size of text, color-scheme and apply logarithm scaling on the x and y axis.

3. `categorical_eda_plot:` This function takes in a data frame object, a numerical and a categorical column and produces either a jitter, violin, barchar and boxplot (two categoricals) for comparison. User can optionally change default arguements for plot-type, color/fill, title, size of text and color-scheme.

## How the simpler_eda package fits into the Python ecosystem

The simpler_eda package improves upon existing functions in the Altair packages library. Altair already includes many useful functions to visualize relationship between numerical and categorical features with the use of grammar of graphics syntax. But often this is quite cumbersome and prone to errors, simpler_eda package provides convenience by allowing user to perform EDA with a single line of code. There are a number of packages that already provides similar functionality in the Python Ecosystem, but most of them are not easily customizable. Some examples of the packages are [pandas profiling](https://github.com/pandas-profiling/pandas-profiling), [DataPrep](https://docs.dataprep.ai/index.html), [SweetViz](https://pypi.org/project/sweetviz/) and [Holoviwes](https://github.com/holoviz/holoviews).

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
