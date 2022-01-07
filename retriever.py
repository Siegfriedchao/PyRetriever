### Written By Youchao Wang, yw479
### 2022.01.07
### Created using Python 3.8.3

import os
import pandas as pd
import time
from pathlib import Path

root_path = r"D:\Pictures\Peter"
init_counter = root_path.count(os.sep)

for root, dirs, files in os.walk(root_path, topdown=False):
    # A treewalk using os.walk method from root
    for name in files:
        raw = os.path.join(root, name)
        base = os.path.basename(raw)
        
        # Retrieve basic information
        file_name, file_extension = os.path.splitext(base)
        f_d = pd.DataFrame([file_name])
        f_e = pd.DataFrame([file_extension])

        # Retrieve creation date and time
        # Note this returns the local time, instead of UTC
        # Currently not in use
        # file_ct_time = time.asctime(time.localtime(os.path.getctime(raw)))
        # f_ctmie = pd.DataFrame([file_ct_time])

        # Retrieve last modified date and time
        # Note this returns the local time, instead of UTC
        file_at_time = time.asctime(time.localtime(os.path.getmtime(raw)))
        f_atime = pd.DataFrame([file_at_time])

        # Retrieve ABS path
        file_path = Path(raw).parent.absolute()
        f_p = pd.DataFrame([file_path])

        # Calculate the depth of the tree walk
        file_depth = raw.count(os.sep) - init_counter
        f_l = pd.DataFrame([file_depth])

        # Generate CSV output
        # in the form of Name, Modified Date, Document Type, Path
        file_check = pd.concat([f_d, f_atime, f_e, f_p, f_l], axis=1)
        file_check.to_csv('file_check.csv', mode='a', header=None, index=None, encoding='utf-8-sig')