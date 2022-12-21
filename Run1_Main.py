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

movement_motors.move(27,'cm')
motor = Motor('A')
motor.run_for_degrees(-540) #moving the robot twords the direction of th windmill
movement_motors.set_default_speed(70)
movement_motors.move(-3,'cm')
movement_motors.move(19,'cm')
movement_motors.move(-10,'cm')
movement_motors.move(19,'cm')
movement_motors.move(-10,'cm')
movement_motors.move(19,'cm')
movement_motors.move(-10,'cm')

#End of the windmill mission 

#Start of hybrid car mission 

movement_motors.set_default_speed(50)

movement_motors.move(-20,'cm')#moving the robot backwards away from the last mission
motor = Motor('B')

motor.run_for_degrees(400)#Rotate the motor 400 degrees clockwise
movement_motors.move(50,'cm')#moving twoards the hybrid car 
movment_motors.move(-10,'cm')#pushing the hybrid car 




