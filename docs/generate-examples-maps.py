#!/usr/bin/env python3
# (C) Copyright 2020 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#


import os
import yaml
import requests
from magpye import GeoMap


def gallery(method, data, style, background):
    fname = "gallery/styles/{}.py".format(style)
    script = '''
"""
{style}
==================

| style = "{style}"

.. image:: /_static/styles/{style}.png
    :width: 400

| **magpye** has a list of predefined styles, that can be used to visualise your data.
| More options are available to customise your visualisation.

"""

from magpye import GeoMap

map = GeoMap(area_name="europe")
{background}
map.{method}("{data}", style={style})
map.gridlines(line_style="dash")
map.coastlines()
map.show()


# sphinx_gallery_thumbnail_path = '_static/styles/{style}.png'

    '''.format(
        style=style,
        background=background,
        method=method, 
        data=data
    )

    with open(fname, "w") as stream:
        stream.write(script)



def contour_shaded(data, style):
    map = GeoMap(area_name="europe")
    # map.coastlines(land_colour="grey")
    map.contour_shaded(data, style = style)
    map.gridlines(line_style="dash")
    map.coastlines()
    map.save("_static/styles/{}.png".format(style))
    gallery("contour_shaded", data, style, background="")

def contour_lines(data, style):
    map = GeoMap(area_name="europe")
    map.coastlines(land_colour="grey")
    map.contour_lines(data, style = style)
    map.gridlines(line_style="dash")
    map.coastlines()
    map.save("_static/styles/{}.png".format(style))
    gallery("contour_lines", data, style, background="map.coastlines(land_colour='grey')")


url = "http://get.ecmwf.int/repository/magpye/data"
def example(name, method, style):
    methods = {"contour_shaded" : contour_shaded,
            "contour_lines": contour_lines }
          

    if "data" in style:
        print (name , style["data"])
        r = requests.get('{}/{}'.format(url, style["data"]))
        print(r.status_code)
        if r.status_code == 200:
            data = "data/{}".format(style["data"])
            with open(data, "wb") as stream:
                stream.write(r.content)
            
            if method in methods:
                methods[method](data, name)

           
            
       
        



    

for root, _, files in os.walk("../magpye/static/styles"):
    
    for f in files:
        method = os.path.basename(root)
        style = os.path.join(root, f)
        with open(style) as stream:
            s = yaml.safe_load(stream)
            name, ext = f.split(".")
            example(name, method, s)
