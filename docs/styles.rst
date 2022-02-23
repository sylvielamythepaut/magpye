Predefined styles
=================

Here is the list of the predefined styles define in **magpye**,

To create a map

.. code-block:: python

   from magpye import GeoMap
   
   geomap = GeoMap(area_name="europe")
   geomap.coastlines(land_colour="grey")
   geomap.contour_lines("style/iso.grib", style = "black_i5")
   geomap.show()

.. image:: _static/examples/styles.png
   :width: 50%

.. toctree::
   :maxdepth: 2
   :glob:

   styles/*