from app.domain.UserNameResolver import UserNameResolver


class LocalThreadUserNameResolver(UserNameResolver):

    def get_user_name(self) -> str:
        pass

    def set_user_name(self, user_name : str):
        pass
