
"""
speed_green_low
==================

| style = "speed_green_low"

.. image:: /_static/styles/speed_green_low.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

The data for this example can be downloaded from one of our repositories:   
`<http://get.ecmwf.int/repository/magpye/data/10si.grib>`_

"""

from magpye import GeoMap

map = GeoMap(area_name="europe")

map.contour_shaded("10si.grib", style="speed_green_low")
map.gridlines(line_style="dash")
map.coastlines()
map.save("speed_green_low.png")

# sphinx_gallery_thumbnail_path = '_static/styles/speed_green_low.png'

    