===============================
Blinker Herald
===============================

.. image:: https://img.shields.io/pypi/v/blinker_herald.svg
        :target: https://pypi.python.org/pypi/blinker_herald

.. image:: https://img.shields.io/travis/rochacbruno/blinker_herald.svg
        :target: https://travis-ci.org/SatelliteQE/blinker_herald

.. image:: https://readthedocs.org/projects/blinker_herald/badge/?version=latest
        :target: https://readthedocs.org/projects/blinker_herald/?badge=latest
        :alt: Documentation Status

.. image:: docs/The_Herald.jpg
   :height: 200px

The Blinker Herald includes helpers to easily emit signals using the excelent
`blinker`_ library.

Decorate a function or method with :code:`@blinker_herald.emit()`
and **pre** and **post** signals will be automatically emitted to
all connected handlers.

* Free software: ISC license
* Documentation: https://blinker_herald.readthedocs.org.

Features
--------

* All the features provided by `blinker`_
* + An easy decorator :code:`@emit()` to magically emit signals when your functions are called and before it returns a result.
* Customizable for your needs

Let's say you have a class that does something::

    from blinker_herald import emit

    class SomeClass(object):
        @emit()
        def do_something(self, arg1):
            # here is were magically the 'pre' signal will be sent
            return 'something done'
            # here is were magically the 'post' signal will be sent


using :code:`@emit` decorator makes blinker_herald to emit a signal for that method
and now you can connect handlers to capture that signals

You can capture **pre** signal to manipulate the object::

    SomeClass.do_something.pre.connect
    def handle_pre(sender, signal_emitter, **kwargs):
        signal_emitter.foo = 'bar'
        signal_emitter.do_another_thing()

And you can also capture the **post** signal to log the results::

    SomeClass.do_something.post.connect
    def handle_post(sender, signal_emitter, result, **kwargs):
        logger.info("The method {0} returned {1}".format(sender, result))


Credits
-------

This software was first created by SatelliteQE team to provide signals to
Robottelo and Nailgun

.. _blinker: http://pypi.python.org/pypi/blinker
