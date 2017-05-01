# Successesive-Convex-Hulls

Given a set of n points. We need to find the convex hull, then we take the remaining interior points and find the convex hull of the remaining points, we repeat this process untill no points remain. We have to create a GUI to illustrate the process for a given value of n. Points( x and y coordinates) are chosen randomly. 

Algorithms:

1. Apply Jarvis March to find the first hull. 

Jarvis March:


	•	Initialize p as leftmost point.
	•	Do following while we don’t come back to the first (or leftmost) point.
	
	- The next point q is the point such that the triplet (p, q, r) is counterclockwise for any other point r.
	- next[p] = q (Store q as next of p in the output convex hull).
	- p = q (Set p as q for next iteration).

2. For the remaining set of points, we use recursive Quick Hulls.


Quick Hull:


	•	Find the points with minimum and maximum x coordinates, as these will always be part of the convex hull.
	•	Use the line formed by the two points to divide the set in two subsets of points, which will be processed 		  recursively.
	•	Determine the point, on one side of the line, with the maximum distance from the line. The two points found 		    before along with this one form a triangle.
	•	The points lying inside of that triangle cannot be part of the convex hull and can therefore be ignored in the 		       next steps.
	•	Repeat the previous two steps on the two lines formed by the triangle (not the initial line).
	•	Keep on doing so on until no more points are left, the recursion has come to an end and the points selected 		    constitute the convex hull.

3. We store the point of each successive hull and plot the illustration through pyplot. 

