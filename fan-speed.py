import RPi.GPIO as gpio
import timeit
import time

gpio.setmode(gpio.BOARD) #设置模式为board
gpio.setup(7,gpio.OUT)
gpio.output(7,0)
time.sleep(1)
gpio.output(7,1) #无论如何先这样操作一下
gpio.setup(7,gpio.IN)
def timer1() :
        while True :
                if gpio.input(7) == 0 : #检测下降沿
                        gpio.setup(7,gpio.OUT)
                        gpio.output(7,1)
                        gpio.setup(7,gpio.IN)
                        if gpio.input(7) == 0:
                                break

def load1() :
        gpio.setup(7,gpio.OUT) #排除掉设置的时间
        gpio.setup(7,gpio.IN)
if __name__=='__main__':
        from timeit import Timer
        import RPi.GPIO as gpio
        t1=Timer("timer1()","from __main__ import timer1") #计算两次下降沿的时间
        t2=Timer("load1()","from __main__ import load1")
        t1=t1.timeit(1)-t2.timeit(1)
        t1=t1/0.00004 #计算占空比
        print t1

