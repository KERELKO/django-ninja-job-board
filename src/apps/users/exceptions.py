from dataclasses import dataclass


class AuthException(Exception):
    ...


@dataclass
class PasswordsDidNotMatchException(AuthException):
    password_1: str
    password_2: str

    @property
    def message(self):
        return 'Passwords did not match'


class IncorrectCredentialsException(AuthException):
    ...
