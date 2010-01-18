#!/usr/bin/env python

import time
import datetime

from lcdproc.server import Server

def main():

    lcd = Server("media", debug=False)
    lcd.start_session()
    
    screen1 = lcd.add_screen("Screen1")
    screen1.set_heartbeat("off")
    screen1.set_duration(10)
    
    screen2 = lcd.add_screen("Screen2")
    screen2.set_heartbeat("off")
    screen2.set_duration(2)

    #string_widget = screen.add_string_widget("MyStringWidget", text="TestwWEJIowejioewjio", x=1, y=2)
    #scroller_widget = screen.add_scroller_widget("MyScrollerWidget", text="This Is A Test Message, Yeah, Yeah, Yeah", speed=2)
    #hbar_widget = screen.add_hbar_widget("MyHBarWidget", x=1, y=4, length=60)
    #frame_widget = screen.add_frame_widget("MyFrameWidget")
    
    num1_widget = screen1.add_number_widget("MyNumber1Widget", x=1, value=0)
    num2_widget = screen1.add_number_widget("MyNumber2Widget", x=5, value=0)
    num3_widget = screen1.add_number_widget("MyNumber3Widget", x=9, value=0)    
    num4_widget = screen1.add_number_widget("MyNumber4Widget", x=13, value=0)    

    time.sleep(2)

    progress = 0
    
    while True:
    
        num1_widget.set_value(progress)
        num2_widget.set_value(progress)
        num3_widget.set_value(progress)
        num4_widget.set_value(progress)                
    
        time.sleep(0.5)
        
        progress = progress + 1
        if progress > 9: progress = 0
        
# Run

if __name__ == "__main__":
    main()