
import threading
from time import sleep


class time_test(threading.Thread): 
      
    def __init__(self, t, dt): 
        super().__init__()
        self.t = t
        self.dt = dt
        self._running = False
    
    def stop(self):
        if self._running:
            self._running = False

    def __enter__(self):
        self.start()
        #self.wait()
        return self

    def __exit__(self, exc_type, value, traceback):
        self.stop()
            
    def run(self):
        self._running = True
        t0 = 0
        while self._running:
            if t0 != self.t:
                print('runnning '+str(t0))
                t0 += 1
                sleep(self.dt)
            else:
                self._running = False


class function_thread(threading.Thread): 
      
    def __init__(self, function, args): 
        super().__init__()
        self.function = function
        self.args = args
        self._running = False
    
    def stop(self):
        if self._running:
            self._running = False

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, value, traceback):
        self.stop()
            
    def run(self):
        self._running = True
        self.function(self.args)
        self._running = False
        


                
def get_thread_list():
    return [thread.name for thread in threading.enumerate()]



                
#time_test(5,1).start()
#time_test(5,0.2).start()

thread_count = 0
max_threads = 10
n_loops = 10


n0 = len(get_thread_list())

n_threads = 5
n = 0
while n < n_loops:
    if len(get_thread_list())-n0 < n_threads:
        
        function_thread(sleep, n+1).start()
        n += 1
        print(len(get_thread_list())-n0)
    
    
    


#print(get_thread_list())