import utils
import json
import algorithms
#import peak 
import trace
import sys

############################################################################
####################### Algorithm for 1D Peak Problems #####################
############################################################################

def algorithm1(problem, trace = None):
    # If it is an empty list, we are done
    if problem.numRow <= 0 or problem.numCol <= 0:
        return None
    
    # the algorithm only works for 1D peak problems --- if the dimensions are
    # wrong, we should just give up, because whatever answer we give will not
    # be correct
    if problem.numCol != 1:
        return None

    # the recursive subproblem will involve half the number of rows
    mid = problem.numRow // 2

    # information about the two subproblems
    (subStartR1, subNumR1) = (0, mid)
    (subStartR2, subNumR2) = (mid + 1, problem.numRow - (mid + 1))

    subproblems = []
    subproblems.append((subStartR1, 0, subNumR1, 1))
    subproblems.append((subStartR2, 0, subNumR2, 1))

    # see if the center location has a better neighbor
    center = (mid, 0)
    neighbor = problem.getBetterNeighbor(center, trace)

    # this is a peak, so return it
    if neighbor == center:
        if not trace is None: trace.foundPeak(center)
        return center
    
    # otherwise figure out which subproblem contains the neigbor, and
    # recurse in that half
    sub = problem.getSubproblemContaining(subproblems, neighbor)
    if not trace is None: trace.setProblemDimensions(sub)
    result = algorithm1(sub, trace)
    return problem.getLocationInSelf(sub, result) 