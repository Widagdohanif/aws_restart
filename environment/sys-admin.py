import os
import subprocess

os.system("ls")
subprocess.run(["ls"])

subprocess.run(["ls","-l"])
subprocess.run(["ls","-l","README.md"])

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])