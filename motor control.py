import board #start board
import analogio #start board
import pwmio

motor=pwmio.PWMOut(board.D3, duty_cycle=2**15,frequency=5000) #
pot=analogio.AnalogIn(board.A1)
while True:
    print(pot.value)
    speed=pot.value
    motor.duty_cycle=speed