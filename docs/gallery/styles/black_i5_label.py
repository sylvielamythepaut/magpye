
"""
black_i5_label
==================

| style = "black_i5_label"

.. image:: /_static/styles/black_i5_label.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

Need some data to try ? 
-----------------------

The data for this example can be downloaded from one of our repositories:   
http://get.ecmwf.int/repository/magpye/data/10si.grib

"""

from magpye import GeoMap

map = GeoMap(area_name="europe")
map.coastlines(land_colour='grey')
map.contour_lines("10si.grib", style="black_i5_label")
map.gridlines(line_style="dash")
map.coastlines()
map.save("black_i5_label.png")

# sphinx_gallery_thumbnail_path = '_static/styles/black_i5_label.png'

    