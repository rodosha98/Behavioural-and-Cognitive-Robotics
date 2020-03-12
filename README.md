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
# Advices
You can connect your container with VScode application.

The working directory is /opt for a reason. If you restart the container, the files will only be saved within this folder.
