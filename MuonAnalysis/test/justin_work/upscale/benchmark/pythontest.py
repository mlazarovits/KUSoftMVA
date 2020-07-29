
import numpy as np

arr = [[0.2,0.8],[0.7,0.3],[0.51,0.49]]
arr = np.array(arr)
print(arr)
pthreshold = 0.6
#arr[ arr >= pthreshold ] = 1.
#arr[ arr < pthreshold ] = 0.
#arr[

#arr[ arr >= pthreshold, : ] = 1.
#arr[ arr 
#arr[ arr >= pthreshold ] = 1.

arr = [ [0,1] if x[0] <pthreshold else [1,0]  for x in arr]
#arr[ arr < pthreshold ] = 0.
#arr[ (arr == [0,0]).all ] = [0.,1.]


print(arr)


