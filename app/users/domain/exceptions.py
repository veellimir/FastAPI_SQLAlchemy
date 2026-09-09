from fastapi import HTTPException, status


class UserNotFoundException(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден",
        )
