# Successesive-Convex-Hulls

Algorithms:


Jarvis March:
	•	Initialize p as leftmost point.
	•	Do following while we don’t come back to the first (or leftmost) point.
- The next point q is the point such that the triplet (p, q, r) is counterclockwise for any other point r.
- next[p] = q (Store q as next of p in the output convex hull).
- p = q (Set p as q for next iteration).

Quick Hull:
	•	Find the points with minimum and maximum x coordinates, as these will always be part of the convex hull.
	•	Use the line formed by the two points to divide the set in two subsets of points, which will be processed recursively.
	•	Determine the point, on one side of the line, with the maximum distance from the line. The two points found before along with this one form a triangle.
	•	The points lying inside of that triangle cannot be part of the convex hull and can therefore be ignored in the next steps.
	•	Repeat the previous two steps on the two lines formed by the triangle (not the initial line).
	•	Keep on doing so on until no more points are left, the recursion has come to an end and the points selected constitute the convex hull.



