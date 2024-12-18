import sys
import pywebio
import pywebio.pin as webpin
import pywebio.input as webin
import pywebio.output as webout
import pywebio.session as websession
import pywebio_battery as webbattery

from loguru import logger
from collections import OrderedDict

from pages.examplepage import ExamplePage
from pages.examplepage2 import ExamplePage2

class SessionState:

    def __init__(self, username):
        self.username = username
        self.initialize_logger()

    def initialize_logger(self):

        log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | " \
                     "{level.icon} <level>{level: <8}</level> | " \
                     "<cyan>{extra[identifier]}</cyan> | " \
                     "<level>{message}</level>"
        
        logger.remove()
        logger.add(sys.stderr, format=log_format, colorize=True)
        self.logger = logger.bind(identifier=self.username)

class Server(
    ExamplePage,
    ExamplePage2
):

    def __init__(self, max_sessions = 1000):
        super().__init__()
        self.max_sessions = max_sessions
        self.sessions = OrderedDict()


    def init_global_style(self):

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
            webout.put_scope("main_sidebar").style('width: 10vw; display: flex; flex-direction: column; justify-content: space-between; border-right: 2px solid #0333; padding-left: 5px; !background-color: red;'),
            webout.put_column([
                webout.put_scope("main_header").style('height: 5vh; !background-color: yellow;'),
                webout.put_scope("main_body").style('height: 85vh; !background-color: green; '),
                webout.put_scope("main_footer").style('height: 10vh; !background-color: blue; ')
            ]).style('width: 90vw; height: 100vh; padding-left: 10px;')
        ]).style('height: 100vh;')

    def clear_border(self):
        websession.run_js('document.getElementsByClassName("footer")[0].style.display="none"')

    def verify_user(self, username, password):
        # Add auth logic here
        return True

    def check_login(self):
        if websession.local.session:
            # Already logged in
            return

        # Assumes usernames are unique
        username = webbattery.basic_auth(verify_func=self.verify_user, secret="SECRETKEY")
        if username in self.sessions:
            websession.local.session = self.sessions[username]
        else:
            if len(self.sessions) >= self.max_sessions:
                self.sessions.popitem(last=False)
            # Create new session
            self.sessions[username] = SessionState(
                username = username
            )
            websession.local.session = self.sessions[username]
            websession.local.session.logger.info("New login!")
            

    def new_page(self):
        """
        Helper function to run everytime app moves to a new page
        """
        self.check_login()
        self.init_global_style()
        self.define_layout()
        #self.clear_border()

        print(self.sessions)

    