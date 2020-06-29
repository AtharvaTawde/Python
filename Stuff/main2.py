#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

#gripper_motor = Motor(Port.A)
#elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])
#base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
#elbow_motor.set_run_settings(60, 120) 
#base_motor.set_run_settings(60, 120)
#base_switch = TouchSensor(Port.S1)
#elbow_sensor = ColorSensor(Port.S3)
#elbow_motor.run_time(-30, 1000) 
#elbow_motor.run(15) 
#while elbow_sensor.reflection() < 32: 
#    wait(10) 
#elbow_motor.reset_angle(0) 
#elbow_motor.stop(Stop.HOLD)
#
#base_motor.run(-60) 
#while not base_switch.pressed(): 
#    wait(10) 
#base_motor.reset_angle(0) 
#base_motor.stop(Stop.HOLD)
#
#gripper_motor.run_until_stalled(200, Stop.COAST, 50) gripper_motor.reset_angle(0) gripper_motor.run_target(200, -90)
#def robot_pick(position): 
#    base_motor.run_target(60, position, Stop.HOLD) 
#    elbow_motor.run_target(60, -40) #
#    gripper_motor.run_until_stalled(200, Stop.HOLD, 50) 
#    elbow_motor.run_target(60, 0, Stop.HOLD)
#def robot_release(position): 
#    base_motor.run_target(60, position, Stop.HOLD) 
#    elbow_motor.run_target(60, -40) 
#    gripper_motor.run_target(200, -90) 
#    elbow_motor.run_target(60, 0, Stop.HOLD)
#brick.sound.beeps(3)
#LEFT = 160 
#MIDDLE = 100 
#RIGHT = 40
#
#while True: 
#    robot_pick(LEFT) 
#    robot_release(MIDDLE)
#    robot_pick(RIGHT) 
#    robot_release(LEFT)
#    robot_pick(MIDDLE) 
#    robot_release(RIGHT)

brick.sound.beep()