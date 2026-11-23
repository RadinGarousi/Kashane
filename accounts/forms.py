from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "رمزعبور یا نام کاربری اشتباه است",
        "inactive": "رمزعبور یا نام کاربری اشتباه است"
    }

    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        # Password Field
        self.fields["password"].strip = True
        self.fields["password"].label = "رمزعبور"
        # Username Field
        self.fields["username"].label = "نام کابری"
