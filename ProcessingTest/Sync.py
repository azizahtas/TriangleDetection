import sys
import subprocess
path = "000004/2018/06/22"
'''
Info: Racknumber/year/Month/Day
'''
sys.stdout.write(path+" ")
command = "aws s3 sync s3://my-rack/"+path+" C://smartrack/"+path
try:
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait(60)
except subprocess.TimeoutExpired:
    pass

print('Sync Completed')
