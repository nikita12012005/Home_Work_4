import os
import sys

def write(*args, **kwargs):
    sep= kwargs.get('sep',' ')
    end= kwargs.get('end', os.linesep)
    if end is None:
        end = os.linesep
    file = kwargs.get('file', sys.stdout)
    flush= kwargs.get('flush', False)
    file.write('%s%s' % (sep.join(str(arg) for arg in args), end))
    if flush:
        file.flush()
write('Hello')