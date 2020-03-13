import gym
import time 
gym.logger.set_level(40)
env = gym.make('CartPole-v0')

env.reset()
print(env.action_space)
print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)
for _ in range(200):
    time.sleep(0.01)
    env.render()
    observation, reward, done, info = env.step(env.action_space.sample())
    if done == True:
        env.reset()
env.close()
