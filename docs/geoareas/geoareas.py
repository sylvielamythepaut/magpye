from Magics import macro as magics
from ecmwf.geomaps import GeoMap
import nbformat as nbf

nb = nbf.v4.new_notebook()
title = """\
# Predefined areas in **mappye**"""
import_magpye = """\
from ecmwf.geomaps import GeoMap"""

nb.cells.append(nbf.v4.new_markdown_cell(title))
nb.cells.append(nbf.v4.new_code_cell(import_magpye))

areas = magics.predefined_areas()

for area in areas:
    title = """\
## {} """.format(area)


    code = """\
map = GeoMap(area_name="{}")
map.coastlines(land_colour="grey")
map.gridlines(line_style="dash")
map.show()""".format(area)
    nb.cells.append(nbf.v4.new_markdown_cell(title))
    nb.cells.append(nbf.v4.new_code_cell(code))

fname = 'test.ipynb'

with open(fname, 'w') as f:
    nbf.write(nb, f)





for area in areas:

    map = GeoMap(area_name=area)
    map.coastlines(land_colour="grey")
    map.gridlines(line_style="dash")
    map.save("{}.png".format(area))