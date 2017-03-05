import re
import os

pathsub = 'g21flow/pd_sublevel/'
pathsuper = 'g21flow/pd_superlevel/'
pathoutsub = 'cutoff/pd_sublevel/'
pathoutsuper = 'cutoff/pd_superlevel/'



outn = 'out.txt'

"the function select points in a subdiagram according to the provided rules"
def inRelevantRangeH0sub(x, y):
	TRIANGLESTART = 50
	EPSILON = 7
	r = 1
	"cutoff the corner triangle"
	if( y <= TRIANGLESTART ):
		r = 0
	"cutoff the left stripe"
	if( x <= EPSILON):
		r = 0
	"cutoff the part close to diagonal"
	if( abs(x - y) <= EPSILON ):
		r = 0
	return r


def inRelevantRangeH1sub(x, y):
	TRIANGLESTART = 200
	EPSILON = 7
	r = 1
	if( x >= TRIANGLESTART ):
		r = 0
	if( y >= 255 - EPSILON):
		r = 0
	if( abs(x - y) <= EPSILON ):
		r = 0
	return r


def inRelevantRangeH0sup(x, y):
	TRIANGLESTART = 195
	EPSILON = 7
	r = 1
	if( y >= TRIANGLESTART ):
		r = 0  
	if( x >= 255 - EPSILON):
		r = 0  
	if( abs(x - y) <= EPSILON ):
		r = 0  
	return r


def inRelevantRangeH1sup( x, y):
	EPSILON = 7
 	r = 1
	if( y <= EPSILON):
		r = 0
	if( abs(x - y) <= EPSILON ):
		r = 0
	return r


count = 0


for filen1 in os.listdir(pathsub):
	mf = re.match('^.+\.csv$', filen1)
	if mf:		
		file1 = open( pathsub + filen1, 'r')	
		outsub = open(pathoutsub + filen1, 'w')
		outsub.write('dim,birth,b_x,b_y,b_z,death,d_x,d_y,d_z,b_lyap,d_lyap\n')			

		line = misc.imsave()
		while line :
			m = re.match('^(\d+)\,\s(\d+)\,\s(\d+)\,\s(\d+)\,\s(\d+)\,\s(\d+)\,\s(\d+)\,\s(\d+)\,\s(\d+)\,\s(\d+)\,\s(\d+)$', line)	
			if m:
				if m.group(1) == '0':
					if inRelevantRangeH0sub(int(m.group(2)), int(m.group(6))):
						outsub.write(line)							
				if m.group(1) == '1':
					if inRelevantRangeH1sub(int(m.group(2)), int(m.group(6))):
						outsub.write(line)
			line = file1.readline()			

		file1.close()
		outsub.close()

for filen2 in os.listdir(pathsuper):
	mf = re.match('^.+\.csv$', filen2)
	if mf:		
		file2 = open( pathsuper + filen2, 'r')	
		outsuper = open(pathoutsuper + filen2, 'w')
		outsuper.write('dim,birth,b_x,b_y,b_z,death,d_x,d_y,d_z,b_lyap,d_lyap\n')

		line = file2.readline()
		while line :
			m = re.match('^(\d+)\,\s(\d+)\,\s([\d,\.]+)\,\s([\d,\.]+)\,\s(\d+)\,\s(\d+)\,\s([\d,\.]+)\,\s([\d,\.]+)\,\s(\d+)\,\s(\d+)\,\s(\d+)$', line)	
			if m:
				if m.group(1) == '0':
					if inRelevantRangeH0sup(int(m.group(2)), int(m.group(6))):
						outsuper.write(line)							
				if m.group(1) == '1':
					if inRelevantRangeH1sup(int(m.group(2)), int(m.group(6))):
						outsuper.write(line)
			line = file2.readline()			

		file2.close()
		outsuper.close()



