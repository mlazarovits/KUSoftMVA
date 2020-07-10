

from root_pandas import read_root
#from progressbar import ProgressBar
from tqdm import tqdm

f = '/home/t3-ku/janguian/storeUser/malazaro/softMVA/Train_dyjets.root'
#df = read_root(f)

#pbar = ProgressBar()
i=0;
#for df in tqdm(read_root(f, chunksize=100000, unit='chunks')):
#	print("Chunk "+str(i))
#	i = i+1

for df in read_root(f,chunksize=100000):
	print("Chunk "+str(i))
 	i = i+1

