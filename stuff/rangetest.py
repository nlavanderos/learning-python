# the following works only for postional arguments,
# and assumes they always appear at the same position
# in every call; they cannot be passed by keyword name,
# and we don't suport **args keywords in calls because
# this can invalidate the positions declared in the
# decorator;  these examples all run under 2.6 and 3.0;


def rangetest(*argchecks):                  # validate positional arg ranges
    def onDecorator(func):
        if not __debug__:                   # True if "python -O main.py args.."
            return func                     # no-op: call original directly
        else:                               # else wrapper while debugging
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = 'Argument %s not in %s..%s' % (ix, low, high)
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator