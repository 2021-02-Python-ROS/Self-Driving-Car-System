# deu car
2021-02 Robot Programming Project
- Autonomous Driving Robot

## How To Launch
**Use roslaunch:**
```markdown
$ roscd deu_car
$ source ./gazebo_env.sh
$ roslaunch deu_car car_test.launch
```

**Use .bashrc alias:**
```markdown
$ echo "alias car='roscd deu_car && source ./gazebo_env.sh && roslaunch deu_car car_test.launch''" >> .bashrc
$ car
```
