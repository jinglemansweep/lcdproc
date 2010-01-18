#!/usr/bin/env python

import time
import datetime

from lcdproc.server import Server
#from lcdproc.screen import Screen

def main():
    lcd = Server("media", debug=False)
    lcd.start_session()
    screen = lcd.add_screen("Hello")
    screen.set_cursor("off")
    screen.set_heartbeat("off")
    screen.set_backlight("on")

    
    #string_widget = screen.add_string_widget("MyStringWidget", text="TestwWEJIowejioewjio", x=1, y=2)
    #scroller_widget = screen.add_scroller_widget("MyScrollerWidget", text="This Is A Test Message, Yeah, Yeah, Yeah", speed=2)
    #hbar_widget = screen.add_hbar_widget("MyHBarWidget", x=1, y=4, length=60)
    #frame_widget = screen.add_frame_widget("MyFrameWidget")
    num1_widget = screen.add_number_widget("MyNumber1Widget", x=1, value=0)
    num2_widget = screen.add_number_widget("MyNumber2Widget", x=5, value=0)
    num3_widget = screen.add_number_widget("MyNumber3Widget", x=9, value=0)    
    num4_widget = screen.add_number_widget("MyNumber4Widget", x=13, value=0)    
    time.sleep(2)

    count = 0
    progress = 0
    while True:
        sec = datetime.datetime.now().second
        #string_widget.set_text("Hello" + str(count))
        #hbar_widget.set_length(progress)
        num1_widget.set_value(progress)
        num2_widget.set_value(progress)
        num3_widget.set_value(progress)
        num4_widget.set_value(progress)                
        time.sleep(0.1)
        count = count + 1
        progress = progress + 1
        if progress > 9: progress = 0
        pass

# Run

if __name__ == "__main__":
    main()