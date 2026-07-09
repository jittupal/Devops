import sys
import socket

print(sys.argv)
if len(sys.argv) != 2:
    print("please provide the file name to write")
    sys.exit()
    
hostname_value = socket.gethostname()

output_file = sys.argv[1]

with open(output_file, "w") as file:
    file.write(hostname_value)
    
print("hostname is written to file")