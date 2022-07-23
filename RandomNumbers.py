from CollatzSeries import NumberGenerator
import random as rand
#define patterns from randoms
PARAM1 = 100
PARAM2 = 1000000
Collection = [[0 for x in range(PARAM2)] for y in range(PARAM1)] 
MAX = 2 ** 128
print(MAX)
for i in range(0,PARAM1-1): #take 100 random samples of 1000000 random numbers
	for j in range(0,PARAM2-1):
		k = rand.randint(0,MAX)
		if(k not in Collection):
			Collection[i][j] = k
		else:
			k = k % 7
			Collection[i][j] = k
print(Collection)	
