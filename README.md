# map-projections-games
A few games with different types of projections of world maps.

## Looking at water fractions
The fraction of earth covered by water is about 71%
(https://water.usgs.gov/edu/earthhowmuch.html)

A simple question is how does this fraction change when looking at a
projection of the globe on a 2d map. For example, what is the
percentage of water in a Mercator map projection?

Here we simply estimate via Monte Carlo the fraction of water using
python's Basemap.

The rundown is:

| Projection                        | Fraction | Error   |
| --------------------------------- | -------- | ------- |
| Cylindrical Equidistant           | 0.76528  | 0.00190 |
| Mercator                          | 0.93496  | 0.00110 |
| Miller Cylindrical                | 0.79562  | 0.00180 |
| Gall Stereographic Cylindrical    | 0.78514  | 0.00184 |
| Cylindrical Equal Area            | 0.74032  | 0.00196 |
| Azimuthal Equidistant             | 0.87124  | 0.00150 |
| Orthographic                      | 0.71428  | 0.00202 |
| Geostationary                     | 0.70108  | 0.00205 |
| Near-Sided Perspective            | 0.70324  | 0.00204 |
| Sinusoidal                        | 0.83598  | 0.00166 |
| Mollweide                         | 0.79486  | 0.00181 |
| Hammer                            | 0.79400  | 0.00181 |
| Robinson                          | 0.77758  | 0.00186 |
| Eckert IV                         | 0.76992  | 0.00188 |
| Kavrayskiy VII                    | 0.78846  | 0.00183 |
| van der Grinten                   | 0.84238  | 0.00163 |
| McBryde-Thomas Flat-Polar Quartic | 0.79544  | 0.00180 |
