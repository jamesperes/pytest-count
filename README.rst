============
pytest-count
============

.. image:: https://travis-ci.org/jamesperes/pytest-count.svg?branch=master
    :target: https://travis-ci.org/jamesperes/pytest-count
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/jamesperes/pytest-count?branch=master
    :target: https://ci.appveyor.com/project/jamesperes/pytest-count/branch/master
    :alt: See Build Status on AppVeyor

count erros and send email

----

This `Pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.


Features
--------

* TODO


Requirements
------------

* TODO


Installation
------------

You can install "pytest-count" via `pip`_ from `PyPI`_::

    $ pip install pytest-count


Configuration
------------

Open mail.py and configure your e-mail,

```sh
your_email = "EMAIL"
send_email = "EMAIL"
server = smtplib.SMTP("SMTP", 587)
server.login(your_email, "PASSWORD")
```



Usage
-----

* TODO

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-count" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/jamesperes/pytest-count/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
