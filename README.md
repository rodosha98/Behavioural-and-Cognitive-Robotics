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
 Questions:
 Test your program on the CartPole-v0 problem. Does the robot manage to solve the problem? Does it solve the problem every time you run the training process? What happen by changing the parameters (e.g. size of the population, number of hidden units, the variance of the perturbation vector, the number of evaluation episodes). Test your algorithm on other simple control problem such as the Pendulum-v0.

 
 With evolututional strategy robot is able to solve the problem. But it doesn't solve it every new run. It's related to random noise. When we take best models and add randomness, even the small value of noise can dramatically affect on results, the pole will fail. The criterion of success in our case - the sum of rewards. In the best case it is equal to number of steps(Fail has not occured).
1. If you increase number of popiulation, i.e. number of networks, it will train better, the algorithm can converge faster.

2. The number of hidden layers affects on flexability of the model. Increasing of this parameter  may improve the situation a little up to a certain value.

3. Randomness can dramatically influence on the results. If you decrease it significantly, the algorithm may not evolve. But if the value is great, algorithm may not get a desired result.

4. Increasing a number of episodes enlarges the duration procedure and, correspondingly,  enlarges probability of convergence. It make our model better.

Also I've implemented script "Exercise2post.py", where you can see the behaviour of the agent after evolutionong algorithm. In case of cart pole it usually keeps the pole stable.

``` bash
Pendulum
```
The algorithm doesn't work well with a pendulum task. In my opinion, it may connected with fitness parameter(reward estimation). 
 # Evorobotpy
 It's a software with a number of libraries with network policies, scripts and etc for implementing of evolutionary algorithms. 
 ``` bash
 ```
1. Compile the source code. Go to the /lib folder and use:
``` bash
python3 setupevonet.py build_ext --inplace
cp net*.so ../bin # or cp net*.dll ../bin
```
2. You can run evolutionary algorithm with script in /bin folder (/bin/es.py). 
# Exercise 3

For this task I've cloned repository, because default one had some errors and didn't work well.
I've run few replications of the experiment by using different seeds (integer numbers like 7, 28, 9, 10).

You need to go to ./xacrobot directory.
1. Start the algorithm: 
``` bash
python3 ../bin/es.py -f acrobot.ini -s {seed}
```
where seed is your integer number. Note, that algorithm uses only one core of your processor, so you can laucnch algorithms with different seeds simultaneously.

2.The behavior of an evolved agent can be inspected with the command:
``` bash
python3 ../bin/es.py -f acrobot.ini -t bestgS11.npy
```
where the program parameter -t is used to indicate the name of the file containing the evolved
solution, it will appear in your folder. If the program parameter -t is not followed by any file name, the program will display the behavior of a robot with random parameters.

You can see the behaviour of the robot of current model(your choice). I've attached the image as an exsmple.

3. To display the variation of performance across generations and the average and standard deviation of
performance among multiple runs, you can use the following command, respectively:
``` bash
python3 ../bin/plotstat.py
python3 ../bin/plotave.py
```
In my case, the result is:
``` bash
Average Generalization: -66.64 +-1.52 (12 S*.fit files)\
 ```
I've attached images(plots) to the repository. Also I've added all files with models in my repo.
Here you can see plot of perfomance with different seeds:
![Alt text](https://github.com/rodosha98/Behavioural-and-Cognitive-Robotics/blob/master/Exercise3/plot.jpg "Behavoural plot")
On that plot we can see that algorithm converged with any value of seed and in the end it's very similar. 
And here is the example of simulation(seed 7)
![Alt text](https://github.com/rodosha98/Behavioural-and-Cognitive-Robotics/blob/master/Exercise3/robot.jpg "An example of simulation")
