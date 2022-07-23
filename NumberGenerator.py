class NumberGenerator():
	def __init__():
		//nothing  to do
	def generatePath(int x): //returns an array with the path of X to 1
		path = []
		path.append(x) //starter makes sure 1 is included
		while(x != 1):
			if(x % 2 != 0): //odd
				x = 3*x + 1
				path.append(x)
			 else 
				x = x / 2;
				path.append(x)
		return path
	def stepsToOne(int x): //return counter of steps to 1
		steps = 0
		while(x != 1):
			if(x % 2 != 0): //odd
				steps += stepsToOne(3 * x + 1)
			else:
				steps += stepsToOne(x / 2)
		return steps


	