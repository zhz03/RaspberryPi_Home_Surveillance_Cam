import glob
import os 
from datetime import datetime
import cv2.cv2 as cv2

# constraints the least space limitation percentage
SPACE_LIMIT=50

# The time of the section of recording videos(unit:second) 
PER_LENGTH = 60

# location
LOCATION = '/home/zhaoliang/Videos/'

def disk_per():
    """
    calculate the free space of current space ratio
    return: the persentage of free space
    """

    info = os.statvfs('/')
    free_size = info.f_bsize * info.f_bavail
    total_size = info.f_blocks * info.f_bsize
    percent = round(free_size / total_size * 100)
    return percent

def record():
    """
    record video
    return: 
    """
    
    WIDTH = 640
    HEIGHT = 480
    FPS = 24.0
    
    # capture video from the default camera
    cap = cv2.VideoCapture(0)
    
    # set the resolution of your camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,HEIGHT)
    # set camera frames, if not, by default is 600 
    cap.set(cv2.CAP_PROP_FPS,FPS)
    # use XVID coding, quality and size are both considered
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    start_time = datetime.now()
    filename = LOCATION + start_time.strftime('%Y-%m-%d_%H-%M-%S') + '.avi'
    out = cv2.VideoWriter(filename,fourcc,FPS,(WIDTH,HEIGHT))

    print('recording start')
    flag = True
    while flag:
        # check if the disk space is enough
        if disk_per() > SPACE_LIMIT:
            if (datetime.now() - start_time).seconds >= PER_LENGTH:
                print('start section recording')
                #logger.info(f'Section recording finish, save file name as {filename}')
                out.release()
                # restart recording new vide
                start_time = datetime.now()
                filename = LOCATION + start_time.strftime('%Y-%m-%d_%H-%M-%S') + '.avi'
                out = cv2.VideoWriter(filename,fourcc,FPS,(WIDTH,HEIGHT))
                
            else:
                ret,frame = cap.read()
                if ret:
                    out.write(frame)
        else:

            files = get_files_list(LOCATION + '*.avi')
            os.remove(files[0])

            print(f'{files[0]} has been deleted')
            
    cap.release()
    
    
if __name__ == '__main__':
    #logger.info('start recording')
    record()
