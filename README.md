# map-projections-games

A few simple games with different types of world map projections.

## Looking at water fractions
The fraction of earth covered by water is about 71%
(https://water.usgs.gov/edu/earthhowmuch.html).

A simple question one can ask is how much does this fraction change
when looking at a projection of the globe on a 2d map. For example,
what is the percentage of water in a Mercator map projection?

![Mercator projection](images/merc.png?raw=true "Mercator projection")


Here we simply estimate via Monte Carlo sampling the fraction of water
using python's Basemap.

The rundown is:

| Projection                        | Fraction | Error  |
| --------------------------------- | -------- | ------ |
| Cylindrical Equidistant           |  0.7693  | 0.0019	|
| Mercator                          |  0.7767  | 0.0019	|
| Miller Cylindrical                |  0.7991  | 0.0018	|
| Gall Stereographic Cylindrical    |  0.7800  | 0.0019	|
| Cylindrical Equal Area            |  0.7371  | 0.0020	|
| Azimuthal Equidistant             |  0.6589  | 0.0021	|
| Orthographic                      |  0.4977  | 0.0022	|
| Geostationary                     |  0.7031  | 0.0020	|
| Near-Sided Perspective            |  0.4842  | 0.0022	|
| Mollweide                         |  0.5801  | 0.0022	|
| Hammer                            |  0.5804  | 0.0022	|
| van der Grinten                   |  0.6307  | 0.0022 |
