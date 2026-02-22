from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    visited = []
    
    path = []
    
    stack = utils.Stack()
    
    start = problem.getStartState()
    
    visited.append(start)
    
    if not problem.isGoalState(start):
        found = False
        latest = start

        
        while not found:
            advanced=False
            paths = problem.getSuccessors(latest)
            for i in paths:
                
                if i[0] not in visited:
                    
                    stack.push((i[0],i[1]))
                    visited.append(i[0])
                    latest = i[0]
                    advanced = True
                    break
                
            if problem.isGoalState(latest):
                found = True
                
            elif not advanced:
                stack.pop()
                latest = stack.list[-1][0]
        
        while not stack.isEmpty():
            path.insert(0,stack.pop()[1])
        return path
        
    else:
        return path
    utils.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    queue = utils.Queue()
    
    visited = []
    
    start = problem.getStartState()
    
    
    
    queue.push( (start,[]) ) #Estado, Path
    

    
    if not problem.isGoalState(start):
        
        while not queue.isEmpty():
            state, path = queue.pop()
            
            
            
            neighbors = problem.getSuccessors(state)
            
            for i in neighbors:
                if not i[0] in visited:
                    newPath = path + [i[1]]
                    queue.push((i[0],newPath))
                    visited.append(i[0])

            if problem.isGoalState(state):
                return path
            
            
            

    else: 
        return []
    utils.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    inicio = problem.getStartState()
    frontera = utils.PriorityQueue()
    frontera.push((inicio, [], 0), 0)

    mejor_costo = {inicio: 0}

    while not frontera.isEmpty():
        estado, acciones, costo = frontera.pop()

        if costo > mejor_costo.get(estado, float("inf")):
            continue

        if problem.isGoalState(estado):
            return acciones

        for sucesor, accion, costo_paso in problem.getSuccessors(estado):
            nuevo_costo = costo + costo_paso
            if nuevo_costo < mejor_costo.get(sucesor, float("inf")):
                mejor_costo[sucesor] = nuevo_costo
                frontera.push((sucesor, acciones + [accion], nuevo_costo), nuevo_costo)

    return []


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
