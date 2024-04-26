class Process:
    current_time = 0
    request_delay_queue = {}
    request_queue = []

    def __init__(self, id):
        self.isRequesting = False
        self.id = id
        self.timestamp = None

    def update_time(self):
        self.current_time += 1
        if self.current_time in self.request_delay_queue:
            process = self.request_delay_queue[self.current_time]
            process.respond()
    
    def request(self, process, timestamp):
        if(timestamp < self.timestamp):
            self.request_delay_queue[self.current_time+2] = process
