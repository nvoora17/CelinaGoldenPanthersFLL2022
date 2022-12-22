from spike import MotorPair,Motor


# Mission 8 Watching Tv Start
movement_motors = MotorPair('A','B') # Set up the movement motors (wheels)

movement_motors.set_default_speed(50) # Set up the motor speed

movement_motors.move(45,'cm') # moving the robot forwards
# Mission 8 Watching Tv End

# Mission Windmill Start

movement_motors.move(-10,'cm') #moving the robot backwards away from the last mission

motor = Motor('B')
# Rotate the motor 270 degrees clockwise
motor.run_for_degrees(270)

movement_motors.move(25,'cm')
motor = Motor('A')
motor.run_for_degrees(-538) #moving the robot twords the direction of th windmill
movement_motors.set_default_speed(75)
movement_motors.move(-3,'cm')
movement_motors.move(21,'cm')
movement_motors.move(-12,'cm')
movement_motors.move(21,'cm')
movement_motors.move(-12,'cm')
movement_motors.move(22,'cm')
movement_motors.move(-10,'cm')

#End of the windmill mission

#Start of hybrid car mission

movement_motors.set_default_speed(50)

movement_motors.move(-39,'cm')#moving the robot backwards away from the last mission
motor = Motor('B')

motor.run_for_degrees(525)#Rotate the motor 515 degrees clockwise
movement_motors.move(34,'cm')#moving twoards the hybrid car

motor = Motor('A')
motor.run_for_degrees(-300)#turning -300 degrees twoards the hybrid car

movement_motors.move(-10,'cm')#pushing the hybrid car




