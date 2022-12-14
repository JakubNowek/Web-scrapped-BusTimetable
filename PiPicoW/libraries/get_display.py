# using library from https://github.com/rdagger/micropython-ili9341

import ili9341
import mySetup

from machine import Pin, SPI
from xglcd_font import XglcdFont
led = Pin(21, Pin.OUT)
led.high()
display = mySetup.createMyDisplay()
unispace = XglcdFont('lib/fonts/Unispace12x24.c', 12, 24)

# definicja kolorow linii tekstu na wyswietlaczu
def_color = {"Head": ili9341.color565(10, 200, 252),
             "First": ili9341.color565(0, 0, 200),
             "Middle": ili9341.color565(200, 200, 200),
             "Last": ili9341.color565(200, 20, 10),
             "Black":ili9341.color565(0,0,0) 
            }
    
    
def print_board(data,update,name):
    
    name = '{:' '<15}'.format(name[:15])
    update = '{:' '>10}'.format(update)
    x = 0
    y = 0
    # define head
    text = "Linia Kierunek      Odjazd"
    display.draw_text(x, y, text, unispace,
                      def_color["Head"])  # ostatnia wyświetlana linia
    for line in data:
        y+=36
        if y==36:
            color = def_color["First"]
        elif y==72 or y==108 or y==144:
            color = def_color["Middle"]
        elif y==180:
            color = def_color["Last"]
            
        # read line
        linia, kierunek, odjazd = line[0], line[1], line[2]
        # line format
        text2 = '{:' '<3}'.format(linia[:3]) +\
                ' ' + '{:' '<11}'.format(kierunek[:11]) +\
                ' ' + '{:>9}'.format(odjazd[:9])
        display.draw_text(0, y , text2, unispace,
                          color)
    # display.fill_hrect(200, 216 ,119 ,24, def_color["Black"]) 
    display.draw_text(0, 216 , name+update, unispace,
                          def_color["Head"])
                   
    


