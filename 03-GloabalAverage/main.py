from datetime import datetime, timedelta

class Node:
    def __init__(self,current_time) :
        self.current_time = current_time
        self.sync_diffs = []

    def update_time(self):
        self.current_time += timedelta(minutes=1)
    
    def store_sync_diff(self,sync_time):
        self.sync_diffs.append((self.current_time - sync_time).total_seconds() // 60)
    
    def adjust_to_global_average(self):
        self.global_average = sum(self.sync_diffs) / len(self.sync_diffs)
        self.current_time -= timedelta(minutes=self.global_average)



nodes = []
current_time = datetime.now().replace(hour=10, minute=15, second=0, microsecond=0)
nodes.append(Node(current_time))
nodes.append(Node(current_time - timedelta(minutes=5)))
nodes.append(Node(current_time - timedelta(minutes=3)))
nodes.append(Node(current_time - timedelta(minutes=6)))

sync_time = current_time + timedelta(minutes=15)

print("Sync time:",sync_time)

# util functions:
def update_time():
    for node in nodes: node.update_time()

def is_sync_node():
    for node in nodes:
        if (node.current_time.hour == sync_time.hour and node.current_time.minute == sync_time.minute): return True
    return False

def store_sync_node(): 
    for node in nodes: node.store_sync_diff(sync_time)

def display():
    for node in nodes: print(node.current_time)
    print()


# simulate for 30s
print("Initial: ")
display()

time_diff = 0
for i in range(30):
    update_time()
    time_diff+=1
    
    if is_sync_node():
        print(f"After {time_diff} minutes")
        display()
        store_sync_node()
        time_diff = 0


# Perform global average sync
for node in nodes: node.adjust_to_global_average()
print("After global average sync: ")
display()
