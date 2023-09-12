import time
import threading

global_num = 10
run_thread = True

def func():
        global global_num
        global run_thread
        #print("lets strart thread")
        while run_thread:
            global_num +=1
            #print (hi from thread flobal_num= {global_num})
            time.sleep(2)

def stop_func():
    global run_thread
    a=" "
    while a != "1":
        #print (currently the glabal_num={global_num}")
        a= input("type stop to stop: \n")
    run_thread=False1


my_thread= threading.Thread(target=func)
my_thread.start()
stop_func()
my_thread.join()
print(f"done {global_num}")


