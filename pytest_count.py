# -*- coding: utf-8 -*-

import json
import os.path
from datetime import date

import pytest

today = str(date.today())
BASE_DIR = os.path.dirname(__file__)


<<<<<<< HEAD
# with open('failures.json') as json_data:
#     d = json.loads(json_data)
#     for p in d['erros']:
#         print(p['id'])

def pytest_addoption(parser):
    group = parser.getgroup('count')
    group.addoption(
        '--count',
        action='store_true',
        dest='counter',
        default=False,
        help='Show number of erros '
    )


new_failures = {'erros': []}  # fazer isso aqui não persistir entre runpytest

# fix a birosca do JSON
# ver se o cache do pytest resolve a persistencia
# ver o que dá pra aproveitar do proprio lastfailed


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global new_failures

    outcome = yield
    rep = outcome.get_result()

    if rep.when != 'call' or rep.fspath == 'tests/test_count.py':  # ToDo: make it pretty
        return

    filename = os.path.join(BASE_DIR, 'failures.json')

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            old_failures = json.loads(''.join(f.readlines()))[-1]
    else:
        old_failures = {'erros': []}

    # new_failures = {'erros': []}
    if rep.failed:
        if 'tmpdir' in item.fixturenames:
            extra = ' (%s)' % item.funcargs['tmpdir']
        else:
            extra = ''

        new_failures['erros'].append({'id': rep.nodeid, 'extra': extra})

    # with open(filename, 'a') as f:
    #     json.dump(new_failures, f)

    if len(new_failures['erros']) > len(old_failures['erros']):
        # send mail
        print('send email')
