# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    _stack = util.Stack()
    _visited = []
    _path = []
    if problem.isGoalState(problem.getStartState()):
        return []
    _stack.push((problem.getStartState(), []))

    while not (_stack.isEmpty()):
        _xy, _path = _stack.pop()
        _visited.append(_xy)

        if problem.isGoalState(_xy):
            return _path

        successors = problem.getSuccessors(_xy)
        if successors:
            for item in successors:
                if item[0] not in _visited:
                    _stack.push((item[0], _path + [item[1]]))
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    "*** YOUR CODE HERE ***"
    from util import Queue
    _queue= Queue()
    _visited = []
    _path = []
    if problem.isGoalState(problem.getStartState()):
        return []
    _queue.push((problem.getStartState(), []))

    while not (_queue.isEmpty()):
        _xy, _path = _queue.pop()
        _visited.append(_xy)
        if problem.isGoalState(_xy):
            return _path

        successors = problem.getSuccessors(_xy)
        if successors:
            for item in successors:
                if item[0] not in _visited:
                    _queue.push((item[0], _path + [item[1]]))


    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    _PrQueue = util.PriorityQueue()
    _visited = dict()
    _xy = problem.getStartState()
    nd = {}
    nd["pred"] = None  # We are getting the parent of a node,the _xy the action and
    nd["act"] = None  # compute the cost and building the path(aka actions)
    nd["_xy"] = _xy
    nd["cost"] = 0
    _PrQueue.push(nd, nd["cost"])

    while not _PrQueue.isEmpty():
        nd = _PrQueue.pop()
        _xy = nd["_xy"]
        cost = nd["cost"]

        if _visited.has_key(_xy):
            continue
        _visited[_xy] = True
        if problem.isGoalState(_xy) == True:
            break
        for suc in problem.getSuccessors(_xy):
            if not _visited.has_key(suc[0]):
                new_nd = {}
                new_nd["pred"] = nd
                new_nd["_xy"] = suc[0]
                new_nd["act"] = suc[1]
                new_nd["cost"] = suc[2] + cost
                _PrQueue.push(new_nd, new_nd["cost"])
    _path = []

    while nd["act"] != None:
        _path.insert(0, nd["act"])
        nd = nd["pred"]
    return _path
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    _PrQueue = util.PriorityQueue()
    _visited = dict()

    _xy = problem.getStartState()
    nd = {}
    nd["pred"] = None
    nd["act"] = None
    nd["_xy"] = _xy
    nd["cost"] = 0
    nd["eq"] = heuristic(_xy, problem)
    _PrQueue.push(nd, nd["cost"] + nd["eq"])

    while not _PrQueue.isEmpty():
        nd = _PrQueue.pop()
        _xy = nd["_xy"]
        cost = nd["cost"]
        v = nd["eq"]
        # In the A star algorithm we are working in a similar way to the UCS
        if _visited.has_key(_xy):  # But now for cost we are having the cost + heuristic combined
            continue
        _visited[_xy] = True
        if problem.isGoalState(_xy) == True:
            break
        for suc in problem.getSuccessors(_xy):
            if not _visited.has_key(suc[0]):
                new_nd = {}
                new_nd["pred"] = nd
                new_nd["_xy"] = suc[0]
                new_nd["act"] = suc[1]
                new_nd["cost"] = suc[2] + cost
                new_nd["eq"] = heuristic(new_nd["_xy"], problem)
                _PrQueue.push(new_nd, new_nd["cost"] + new_nd["eq"])
    _path = []
    while nd["act"] != None:
        _path.insert(0, nd["act"])
        nd = nd["pred"]
    return _path
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
