import os

MEM = '''free | tail -2 | head -1 | tr -s " " | cut -d " " -f {}'''
MEM_COLUMNS = {'free':4,'avilable':7}
PROCCES_COUNT = '''ps aux | wc -l'''
SYSTEM_LOAD = '''uptime | cut -d ":" -f 5'''

def get_mem_info(mod):
    mod_num = MEM_COLUMNS.get(mod,4)
    result = os.popen(MEM.format(mod_num)).read().strip('\n')
    return int(result)

def get_proc_count():
    count = os.popen(PROCCES_COUNT).read().strip('\n')
    count = int(count) - 1
    return count

def get_sys_load():
    time_frames = ['1 min','5 mins','15 mins']
    times = os.popen(SYSTEM_LOAD).read().strip('\n')
    times = times[1:].split(', ')
    result = dict(zip(time_frames,times))
    return result