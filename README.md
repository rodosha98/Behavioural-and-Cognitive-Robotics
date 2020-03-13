Tasks 1 and 2 on Behavioural robotics course.

# Download the container
``` bash
docker pull vkurenkov/cognitive-robotics
```
If you have troubles with permissions, use:
``` bash
sudo usermod -a -G docker username
```
where "username" is your actual docker username


# Run container
``` bash
docker run -it \
  -p 6080:6080 \
  -p 8888:8888 \
  --mount source=cognitive-robotics-opt-volume,target=/opt \
  vkurenkov/cognitive-robotics
```
If you have troubles with one of this ports, try to remove the string with it.
To launch jupiter notebook use:
``` bash
jupyter notebook --ip=0.0.0.0 --port=8888
```
To open remote Desktop, write in your browser 
``` bash
localhost:6080 (or 8888)
```
# Advices
You can connect your container with VScode application. You will need to attach VScode window to launched container.

The working directory is /opt for a reason. If you restart the container, the files will only be saved within this folder.

 # Exercises and Answering the questions
 # Exercise 1
 It contains simle simulation of cart pole.
 # Exercise 2a
 We're trying to solve cart pole stability problem. In case a we use single neural network, it can't solve the problem, even if you will change the parameters.
 # Exercise 2b
 The goal is to have maximum fitting parameter(in this case - the sum of rewards)
``` bash
 Test your program on the CartPole-v0 problem. Does the robot manage to solve the problem? Does it solve the problem every time you run the training process? What happen by changing the parameters (e.g. size of the population, number of hidden units, the variance of the perturbation vector, the number of evaluation episodes). Test your algorithm on other simple control problem such as the Pendulum-v0.
``` 
 
 With evolututional strategy robot is able to solve the problem. But it doesn't solve it every new run. It's related to random noise. When we take best models and add randomness, even the small value of noise can dramatically affect on results, the pole will fail.
1. If you increase number of popiulation, i.e. number of networks, it will train better, the algorithm can converge faster.

2. The number of hidden layers affects on flexability of the model. Increasing of this parameter  may improve the situation a little up to a certain value.

3. Randomness can dramatically influence on the results. If you decrease it significantly, the algorithm may not evolve. But if the value is great, algorithm may not converge.

4. Increasing a number of epizodes increase the duration procedure and, correspondingly,  enlarges probability of convergence.




 
