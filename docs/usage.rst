=====
Usage
=====

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

