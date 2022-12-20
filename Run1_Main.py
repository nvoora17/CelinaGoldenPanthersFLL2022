from spike import MotorPair,Motor


# Mission 8 Watching Tv Start
movement_motors = MotorPair('A','B') # Set up the movement motors (wheels)

movement_motors.set_default_speed(50) # Set up the motor speed

movement_motors.move(45,'cm') # moving the robot forwards
# Mission 8 Watching Tv End

# Mission Windmill Start
movment_motors = MotorPair('A','B')

movment_motors.set_default_speed(50)
movment_motors.move(-10,'cm') #moving the robot backwards away from the last mission 

motor = Motor('B')
# Rotate the motor 90 degrees clockwise
motor.run_for_degrees(270)


movment_motors.move(27,'cm')
motor = Motor('A')
motor.run_for_degrees(-540) #moving the robot twords the direction of th windmill
movment_motors.set_default_speed(75)
movment_motors.move(-3,'cm')
movment_motors.move(17,'cm')
movment_motors.move(-10,'cm')
movment_motors.move(19,'cm')
movment_motors.move(-10,'cm')
movment_motors.move(17,'cm')
movment_motors.move(-5,'cm')



movment_motors.move(-5,'cm')





