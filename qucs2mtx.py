#!/usr/bin/python -W ignore::DeprecationWarning

import numpy as np
import parse_result as pr
import sys as sys
import time as time

args = sys.argv
print('Processing file: %s' % str(args[1]))

filename=args[1]
qucs_data = pr.parse_file(str(filename))

if len(sys.argv) < 3:
    print('Variable list in file:')
    for key, value in qucs_data.items():
        if isinstance(data[key], dict) is False:
               print ('%s\t\t%s' % (key, data[key].shape))
    sys.exit()       

key=sys.argv[2]
data = qucs_data[key].real
outfile = filename + '.' + time.strftime('%Y-%m-%d-%H.%M.%S') + '.' + key + '.mtx'

print('Exporting variable %s, size %s to file %s' % (key, data.shape, outfile))

fp = open(outfile, 'wb')
metadata = '%d %d %d 8\n' % (data.shape[0], data.shape[1], data.shape[2])
fp.write(metadata.encode('ascii'))
# This should be by default float64 binary to disk?
#np.array(data, dtype=np.float64).tofile(fp)
# why the fuck is this giving a syntax error!!??!! (It was a missing bracke above!!!)
data.tofile(fp)
fp.close()


#
#f = data['frequency']
#var = data['Z']
#y=data['y']
#
#outf=open('out.dat', 'wb')
#for i in range(0,var.shape[0]):
#    out = np.real(y[i]);
#    np.savetxt(outf, out);
#    outf.write('\n');
#outf.close();
