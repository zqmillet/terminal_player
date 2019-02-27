import sys; from PIL import Image; import numpy as np

chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))

f, SC, GCF, WCF = './videos/JZM1947.jpg', 0.1, 2, 8/4

img = Image.open(f)

import pdb; pdb.set_trace()
S = (round(img.size[0]*SC*WCF), round(img.size[1]*SC) )

img = np.sum( np.asarray( img.resize(S) ), axis=2)

img -= img.min()

img = (1.0 - img/img.max())**GCF*(chars.size-1)

print( "\n".join( ("".join(r) for r in chars[img.astype(int)]) ) )
