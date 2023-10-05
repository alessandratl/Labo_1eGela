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

from abc import ABC, abstractmethod

import util


class SearchProblem(ABC):
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    @abstractmethod
    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()
        

    @abstractmethod
    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    @abstractmethod
    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    @abstractmethod
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
    return [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    """
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    """print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's succesors:", problem.getSuccessors(problem.getStartState()))"""


    inicio = problem.getStartState()
    if problem.isGoalState(inicio):
        return []

    porVisitar = util.Stack() #utilizamos una pila
    visitados = []
    porVisitar.push((inicio,[]))

    while not porVisitar.isEmpty():
        actual, camino = porVisitar.pop()
        if actual not in visitados:
            visitados.append(actual)
            if problem.isGoalState(actual):
                print("Camino encontrado: ", camino) #imprimir el camino recorrido
                return camino
            for siguiente, accion, coste in problem.getSuccessors(actual):
                caminoSiguiente = camino + [accion]
                porVisitar.push((siguiente, caminoSiguiente ))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    """print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's succesors:", problem.getSuccessors(problem.getStartState()))"""

    inicio = problem.getStartState()
    if problem.isGoalState(inicio):
        return []

    porVisitar= util.Queue() #utilizamos una cola
    visitados = []
    porVisitar.push((inicio, []))

    while not porVisitar.isEmpty():
        actual, camino = porVisitar.pop()
        if actual not in visitados:
            visitados.append(actual)
            if problem.isGoalState(actual):
                print("Camino encontrado: ", camino)  # imprimir el camino recorrido
                return camino
            for siguiente, accion, coste in problem.getSuccessors(actual):
                siguientePaso = camino + [accion]
                porVisitar.push((siguiente, siguientePaso))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    porVisitar = util.PriorityQueue()
    visitados = []
   ## inicio = problem.getStartState()
    visitados.append(problem.getStartState())
   
    print(visitados)
    if problem.isGoalState(problem.getStartState()):
         return []
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
   
    
    #print(problem.getSuccesors(inicio))
    inicio = problem.getStartState()
    print("NODO INICIAL: ")
    print(inicio)
    sucesores = problem.getSuccessors(inicio)
    print(sucesores)
   
    for sucesor in sucesores:
        print(sucesor[2])
        porVisitar.update(sucesor,sucesor[2])


    while not porVisitar.isEmpty():

        nodo_actual= porVisitar.pop()
        print(nodo_actual)
        if problem.isGoalState(nodo_actual[0]):
             return print("es el objetivo") ##falta devolver camino
        print(nodo_actual[0])
        visitados.append(nodo_actual[0])
        sucesores = problem.getSuccesors(nodo_actual[0])
        
        for sucesor in sucesores:
             porVisitar.update(sucesor,sucesor[2])
             
        print(nodo_actual)


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
    util.raiseNotDefined()


# Abbreviations
##bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch