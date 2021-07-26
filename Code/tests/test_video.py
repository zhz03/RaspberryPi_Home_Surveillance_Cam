# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 23:28:47 2021

@author: zhaoliang
"""
import glob
import os
from datetime import datetime
import cv2.cv2 as cv2
import shutil

current_dir = os.getcwd()

SPACE_LIMIT = 50

def desk_per_Win(path):
    """
    path: the disk that you want to check, example: path = 'C:'
    return: the percentage of the free space on that disk
    """
  
    # Get the disk usage statistics
    # about the given path
    stat = shutil.disk_usage(path)
  
    # Print disk usage statistics
    # rint("Disk usage statistics:")
    percent = round(stat[2]/stat[0]*100)
    return percent

if __name__ == '__main__':
    #percent = disk_per()
    percent = desk_per_Win('E:')