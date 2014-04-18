#"Stopwatch: The Game"
import simplegui

# define global variables
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
def start():
    timer.start()
    
def stop():
    global numberOfStops, success
    if timer.is_running():
        timer.stop()
        numberOfStops += 1
        if seconds%10 == 0:
            success += 1
             
def reset():
    global minutes, seconds, tenths, success, numberOfStops
    minutes,seconds,tenths,success,numberOfStops = 0,0,0,0,0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global tenths
    tenths += 1

# defining draw handler
def draw(canvas):
    FormatTime = format(0)
    fontSize = 50
    width = frame.get_canvas_textwidth(FormatTime, fontSize)
    canvasWidth = (frameWidth - width)//2
    canvasHeight = (frameHeight*2 + fontSize)//4
    canvas.draw_text(FormatTime,[canvasWidth, canvasHeight],fontSize,'RED')
    
    fontSize = 30
    formatAttempt = str(success)+'/'+str(numberOfStops)
    widthOfScore = frame.get_canvas_textwidth(formatAttempt, fontSize)
    canvas.draw_text(formatAttempt, (frameWidth - widthOfScore*5//4, fontSize), fontSize,'YELLOW')
    
# creating frame
frame = simplegui.create_frame("STOPWATCH", frameWidth, frameHeight)
timer = simplegui.create_timer(100, tick)

# registering event handlers
frame.set_draw_handler(draw)
startButton = frame.add_button("START", start)
stopButton = frame.add_button("STOP", stop)
resetButton = frame.add_button("RESET", reset)

# starting frame
frame.start()

