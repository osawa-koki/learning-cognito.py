"""FastAPIのサンプルコード。
"""
from os import environ

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from . import initializer
from .cognito_client import cognito_client
from .models.resend_code import ResendCodeModel
from .models.sign_in import SignInModel
from .models.sign_up import SignUpModel
from .models.verify_code import VerifyCodeModel

app = FastAPI()

initializer.main()

COGNITO_CLIENT_ID = environ["USER_POOL_CLIENT_ID"]


@app.get("/")
def read_root():
    """`Hello World`を返す。

    Returns:
        dict: `Hello World`を含む辞書データ。
    """
    return {"Hello": "World"}


@app.get("/envs")
def read_envs():
    """環境変数を返す。

    Returns:
        dict: 環境変数を含む辞書データ。
    """
    return environ


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """パスパラメタを受け取って返す。

    Args:
        item_id (int): 整数のパスパラメタ。
        q (str, optional): クエリパラメタ。デフォルトは`None`。

    Returns:
        dict: パスパラメタとクエリパラメタを含む辞書データ。
    """
    return {"item_id": item_id, "q": q}


@app.post("/sign_up")
def sign_up(params: SignUpModel):
    """Cogntioを用いてサインアップする。
    """
    try:
        cognito_client.sign_up(
            ClientId=COGNITO_CLIENT_ID,
            Username=params.email,
            Password=params.password,
            UserAttributes=[
                {
                    "Name": "name",
                    "Value": params.name,
                },
            ],
        )
        content = {"message": "success."}
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=content)
    except cognito_client.exceptions.UsernameExistsException:
        content = {"message": "User already exists."}
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content,
        )
    except cognito_client.exceptions.InvalidParameterException:
        content = {"message": "Invalid parameter."}
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content,
        )


@app.post("/verify_code")
def verify_code(params: VerifyCodeModel):
    """サインアップ時に送信されたコードを検証する。
    """
    email = params.email
    code = params.code
    try:
        cognito_client.confirm_sign_up(
            ClientId=COGNITO_CLIENT_ID,
            Username=email,
            ConfirmationCode=code,
        )
        content = {"message": "success."}
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=content,
        )
    except cognito_client.exceptions.CodeMismatchException:
        content = {"message": "Invalid code."}
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content,
        )
    except cognito_client.exceptions.ExpiredCodeException:
        content = {"message": "Expired code."}
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content,
        )
    except cognito_client.exceptions.NotAuthorizedException:
        content = {"message": "Not authorized."}
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content,
        )
    except cognito_client.exceptions.UserNotFoundException:
        content = {"message": "User not found."}
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content,
        )


@app.post("/resend_code")
def resend_code(params: ResendCodeModel):
    """サインアップ時に送信されたコードを再送する。
    """
    email = params.email
    try:
        cognito_client.resend_confirmation_code(
            ClientId=COGNITO_CLIENT_ID,
            Username=email,
        )
        content = {"message": "success."}
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=content,
        )
    except cognito_client.exceptions.CodeDeliveryFailureException:
        content = {"message": "Code delivery failure."}
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content,
        )
    except cognito_client.exceptions.InvalidParameterException:
        content = {"message": "Invalid parameter."}
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content,
        )
    except cognito_client.exceptions.UserNotFoundException:
        content = {"message": "User not found."}
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content,
        )


@app.post("/sign_in")
def sign_in(params: SignInModel):
    """サインインする。(USER_SRP_AUTHを使用する)
    """
    email = params.email
    password = params.password
    try:
        cognito_client.initiate_auth(
            ClientId=COGNITO_CLIENT_ID,
            AuthFlow="USER_SRP_AUTH",
            AuthParameters={
                "USERNAME": email,
                "PASSWORD": password,
            },
        )
        content = {"message": "success."}
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=content,
        )
    except cognito_client.exceptions.NotAuthorizedException:
        content = {"message": "Not authorized."}
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content,
        )
    except cognito_client.exceptions.UserNotFoundException:
        content = {"message": "User not found."}
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content,
        )
    except cognito_client.exceptions.UserNotConfirmedException:
        content = {"message": "User not confirmed."}
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content,
        )
    except cognito_client.exceptions.InvalidParameterException:
        content = {"message": "Invalid parameter."}
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content,
        )
    except cognito_client.exceptions.InvalidPasswordException:
        content = {"message": "Invalid password."}
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content,
        )
