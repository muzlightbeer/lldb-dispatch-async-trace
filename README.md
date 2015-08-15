# lldb-dispatch-async-trace - Work in Progress!!!

command script import tracedispatch.py

Tries to log where a block was dispatched from. Does not catch everything.

Breaks pretty bad on Preview and Pages (need to kill terminal). Works better if the script is not loaded until you are about to load a document.

Output not cleaned up. Preview examples from log.txt:

```
(long) $1 = 0x00007fff88bdeb40
Was dispatched by...
frame #1: 0x00007fff88a6deae CoreFoundation`__CFRunLoopSetOptionsReason + 4094
CoreFoundation`__CFRunLoopSetOptionsReason:
    0x7fff88a6deae <+4094>: lea    rdi, qword ptr [rip - 0x13fc173d] ; gAppSleepInfo
    0x7fff88a6deb5 <+4101>: call   0x7fff88be5296            ; symbol stub for: pthread_mutex_unlock
    0x7fff88a6deba <+4106>: lea    rdi, qword ptr [rbp - 0x2098]
    0x7fff88a6dec1 <+4113>: mov    esi, 0x8

...

(long) $28 = 0x00000001000029f5
Was dispatched by...
frame #1: 0x00000001000029be Preview`___lldb_unnamed_function26$$Preview + 122
Preview`___lldb_unnamed_function26$$Preview:
    0x1000029be <+122>: add    rsp, 0x28
    0x1000029c2 <+126>: pop    rbx
    0x1000029c3 <+127>: pop    rbp
    0x1000029c4 <+128>: ret
```  
