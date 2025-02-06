import threading 

def my_callback(): 
        print("Timer finish") 

def start_timer(seconds, callback): 
        def timer_thread(); 
                threading.Event().wait(seconds)
                callback() 

thread = threading.Thread(target=timer_thread)
thread.start() 

# start a 5 second timer
start_timer(5, my_callback)

print("timer start")