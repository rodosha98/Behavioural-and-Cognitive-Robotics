# Exercise 4: 

We have target point and want the robot to move to it in both cases. 
Reward function of original version is comprised of several functions: alive - it checks fall robot or not by measuring the height of the robot, progress - Difference between new and old potentials, it shows the movement to the target, electricity_cost -  a cost against the motors, must be tuned against the reward, joints_at_limit_cost -  a penalty due to stucking joints of the robot and feet_collision_cost - it's a penalty to avoid the unnecessary collisions.
All these parameters are described for each class of robot separately.
The robot_loclomotors.py function is able to calculate states, apply actions, calculete alive bonuses and rewards, etc for each type of robot.

Components of the modified version and main differences. It has the same components but they have some changes:
* alive bonus is changed.  
* feet_cost and feet_collision_cost - allows to calculate feet contacts and shows if both of the feet on the ground or not.  Also, there is condition rule that gives penalty -1.0 if both feet not on the ground, and -0.33 if both feet on the ground somehow
* angle_offset_cost - in addition we measure the angle to the target and this term is the penalty that shows how much is angle offset between the robot and the target.
Reward function were changed for each type of robot, because they have different structures, moving important parts, etc.

# How to launch model:
1. Use commands to build the net in the ./lib directory:
``` bash
python3 setupevonet.py build_ext --inplace
cp net*.so ../bin # or cp net*.dll ../bin
```
2. Launch learning process(from the model.ini directory)
``` bash
python3 ../bin/es.py -f (model name).ini -s (number of seed)
```
3. See results(behavior)
``` bash
python3 ../bin/es.py -f (model name).ini  -t (bestmodel.npy)
```
I've launched the algorithm for hopper and halfcheetah models and humanoid with both of reward functions. In case of original rewarding function, the robot can't move toward the target, it either falls down(hopper) or get stucked(cheetah), i.e. legs are moving, but the whole robot can't move properly.  Modified function gave better results, and agents are able to move forward the goal. 

# Explanation

In evolutionary algorithms we must use the population of agents, learn them and pick only best ones, further learning is based on that ones (next generation). The whole process continues until certain moment. Original function are suitable for only reinforcement method, which is working with only one agent, so it can't produce evolutionary algorithms. 

Modified function is adapted to fit evolutionary strategies. There is some changes in alive bonus estimation, additional constraints like angle estimation and feet collision(calculating feet contacts), body_minx. Main contribution in my opinion gives the function that estimates the contact of the floor for each pair of limbs. Thus, that allows robot to avoid meaningless movements and be stable. Strategies of estimation were rewritten for each class of robot and the important thing is that for each single robot we can choose main criterions of reward functions(not the sum of rewards), and that combination of features will depend on configuration of the robot. That is why the robots can reach their goal.



