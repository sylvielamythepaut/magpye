
"""
speed_green_low
==================

| style = "speed_green_low"

.. image:: /_static/styles/speed_green_low.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

"""

from magpye import GeoMap

map = GeoMap(area_name="europe")

map.contour_shaded("data/10si.grib", style=speed_green_low)
map.gridlines(line_style="dash")
map.coastlines()
map.show()


# sphinx_gallery_thumbnail_path = '_static/styles/speed_green_low.png'

    