from spike import MotorPair,Motor
from spike.control import wait_for_seconds
#truck mission
movement_motors = MotorPair('A','B') # Set up the movement motors (wheels)
right_motor = Motor('B')
left_motor = Motor('A')
extension_motor= Motor ('D')

movement_motors.set_default_speed(60) # Set up the motor speed 60

movement_motors.move(58,'cm') # moving the robot forwards
left_motor.run_for_degrees(190)
movement_motors.move(-58,'cm')
#left_motor.run_for_degrees(-140)
#movement_motors.move(-30,'cm')
#extension_motor.run_for_degrees(-40,80)
