import re
import os

pathsub = 'perg21data_bmps/original_diags/'
pathoutsub = 'perg21data_bmps/cutoff_diags/'



outn = 'out.txt'


def inRelevantRangeH1sub(x, y):
	TRIANGLESTART = 0.2 * 255
	EPSILON = 0.01 * 255
	r = 1
	if( y <= TRIANGLESTART):
		r = 0
	if( abs(x - y) <= EPSILON ):
		r = 0
	return r

count = 0


for filen1 in os.listdir(pathsub):
	mf = re.match('^.+sub_all\.csv$', filen1)
	if mf:		
		file1 = open( pathsub + filen1, 'r')	
		outsub = open(pathoutsub + filen1, 'w')
		outsub.write('dim,birth,b_x,b_y,b_z,death,d_x,d_y,d_z\n')			

		line = file1.readline()
		while line :
			m = re.match('^(\d+)\,\s([\d\.]+)\,\s(\d+)\,\s(\d+)\,\s(\d+)\,\s([\d\.]+)\,\s(\d+)\,\s(\d+)\,\s(\d+)$', line)	
			if m:						
				if m.group(1) == '1':						
					if inRelevantRangeH1sub( float(m.group(2)), float(m.group(6)) ):											
						outsub.write(line)
			line = file1.readline()			

		file1.close()
		outsub.close()




