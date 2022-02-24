
"""
speed_spread_magenta
==================

| style = "speed_spread_magenta"

.. image:: /_static/styles/speed_spread_magenta.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

The data for this example can be downloaded from one of our repositories:   
`<https://get.ecmwf.int/repository/magpye/data/10si_spread.grib>`_


"""

from magpye import GeoMap

map = GeoMap(area_name="europe")

map.contour_shaded("10si_spread.grib", style="speed_spread_magenta")
map.gridlines(line_style="dash")
map.coastlines()
map.legend()
map.save("speed_spread_magenta.png")

# sphinx_gallery_thumbnail_path = '_static/styles/speed_spread_magenta.png'

    