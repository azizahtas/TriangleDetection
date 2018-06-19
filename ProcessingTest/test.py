import os
import sys
import subprocess
def processAfterSync():
    print("Hello It Synced")

aws = 'https://my-rack.s3.amazonaws.com/'
path = "000004/2018/06/17"
sys.stdout.write(path+" ")
command = "aws s3 sync s3://my-rack/"+path+" H://PythonPlayground/smartrack/testing/sync/17/000003"
try:
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait(60)
except subprocess.TimeoutExpired:
    pass

print('Sync Completed')
for filename in sorted(os.listdir('H://PythonPlayground/smartrack/testing/sync/17/000003')):
    print(filename)
