
"""
precipitation_blue_red_250
==================

| style = "precipitation_blue_red_250"

.. image:: /_static/styles/precipitation_blue_red_250.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

"""

from magpye import GeoMap

map = GeoMap(area_name="europe")

map.contour_shaded("data/tp.grib", style="precipitation_blue_red_250")
map.gridlines(line_style="dash")
map.coastlines()
map.show()


# sphinx_gallery_thumbnail_path = '_static/styles/precipitation_blue_red_250.png'

    