from datetime import datetime, timedelta

# util functions
def get_time_diff():
    time_diff = []
    for i in range(len(nodes)):
        time_diff.append((nodes[i]-current_time).total_seconds() // 60)
    return time_diff

def get_average_time(time_diff):
    return sum(time_diff) // (len(nodes)+1)
    

# -----------------------------------------------------

# get current time
current_time = datetime.now()
print("Master node time: ", current_time.ctime())

# take no of slave node
no_of_slave_node = int(input("\nEnter no of slave node: "))

# take time difference
print("\nEnter time difference in minutes: ")
nodes=[]
for i in range(no_of_slave_node):
    time_diff = int(input(f"Node {i+1}: "))
    nodes.append(current_time + timedelta(minutes=time_diff))

# display initial time
print("\nInitial time:")
for i in range(len(nodes)): 
    print(f"Node {i+1}: {nodes[i].ctime()}")

# get time difference
time_diff = get_time_diff()
print("\nTime difference:")
for i in range(len(time_diff)):
    print(f"Node {i+1}: {time_diff[i]}")

# get average time difference
avg_diff = get_average_time(time_diff)
print("\nAverage diff: ", avg_diff)

# adjusting time
print("\nAdjusted time:")
for i in range(len(nodes)):
    nodes[i] = nodes[i] - timedelta(minutes=(time_diff[i] - avg_diff))
    print(f"Node {i+1}: {nodes[i].ctime()}")
