import glob
import os 
from datetime import datetime

# location
LOCATION = '/home/zhaoliang/Videos/'


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
  
  
    
if __name__ == '__main__':
    files = get_files_list(LOCATION + '*.avi')
    print(files)
