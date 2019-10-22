# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
import math


class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.
      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.
        getAction chooses among the best options according to the evaluation function.
        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.
        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.
        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.
        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        food = currentGameState.getFood()
        currentPos = list(successorGameState.getPacmanPosition())
        distance = float("-Inf")

        foodList = food.asList()

        if action == 'Stop':
            return float("-Inf")

        for state in newGhostStates:
            if state.getPosition() == tuple(currentPos) and (state.scaredTimer == 0):
                return float("-Inf")

        for x in foodList:
            tempDistance = -1 * (manhattanDistance(currentPos, x))
            if (tempDistance > distance):
                distance = tempDistance

        return distance


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.
      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.
      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.
      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def minimax(self, state, depth, agent=0, maximizing=True):
        if depth == 0 or state.isWin() or state.isLose():
            return self.evaluationFunction(state), Directions.STOP

        actions = state.getLegalActions(agent)
        if maximizing:
            scores = []

            for action in actions:
                scores.append(self.minimax(state.generateSuccessor(agent, action), depth - 1, agent + 1, False)[0])

            bestScore = max(scores)

            for i in range(len(scores)):
                if scores[i] == bestScore:
                    return bestScore, actions[i]

        else:
            scores = []

            if agent == state.getNumAgents() - 1:

                for action in actions:
                    scores.append(self.minimax(state.generateSuccessor(agent, action), depth - 1, 0, True)[0])
            else:
                for action in actions:
                    scores.append(self.minimax(state.generateSuccessor(agent, action), depth, agent + 1, False)[0])

            bestScore = min(scores)
            for i in range(len(scores)):
                if scores[i] == bestScore:
                    return bestScore, actions[i]

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.
          Here are some method calls that might be useful when implementing minimax.
          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1
          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action
          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        return self.minimax(gameState, self.depth * 2, 0, True)[1]


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def minimax(self, state, depth, a, b, agent=0, maximizing=True):
        if depth == 0 or state.isWin() or state.isLose():
            return self.evaluationFunction(state), Directions.STOP

        actions = state.getLegalActions(agent)
        if maximizing:
            bestScore = float("-Inf")
            bestActions = []
            for action in actions:
                score = self.minimax(state.generateSuccessor(agent, action), depth - 1, a, b, agent + 1, False)[0]
                a = max(a, score)
                if score > bestScore:
                    bestScore = score
                    bestActions = [action]
                if bestScore > b: break
            return bestScore, random.choice(bestActions)
        else:
            bestScore = float("Inf")
            bestActions = []
            if agent == state.getNumAgents() - 1:
                for action in actions:
                    score = self.minimax(state.generateSuccessor(agent, action), depth - 1, a, b, 0, True)[0]
                    b = min(b, score)
                    if score < bestScore:
                        bestScore = score
                        bestActions = [action]
                    if a > bestScore: break
            else:
                for action in actions:
                    score = self.minimax(state.generateSuccessor(agent, action), depth, a, b, agent + 1, False)[0]
                    b = min(b, score)
                    if score < bestScore:
                        bestScore = score
                        bestActions = [action]
                    if a > bestScore: break
            return bestScore, random.choice(bestActions)

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        return self.minimax(gameState, self.depth * 2, float("-Inf"), float("Inf"), 0, True)[1]


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """


    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction
          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"

        def expectFinder(gameState, depth, agentcounter):
            expectimax = ["", 0]
            ghostActions = gameState.getLegalActions(agentcounter)

            probability = 1.0 / len(ghostActions)

            if not ghostActions:
                return self.evaluationFunction(gameState)

            for action in ghostActions:
                currState = gameState.generateSuccessor(agentcounter, action)
                current = expectimant(currState, depth, agentcounter + 1)
                if type(current) is list:
                    newVal = current[1]
                else:
                    newVal = current
                expectimax[0] = action
                expectimax[1] += newVal * probability
            return expectimax

        def maxValue(gameState, depth, agentcounter):
            maximum = ["", -float("inf")]
            actions = gameState.getLegalActions(agentcounter)

            if not actions:
                return self.evaluationFunction(gameState)

            for action in actions:
                currState = gameState.generateSuccessor(agentcounter, action)
                current = expectimant(currState, depth, agentcounter + 1)
                if type(current) is not list:
                    newVal = current
                else:
                    newVal = current[1]
                if newVal > maximum[1]:
                    maximum = [action, newVal]
            return maximum

        def expectimant(gameState, depth, agentcounter):
            if agentcounter >= gameState.getNumAgents():
                depth += 1
                agentcounter = 0

            if (depth == self.depth or gameState.isWin() or gameState.isLose()):
                return self.evaluationFunction(gameState)
            elif (agentcounter == 0):
                return maxValue(gameState, depth, agentcounter)
            else:
                return expectFinder(gameState, depth, agentcounter)

        actionsList = expectimant(gameState, 0, 0)
        return actionsList[0]





def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).
      DESCRIPTION: <write something here so we know what you did>
    """

    "[Project 3] YOUR CODE HERE"


    baseScores = [-50.0, -100.0, -75.0]
    decayFacts = [0.1, 0.2, 0.1]
    pos = currentGameState.getPacmanPosition()

    score = currentGameState.getScore() - 200.0 * currentGameState.getNumFood()

    foodList = currentGameState.getFood().asList()
    for food in foodList:
        score += baseScores[0] * (1 - math.exp(-1.0 * decayFacts[0] * util.manhattanDistance(pos, food)))

    capsuleList = currentGameState.data.capsules
    for capsule in capsuleList:
        score += baseScores[1] * (1 - math.exp(-1.0 * decayFacts[1] * util.manhattanDistance(pos, capsule)))


    ghostList = currentGameState.getGhostPositions()
    for ghost in ghostList:
        dist = util.manhattanDistance(pos, ghost)
        score += baseScores[2] * math.exp(-1.0 * decayFacts[2] * dist)
        if dist < 2:
            score -= 1e6



    return score


# Abbreviation
better = betterEvaluationFunction