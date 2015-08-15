import lldb
import sys

def breakpoint_function(frame, bp_loc, dict):
        fp = open('log.txt', 'a')
        lldb.debugger.SetOutputFileHandle(fp, True)
        lldb.debugger.HandleCommand('p/x *(long*)($rsi+0x10)')
        fp.write("Was dispatched by...\n")
        lldb.debugger.HandleCommand('frame select --relative 1')
        fp.write("\n\n\n\n")
        fp.close()
        lldb.debugger.SetOutputFileHandle(sys.stdout, True)
        lldb.debugger.HandleCommand('c')

def __lldb_init_module (debugger, dict):
        target = lldb.debugger.GetSelectedTarget()
        breakpoint = target.BreakpointCreateByName('dispatch_async')
        lldb.debugger.HandleCommand('br command add -F tracedispatch.breakpoint_function')
