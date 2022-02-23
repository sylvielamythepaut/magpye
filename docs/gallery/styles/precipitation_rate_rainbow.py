
"""
precipitation_rate_rainbow
==================

| style = "precipitation_rate_rainbow"

.. image:: /_static/styles/precipitation_rate_rainbow.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

"""

from magpye import GeoMap

map = GeoMap(area_name="europe")

map.contour_shaded("data/tprate.grib", style=precipitation_rate_rainbow)
map.gridlines(line_style="dash")
map.coastlines()
map.show()


# sphinx_gallery_thumbnail_path = '_static/styles/precipitation_rate_rainbow.png'

    