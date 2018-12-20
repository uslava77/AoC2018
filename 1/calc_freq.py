#!/usr/bin/python

with open("./input.txt", 'r') as f:
    summ = 0
    for line in f:
        cur_num = int(line)
        summ += cur_num
    print "Total: ", summ
