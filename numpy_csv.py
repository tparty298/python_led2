import numpy as np
import time
#file=np.loadtxt('output.txt',delimiter=',',skiprows=0,usecols=None)
#data = np.genfromtxt("nisample.csv",delimiter=",", dtype='int')
print("read file")
data = np.genfromtxt("output.txt",delimiter=",", skip_header=0,dtype='int')
print("readed file")
start=time.time()
LOOP=100
print("before loop")
for i in range(289):
   s_line=LOOP*(289+1)
   tmp_x=data[s_line,0]
   tmp_y=data[s_line,1]
   tmp_z=data[s_line,2]
end_time=time.time()-start
print(end_time)
