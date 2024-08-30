import sys
import uuid
import pywebio.pin as webpin
import pywebio.input as webin
import pywebio.output as webout
import pywebio.session as websession

from loguru import logger

# Import utilities

# Import subpages
from pages.loginpage import LoginPage
from pages.examplepage import ExamplePage

class BaseWebapp(
    LoginPage,
    ExamplePage
):

    def __init__(self):
        super().__init__()
        self.id = str(uuid.uuid4())
        self.initialize_logger()
        self.init_master_page_settings()
        self.define_layout()
        self.logger.info(websession.info)
        
        #webout.put_text('Hello')
        websession.defer_call(self.cleanup)
        self.start_app()

    def initialize_logger(self):

        log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | " \
                     "{level.icon} <level>{level: <8}</level> | " \
                     "<cyan>{extra[identifier]}</cyan> | " \
                     "<level>{message}</level>"
        
        logger.remove()
        logger.add(sys.stderr, format=log_format, colorize=True)
        self.logger = logger.bind(identifier=self.id)

    def init_master_page_settings(self):
        # Clear default pywebio footer
        websession.run_js('document.getElementsByClassName("footer")[0].style.display="none"')

        style = """
    <style>
    .pywebio {
        padding: 0 !important;
    }
    #output-container {
        max-width: 100% !important;
        width: 100vw !important;
        height: 100vh !important;
        padding: 0 !important;
    }
    
    </style>
    """
        webout.put_html(style)


    def define_layout(self):

        webout.put_row([
            webout.put_scope("main_sidebar").style('width: 10vw; !background-color: red;'),
            webout.put_column([
                webout.put_scope("main_header").style('height: 5vh; !background-color: yellow;'),
                webout.put_scope("main_body").style('height: 85vh; !background-color: green; '),
                webout.put_scope("main_footer").style('height: 10vh; !background-color: blue; ')
            ]).style('width: 90vw; height: 100vh;')
        ]).style('height: 100vh;')

    def start_app(self):
        self.render_login_page()
        
    def cleanup(self):
        # cleanup logic when user closes the session
        self.logger.info("Session exited!")


