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
ep_num = 100 #10 episodes
net_num = 10 #diff networks on each epizode
steps = 200 # 200 steps for each NN
sub_num = 5 # number of substitutions of networks 
W1 = np.random.randn(nhiddens, ninputs, net_num) * pvariance # Quantity corresponds to the number of nets
# first layer
W2 = np.random.randn(noutputs, nhiddens, net_num) * pvariance
# second layer
b1 = np.zeros(shape=(nhiddens, 1, net_num))
# bias first layer
b2 = np.zeros(shape=(noutputs, 1, net_num))
# bias second layer
for ep in range (ep_num):
    rew_sum = np.zeros(net_num, dtype = float)
    for net in range (net_num):
        observation = env.reset() # Start from the initial point
        for _ in range (steps):
            # UPDATE nn on each step
            
            #time.sleep(0.1)
            
            # convert the observation array into a matrix with 1 column and ninputs rows
            observation.resize(ninputs,1)
            # convert the observation array into a matrix with 1 column and ninputs rows
            observation.resize(ninputs,1)
            # compute the netinput of the first layer of neurons
            Z1 = np.dot(W1[:, :, net], observation) + b1[:, :, net]
            # compute the activation of the first layer of neurons with the tanh function
            A1 = np.tanh(Z1)
            # compute the netinput of the second layer of neurons
            Z2 = np.dot(W2[:, :, net], A1) + b2[:, :, net]
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
            rew_sum[net] = rew_sum[net] + reward #fitting value is the sum of the reward
    #Sort, inverse the order and take the best ones (minus means take from the end)
    good = rew_sum.argsort()[-sub_num:][::-1] 
    bad = rew_sum.argsort()[:sub_num][::-1]
    print('Reward sum', rew_sum)
    print('Indeces of best networks', good)
    # Replace 
    W1[:, :, bad] = W1[:, :, good] + np.random.randn(nhiddens, ninputs,sub_num) * ppvariance
    W2[:, :, bad] = W2[:, :, good] + np.random.randn(noutputs, nhiddens, sub_num) * ppvariance
    b1[:, :, bad] = b1[:, :, good] + np.random.randn(nhiddens, 1, sub_num) * ppvariance
    b2[:, :, bad] = b2[:, :, good] + np.random.randn(noutputs, 1, sub_num) * ppvariance

#POST evaluation 
# Best nn
# Post-evaluation stage
print('\nStart stage after trainig\n')

best_nn = rew_sum.argsort()[-1:] # take the best neural network controller

W1 = W1[:, :, best_nn].reshape((nhiddens, ninputs))
W2 = W2[:, :, best_nn].reshape((noutputs, nhiddens))
b1 = b1[:, :, best_nn].reshape((nhiddens, 1))
b2 = b2[:, :, best_nn].reshape((noutputs, 1))

for ep in range(ep_num):
    best_rew_sum = 0
    observation = env.reset()
    for _ in range(steps):
        env.render()
        time.sleep(0.01)

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
        if (isinstance(env.action_space, gym.spaces.box.Box)):
            action = A2
        else:
            action = np.argmax(A2)

        observation, reward, done, info = env.step(action)
        best_rew_sum = best_rew_sum + reward

    print('Reward during the post-evaluation', rew_sum)

env.close()
