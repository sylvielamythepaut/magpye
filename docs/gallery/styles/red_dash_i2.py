
"""
red_dash_i2
==================

| style = "red_dash_i2"

.. image:: /_static/styles/red_dash_i2.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

The data for this example can be downloaded from one of our repositories:   
`<https://get.ecmwf.int/repository/magpye/data/2t_mean.grib>`_


"""

from magpye import GeoMap

map = GeoMap(area_name="europe")
map.coastlines(land_colour='grey')
map.contour_lines("2t_mean.grib", style="red_dash_i2")
map.gridlines(line_style="dash", labels=False)
map.coastlines()
map.legend()
map.save("red_dash_i2.png")

# sphinx_gallery_thumbnail_path = '_static/styles/red_dash_i2.png'

    