# threading cannot be used for cpu bound operations
# it can only be used for i/o bound operations

import threading
import time
start = time.perf_counter()

#def some():
#    time.sleep(1)
#    print(1)
#some()
#some()

# on calling the above function  once it will take approx one minute to complete
# and on calling it twice it will take approx 2 sec
# but if we want it to take only one sec on calling it twice
# we will use threading
# see -->>

# we will create a thread


#thread = threading.Thread(target=some)
#t2 = threading.Thread(target=some)

# we have just created a thread we are not running the code inside the function
# no we'll start the object that we have created


#thread.start()
#t2.start()

# now if we run the code it will show that it finished in 0.0secs and print the 1s
# this is because while our inside the function was seeping it came outside and run the code that tells us about the time
# and when the code was done with sleeping it run the script 
# now to overcome this will use the join()

#thread.join()
#t2.join()

#now if want to run this code more than two times or maybe 8 times
# usually if we look at it without using thread it will take 8 sec as it will run the code simlutenously
# do not use t.join() or join() in the loop as it join on the thread before the next call
# to overcome this will append the threads to a list and run the join() on that list
#threads = []
#for _ in range(8):
#    t = threading.Thread(target=some)
#    t.start()
#    threads.append(t)
#print(threads)
# just do it 
#for thread in threads:
#    thread.join()

# now lets do something new
# lets the function argument decide that for how much time the function will sleep
def some(sec):
    print(f'sleep for {sec} seconds')
    time.sleep(sec)
    print("done sleeping")
# how do we pass in the arguments??
# for that we will pass the arguments as list.. jst look

threads = []
for _ in range(10):
    t = threading.Thread(target=some, args=[1.3])
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()

# we can see in the argumnets that it had only taken that much time 
# that we have passed in the args= 

        finish = time.perf_counter()
print(f'finished in {round(finish-start, 2)}secs')
