from django.core.urlresolvers import resolve
from djangobench.utils import run_benchmark

def benchmark():
    import cProfile, pstats, StringIO
    pr = cProfile.Profile()
    pr.enable()
    for i in range(0, 100):
        for path in (
          '/user/repo/feature19',
          '/section0/feature0',
          '/en/feature10',
          '/ru/feature10',
          '/missing'):
            try:
                resolve(path)
            except:
                pass
    pr.disable()
    s = StringIO.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    f = open('/tmp/url_resolve_flat_i18n_off.txt', 'a')
    f.write(s.getvalue())
    f.close()

run_benchmark(
    benchmark,
    meta = {
        'description': 'URL resolution with long-flat list of patterns. With USE_I18N=False.',
    }
)
