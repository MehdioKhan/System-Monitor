from flask import Flask
import json
from terminal import get_mem_info,get_proc_count,get_sys_load

app = Flask(__name__)
route = app.route

@route('/memory/<mod>')
def mem_info(mod):
    mem = get_mem_info(mod)
    return json.dumps({'amount':mem,'unit':'KB'})

@route('/process/count')
def process_count():
    count = get_proc_count()
    return json.dumps({'count':count})

@route('/process/load')
def sys_load():
    res = get_sys_load()
    return json.dumps(res)

app.run('0.0.0.0')
