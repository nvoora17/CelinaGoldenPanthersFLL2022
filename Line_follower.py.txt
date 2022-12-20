from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

# declare the hardware attached to the robot
hub = PrimeHub()
color = ColorSensor('E')
right = Motor('B')
left = Motor('A')
motors = MotorPair('A', 'B')

motors.set_default_speed(50)
motors.move(15,'cm')
# Number of loops to follow the line for
count = 0;
while count < 170:
    # Debugging
    print("light: {}".format(color.get_reflected_light()))

    # What to do if we see white
    if (color.get_reflected_light() > 50):
        left.start_at_power(-35)
        right.start_at_power(0)

    # What to do if we see black
    else:
        right.start_at_power(30)
        left.start_at_power(0)
    count +=1
# Turn off motors
left.start_at_power(0)
right.start_at_power(0)
print("program over") 