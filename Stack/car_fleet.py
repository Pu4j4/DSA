#brute force
def car_fleet(target,position,speed):
    cars = list(zip(position, speed))
    cars.sort()
    times = []
    for pos,spd in cars:
        time = (target-pos)/spd
        times.append(time)
    fleets = 0
    while times:
        curr = times.pop()
        fleets+=1
        while times and times[-1] < curr:
            times.pop()
    return fleets


target = 12
position = [10,8,0,5,3]
speed    = [2,4,1,1,3]
print(car_fleet(target,position,speed))