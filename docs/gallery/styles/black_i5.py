
"""
black_i5
==================

| style = "black_i5"

.. image:: /_static/styles/black_i5.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

The data for this example can be downloaded from one of our repositories:   
`<https://get.ecmwf.int/repository/magpye/data/msl.grib>`_


"""

from magpye import GeoMap

map = GeoMap(area_name="europe")
map.coastlines(land_colour='grey')
map.contour_lines("msl.grib", style="black_i5")
map.gridlines(line_style="dash")
map.coastlines()
map.legend()
map.save("black_i5.png")

# sphinx_gallery_thumbnail_path = '_static/styles/black_i5.png'

    