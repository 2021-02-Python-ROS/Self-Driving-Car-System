# Self-Driving Car System
2021-02 Robot Programming Project
- What is? : ROS(Robot Operating System) Project
- Project Name : Self-Driving(Autonomous Driving) Car(Robot)

## How To Launch
### Gazebo
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

### Python Source
**Execute Gazebo then execute .py file**
```markdown
$ rosrun deu_car bot_state_machine.py
```
