from scipy import misc
from skimage import color
from skimage import io
import os
from scipy import ndimage
import numpy as np
import re

pathgs = 'perg21data_bmps/bmps/'
patht = 'perg21data_bmps/bmps_t/'
pathdiag = 'perg21data_bmps/cutoff_diags/'
pathcomp = 'perg21data_bmps/cutoff_comp/'

peaks_filen = 'per_peaks.txt'

#outf = open(peaks_filen, 'w')

#quotient out pixels of how many percent intensity
quot = 0.2

#threshold images
for filen1 in sorted( os.listdir(pathgs) ):

	peaks = np.zeros( (421, 421), dtype=np.int )
	peaks_indices = []
	index = 0
	#load the relevant persistence points location and save them as 1 in a binary matrix
	m = re.match('(\d+)', filen1)
	filediag =  "%05d__sub_all.csv" % int(m.group(0)) 
	f = open( pathdiag + filediag, 'r')
	line = f.readline()
	#outf.write(m.group(0) + ' ')
	while line:
		m = re.match('^(\d+)\,\s([\d\.]+)\,\s(\d+)\,\s(\d+)\,\s(\d+)\,\s([\d\.]+)\,\s(\d+)\,\s(\d+)\,\s(\d+)$', line)	
		if m:	
			peaks[ int(m.group(7)), int(m.group(8)) ] = 1
			peaks_indices.append( (int(m.group(7)), int(m.group(8))) )
			#outf.write('(' + m.group(7) + ' ' + m.group(8) + ')')
			index = index + 1
		line = f.readline()
	f.close()
	#outf.write('\n')

	
	img = io.imread(pathgs + filen1)
	binary_img = img > quot * 255
	#binary dilation
	DIL_STEPS = 5
	for i in range(DIL_STEPS):
		binary_img = ndimage.binary_dilation(binary_img).astype(binary_img.dtype)
	label_im, nb_labels = ndimage.label(binary_img)
	
	#select components containing the selected peaks of the lyapunov vector
	labels = []
	for idx in peaks_indices:
		labels.append(label_im[idx[0], idx[1]])
	labelsuq = np.sort( np.unique(labels) )
	int_labels_mask = np.zeros( label_im.shape )
	for idx in labelsuq:
		labels_mask = (label_im != idx)
		int_labels_mask = int_labels_mask + labels_mask

	print(filen1 + ' ' + str(nb_labels) + ' ' + str(labelsuq.shape))
	misc.imsave(pathcomp + filen1 + '.bmp', int_labels_mask)
	#misc.imsave('tmp/' + filen1 + '.bmp', label_im)
	#misc.imsave(patht + filen1, (label_im == labelsuq) )
	
	#print(filen1 + ' ' + str(nb_labels))
	#print(label_im2[])

	misc.imsave(patht + filen1 + '.bmp', binary_img)
	

	#select the components correspoing to the list of the H1 persistence generators
	


