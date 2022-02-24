
"""
accumulated_tp_1000
==================

| style = "accumulated_tp_1000"

.. image:: /_static/styles/accumulated_tp_1000.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

The data for this example can be downloaded from one of our repositories:   
|location_link|

.. |location_link| raw:: html

   <a href="http://get.ecmwf.int/repository/magpye/data/tp_acc.grib"> http://get.ecmwf.int/repository/magpye/data/tp_acc.grib  </a>


"""

from magpye import GeoMap

map = GeoMap(area_name="europe")

map.contour_shaded("tp_acc.grib", style="accumulated_tp_1000")
map.gridlines(line_style="dash")
map.coastlines()
map.save("accumulated_tp_1000.png")

# sphinx_gallery_thumbnail_path = '_static/styles/accumulated_tp_1000.png'

    