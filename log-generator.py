"""Usage: log_generator.py (--conf | -c) CONF  [--iterations ITERATIONS] [--maxLines MAXLINES] [--target_file TARGET]


Arguments:

    TEXT  Message to be printed



Options:

    --count=N  number of times the message will be output

    --caps  convert the text to upper case

    --nocaps

"""

import logging
import docopt
import sys
import time
import random
import json
import os
import plugin
from collections import OrderedDict

def read_conf(conf_file):
    with open(conf_file) as conf_data:
        test_data = json.load(conf_data, object_pairs_hook=OrderedDict)
        return test_data
def call_function(function_name, number):
    if function_name in plugin.functions:
        res = plugin.functions[function_name](number)
        return res
def create_log_entry(conf_data, maxLines, log_index):
    log = ''
    for element in conf_data.values():
        if element['is_cmd'] == 'False':
            index = random.randint(0,len(element["val"]) - 1)
            log_entry = element["val"][index]
            if element.get('format', None):
                log_entry = ('{}' + log_entry + '{}').format('"', '"')
            log = log + log_entry + ' '
        else:
            res = call_function(element["val"], maxLines)
            if element['is_random'] == 'False':
                log = log + res[log_index] + ' '
            else:
                index = random.randint(0,len(res) - 1)
                log = log + res[index]+ ' '
    log = log + '\n'
    return log
    
    
def main(args):
    #import pdb; pdb.set_trace()
    iterations = 1 # infinate
    maxLines = 500
    logFile = 'logGenerator.log'
    datePattern = "[%d/%m/%y %H:%M:%S]"
    conf_file = args['CONF']
    if args['TARGET']:
        logFile = args['TARGET']
    if args['MAXLINES']:
        maxLines = args['MAXLINES']
    log = ''
    conf_data = read_conf(conf_file)
    with open(logFile, 'w') as fp:
        for log_index in xrange(maxLines):
            fp.write(create_log_entry(conf_data, maxLines, log_index))
                    
    
if __name__ == "__main__":

    arguments = docopt.docopt(__doc__)
    print arguments
    main(arguments)
