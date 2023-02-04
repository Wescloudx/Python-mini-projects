class channel_list():
    
    def __init__(self,current = -1):
        self.current = current
        self.list = ["Show","ATV","Bloomberg","NTV","TLC"]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.current < len(self.list)):
                self.current += 1
                return self.list[self.current]
        else:
            raise StopIteration
            
channel = channel_list()
channel_iter = iter(channel)

print(next(channel_iter))