"""
Example:
Print the state of all variables when an Exception occurs. 
"""

import sys, traceback

def print_exc():
    tb = sys.exc_info()[2]
    while tb.tb_next: 
        # jump through execution frames
        tb = tb.tb_next
    frame = tb.tb_frame
    code = frame.f_code
    print("Frame %s in %s at line %s"%\
              (code.co_name,
               code.co_filename,
               frame.f_lineno))
    # print local variables
    for k, v in frame.f_locals.items():
        print("%20s = %s"%(k,str(v)))

    
try:
    a = 3
    b = "Carrots"
    c = a / 0
except ZeroDivisionError:
    print_exc()
