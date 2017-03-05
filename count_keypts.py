import os
import numpy as np
import re
import math

pathfeatures = 'g21/feature_vectors/'

outf = open('total_keypts.txt', 'w')
outf2 = open('total_keypts_nobd.txt', 'w')

RING = 20 #boundary ring radius

N=2000

cts = np.zeros(N)
cts_per = np.zeros(N)
cts_pi = np.zeros(N)
cts_mid = np.zeros(N)
cts_mid_per = np.zeros(N)
cts_mid_pi = np.zeros(N)

for filen1 in os.listdir(pathfeatures):
	count = 0
	count_per = 0
	count_pi = 0
	count_mid = 0
	count_mid_per = 0
	count_mid_pi = 0
	file1 = open( pathfeatures + filen1, 'r')
	m = re.match('(\d+)', filen1)
	line = file1.readline()
	while line:
		m2 = re.match('^\d+\s[-\d]+\s[-\d]+\s(\d+)\s(\d+)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)$', line)
		if math.sqrt( ( (210.5- (float)(m2.group(1)))*(210.5-(float)(m2.group(1)))) + (210.5-(float)(m2.group(2)))*(210.5-(float)(m2.group(2))) ) < (204.005 - RING) : 
			count_mid = count_mid + 1;
			if (int)(m2.group(3)) == 1 or (int)(m2.group(4)) == 1 or (int)(m2.group(5)) == 1 or (int)(m2.group(6)) == 1:
				count_mid_per = count_mid_per + 1
			if (int)(m2.group(7)) == 1 or (int)(m2.group(8)) == 1 or (int)(m2.group(9)) == 1 or (int)(m2.group(10)) == 1:
				count_mid_pi = count_mid_pi + 1
		
		count = count + 1
		if (int)(m2.group(3)) == 1 or (int)(m2.group(4)) == 1 or (int)(m2.group(5)) == 1 or (int)(m2.group(6)) == 1:
			count_per = count_per + 1
		if (int)(m2.group(7)) == 1 or (int)(m2.group(8)) == 1 or (int)(m2.group(9)) == 1 or (int)(m2.group(10)) == 1:
			count_pi = count_pi + 1
		line = file1.readline()

	cts[int(m.group(1))] = count
	cts_mid[int(m.group(1))] = count_mid
	cts_mid_per[int(m.group(1))] = count_mid_per
	cts_mid_pi[int(m.group(1))] = count_mid_pi
	cts_per[int(m.group(1))] = count_per
	cts_pi[int(m.group(1))] = count_pi

for i in range(N):
	outf.write(str(i) + ' ' + str(int(cts[i])) + ' ' + str(int(cts_per[i])) + ' ' + str(int(cts_pi[i])) + '\n')
	outf2.write(str(i) + ' ' + str(int(cts_mid[i])) + ' ' + str(int(cts_mid_per[i])) + ' ' + str(int(cts_mid_pi[i])) + '\n')
