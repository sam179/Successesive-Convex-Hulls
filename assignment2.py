import numpy as np 

def Orientation(pointOnHull,x,temporaryPoint):

	val = 0
	#print temporaryPoint.shape
	val = ((x[1]-pointOnHull[1])*(temporaryPoint[0]-x[0]) - (x[0]-pointOnHull[0])*(temporaryPoint[1]-x[1]))
	#print val
	if val==0:
		return 0
	elif val>0:
		return 1
	else:
		return 2


def Gift_Wrapping(Points):

	initialPoint = pointOnHull = 0

	temporaryPoint = pointOnHull

	Hull = np.array((0,2),int)
	ikx=0
	while True:
		
		Hull = np.vstack([Hull,Points[pointOnHull]])
		
		temporaryPoint = (pointOnHull+1)%Points.shape[0]; 
		idx=0
		for x in Points:

			if Orientation(Points[pointOnHull],x,Points[temporaryPoint])==2:

				temporaryPoint = idx
				#print temporaryPoint.shape
			idx=idx+1	


		pointOnHull = temporaryPoint

		if pointOnHull == initialPoint:

			break

		print Hull.shape		
		if ikx==0:

			Hull = np.delete(Hull,0)
			Hull = np.delete(Hull,0)
		
		print Hull.shape
		ikx=ikx+1


	print Hull.shape
	for p in Hull:

		print p
		index = np.argwhere(Points==p)
		Points = np.delete(Points,index)


	#for p in Points:


def main():

	#Entering no. of points
	n = input("Enter the value for n: ")

	Points = np.random.randint(100000,size=(n,2))

	#sorting points
	Points[Points[:0].argsort()]

	#for p in Points:
		#print p

	Gift_Wrapping(Points)

if __name__=="__main__":

	main()


