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
| Cylindrical Equidistant           |  0.7656  | 0.0019 |
| Mercator                          |  0.7738  | 0.0019 |
| Miller Cylindrical                |  0.7950  | 0.0018 |
| Gall Stereographic Cylindrical    |  0.7862  | 0.0018 |
| Cylindrical Equal Area            |  0.7420  | 0.0020 |
| Azimuthal Equidistant             |  0.8726  | 0.0015 |
| Orthographic                      |  0.7125  | 0.0020 |
| Geostationary                     |  0.6996  | 0.0021 |
| Near-Sided Perspective            |  0.6991  | 0.0021 |
| Sinusoidal                        |  0.8368  | 0.0017 |
| Mollweide                         |  0.7976  | 0.0018 |
| Hammer                            |  0.7945  | 0.0018 |
| Robinson                          |  0.7801  | 0.0019 |
| Eckert IV                         |  0.7678  | 0.0019 |
| Kavrayskiy VII                    |  0.7910  | 0.0018 |
| van der Grinten                   |  0.8421  | 0.0016 |
| McBryde-Thomas Flat-Polar Quartic |  0.7894  | 0.0018 |

