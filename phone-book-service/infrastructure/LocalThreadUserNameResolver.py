import threading

from domain.UserNameResolver import UserNameResolver


class LocalThreadUserNameResolver(UserNameResolver):
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if LocalThreadUserNameResolver.__instance is None:
            LocalThreadUserNameResolver.__instance = LocalThreadUserNameResolver()
        return LocalThreadUserNameResolver.__instance

    def __init__(self):
        self.context = threading.local()

    def get_user_name(self) -> str:
        print(f"self.context: {self.context}")
        print(f"self.context: {self.context.__dict__}")
        print(f"threading: {threading.current_thread()}")
        return self.context.user_name

    def set_user_name(self, user_name: str):
        print(f"self.context: {self.context}")
        print(f"threading: {threading.current_thread()}")
        print(f"user_name: {user_name}")
        self.context.user_name = user_name
        print(f"self.context: {self.context.__dict__}")
