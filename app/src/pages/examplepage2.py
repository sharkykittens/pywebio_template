import pywebio.pin as webpin
import pywebio.input as webin
import pywebio.output as webout
import pywebio.session as websession

from functools import partial

class ExamplePage2:

    def render_example_page2(self):

        self.new_page()

        with webout.use_scope("main_body"):

            webout.put_text("page 2")

        with webout.use_scope("main_sidebar"):

            webout.put_button(label="page1", onclick= lambda: websession.run_js("window.location.href = '/page1'"))