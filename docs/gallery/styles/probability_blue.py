
"""
probability_blue
==================

| style = "probability_blue"

.. image:: /_static/styles/probability_blue.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

The data for this example can be downloaded from one of our repositories:   
|location_link|

.. |location_link| raw:: html

   <a href="http://get.ecmwf.int/repository/magpye/data/tpg1.grib"> http://get.ecmwf.int/repository/magpye/data/tpg1.grib  </a>


"""

from magpye import GeoMap

map = GeoMap(area_name="europe")

map.contour_shaded("tpg1.grib", style="probability_blue")
map.gridlines(line_style="dash")
map.coastlines()
map.save("probability_blue.png")

# sphinx_gallery_thumbnail_path = '_static/styles/probability_blue.png'

    