# qlearningAgents.py
# ------------------
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


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        self.QTable=util.Counter()#kind of dict QTable[]
    def ShowHyperparameters(self):
        print("alpha is "+str(self.alpha))
        print("epsilon is "+str(self.epsilon))
        print("Gamma is "+str(self.discount))
    def setEpsilon(self, epsilon):
        return super().setEpsilon(epsilon)
    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        #print(state)
        return self.QTable[(state,action)]
        util.raiseNotDefined()
    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action) 
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        AvailableActionQvalue=util.Counter()
        Actions=self.getLegalActions(state)
        if len(Actions)==0:
          return 0.0
        for Action in Actions:
          AvailableActionQvalue[Action]=self.getQValue(state,Action)
        return AvailableActionQvalue[AvailableActionQvalue.argMax()]#return the key for max_actionQ(state,action)
        util.raiseNotDefined()
    def computeActionFromQValues(self, state):
        """
          GetPolicy function will use this method, so implement epsilon greedy in here is right.
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        AvailableAction=util.Counter()
        Actions=self.getLegalActions(state)
        for Action in Actions:
            AvailableAction[Action]=self.getQValue(state,Action)
        if AvailableAction.totalCount()==0:
          return random.choice(Actions)
        else:
          return AvailableAction.argMax()
        util.raiseNotDefined()  
    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.
          epsilon-greedy 
          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        Actions=self.getLegalActions(state)
        if len(Actions)==0:
          return None
        if(util.flipCoin(self.epsilon)):
          return random.choice(Actions)
        else:
          return self.getPolicy(state)
        util.raiseNotDefined()
    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here
          NOTE: You should never call this function,
          it will be called on your behalf
        """
        # print("state:"+str(state)+"action:"+str(action)+"nextState:"+str(nextState)+"R:"+str(reward))
        # print("Qvalue:"+str(self.getQValue(state,action)))
        # print(str(self.getValue(nextState)))
        self.QTable[(state,action)]=self.getQValue(state,action)+self.alpha*(reward+self.discount*self.getValue(nextState)-self.getQValue(state,action))
        #util.raiseNotDefined()
    def getPolicy(self, state):
        return self.computeActionFromQValues(state)
    def getValue(self, state):
        return self.computeValueFromQValues(state)
class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.3,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1
        alpha    - learning rate : 
        epsilon  - exploration rate :
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action
    def OutputQtableToFile(self):
        '''
        output all value in Qtable for review
        '''
        self.QTable.QvalueToFile()

class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        q_value=0
        Features=self.featExtractor.getFeatures(state,action)
        for feature in Features:
          q_value+=Features[feature]*self.weights[feature]
        return q_value
        util.raiseNotDefined()

    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        features = self.featExtractor.getFeatures(state, action)
        features_list = features.sortedKeys()
        for feature in features:
            difference = 0
            if len(self.getLegalActions(nextState)) == 0:
                difference = reward - self.getQValue(state, action)
            else:
                difference = (reward + self.discount * max([self.getQValue(nextState, nextAction) for nextAction in self.getLegalActions(nextState)])) - self.getQValue(state, action)
            self.weights[feature] = self.weights[feature] + self.alpha * difference * features[feature]
    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass
    def OutputQtableToFile(self):
        '''
        output all value in Qtable for review
        '''
        self.weights.WeightToFile()
    