# now we will use threading pool executer 
# its not in the threding module instead it is in concurrent.futures module

import time
import concurrent.futures

start = time.perf_counter()

def some(seconds):
    print(f'sleeping for {seconds} seconds')
    time.sleep(seconds)
    return f'we are slept ....{seconds} '

# we are going to create context manager
#with concurrent.futures.ThreadPoolExecutor() as executor:
    # we are going to use submit method
    # it schedules a function to be executed and returns a future object
#    f = executor.submit(some, 1)
    # here 'f' is the future object 
    # a future object encapsulate the execution of our function
    # helps us to grab its result
#    print(f.result())

# now if we want to run it multiple time then we can use loop

with concurrent.futures.ThreadPoolExecutor() as exe:
    # i m gonna use list comprehension
    secs = [4,3,2,1]
    #results = [exe.submit(some, sec) for sec in secs]
    
    
    #to get the results we can use as_completed method that returns us the 
    # itreator on which we can loop over to get the results

    #for f in concurrent.futures.as_completed(results):
    #    print(f.result())
    # with map method
    results = exe.map(some, secs)
    for result in results:
        print(result)

    #now map function will return the results instead of the future object
    
finish = time.perf_counter()
print(f'finished in {round(finish-start)} seconds')