# -*- coding: utf-8 -*-
#
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
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
    
    "______________________________________________________________________"
    "______________________________________________________________________"
    
    # -- Cojemos el primer nodo del problema, creamos la pila
    # frontera y la lista cerrados.
    inicio = problem.getStartState()
    frontera = util.Stack()
    cerrados = []

    # -- Guardamos el elemento inicio, una lista vacia (acciones)
    # y un coste inicial de 1 en la pila frontera.
    frontera.push((inicio, [], 1))

    # -- Este bucle while se ejecutara siempre que existan elementos
    # en la pila frontera. 
    while not frontera.isEmpty():
        # -- Sacamos el ultimo elemento añadido en la pila frontera,
        # guardamos las acciones de este elemento y añadimos este
        # elemento a la lista cerrados.
        n = frontera.pop()
        acciones = n[1]
        cerrados.append(n[0])
        
        # -- Si el elemento actual es la meta devolvemos la lista acciones.
        if problem.isGoalState(n[0]):
            return acciones
        
        # -- Este bucle recorre todos los sucesores del elemento actual.
        for sucesor in problem.getSuccessors(n[0]):
            
            # -- Solo miramos los sucesores que no estan en cerrados.
            if not sucesor[0] in cerrados:
                
                # -- Guardamos las acciones del elemento actual, del sucesor
                # actual y añadimos el sucesor actual en la pila frontera.
                sucesorAcciones = list(n[1])
                sucesorAcciones.append(sucesor[1])
                frontera.push((sucesor[0], sucesorAcciones, sucesor[2]))
    
    # -- Devolvemos acciones en caso de que termine el while.
    # (no se ha encontrado la meta)
    return acciones

    "----------------------------------------------------------------------"
    "----------------------------------------------------------------------"
    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    "______________________________________________________________________"
    "______________________________________________________________________"
    
    # -- Cojemos el primer nodo del problema, creamos la cola
    # frontera y la lista cerrados y exitosos.
    inicio = problem.getStartState()
    frontera = util.Queue()
    cerrados = []
    exitosos = []

    # -- Guardamos el elemento inicio, una lista vacia (acciones)
    # y un coste inicial de 1 en la cola frontera.
    frontera.push((inicio, [], 1))

    # -- Este bucle while se ejecutara siempre que existan elementos
    # en la cola frontera. 
    while not frontera.isEmpty():
        
        # -- Sacamos el ultimo elemento añadido en la cola frontera,
        # guardamos las acciones de este elemento y añadimos el nodo
        # del elemento actual a la lista cerrados.
        n = frontera.pop()
        acciones = n[1]
        cerrados.append(n[0])

        # -- Si el elemento actual es la meta devolvemos la lista acciones.
        if problem.isGoalState(n[0]):
            return acciones

        # -- Este bucle recorre todos los sucesores del elemento actual.
        for sucesor in problem.getSuccessors(n[0]):
            
            # -- Solo miramos los sucesores que no estan en cerrados.
            if not sucesor[0] in cerrados:
                
                # -- Solo miramos los sucesores que no estan en exitosos.
                if not sucesor[0] in exitosos:
                    
                    # -- Guardamos el nodo del sucesor actual en exitosos,
                    # las acciones del elemento actual y las del sucesor
                    # actual y añadimos el sucesor actual en la cola
                    # frontera con sus acciones i peso.
                    exitosos.append(sucesor[0])
                    sucesorAcciones = list(n[1])
                    sucesorAcciones.append(sucesor[1])
                    frontera.push((sucesor[0], sucesorAcciones, sucesor[2]))
    
    # -- Devolvemos acciones en caso de que termine el while.
    # (no se ha encontrado la meta)
    return acciones

    "----------------------------------------------------------------------"
    "----------------------------------------------------------------------"

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
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
    
    "______________________________________________________________________"
    "______________________________________________________________________"
    
    # -- Cojemos el primer nodo del problema, creamos la cola
    # frontera y la lista cerrados y exitosos.
    inicio = problem.getStartState()
    frontera = util.PriorityQueue()
    cerrados = []
    exitosos = []
    
    # -- Guardamos el elemento inicio, una lista vacia (acciones),
    # un coste inicial de 1 en la cola frontera y la heuristica 
    # del elemento inicial.
    frontera.push((inicio, [], 0), heuristic(inicio, problem))

    # -- Este bucle while se ejecutara siempre que existan elementos
    # en la cola frontera.
    while not frontera.isEmpty():
        
        # -- Sacamos el ultimo elemento añadido en la cola frontera,
        # guardamos las acciones de este elemento y añadimos el nodo
        # del elemento actual a la lista cerrados.
        n = frontera.pop()
        accions = n[1]
        cerrados.append(n[0])

        # -- Si el elemento actual es la meta devolvemos la lista acciones.
        if problem.isGoalState(n[0]):
            return accions

        # -- Este bucle recorre todos los sucesores del elemento actual.
        for successor in problem.getSuccessors(n[0]):
            
            # -- Solo miramos los sucesores que no estan en cerrados.
            if not successor[0] in cerrados:
                
                # -- Solo miramos los sucesores que no estan en exitosos
                # o los que sean la meta.
                if (not successor[0] in exitosos) or (problem.isGoalState(successor[0])):
                    
                    # -- Guardamos el nodo del sucesor actual en exitosos,
                    # las acciones del elemento actual y las del sucesor
                    # actual y calculamos la nueva heuristica formada por
                    # el elemento actual, el coste del sucesor actual y
                    # la heuristica del sucesor actual por ultimo añadimos
                    # el sucesor actual en la cola frontera con sus acciones y peso.
                    exitosos.append(successor[0])
                    sucesorAcciones = list(n[1])
                    sucesorAcciones.append(successor[1])
                    costeSucesor = n[2] + successor[2]
                    heuristicaSuccessor = heuristic(successor[0], problem)
                    frontera.push((successor[0], sucesorAcciones, costeSucesor), costeSucesor + heuristicaSuccessor)
    
        # -- Si el elemento actual es la meta devolvemos la lista acciones.
        if problem.isGoalState(n[0]):
            return accions
        
    # -- Devolvemos acciones en caso de que termine el while.
    # (no se ha encontrado la meta)
    return accions

    "----------------------------------------------------------------------"
    "----------------------------------------------------------------------"


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
