import altair as alt
import numpy as np
import pandas as pd
import pytest
from vega_datasets import data
from simpler_eda.categorical_eda import categorical_plot

cars = data.cars()

categorical_histogram = categorical_plot(data = cars,
                                         xval = "Origin",
                                         plot_type = "histogram",
                                         color = "Origin",
                                         title = "Histogram",
                                         font_size = 10,
                                         color_scheme = "yellowgreenblue",
                                         plot_height = 200,
                                         plot_width = 400,
                                         facet_factor = "Year",
                                         facet_col=3)

categorical_density = categorical_plot(data = cars,
                                       xval = "Horsepower",
                                       plot_type = "density",
                                       color = "Origin",
                                       title = "Density Plot",
                                       font_size = 15,
                                       color_scheme = "dark2",
                                       plot_height = 200,
                                       plot_width = 400,
                                       opacity = 0.4)
def test_categorical_plot():
    #testings for the histogram
    assert categorical_histogram.columns == 3, "number of columns facetted should be 3, as specified"
    assert categorical_histogram.facet.shorthand == "Year", "Facet factor should be 'Year', as specified"
    assert categorical_histogram.config.title.fontSize == 10, "Title font size should be 10, as speicified"
    assert categorical_histogram.data.shape == cars.shape, "the shape of data should be the same as input"
    assert categorical_histogram.title == "Histogram", "the plot title should be 'Histogram', as specified"
    
    #testings for the density plot
    assert str(type(categorical_density)) == "<class 'altair.vegalite.v4.api.Chart'>", "the returned object should be an altair plot"
    assert categorical_density.mark.type == "area", "mark of density plot should be 'area'"
    assert categorical_density.encoding.x.shorthand == "Horsepower", "Horsepower should be mapped to the x-axis"
    assert categorical_density.encoding.y.shorthand == "density:Q", "Density should be mapped to the y-axis"
    assert categorical_density.encoding.color.scale.scheme == "dark2", "color scheme should be 'dark2', as specified"
    assert categorical_density.height == 200, "plot height should be 200, as specified"
