import webbrowser
import time

total_break=3
break_count=0

print("This program started on"+ time.ctime())

while(break_count<total_break):
    time.sleep(10)
    webbrowser.open("http://www.udacity.com")
    break_count = break_count + 1
