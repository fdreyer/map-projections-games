# Frederic Dreyer, 2017

"""Small script to look at different projections and check how the
land v. water fraction changes."""

import numpy as np
import mpl_toolkits.basemap as bm
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Sample all maps n times')
parser.add_argument('-n', type=int, default=50000, dest='nsample')

nsample = parser.parse_args().nsample
path    = 'images/'

# set up the projections we want to consider
projections = ['cyl','merc','mill','gall','cea','aeqd','ortho',
               'geos','nsper','sinu','moll','hammer','robin',
               'eck4','kav7','vandg','mbtfpq']

# get a description for each projection keyword
descriptions={}
for x in bm.supported_projections.split('\n'):
    vals=list(filter(None,x.split('  ')))
    if len(vals) > 0:
        descriptions[vals[0].strip()] = vals[1].strip()

water_frac = {}
# loop over all projections and calculate water fraction
for proj in projections:
    fn = path+proj+'.png'
    print('Processing {}, saving image to {}'.format(proj,fn))
    # createa a map with desired projection
    if proj=='merc':
        # for the mercator projection, take latitude in range [-82,82]
        m=bm.Basemap(llcrnrlat=-82,urcrnrlat=82,llcrnrlon=-180,urcrnrlon=180,
                     projection=proj)
    else:
        m=bm.Basemap(lat_0=0,lon_0=0, projection=proj)
    # find the x and y boundaries
    xbounds = [m.xmin, m.xmax]
    ybounds = [m.ymin, m.ymax]
    fraction_water = 0.0
    for i in range(nsample):
        r = np.random.rand(2)
        x = xbounds[0] + r[0]*(xbounds[1] - xbounds[0])
        y = ybounds[0] + r[1]*(ybounds[1] - ybounds[0])
        if not m.is_land(x,y):
            fraction_water += 1.0
    fraction_water /= float(nsample)
    # the standard deviation is sqrt(n * p * (1-p))/n
    error_fraction = np.sqrt(fraction_water * (1.0-fraction_water)/nsample)
    water_frac[proj] = [fraction_water, error_fraction]
    plt.figure(figsize=(12,9))
    m.drawmapboundary(fill_color='#A6CAE0')
    m.fillcontinents(color='white', alpha=1.0)
    plt.savefig(path+proj+'.png',bbox_inches='tight')
    plt.close()

for proj in projections:
    print('%-33s :  %.4f +- %.4f' % (descriptions[proj],
                                    water_frac[proj][0],
                                    water_frac[proj][1]))

