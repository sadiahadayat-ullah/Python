import datetime
current = datetime.datetime.now()
print(current.strftime('%y-%m-%d %H:%M:%S'))
print(current.strftime("%A %B %Y"))
print(current.strftime("%A %B %d, %Y"))
print(current.strftime("%y-%m-%d %I:%M:%S:%p"))