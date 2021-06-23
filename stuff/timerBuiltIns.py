import sys,time
if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
 timer = time.perf_counter # or process_time
else:
 timer = time.time if sys.platform[:3] == 'win' else time.time
 
def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    """
    repslist = list(range(reps)) # Hoist out, equalize 2.x, 3.x
    start = timer() # Or perf_counter/other in 3.3+
    for i in repslist:
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
    return (elapsed, ret)
def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    Returns (best time, last result)
    """
    best = 2 ** 32 # 136 years seems large enough
    for i in range(reps): # range usage not timed here
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start # Or call total() with reps=1
    if elapsed < best: best = elapsed # Or add to list and take min()
    return (best, ret)
def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)


 
def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res
 
def listComp():
    return [abs(x) for x in repslist]
 
def mapCall():
    return list(map(abs, repslist))
 
def genExpr():
    return list(abs(x) for x in repslist)
 
def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())

reps = 10000
repslist = list(range(reps))
print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    bestof_, (total_, result) = bestoftotal(5, 1000, test)
    print ('%-9s: %.5f => [%s...%s] %s' % (test.__name__, bestof_, result[0], result[-1],total_))
 
