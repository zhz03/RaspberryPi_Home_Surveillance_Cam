# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 23:28:47 2021

@author: zhaoliang
"""

import os
from datetime import datetime
import cv2.cv2 as cv2
import shutil

current_dir = os.getcwd()

SPACE_LIMIT = 10

PER_LENGTH = 5

def disk_per_Win(path):
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

def record():
    """
    record video
    return: 
    """
    
    # if you use the external camera, set the right WIDTH and HEIGHT
    WIDTH = 1280
    HEIGHT = 720
    FPS = 24.0
    
    # capture video from the default camera
    cap = cv2.VideoCapture(1)
    
    # set the resolution of your camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,HEIGHT)
    # set camera frames, if not, by default is 600 
    cap.set(cv2.CAP_PROP_FPS,FPS)
    # use MJPG coding, this will work on Windows
    fourcc = cv2.VideoWriter_fourcc(*'MJPG') 
    
    start_time = datetime.now()
    filename = current_dir +  start_time.strftime('%Y-%m-%d_%H-%M-%S') + '.avi'
    out = cv2.VideoWriter(filename,fourcc,FPS,(WIDTH,HEIGHT))

    print('recording start')
    flag = True
    while flag:
        # check if the disk space is enough
        if disk_per_Win('E:') > SPACE_LIMIT:
            if (datetime.now() - start_time).seconds >= PER_LENGTH:
                print('start section recording')
                #logger.info(f'Section recording finish, save file name as {filename}')
                out.release()
                # restart recording new vide
                start_time = datetime.now()
                filename = current_dir + '/'+ start_time.strftime('%Y-%m-%d_%H-%M-%S') + '.avi'
                out = cv2.VideoWriter(filename,fourcc,FPS,(WIDTH,HEIGHT))
                
            else:
                ret,frame = cap.read()
                if ret:
                    out.write(frame)
    

            #files = get_files_list(LOCATION + '*.avi')
            #os.remove(files[0])
            
            # print(f'{files[0]} has been deleted')
            
    cap.release()
    
        
if __name__ == '__main__':
    #logger.info('start recording')
    record()
    