import altair as alt
import numpy as np
import pandas as pd
import pytest
from vega_datasets import data
from simpler_eda.categorical_eda import categorical_eda

cars = data.cars()

categorical_histogram_facet = categorical_eda(data = cars,
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

categorical_histogram = categorical_eda(data = cars,
                                         xval = "Origin",
                                         plot_type = "histogram",
                                         color = "Origin",
                                         title = "Histogram",
                                         font_size = 10,
                                         color_scheme = "yellowgreenblue",
                                         plot_height = 200,
                                         plot_width = 400)

categorical_density_facet = categorical_eda(data = cars,
                                       xval = "Horsepower",
                                       plot_type = "density",
                                       color = "Origin",
                                       title = "Density Plot",
                                       font_size = 15,
                                       color_scheme = "dark2",
                                       plot_height = 200,
                                       plot_width = 400,
                                       facet_factor = "Origin",
                                       facet_col = 3,
                                       opacity = 0.4)
                                       
categorical_density = categorical_eda(data = cars,
                                       xval = "Horsepower",
                                       plot_type = "density",
                                       color = "Origin",
                                       title = "Density Plot",
                                       font_size = 15,
                                       color_scheme = "dark2",
                                       plot_height = 200,
                                       plot_width = 400,
                                       opacity = 0.4)
                                      
                                       
def test_categorical_eda():
    """
    Tests the categorical_eda function to make sure the output plot are correct. 
    
    Returns
    -------
    None
        The test should pass and no asserts error should be displayed. 
    """
    #testings for the histogram with facet
    assert str(type(categorical_histogram_facet)) == "<class 'altair.vegalite.v4.api.FacetChart'>", \
    "the returned object should be an altair plot"
    assert categorical_histogram_facet.columns == 3, \
    "number of columns facetted should be 3, as specified"
    assert categorical_histogram_facet.facet.shorthand == "Year", \
    "Facet factor should be 'Year', as specified"
    assert categorical_histogram_facet.config.title.fontSize == 10, \
    "Title font size should be 10, as speicified"
    assert categorical_histogram_facet.data.shape == cars.shape, \
    "the shape of data should be the same as input"
    assert categorical_histogram_facet.title == "Histogram", \
    "the plot title should be 'Histogram', as specified"
    
    #testing for the histogram without facet
    assert str(type(categorical_histogram)) == "<class 'altair.vegalite.v4.api.Chart'>", \
    "the returned object should be an altair plot"
    assert categorical_histogram.config.title.fontSize == 10, \
    "Title font size should be 10, as speicified"
    assert categorical_histogram.data.shape == cars.shape, \
    "the shape of data should be the same as input"
    assert categorical_histogram.title == "Histogram", \
    "the plot title should be 'Histogram', as specified"
    assert categorical_histogram.encoding.x.shorthand == "Origin", \
    "Origin should be mapped to the x-axis"
    assert categorical_histogram.encoding.y.shorthand == "count()", \
    "count should be mapped to the y-axis for histogram"
    
    #testing for the density plot with facet
    assert str(type(categorical_density_facet)) == "<class 'altair.vegalite.v4.api.FacetChart'>", \
    "the returned object should be an altair plot"
    assert categorical_density_facet.columns == 3, \
    "number of columns facetted should be 3, as specified"
    assert categorical_density_facet.facet.shorthand == "Origin", \
    "Facet factor should be 'Origin', as specified"
    assert categorical_density_facet.config.title.fontSize == 15, \
    "Title font size should be 15, as speicified"
    assert categorical_density_facet.config.axis.labelFontSize == 15, \
    "Axis label font size should be 15, as speicified"
    assert categorical_density_facet.title == "Density Plot", \
    "the plot title should be 'Density Plot', as specified"
    assert categorical_density_facet.data.shape == cars.shape, \
    "the shape of data should be the same as input"
    
    #testings for the density plot without facet
    assert str(type(categorical_density)) == "<class 'altair.vegalite.v4.api.Chart'>", \
    "the returned object should be an altair plot"
    assert categorical_density.mark.type == "area", \
    "mark of density plot should be 'area'"
    assert categorical_density.encoding.x.shorthand == "Horsepower", \
    "Horsepower should be mapped to the x-axis"
    assert categorical_density.encoding.y.shorthand == "density:Q", \
    "Density should be mapped to the y-axis"
    assert categorical_density.encoding.color.scale.scheme == "dark2", \
    "color scheme should be 'dark2', as specified"
    assert categorical_density.height == 200, \
    "plot height should be 200, as specified"
    assert categorical_density.data.shape == cars.shape, \
    "the shape of data should be the same as input"
    
   
    
def test_categorical_eda_exceptions():
    """
    Tests for exceptions handling. 
    
    Returns
    -------
    None
        The test should pass and no asserts error should be displayed. 
    """
    try:
        categorical_eda(data = list(cars),
                         xval = "Horsepower",
                         plot_type = "density",
                         color = "Origin",
                         title = "Density Plot",
                         font_size = 15,
                         color_scheme = "dark2",
                         plot_height = 200,
                         plot_width = 400,
                         opacity = 0.4)
    except Exception as e:
        assert str(e) == "the input data has to be a dataframe."
    
    try:
        categorical_eda(data = cars,
                         xval = "Horsepower",
                         plot_type = "density",
                         color = "Origin",
                         title = "Density Plot",
                         font_size = 15,
                         color_scheme = "dark2",
                         plot_height = 200,
                         plot_width = 400,
                         facet_col = 3,
                         opacity = 0.4)
    except Exception as e:
        assert str(e) == "facet_factor must be provided along with facet_col."

    try:
        categorical_eda(data = cars,
                         xval = "Horsepower",
                         plot_type = "density",
                         color = "Origin",
                         title = "Density Plot",
                         font_size = 15,
                         color_scheme = "dark2",
                         plot_height = 200,
                         plot_width = 400,
                         facet_factor = "Year",
                         opacity = 0.4)
    except Exception as e:
        assert str(e) == "Specify facet_col for facetting the plot"

    try:
        categorical_eda(data = cars,
                         xval = "Horsepower",
                         plot_type = "scatter",
                         color = "Origin",
                         title = "Density Plot",
                         font_size = 15,
                         color_scheme = "dark2",
                         plot_height = 200,
                         plot_width = 400,
                         opacity = 0.4)
    except Exception as e:
        assert str(e) == "plot_type must be either 'histogram' or 'density'"

    try:
        categorical_eda(data = cars,
                         xval = "Horsepower",
                         plot_type = "histogram",
                         color = "Origin",
                         title = "Density Plot",
                         font_size = 15,
                         color_scheme = "dark2",
                         plot_height = 200,
                         plot_width = 400,
                         opacity = 1.5)
    except Exception as e:
        assert str(e) == "opacity must be in range (0, 1)"
 
    try:
        categorical_eda(data = cars,
                         xval = "Country",
                         plot_type = "histogram",
                         color = "Origin",
                         title = "Density Plot",
                         font_size = 15,
                         color_scheme = "dark2",
                         plot_height = 200,
                         plot_width = 400,
                         opacity = 0.4)
    except Exception as e:
        assert str(e) == "xval must be a feature in the input dataframe"
        
    try:
        categorical_eda(data = cars,
                         xval = "Origin",
                         plot_type = "histogram",
                         color = "Country",
                         title = "Density Plot",
                         font_size = 15,
                         color_scheme = "dark2",
                         plot_height = 200,
                         plot_width = 400,
                         opacity = 0.4)
    except Exception as e:
        assert str(e) == "color must be a feature in the input dataframe"

