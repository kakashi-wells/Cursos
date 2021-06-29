def resulthanoi(disks, source, middle, destination):
    if disks >= 1:
        resulthanoi(disks-1, source, destination, middle)
        print("Mover disco de torre", source, "a", destination)
        resulthanoi(disks-1, middle, source, destination)
resulthanoi(3,1,2,3)