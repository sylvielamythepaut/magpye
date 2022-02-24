
"""
black_i5
==================

| style = "black_i5"

.. image:: /_static/styles/black_i5.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

Need some data to try ? 
-----------------------

The data for this example can be downloaded from one of our repositories:   
http://get.ecmwf.int/repository/magpye/data/msl.grib

"""

from magpye import GeoMap

map = GeoMap(area_name="europe")
map.coastlines(land_colour='grey')
map.contour_lines("msl.grib", style="black_i5")
map.gridlines(line_style="dash")
map.coastlines()
map.save("black_i5.png")

# sphinx_gallery_thumbnail_path = '_static/styles/black_i5.png'

    