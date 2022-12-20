from spike import MotorPair,Motor



# Mission 8 Watching Tv Start



movement_motors = MotorPair('A','B') # Set up the movement motors (wheels)

movement_motors.set_default_speed(50) # Set up the motor speed



movement_motors.move(45,'cm') # moving the robot forwards 



# Mission 8 Watching Tv End



# Mission Windmill Start



movment_motors = MotorPair('A','B')

movment_motors.set_default_speed(50)



movment_motors.move(-10,'cm') #moving the robot backwards 