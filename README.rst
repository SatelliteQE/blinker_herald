===============================
Blinker Herald
===============================

.. image:: docs/The_Herald.jpg
        :alt: The Herald

.. image:: https://img.shields.io/pypi/v/blinker_herald.svg
        :target: https://pypi.python.org/pypi/blinker_herald

.. image:: https://img.shields.io/travis/rochacbruno/blinker_herald.svg
        :target: https://travis-ci.org/SatelliteQE/blinker_herald

.. image:: https://readthedocs.org/projects/blinker_herald/badge/?version=latest
        :target: https://readthedocs.org/projects/blinker_herald/?badge=latest
        :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/SatelliteQE/blinker_herald/badge.svg?branch=master
        :target: https://coveralls.io/github/SatelliteQE/blinker_herald?branch=master
        :alt: Coverage

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
* `+` an easy decorator :code:`@emit()` to magically emit signals when your functions are called and before it returns a result.
* A :code:`signals` namespace proxy to discover the signals in your project
* Customizable for your needs


Usage
-----
Let's say you have a class and wants to emit a signal for a specific method::

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


.. note::

  Post-signals are only called if there were no exceptions
  raised during the processing of their related function.

You can also use the namespace proxy :code:`blinker_herald.signals` to connect
handlers to signals, the signal name is the prefix **pre** or **post**
followed by **_** and the method name::

    from blinker_herald import signals

    @signals.pre_do_something.connect
    def handle_pre(sender, signal_emitter, **kwargs):
        ...


If you have a lot of subclasses emitting signals with the same name and you
need to capture only specific signals, you can specify that you want to listen
to only one type of sender::

    from blinker_herald import emit, signals, SENDER_CLASS
    class BaseModel(object):
        ...
        @emit(sender=SENDER_CLASS)
        def create(self, **kwargs):
            new_instance = my_project.new(self, **kwargs)
            return new_instance

    class One(BaseModel):
        pass

    class Two(BaseModel):
        pass

.. note::
   By default the sender is always the instance but you can use :code:`SENDER_CLASS`
   to force the sender to be the **class** another options are **SENDER_CLASS_NAME**,
   **SENDER_MODULE**, **SENDER_NAME** and you can also pass a string, an object
   or a lambda receiving the **sender** instance e.g: :code:`@emit(sender=lambda self: self.get_sender())`

Using :code:`SENDER_CLASS` you can now connect to specific signal::

    from blinker_herald import signals

    @signals.post_create.connect_via(One)
    def handle_post_only_for_one(sender, signal_emitter, result, **kwargs):
        # sender is the class One (cls)
        # signal the instance of the class One (self)
        # result is the return of the method create

The above will handle the :code:`create` method signal for the class **One** but not for the class **Two**


You can also be more specific about the signal you want to connect using the
**__** double underscore to provide method name::

    from blinker_herald import signals

    @signals.module_name__ClassName__post_method_name.connect
    def handle_post(sender, signal_emitter, result, **kwargs):
        ...

The above will connect to the **post** signal emitted by :code:`module_name.ClassName.method_name`

.. note::
  You don't have to use the pattern above if your project do not have a lot of
  method name collisions, using only the method name will be just fine for most cases.



Credits
-------

This software was first created by SatelliteQE team to provide signals to
Robottelo and Nailgun

.. _blinker: http://pypi.python.org/pypi/blinker
