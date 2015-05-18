Using tail to explore logs
##########################

:date: 2013-10-03 12:30
:tags: unix
:category: misc
:slug: using-tail-to-explore-logs
:summary: tail -f vs tailf


When I am testing, I always keep an eye on the logs because they are a valuable
resource for finding problems on the system. They can act as an early warning
system. The ``tail`` commnand alongside with ``view`` or ``vim`` are great ways
to explore big log entries.

Some simple examples:

.. sourcecode:: python

    >> tail -f web_app.log import.log
    >> tail -f *.log

.. sourcecode:: python

    >> tail -f web_app.log import.log | grep ERROR

... or get and read log from remote host

.. sourcecode:: python

    >> ssh remoteUser@remoteHost "tail -f /var/log/app/app.log" | tee local.log

*less is more*

More convenient way to monitor logs is by using less. ``less + F app.log``
allows you to switch between watch mode and navigation mode with ``ctrl+c`` and
back to watching mode with ``F``. Very helpul when you need to search, find
occurrences, create marks etc.

