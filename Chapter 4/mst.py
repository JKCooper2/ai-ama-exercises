# Based on http://people.csail.mit.edu/rivest/mst.py
import numpy as np


def dist(p1,  p2):
    """ Return distance between points p1 and p2. """
    return np.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)


def mst_distance(points):
    mst = compute_mst(points)

    distance = 0

    for p in mst:
        distance += dist(p[0], p[1])

    return distance

def compute_mst(points):
    """ Compute MST of given set of points. """
    # use prim's algorithm
    mst_edge_list = prim(points)
    return mst_edge_list


def prim(points):
    """
    Find mst of set of balls with Prim's algorithm.
    Return set of edges.
    """

    if len(points) == 0:
        return []

    mst_edge_list = []

    p0 = points[0]
    Q = points[1:]

    for point in Q:
        point.d = dist(point, p0)
        point.pred = p0

    while Q != []:
        min_d = 1e20
        for point in Q:
            if point.d < min_d:
                min_d = point.d
                closest_point = point

        Q.remove(closest_point)
        p0 = closest_point
        p1 = closest_point.pred
        mst_edge_list.append((p0, p1))

        for point in Q:
            d = dist(point, closest_point)

            if d < point.d:
                point.d = d
                point.pred = closest_point

    return mst_edge_list
