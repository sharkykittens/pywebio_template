import pywebio.pin as webpin
import pywebio.input as webin
import pywebio.output as webout
import pywebio.session as websession

from functools import partial

class ExamplePage:

    def render_example_page(self):

        # example of creating multiple put calls while iterating and retaining context

        def print_button(id):
            self.logger.debug(id)

        with webout.use_scope("main_body"):

            for i in range(10):

                webout.put_button(label="Click me", onclick= partial(print_button, i))