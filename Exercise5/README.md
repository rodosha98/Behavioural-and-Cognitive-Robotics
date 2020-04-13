# Exercise 5: 
## Implementing a new Gym/Bullet environment

> The guide https://backyardrobotics.eu/2017/11/27/build-a-balancing-bot-with-openai-gym-pt-i-setting-up/. 

I've complited the guide ehich is comprised of 2 parts step by step. I used OpenAI Gym, Baselines and pyBullet to implement this task. As the result I've created new environment 'balancebot.v0'. It has certain structure and contains xml-file with robot description and "balancebot_env.py" script, which contains main environment methods (init(), seed(), step(), reset(), render(), methods for estimation of reward, observations, actuators and termination processs). 

1. Build the environment:
``` bash
cd balance-bot
pip install -e .
```
2.Ready environment can be used in the following way:
```
import balance_bot
```
3. I've decided to train the model as in the previous cases. For this I've created balancebot.ini fail, where you need to identify the environment 'balancebot.v0. Also you need to go to the ./bin/es.py and add there the line from clause 2. 

To train the model use command(from balancebot.ini directory):
``` bash
python3 ../../bin/es.py -f balancebot.ini -s (seed)
```
I've picked s = 7. 
Then to see results use:
``` bash
python3 ../../bin/es.py -f balancebot.ini -t (model_name)
```
Model_name, for example bestgS7.npy. 
You can install the environment with the following instructions:

```bash
cd balance-bot
pip install -e .
```

Finally, you can use balance_bot as a standard gym environment after importing it with the following
instructions:

```bash
import balance_bot
```

If you have some mode problems with ```policy.py``` file, go to it and change line
```bash
self.env.render()
``` 
to 
```bash
self.env.render(mode = 'human')
``` 

Note!
If you evolve model, change line in ```balancebot_env.py``` file
```bash
self.physicsClient = p.connect(p.DIRECT)  # Non-Graphical version (for evolving)
``` 

If you want to seee evolved model, change line in ```balancebot_env.py``` file
```bash
self.physicsClient = p.connect(p.GUI)  # Graphical version
```
If you chose graphical version, you can see the learning process with gpu, the model will fall initially.  
# Picture 
Here you can see the screenshot from the simulation
![Alt text](https://github.com/rodosha98/Behavioural-and-Cognitive-Robotics/blob/task4-6/Exercise5/balancebot.jpg "The balancebot simulation in the new environment.")
