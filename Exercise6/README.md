# Exercise 6: 
## Kinematic Simulations

>The source code (discrim.cpp, discrim.h, utilities.cpp, utilities.h, robot-env.cpp, robot-env.h, ErDiscrim.pxd, ErDiscrim.pyx, and setupErDiscrim.py) can be compiled from the ./lib folder with the following instructions:


```bash
python3 setupErDiscrim.py build_ext --inplace
cp ErDiscrim*.so ../bin # or cp ErDiscrim*.dll ../bin
```

The discrim.cpp and discrim.h files include the definition of the gym functions (i.e. env-reset(), env.step(), env.render() ext.) and the calculation of the reward. The robot-env.cpp and robot-env.h files include a series of methods that permit to simulate the translation and rotation movement of the robot in 2D, the activation of the infrared sensors, and the occurrence of collision. The program terminates the evaluation episode when a collision occurs. Consequently, there is no need to model the effect of collisions in detail. The robot-env.cpp and robot-env.h files permit to simulate also two other type of wheeled robots: the ePuck (Mondada et al., 2009) and the MarXbot (Bonani et al., 2010). These robots are used in other environments.
  
# Task
> Run 10 replications of the experiment from the evorobotpy/xdiscrim folder by using different seeds. 
To launch the training process go to the ./xdiscrim directory and use the following command:
``` bash
python3 ../bin/es.py -f ErDiscrim.ini -s (seed_number)
```
I used this sequence of seeds: 1, 5, 7, 8, 9, 10, 15, 17, 19, 28. I uploaded all files with results.
> Test and analyze the strategy displayed by best robot of each replication. Describe the strategies of the robots by grouping them in families. Try to explain why the robot of each family behave in that manner.  

I noticed 4 different behaviors of the robot:
* 1. Seeds 1, 5, 7, 8, 10, 17. Robot moves to the target, eventually reaches it and stops near it.
* 2. Seeds 15, 28. Robot moves to the target and then it goes around the target in a circle.
* 3. Seed 19. Robot moves to the target and then  rotates around its axis.
* 4. Seed 9. Robot moves to the target and then it oscillates around the point, moving from side to side.

Here you can see the examples of cases 1 and 2:
![Alt text](https://github.com/rodosha98/Behavioural-and-Cognitive-Robotics/blob/task4-6/Exercise6/stuck.jpg "The robot gets stucked near the target")

![Alt text](https://github.com/rodosha98/Behavioural-and-Cognitive-Robotics/blob/task4-6/Exercise6/rotation.jpg "The robot moves to the target and then goes around it in a circle")

The robot is able to reach the target in all cases, because it has sensors, which allow him to perceive the environment very well.Different behavior strategies in my opinion are due to the difference in the training process and the presence of a large number of sensors, that is, in each case, the robot can perceive the environment differently and build its behavior accordingly

> Run other experiments by using a feed-forward neural architecture (without memory). 
To enable Feed Forward neural network mode go to the ./xdiscrim folder and open ErDiscrim.ini file.
There find the line architecture:
``` bash
architecture = 3. Enables LSTM (Long Short Term Memory architecture)
architecture = 0. Enables Feed forward neural architecture without memory.
```
I've run experiments and noticed that sometimes the robot is able to reach the target, sometimes it moves very slowly and drives past the target, sometimes very quickly and can't reach. In all cases it can't stop near the target.
> Explain how the behavior of evolved robots differ from those evolved with the LSTM architecture (i.e. the Long Short Term Memory architecture).
I've run experiments and noticed that sometimes the robot is able to reach the target, sometimes it moves very slowly and drives past the target, sometimes very quickly and can't reach. In all cases it can't stop near the target. The robot doesn't know where to stop due to it hasn't feedback part and can't estimate the state properly. That is why it can go through the target and skip it
