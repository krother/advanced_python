timeit, built-in Python module to measure the execution time of small
code parts

%time

%timeit

%%time

switch from float64 to float32 see if it gets faster

cProfile, the batteries included Python profiler

import cProfile cProfile.run(“[x for x in range(1500)]”)

python -m cProfile -s cumtime mandelbrot.py > profile.txt

insert:

z[index] = z[index] \*\* 2 + c[index]
