import numpy as np 

"""
把文件的第一列改为

"""
exp_str = 0

file_path = 'list_bb.txt'
i = np.loadtxt(file_path,dtype=str)
for j in range(i[:,0].size):
    i[:,0][j] = exp_str
    print(i[:,0][j])
print(i)
np.savetxt('list_bbox_v2.txt',i,fmt='%s')
