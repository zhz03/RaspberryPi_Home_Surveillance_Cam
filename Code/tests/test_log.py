import os
import logzero
from logzero import logger

current_dir = os.getcwd()
path_name = current_dir + '/log.log'
logzero.logfile(path_name,maxBytes=5e6,backupCount=3)

SPACE_LIMIT=90

def disk_per():
    """
    calculate the free space of current space ratio
    return: the persentage of free space
    """
    
    info = os.statvfs('/')
    free_size = info.f_bsize * info.f_bavail
    total_size = info.f_blocks * info.f_bsize 
    percent = round(free_size/total_size * 100)
    return percent
    
if __name__ == '__main__':
    if disk_per() > SPACE_LIMIT:
        pass
    else:
        logger.warn(f'disk space is no more than{SPACE_LIMIT}%,will delete the earliset video file')
        logger.info('file has been deleted')



