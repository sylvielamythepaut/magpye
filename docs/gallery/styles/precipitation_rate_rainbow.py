
"""
precipitation_rate_rainbow
==================

| style = "precipitation_rate_rainbow"

.. image:: /_static/styles/precipitation_rate_rainbow.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

The data for this example can be downloaded from one of our repositories:   
`<https://get.ecmwf.int/repository/magpye/data/tprate.grib>`_


"""

from magpye import GeoMap

map = GeoMap(area_name="europe")

map.contour_shaded("tprate.grib", style="precipitation_rate_rainbow")
map.gridlines(line_style="dash", labels=False)
map.coastlines()
map.legend()
map.save("precipitation_rate_rainbow.png")

# sphinx_gallery_thumbnail_path = '_static/styles/precipitation_rate_rainbow.png'

    