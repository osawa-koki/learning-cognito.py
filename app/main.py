"""FastAPIのサンプルコード。
"""
from os import environ
from fastapi import FastAPI
from . import initializer

app = FastAPI()


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
