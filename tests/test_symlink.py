import os
import pwd
from os import stat

pkg_dir= '/usr/local/bin'
st=stat(pkg_dir)
uid=st.st_uid
username=pwd.getpwuid(st.st_uid).pw_name
print(uid)
print(pwd.getpwuid(st.st_uid))
print(username)
  
assert os.path.isdir(pkg_dir)
print(pkg_dir,"is a directory")
assert username!='root'
print(username,"is owner of",pkg_dir)

