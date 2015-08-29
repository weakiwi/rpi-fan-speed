import RPi.GPIO as gpio

def ctrl():
        gpio.setmode(gpio.BOARD)#rpi.gpio初始化
        gpio.setup(37,gpio.OUT)#设置模式为输出
        p = gpio.PWM(37,1)  #设置pwm
        p.start(1)
        input('press to stop')
        p.stop()
        gpio.cleanup()

if __name__ == '__main__':
        ctrl()
