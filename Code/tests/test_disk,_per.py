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

def desk_per_Win():
    # Path
    path = "C:"
  
    # Get the disk usage statistics
    # about the given path
    stat = shutil.disk_usage(path)
  
    # Print disk usage statistics
    print("Disk usage statistics:")
    return stat
    
if __name__ == '__main__':
    #percent = disk_per()
    stat = desk_per_Win()