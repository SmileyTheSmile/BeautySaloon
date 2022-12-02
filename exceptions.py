
class LoginFailedException(Exception):
    """Raised when user types the wrong login or password."""
    def __init__(self, detail="Неверный логин или пароль"):
        self.detail = detail
        super().__init__(self.detail)
