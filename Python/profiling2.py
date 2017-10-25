python3 -m cProfile program.py
        ncalls = number of calls to function
        tottime = time spent by this function only
        percall = tottime/ncalls
        cumtime = time spent by this function and calls to other function
        percall = cumtime/ncalls

    -s sort_by_this

    -o output_filename


# Use the pstats module to further manipulate the output data.
import pstats
p = pstats.Stats('restats')
p.sort_stats('cumulative').print_stats(10)
