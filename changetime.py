import os
import datetime as dt

now = dt.datetime.now()
ago = now-dt.timedelta(minutes=30)
print('nu is: %s'%(now))

for root, dirs in os.walk('C:\\Users\\eric\\Documents'):  
    for fname in dirs:
        path = os.path.join(root, fname)
        st = os.stat(path)    
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            print('%s modified %s'%(path, mtime))