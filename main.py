import astar
from path_item import PathItem
from datetime import datetime

if __name__== "__main__":
    start = PathItem(1 -1) #station index+1
    target = PathItem(5 -1) #station index+1

    t1 = datetime.now()
    steps = astar.resolve(start,target)
    t2 = datetime.now()
    
    for step in steps:
        print("E{0} acumulando {1} minutos".format(step.station+1, step.calc_G()))
    print("end with {0} steps. started at {1} ended at {2}".format(len(steps), str(t1), str(t2)))
