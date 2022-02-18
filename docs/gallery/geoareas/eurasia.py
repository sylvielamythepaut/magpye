"""
eurasia
==================

| area_name = "eurasia"  

.. image:: /_static/geoareas/eurasia.png
    :width: 400

| **magpye** has a list of predefined geographical areas.    
| Options are available to customise your Coastlines. 

"""

from magpye import GeoMap

map = GeoMap(area_name="eurasia")


map.coastlines(land_colour="grey")
map.gridlines(line_style="dash")
map.show()


# sphinx_gallery_thumbnail_path = '_static/geoareas/eurasia.png'
