import os, sys

def procStatus(pid):
    for line in open("/proc/%d/status" % pid).readlines():
        if line.startswith("State:"):
            return line.split(":",1)[1].strip().split(' ')[1]
    return None

if __name__=="__main__":
    pid = int(sys.argv[1])
    print(procStatus(pid))

