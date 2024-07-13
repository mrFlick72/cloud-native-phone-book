import threading

from domain.UserNameResolver import UserNameResolver


class LocalThreadUserNameResolver(UserNameResolver):

    def __init__(self):
        self.context = threading.local()

    def get_user_name(self) -> str:
        return self.context.user_name

    def set_user_name(self, user_name: str):
        self.context.user_name = user_name
