"""Process the contrast of the faces, while equating mean luminance."""
from PIL import Image
import glob
"""
Note that this replaces all images in place. The original images can
be found other places, and shoudl be recopied if resizing needs to happen again
"""

imNames = []
dirLst = ['Black', 'White', 'GrayGuns', 'GrayNonguns', '../WIT']

for dir in dirLst:
    flList = glob.iglob(dir + '/*.png')
    for imName in flList:
        im = Image.open(imName)
        #alpha = im.split()[-1]

        #im = im.convert('L')
        #im.putalpha(alpha)

        curH = im.height
        curW = im.width
        newH = 250
        newW = int(round(curW * newH / curH))

        im.thumbnail(size=(newW, newH))

        im.save(imName)
