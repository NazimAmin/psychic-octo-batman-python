 "Stopwatch: The Game"
 
import simplegui
import random
import math

# define global variables
t = 0
frameWidth = 300
frameHeight = 200
minutes = 0
seconds = 0
tenths = 0
success = 0
numberOfStops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global seconds
    minutes = tenths//600
    seconds = (tenths//10)%60
    if seconds < 10:
        seconds = '0'+str(seconds)
    t = tenths%10
    
    return str(minutes)+':'+str(seconds)+'.'+str(t)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

#timer start handler
def start():
    timer.start()

#timer stop handler
def stop():
    global numberOfStops, success
    if timer.is_running():
        timer.stop()
        numberOfStops += 1
        if seconds%10 == 0:
            success += 1

#timer reset handler             
def reset():
    global t, minutes, seconds, tenths, success, numberOfStops
    t,minutes,seconds,tenths,success,numberOfStops = 0,0,0,0,0,0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global tenths
    tenths += 1

# define draw handler
def draw(canvas):
    FormatTime = format(t)
    size = 60
    width = frame.get_canvas_textwidth(FormatTime, size)
    canvasWidth = (frameWidth - width)//2
    canvasHeight = (frameHeight*2 + size)//4
    canvas.draw_text(FormatTime,[canvasWidth, canvasHeight],size,'RED')
    
    formatAttempt = str(success)+'/'+str(numberOfStops)
    widthOfScore = frame.get_canvas_textwidth(formatAttempt, 30)
    canvas.draw_text(formatAttempt, (frameWidth - widthOfScore*5//4, 30), 30,'YELLOW')
    
# create frame
frame = simplegui.create_frame("STOPWATCH", frameWidth, frameHeight)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)
startButton = frame.add_button("START", start)
stopButton = frame.add_button("STOP", stop)
resetButton = frame.add_button("RESET", reset)

# start frame
frame.start()
