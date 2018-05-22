#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    side_arr = sorted([a,b,c])
    if side_arr[0]<= 0 or side_arr[2]>= side_arr[0]+side_arr[1]:
        raise TriangleError
    else:
        subEdge = set([a,b,c])
        if len(subEdge) == 1:
            return 'equilateral'
        elif len(subEdge) == 2:
            return 'isosceles'
        else:
            return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
