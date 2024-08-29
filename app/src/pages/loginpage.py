import pywebio.pin as webpin
import pywebio.input as webin
import pywebio.output as webout
import pywebio.session as websession
import pywebio_battery as webbattery

class LoginPage:

    def authenticate_user(self, username, password):

        print(username)
        print(password)

        return True


    def render_login_page(self):

        

        login_user = webbattery.basic_auth(
            verify_func=self.authenticate_user,
            secret="RANDOMSTRING"
        )

        self.render_example_page()