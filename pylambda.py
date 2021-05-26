#!python3
import io
import sys
import iio
import numpy as np
import argparse
from numpy import *

def write_output(outfile, ev):
    #print (ev.shape)
    # TODO: find a way to print out the shapes of the output in case of error
    # TODO: https://stackoverflow.com/questions/242485/starting-python-debugger-automatically-on-error

    if isinstance(ev, np.ndarray) and ev.ndim > 1:
        if outfile == '-':
            f = io.BytesIO()
            np.save(f, ev)
            sys.stdout.buffer.write(f.getvalue())
        else:
            iio.write(outfile,ev)
    else:
        print(ev)


if __name__ == "__main__":
    args = sys.argv[1:]

    parser = argparse.ArgumentParser(description='python plambda')
    parser.add_argument('inputs', metavar='N', type=str, nargs='+',
                    help='input files and expression')
    parser.add_argument('-o', dest='output', default='-',
                    help='output file (default: standar output)')

    args = parser.parse_args()
    infiles = args.inputs[:-1]
    expression = args.inputs[-1]
    outfile = args.output

    #print (infiles)
    #print(expression)
    #print(outfile)
    
    # use the exceptions to catch all the missing variable names
    variables = {}
    for i in range(len(infiles)+1):
        try:
            # evaluate all the expressions but return only the result of the last one
            for expr in expression.split(';'):
                #ev = eval(expr, {}, variables)
                ev = eval(expr)
            # write output
            write_output(outfile, ev)
            break
        except NameError:
            import sys
            varname = str(sys.exc_info()[1]).split('\'')[1]
            #locals()[varname] = float(infiles[i])
            locals()[varname] = iio.read(infiles[i])
            print ('%s <- %s (%s)'%(varname,infiles[i], locals()[varname].shape ) )
            #variables[varname] = iio.read(infiles[i])
