
"""
temperature_spread_magenta
==================

| style = "temperature_spread_magenta"

.. image:: /_static/styles/temperature_spread_magenta.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

The data for this example can be downloaded from one of our repositories:   
`<https://get.ecmwf.int/repository/magpye/data/2t_spread.grib>`_


"""

from magpye import GeoMap

map = GeoMap(area_name="europe")

map.contour_shaded("2t_spread.grib", style="temperature_spread_magenta")
map.gridlines(line_style="dash")
map.coastlines()
map.save("temperature_spread_magenta.png")

# sphinx_gallery_thumbnail_path = '_static/styles/temperature_spread_magenta.png'

    