from scipy import misc
from skimage import color
from skimage import io
import os

pathimgs = 'perg21data_bmps/bmps/'
pathgs = 'perg21data_bmps/bmps_gs/'
patht = 'perg21data_bmps/bmps_t/'

for filen1 in os.listdir(pathimgs):
	img = color.rgb2gray(io.imread(pathimgs + filen1))
	misc.imsave(pathgs + filen1 + '.bmp', img)	

#threshold images
for filen1 in os.listdir(pathgs):
	img = io.imread(pathimgs + filen1)
	binary_img = img > 0.1
	misc.imsave(patht + file1 + '.bmp', binary_img)
	line = file1.readline()
	while line :
