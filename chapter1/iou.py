# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 15:34:10 2022

@author: CHEN
"""

def iou(boxA, boxB):
    # 计算重合部分的上下左右4个边的值，注意最大最小函数的使用
    left_max = max(boxA[0], boxB[0])
    top_max = max(boxA[1], boxB[1])
    right_min = min(boxA[2], boxB[2])
    bottom_min = min(boxA[3], boxB[3])
    
    # 计算重合部分面积
    inter = (right_min-left_max)*(bottom_min-top_max)
    
    Sa = (boxA[2]-boxA[0])*(boxA[3]-boxA[1])
    Ab = (boxB[2]-boxB[0])*(boxA[3]-boxB[1])
    