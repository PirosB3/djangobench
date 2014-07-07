from djangobench.utils import run_benchmark
from query_all.models import Book

def benchmark():
    #import cProfile, pstats, StringIO
    #pr = cProfile.Profile()
    #pr.enable()
    list(Book.objects.iterator())
    #pr.disable()
    #s = StringIO.StringIO()
    #sortby = 'cumulative'
    #ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    #ps.print_stats()
    #with open('/tmp/results.txt', 'a') as f:
        #f.write(s.getvalue())

def setup():
    for i in range(0, 3000):
        Book(pk=i,title='foobar_%s' % i ).save()

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.iterator() call for large number of objects.',
    }
)
