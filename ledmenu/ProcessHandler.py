from multiprocessing import Process
class ProcessHandler:
    #array in case multiple processes get started somehow and desync
    processes = []
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProcessHandler, cls).__new__(cls)
        return cls.instance

    def kill_process(self):
        for process in self.processes:
            process.terminate()
        self.processes = []

    def start_process(self, func, args):
        if len(self.processes) < 2:
            p = Process(target=func, kwargs=args)
            p.start()
            self.processes.append(p)