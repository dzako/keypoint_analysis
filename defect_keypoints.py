from scipy import misc
from skimage import color
from skimage import io
import os
from scipy import ndimage
import numpy as np
import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

pathcomp = 'perg21data_bmps/cutoff_comp/'
pathfeatures = 'g21/feature_vectors/'
pathkeyptsimg = 'perg21data_bmps/keyptsimg/'
pathflow = 'g21/bmps/'

outf = open('defect_keypts.txt', 'w')

PIXS = 421

keyptsoutf = open('keypts.txt', 'w')

def swap( x, y): 
	return[y,x]

for filen1 in sorted(os.listdir(pathfeatures)):
	count = 0
	count_per = 0
	count_pi = 0
	m = re.match('(\d+)', filen1)
	img = mpimg.imread(pathcomp + m.group(0) + '.bmp')
	flowimg = io.imread(pathflow + m.group(0))
	

	mask = (img == 0)
	flowimg[mask] = 0
	imgcolor = np.zeros((PIXS, PIXS, 3))
	imgcolor[:, :, 0] = flowimg
	imgcolor[:, :, 1] = flowimg
	imgcolor[:, :, 2] = flowimg

	#fig = plt.figure()
	#fig.figimage(imgcolor)
	plt.imshow(imgcolor, zorder = 0)
	
	keypts = open(pathfeatures + m.group(0) + '.txt', 'r')
	line = keypts.readline()
	keyptsoutf.write(m.group(0) + ' ')
	while line:
		m2 = re.match('^\d+\s[-\d]+\s[-\d]+\s(\d+)\s(\d+)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)$', line)	
		if m2:		
			idx = swap(int(m2.group(1)), int(m2.group(2)))
			if(img[idx[0], idx[1]] == 255):
				keyptsoutf.write('(' + m2.group(1) + ', ' + m2.group(2) + ')')
				if (int)(m2.group(3)) == 1 or (int)(m2.group(4)) == 1 or (int)(m2.group(5)) == 1 or (int)(m2.group(6)) == 1:
					colorind = 0					
					count_per = count_per + 1
				if (int)(m2.group(7)) == 1 or (int)(m2.group(8)) == 1 or (int)(m2.group(9)) == 1 or (int)(m2.group(10)) == 1:
					colorind = 2
					count_pi = count_pi + 1
				#print filen1
				#print str(int(m2.group(1))) + ' ' + str(int(m2.group(2))) + ' ' + str(colorind)

				RAD = 2
				if((int)(m2.group(3)) == 1 or (int)(m2.group(4)) == 1):
					clr = 'red'
				if((int)(m2.group(5)) == 1 or (int)(m2.group(6)) == 1):
					clr = 'blue'
				if((int)(m2.group(7)) == 1 or (int)(m2.group(8)) == 1):
					clr = 'yellow'
				if((int)(m2.group(9)) == 1 or (int)(m2.group(10)) == 1):
					clr = 'cyan'				
				newidx = swap(idx[0],idx[1])
				plt.scatter( newidx[0], newidx[1], c=clr, zorder = 1)
				#plt.scatter(idx[0], idx[1], color = c)
				#imgcolor[ idx[0]-RAD:idx[0]+RAD , idx[1]-RAD:idx[1]+RAD, 0] = 0
				#imgcolor[ idx[0]-RAD:idx[0]+RAD , idx[1]-RAD:idx[1]+RAD, 1] = 0
				#imgcolor[ idx[0]-RAD:idx[0]+RAD , idx[1]-RAD:idx[1]+RAD, 2] = 0
				#imgcolor[ idx[0]-RAD:idx[0]+RAD , idx[1]-RAD:idx[1]+RAD, colorind] = 255
					
				count = count + 1								
				#print str(int(m.group(1))) + ' ' + str(int(m.group(2))) + ' ' + str(img[int(m.group(1)), int(m.group(2))])
		line = keypts.readline()

	keyptsoutf.write('\n')

	plt.savefig(pathkeyptsimg + filen1 + '.png')
	plt.gcf().clear()
	outf.write(m.group(0) + ' ' + str(int(count)) + ' ' + str(int(count_per)) + ' ' + str(int(count_pi)) + '\n')
	print m.group(0) + ' ' + str(int(count)) + ' ' + str(int(count_per)) + ' ' + str(int(count_pi)) + '\n'


