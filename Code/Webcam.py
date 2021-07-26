# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 19:32:45 2021

@author: Zhaoliang
@source: https://blog.csdn.net/lpwmm/article/details/106482845
"""


import glob
import os 
from datetime import datetime
import cv2
import logzero
from logzero import logger
import shutil

# configure logzero to local file, the maximum single file is 5MB, save at most 3 copies
logzero.logfile('/home/pi/video/log.log',maxBytes=5e6,backupCount=3)

# constraints the least space limitation percentage
SPACE_LIMIT=50

# The time of the section of recording videos(unit:second) 
PER_LENGTH = 5 * 60

# location
current_dir = os.getcwd()

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

def get_files_list(exp):
    """
    acquire the file list of a specified location and create files 
        based on positive order by file creation time(from ealiest to last)
    return: files
    """
    
    files = list(filter(os.path.isfile,glob.glob(exp)))
    
    # file in reverse order of creation time
    files.sort(key=lambda x:os.path.getctime(x),reverse=False)
    return files

def record():
    """
    record video
    return: 
    """
    
    WIDTH = 1280
    HEIGHT = 720
    FPS = 24.0
    
    # capture video from the default camera
    cap = cv2.VideoCapture(0)
    
    # set the resolution of your camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,HEIGHT)
    # set camera frames, if not, by default is 600 
    cap.set(cv2.CAP_PROP_FPS,FPS)
    # use MJPG coding, this will work on Windows
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    
    start_time = datetime.now()
    filename = current_dir + '/' + start_time.strftime('%Y-%m-%d_%H-%M-%S') + '.avi'
    out = cv2.VideoWriter(filename,fourcc,FPS,(WIDTH,HEIGHT))
    
    flag = True
    while flag:
        # check if the disk space is enough
        if desk_per_Win('F:') > SPACE_LIMIT:
            if (datetime.now() - start_time).seconds >= PER_LENGTH:
                logger.info(f'Section recording finish, save file name as {filename}')
                out.release()
                # restart recording new vide
                start_time = datetime.now()
                filename = current_dir + '/' + start_time.strftime('%Y-%m-%d_%H-%M-%S') + '.avi'
                out = cv2.VideoWriter(filename,fourcc,FPS,(WIDTH,HEIGHT))
                
            else:
                ret,frame = cap.read()
                if ret:
                    out.write(frame)
        else:
            logger.warn(f'disk space is no more than{SPACE_LIMIT}%,will delete the earliset video file')
            files = get_files_list(current_dir + '/' + '*.avi')
            os.remove(files[0])
            logger.info(f'{files[0]} has been deleted')
            
    cap.release()
    
    
if __name__ == '__main__':
    logger.info('start recording')
    record()
            
                