from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.
    """
    # TODO: Add your code here

    coordenadas_actuales = state[0]
    x1, y1 = coordenadas_actuales

    x2, y2 = problem.goal
    distancia = abs(x2-x1)+abs(y2-y1)

    return distancia
    


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider: distance to nearest survivor + MST of remaining survivors
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    # TODO: Add your code here
    inicio, sobrevivientes = state 
    restantes = sobrevivientes.asList()

    if len(restantes) == 0: #cuando ya no hay sobrevivientes restantes
        return 0 
    
    cola = utils.PriorityQueue() #Encontrar el sobreviviente más cercano con una cola de prioridad

    for i in restantes:
        distancia = abs(inicio[0] -i[0]) + abs(inicio[1] - i[1]) #calcula la distancia entre el robot y el sobreviviente
        cola.push(distancia, distancia) #guarda la distancia en la cola, se usa la de prioridad para obtener primero el de menor distancia

    return cola.pop() #retorna el sobreviviente más cercano, osea el elemento de menor valor de la cola 
    utils.raiseNotDefined()
