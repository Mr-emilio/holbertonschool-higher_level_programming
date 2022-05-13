#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    scoreXweight, weight = 0, 0
    size_list = len(my_list)
    for i in range(size_list):
        scoreXweight += my_list[i][0] * my_list[i][1]
        weight += my_list[i][1]
    return(scoreXweight / weight)
