
## Group 34 (16114048_16114050) - Samar Singh Holkar & Sachin Aggarwal
## Date April 6th 2017
## Assignment2.py - Jarvis March and Quick Hull coded in the file 

################################################################################################################################################
import numpy as np 
import matplotlib.pyplot as plt

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
###############################################################################################################################################
## Quick Hull recursive algorithm		
###############################################################################################################################################
def isCCW(a,x,b):

    #print b
    val = ((x[1]-a[1])*(b[0]-x[0]) - (x[0]-a[0])*(b[1]-x[1]))
    #print val
    if val==0:
        return 0
    elif val>0:
        return 1
    else:
        return 2

def get_hull_points(listPts):

    # get the min, and max from the list of points
    min, max = get_min_max_x(listPts)

    hullpts = quickhull(listPts, min, max)

    hullpts = hullpts + quickhull(listPts, max, min)

    return hullpts 

'''
    Does the sorting for the quick hull sorting algorithm
'''
def quickhull(listPts, min, max):
    left_of_line_pts = get_points_left_of_line(min, max, listPts)

    ptC = point_max_from_line(min, max, left_of_line_pts)

    if len(ptC) < 1:
        return [max]

    hullPts = quickhull(left_of_line_pts, min, ptC)

    hullPts = hullPts + quickhull(left_of_line_pts, ptC, max)

    return hullPts

'''
    Reterns all points that a LEFT of a line start->end
'''
def get_points_left_of_line(start, end, listPts):
    pts = []

    for pt in listPts:
        if isCCW(start, end, pt)==2:
            pts.append(pt)

    return pts

'''
    Returns the maximum point from a line start->end
'''
def point_max_from_line(start, end, points):
    max_dist = 0

    max_point = []

    for point in points:
        if (point[0]!=start[0] or point[1]!=start[1]) and (point[1]!=end[1] or point[0]!=end[0]):
            dist = distance(start, end, point)
            if dist > max_dist:
                max_dist = dist
                max_point = point

    return max_point

def get_min_max_x(list_pts):
    min_x = float('inf')
    max_x = 0
    min_y = 0
    max_y = 0

    for x,y in list_pts:
        if x < min_x:
            min_x = x
            min_y = y
        if x > max_x:
            max_x = x
            max_y = y

    return [min_x,min_y], [max_x,max_y]

'''
    Given a line of start->end, will return the distance that
    point, pt, is from the line.
'''
def distance(start, end, pt): # pt is the point
    x1, y1 = start
    x2, y2 = end
    x0, y0 = pt
    nom = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denom = ((y2 - y1)**2 + (x2 - x1) ** 2) ** 0.5
    result = nom / denom
    return result


def caller_func(Points):

	if len(Points)<2:

		return

	Current_Hull = get_hull_points(Points)

	draw_hull(Current_Hull)

	print "Point of the current hull:"
	for x in Current_Hull: print x

	temp_list = []

	temp_list = [x for x in Points if x not in Current_Hull]

	caller_func(temp_list)

	return
#############################################################################################################################################
## Gift Wrapping Algorithm
#############################################################################################################################################
def draw_hull(Points):

	n = len(Points)

	for i in range(n):

		plt.plot([Points[i][0], Points[(i+1)%n][0]], [Points[i][1],Points[(i+1)%n][1]],'k-',lw=2)
		plt.pause(0.08)

def Gift_Wrapping(Points,n):

	min_idx = np.argmin(Points,axis=0)
	#print min_idx[0]


	pointOnHull = initialPoint = min_idx[0]

	Hull = np.empty(1,dtype=int)

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

	pointList = []
	for x in Hull:
		pointList.append(Points[x])

	draw_hull(pointList)

	Points = np.delete(Points,Hull,0)
	
	for x in Hull: print x

	print "Points of the current hull:"
	
	#print Points
	for x in Points:

		x.tolist()

	#print Points	

	Points.tolist()

	#print type(Points)
	#print type(Points[0])
	caller_func(Points.tolist())

	return


def main():

	#Entering no. of points
	n = input("Enter the value for n: ")

	Points = np.random.randint(100,size=(n,2))
	
	#sorting points
	
	Points[Points[:0].argsort()]

	for p in Points:
		print p

	for x in Points:

		plt.scatter(x[0],x[1])
		#plt.pause(0.5)
	

	Gift_Wrapping(Points,n)

	plt.show()
	plt.pause(5)


if __name__=="__main__":

	main()


