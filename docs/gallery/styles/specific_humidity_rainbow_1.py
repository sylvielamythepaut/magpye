
"""
specific_humidity_rainbow_1
==================

| style = "specific_humidity_rainbow_1"

.. image:: /_static/styles/specific_humidity_rainbow_1.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

The data for this example can be downloaded from one of our repositories:   
`<http://get.ecmwf.int/repository/magpye/data/q.grib>`_

"""

from magpye import GeoMap

map = GeoMap(area_name="europe")

map.contour_shaded("q.grib", style="specific_humidity_rainbow_1")
map.gridlines(line_style="dash")
map.coastlines()
map.save("specific_humidity_rainbow_1.png")

# sphinx_gallery_thumbnail_path = '_static/styles/specific_humidity_rainbow_1.png'

    