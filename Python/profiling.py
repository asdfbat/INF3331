### cProfile ###
# We can "profile" our code, to search for bottlenecks in CPU usage.
# One profiling implementation is cProfile. It can be run in terminal:
>>> python3 -m cProfile -s sorting_option my_script.py
# Where you can sort after, for instance, "cumtime" (time spent in function and functions called by it),
# or "tottime" (time spent only in function).

# You can also write the output to an (undreadable) file by adding a -o filename flag.
# You can then print the data from this file by
import pstats
p = pstats.Stats('profile.dat')
p.sort_stats('cumulative').print_stats(10)   # Use "time" for total time, not cumulative.


### Line-profiler ###
# We can also profile line by line. We do this by tagging the function(s) we wish to profile:
@profile
def some_func(x):
    ...
# and then running
>>> kernprof -l -v my_script.py
# Note that this will only show time-distribution within each function seperately.
