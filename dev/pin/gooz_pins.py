import dev.pin.gooz_pin_uart
import dev.pin.gooz_pin_adc
import dev.gooz_thread
import dev.pin.gooz_pin_gpio
import dev.pin.gooz_pin_pwm
import dev.pin.gooz_pin_i2c
import _thread

def init(cmd_arr):
    if cmd_arr[1] == "uart":
        if not len(cmd_arr) > 2:
            print("Missing Argument: show, write, listen, p2p or del")
            return
        if cmd_arr[2] == "show":
            dev.pin.gooz_pin_uart.show_registered_uart()
        elif cmd_arr[2] == "write":
            dev.pin.gooz_pin_uart.write(cmd_arr)
        elif cmd_arr[2] == "listen":
            dev.pin.gooz_pin_uart.listen(cmd_arr)
        elif cmd_arr[2] == "p2p":
            dev.pin.gooz_pin_uart.p2p(cmd_arr)
        elif cmd_arr[2] == "del":
            dev.pin.gooz_pin_uart.uart_delete(cmd_arr)
        elif cmd_arr[2] == "update":
            dev.pin.gooz_pin_uart.update(cmd_arr)
        else:
            print("Unknown uart command: "+'"'+cmd_arr[2]+'"')
    
    elif cmd_arr[1] =="i2c":
        if not len(cmd_arr) > 2:
            print("Missing Argument: show, write, listen, p2p or del")
            return
        if cmd_arr[2] == "show":
            dev.pin.gooz_pin_i2c.show_registered_i2c()
        elif cmd_arr[2] == "write":
            dev.pin.gooz_pin_i2c.write(cmd_arr)
        elif cmd_arr[2] == "listen":
            dev.pin.gooz_pin_i2c.listen(cmd_arr)
        elif cmd_arr[2] == "p2p":
            dev.pin.gooz_pin_i2c.p2p(cmd_arr)
        elif cmd_arr[2] == "del":
            dev.pin.gooz_pin_i2c.i2c_delete(cmd_arr)
        elif cmd_arr[2] == "update":
            dev.pin.gooz_pin_i2c.update(cmd_arr)
        else:
            print("Unknown i2c command: "+'"'+cmd_arr[2]+'"')   
            
    elif cmd_arr[1] == "adc":
        if not len(cmd_arr) > 2:
            print("Missing Argument: read, listen, del or update")
            return
        if cmd_arr[2] == "read":
            dev.pin.gooz_pin_adc.read(cmd_arr)
        elif cmd_arr[2] == "listen":
            dev.pin.gooz_pin_adc.listen(cmd_arr)
        elif cmd_arr[2] == "del" or cmd_arr[2] == "delete":
            dev.pin.gooz_pin_adc.delete(cmd_arr)
        elif cmd_arr[2] == "update":
            dev.pin.gooz_pin_adc.update(cmd_arr)
        else:
            print("Unknown ADC command: "+'"'+cmd_arr[2]+'"')
            
    elif cmd_arr[1] == "gpio":
        if not len(cmd_arr) > 2:
            print("Missing Argument: write, read, del or update")
            return
        if cmd_arr[2] == "write":
            dev.pin.gooz_pin_gpio.write(cmd_arr)
        elif cmd_arr[2] == "read":
            dev.pin.gooz_pin_gpio.read(cmd_arr)
        elif cmd_arr[2] == "del" or cmd_arr[2] == "delete":
            dev.pin.gooz_pin_gpio.delete(cmd_arr)
        elif cmd_arr[2] == "update":
            dev.pin.gooz_pin_gpio.update(cmd_arr)
        else:
            print("Unknown gpio command: "+'"'+cmd_arr[2]+'"')
            
    elif cmd_arr[1] == "pwm":
        if not len(cmd_arr) > 2:
            print("Missing Argument: write, test, close, del or update")
            return
        if cmd_arr[2] == "write":          
            dev.pin.gooz_pin_pwm.write(cmd_arr)
        elif cmd_arr[2] == "test":
            dev.gooz_pin_pwm.testing()
        elif cmd_arr[2] == "close":
            dev.pin.gooz_pin_pwm.close(cmd_arr)
        elif cmd_arr[2] == "del" or cmd_arr[2] == "delete":
            dev.pin.gooz_pin_pwm.delete(cmd_arr)
        elif cmd_arr[2] == "update":
            dev.pin.gooz_pin_pwm.update(cmd_arr)
        else:
            print("Unknown PWM command: "+'"'+cmd_arr[2]+'"')
        
    if cmd_arr[1] == "var":
        if not len(cmd_arr) > 2:
            print("Missing Argument: uart, i2c, adc, gpio or pwm")
            return
        if cmd_arr[2] == "uart":
            dev.pin.gooz_pin_uart.register(cmd_arr)
        elif cmd_arr[2] == "i2c":
            dev.pin.gooz_pin_i2c.register(cmd_arr)
        elif cmd_arr[2] == "adc":
            dev.pin.gooz_pin_adc.register(cmd_arr)
        elif cmd_arr[2] == "gpio":
            dev.pin.gooz_pin_gpio.register(cmd_arr)
        elif cmd_arr[2] == "pwm":
            dev.pin.gooz_pin_pwm.register(cmd_arr)
        else:
            print("Unknown var command: "+'"'+cmd_arr[2]+'"')

