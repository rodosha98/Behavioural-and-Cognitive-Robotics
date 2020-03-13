import gym
import numpy as np
import time 
gym.logger.set_level(40)
env = gym.make('CartPole-v0')

pvariance = 0.1
# variance of initial parameters
ppvariance = 0.02
# variance of perturbations
nhiddens = 5
# number of hidden neurons
# the number of inputs and outputs depends on the problem
# we assume that observations consist of vectors of continuous value
# and that actions can be vectors of continuous values or discrete actions
ninputs = env.observation_space.shape[0]
if (isinstance(env.action_space, gym.spaces.box.Box)):
    noutputs = env.action_space.shape[0]
else:
    noutputs = env.action_space.n
    # initialize the training parameters randomly by using a gaussian distribution with average 0.0 and variance 0.1
    # biases (thresholds) are initialized to 0.0


# Describe the model and /nets
ep_num = 10 #10 episodes
#net_num = 1 #diff networks on each epizode
steps = 200 # 200 steps for each NN
sub_num = 5 # number of substitutions of networks 
W1 = np.random.randn(nhiddens, ninputs) * pvariance # Quantity corresponds to the number of nets
# first layer
W2 = np.random.randn(noutputs, nhiddens) * pvariance
# second layer
b1 = np.zeros(shape=(nhiddens, 1))
# bias first layer
b2 = np.zeros(shape=(noutputs, 1))
# bias second layer
for ep in range (ep_num):
    rew_sum = 0
    observation = env.reset() # Start from the initial point
    for _ in range (steps):
        # UPDATE nn on each step
        
        #time.sleep(0.1)
        
        # convert the observation array into a matrix with 1 column and ninputs rows
        observation.resize(ninputs,1)
        # convert the observation array into a matrix with 1 column and ninputs rows
        observation.resize(ninputs,1)
        # compute the netinput of the first layer of neurons
        Z1 = np.dot(W1, observation) + b1
        # compute the activation of the first layer of neurons with the tanh function
        A1 = np.tanh(Z1)
        # compute the netinput of the second layer of neurons
        Z2 = np.dot(W2, A1) + b2
        # compute the activation of the second layer of neurons with the tanh function
        A2 = np.tanh(Z2)
        # if actions are discrete we select the action corresponding to the most activated unit
        # if actions are discrete we select the action corresponding to the most activated unit
        if (isinstance(env.action_space, gym.spaces.box.Box)):
            action = A2
        else:
            action = np.argmax(A2)
        
        env.render()

        observation, reward, done, info = env.step(action)
        rew_sum = rew_sum + reward #fitting value is the sum of the reward
    #Sort, inverse the order and take the best ones (minus means take from the end)
    print('Reward sum', rew_sum)
   
env.close()