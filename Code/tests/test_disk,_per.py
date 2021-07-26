# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 20:34:22 2021

@author: Zhaoliang
Developing in Windows 10
"""


import os 
import shutil
  

def disk_per():
    """
    calculate the free space of current space ratio
    return: the persentage of free space
    """
    
    info = os.statvfs("D:")
    free_size = info.f_bsize * info.f_bavail
    total_size = info.f_blocks * info.f_bsize 
    percent = round(free_size/total_size * 100)
    return percent

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
    percent = desk_per_Win('F:')