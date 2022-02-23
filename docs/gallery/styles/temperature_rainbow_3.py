
"""
temperature_rainbow_3
==================

| style = "temperature_rainbow_3"

.. image:: /_static/styles/temperature_rainbow_3.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

"""

from magpye import GeoMap

map = GeoMap(area_name="europe")

map.contour_shaded("data/2t.grib", style="temperature_rainbow_3")
map.gridlines(line_style="dash")
map.coastlines()
map.show()


# sphinx_gallery_thumbnail_path = '_static/styles/temperature_rainbow_3.png'

    