import numpy as np 

def Orientation(a,x,b):

	#print b
	val = ((x[1]-a[1])*(b[0]-x[0]) - (x[0]-a[0])*(b[1]-x[1]))
	#print val
	if val==0:
		return 0
	elif val>0:
		return 1
	else:
		return 2

def func(Points,a):

	idx=0

	for x in Points:

		if x[0]==a[0] and x[1]==a[1]:
			return idx

		idx = idx + 1


def Gift_Wrapping(Points,n):

	min_idx = np.argmin(Points,axis=0)
	#print min_idx[0]


	pointOnHull = initialPoint = min_idx[0]

	Hull = np.empty(1)

	while True:

		Hull = np.append(Hull,pointOnHull)

		temporaryPoint = (pointOnHull+1)%n

		for x in Points:

			if Orientation(Points[pointOnHull],x,Points[temporaryPoint])==2:

				temporaryPoint = func(Points,x)

		pointOnHull = temporaryPoint

		if pointOnHull == initialPoint:

			break

	Hull = np.delete(Hull,0)

	for x in Hull:

		print x


def main():

	#Entering no. of points
	n = input("Enter the value for n: ")

	Points = np.random.randint(10,size=(n,2))

	#sorting points
	Points[Points[:0].argsort()]

	#for p in Points:
	#	print p

	Gift_Wrapping(Points,n)

if __name__=="__main__":

	main()


