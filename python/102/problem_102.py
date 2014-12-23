#!/usr/bin/env python
# coding=utf-8


"""
Problem Definition :

Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.

"""

__author__ = 'vivek'

import time

startTime = time.clock()


def triangle_area(points):
    return abs((int(points[0])*(int(points[3])-int(points[5])) + int(points[2])*(int(points[5])-int(points[1])) + int(points[4])*(int(points[1])-int(points[3]))))


def triangle_origin_area(points):
    area_one = abs(int(points[2])*int(points[5]) - int(points[4])*int(points[3]))
    area_two = abs(int(points[0])*int(points[5]) - int(points[4])*int(points[1]))
    area_three = abs(int(points[0])*int(points[3]) - int(points[2])*int(points[1]))
    return area_one + area_two + area_three


with open("triangles.txt") as f:
    numbers = [line.split(',') for line in f.readlines()]

count = 0

for points_data in numbers:
    if triangle_area(points_data) == triangle_origin_area(points_data) :
        count += 1

print(count)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
