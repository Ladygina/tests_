def discriminant(a, b, c):
    D = b**2 - 4 * a * c
    return D

# 3 tests
def solution(a, b, c):
   D = discriminant(a,b,c)
   if D<0:
      return 'корней нет'
   elif D==0:
      return ( (-b-D**(0.5))/(2*a))
   else:
       return ((-b+D**(0.5))/(2*a),(-b-D**(0.5))/(2*a))

# 1 test
def solve_list(todo_list: list, workday: float = 8):
    worktime = 0.0
    for j in range(len(todo_list)): # посчитайте в цикле сумму рабочего времени и сохраните в переменную worktime
        worktime += float(todo_list[j][1])
    return workday - worktime


# 3 tests
def solve(hare_distances: list, turtle_distances: list):
    hare_all = 0 # подсчитайте общую дистанцию зайца
    for h in range(len(hare_distances)):
        hare_all += hare_distances[h]

    turtle_all = 0 # подсчитайте общую дистанцию черепахи
    for t in range(len(turtle_distances)):
        turtle_all += turtle_distances[t]
    # определите, кто из двоих прошел бОльшую дистанцию
    if turtle_all> hare_all:
        result = "черепаха"
    elif turtle_all == hare_all:
        result = "одинаково"
    else:
        result = "заяц"
    return result

