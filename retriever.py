### Written By Youchao Wang, yw479
### 2022.01.07
### Created using Python 3.8.3
 
import os
import pandas as pd
import time
import win32security
from pathlib import Path

# Please type in your root
root_path = r"D:\Pictures\Peter"
init_counter = root_path.count(os.sep)

for root, dirs, files in os.walk(root_path, topdown=False):
    # A treewalk using os.walk method from root
    for name in files:
        raw = os.path.join(root, name)
        path_list = root.split(os.sep)
        f_plist = pd.DataFrame([path_list])
        
        # Retrieve basic information
        base = os.path.basename(raw)
        f_d = pd.DataFrame([base])
        _, file_extension = os.path.splitext(base)
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

        # Retrieve ownership information
        # ref:https://stackoverflow.com/questions/66248783/
        try:
            sd = win32security.GetFileSecurity(raw, win32security.OWNER_SECURITY_INFORMATION)
            owner_sid = sd.GetSecurityDescriptorOwner ()
            file_owner, _, _ = win32security.LookupAccountSid (None, owner_sid)
        except:
            file_owner = "Error."
        f_o = pd.DataFrame([file_owner])

        # Generate CSV output
        # in the form of Name, Modified Date, Document Type, Path
        # Note Delete the generated csv before rerunning this programme
        file_check = pd.concat([f_d, f_atime, f_e, f_p, f_l, f_o, f_plist], axis=1)
        file_check.to_csv('file_check.csv', mode='a', header=None, index=None, encoding='utf-8-sig')