""""This script will parse logs' lines and times."""

from datetime import datetime

def parse_time(ts):
   #07/Jul/1995:16:30:08 -0400
    
    time = datetime.strptime(ts, '[%d/%b/%Y:%H:%M:%S %z]')
    return time.replace(tzinfo = None)

def parse_line(lines):
    line_dict = {}
    fields = lines.split()    
    size = 0 if fields[-1] == '-' else int(fields[-1])
    return {
        'origin' : fields[0],
        'time': parse_time(fields[3] + ' ' + fields[4]),
        'path': fields[6],
        'method' : fields[5][1:], # Removes leading double quot
        'size' : size,
        'status_code' : int(fields[-2])
    }
    # return print(line_dict)