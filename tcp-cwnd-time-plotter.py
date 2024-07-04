import matplotlib.pyplot as plt


input_file = "tcp----modified.txt"

time = []
cwnd = []

# Read data from the file
with open(input_file, 'r') as f:
    for line in f:
        t, c = line.split()
        time.append(float(t))
        cwnd.append(int(c))

# Plot the data
plt.plot(time, cwnd)
plt.xlabel('Time (s)')
plt.ylabel('Congestion Window (bytes)')
plt.title('TCP -- Congestion Window Over Time')
plt.grid(True)
plt.show()

