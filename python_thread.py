import threading
import time

def my_callback():
    
    print( "mississipi")
    

def start_timer(seconds, callback):
    def my_sleep():
        time.sleep(seconds)
        callback()
    
    thread = threading.Thread(target=my_sleep)
    thread.start()

# Start a 5-second timer with a callback
start_timer(2, my_callback)

print("Timer started. Waiting for it to finish...")