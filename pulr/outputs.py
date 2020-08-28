from functools import partial
from types import SimpleNamespace
from .beacons import beacon_empty_line

oprint = partial(print, flush=True)

_d = SimpleNamespace()


def output_devnull(*args, **kwargs):
    pass


def output_stdout(o, value):
    oprint(f'{o} {value}')


def output_stdout_ndjson(o, value):
    q = '' if isinstance(value, int) or isinstance(value, float) else '"'
    oprint(f'{{"id":"{o}","v":{q}{value}{q}}}')


def output_eva_datapuller(o, value):
    val_mode = o.endswith('.value')
    s = f'{o[:-6 if val_mode else -7]} u '
    oprint(s + (f'None {value}' if val_mode else str(value)))


OUTPUT_METHODS = {
    None: {
        'output': output_stdout,
        'beacon': beacon_empty_line
    },
    'ndjson': {
        'output': output_stdout_ndjson,
        'beacon': beacon_empty_line
    },
    'eva-datapuller': {
        'output': output_eva_datapuller,
        'beacon': beacon_empty_line
    }
}
