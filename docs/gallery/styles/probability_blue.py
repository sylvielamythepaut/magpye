
"""
probability_blue
==================

| style = "probability_blue"

.. image:: /_static/styles/probability_blue.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

"""

from magpye import GeoMap

map = GeoMap(area_name="europe")

map.contour_shaded("data/tpg1.grib", style="probability_blue")
map.gridlines(line_style="dash")
map.coastlines()
map.show()


# sphinx_gallery_thumbnail_path = '_static/styles/probability_blue.png'

    