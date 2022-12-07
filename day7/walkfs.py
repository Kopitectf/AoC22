import os 
answersum = 0

def get_size(dir):
    global answersum
    sumsize = 0
    for thing in os.scandir(dir):
        size = 0
        if thing.is_dir():
            size = get_size(thing.path)
            if size <= 100000:
                print(f"size {size} {thing.path}")
                answersum += size
        else:
            with open(thing, "r") as thingfile:
                size = int(thingfile.readline())

        sumsize += size
    return sumsize

print(get_size('/home/kopite/Desktop/aco22/day7/fs'))
print(answersum)
