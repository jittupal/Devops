import shutil

def check_usage(disk = "/"):
    usage = shutil.disk_usage(disk)
    print(usage)
    free = usage.free / usage.total * 100
    percentage_used = 100 - free
    
    print(f"Percentage Used {percentage_used:.2f}")
    
check_usage()
    