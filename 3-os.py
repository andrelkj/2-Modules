import os

# 1 - Check available os module functionalities
# help('os')

# 2 - Return current folder
print(os.getcwd())

# 3 - List files and folder
print(os.listdir())

# 4 - Display operational system version
os.system('sw_vers')

# 5 - Display system configurations
os.system('system_profiler SPHardwareDataType')

# 6 - Clear screen
os.system('clear')
