"""
Launch processes with the subprocess module

https://docs.python.org/3/library/subprocess.html
"""

import subprocess

# launch a single external process
# r = subprocess.run(["python", "fibonacci.py", str(5)])
# try some other command than Python


procs = []
for i in range(10):
    cmd = ["python", "fibonacci.py", str(i)]
    p = subprocess.Popen(cmd) # , stdout=subprocess.PIPE)
    # add stdout argument to see results immediately
    procs.append(p)

for p in procs:
    p.wait()
    # read output from pipe
    #print(p.stdout.read().encode())
