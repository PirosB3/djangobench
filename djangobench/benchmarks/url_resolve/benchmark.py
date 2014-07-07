from django.core.urlresolvers import resolve
from djangobench.utils import run_benchmark

def benchmark():
    #import cProfile, pstats, StringIO
    #pr = cProfile.Profile()
    #pr.enable()
    for i in range(0, 100):
        resolve('/basic/')
        resolve('/fallthroughview/')
        resolve('/replace/1')
    #pr.disable()
    #s = StringIO.StringIO()
    #sortby = 'cumulative'
    #ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    #ps.print_stats()
    #f = open('/tmp/lorem.txt', 'a')
    #f.write(s.getvalue())
    #f.close()

run_benchmark(
    benchmark,
    meta = {
        'description': 'URL resolution.',
    }
)
