# learning-cognito.py

🍛🍛🍛 PythonでCognitoの認証フローを実装したサンプルです！  

![成果物](./docs/images/fruit.gif)  

## 準備

### GitHub Secretsの設定

GitHub Secretsに以下の値を設定します。  

| Key | Value |
| --- | --- |
| AWS_ACCESS_KEY_ID | AWSのアクセスキーID |
| AWS_SECRET_ACCESS_KEY | AWSのシークレットアクセスキー |
| AWS_REGION | AWSのリージョン |
| PROJECT_NAME | プロジェクト名(CloudFormationのスタック名) |

### デプロイ

`v-*`形式のタグをプッシュ(or 手動トリガー)すると、`GitHub Actions`が実行され、CloudFormationのスタックがデプロイされます。  
これで、以下のリソースがプロビジョニングされます。  

- Cognito User Pool
- Cognito User Pool Client

ユーザプールIDとユーザプールクライアントIDは、`.env`ファイルに登録する必要があります。  
以下のコマンドを実行して、`.env`ファイルを作成します。  

```shell
./initializer.sh <スタック名(プロジェクト名)>
```

また、その他項目に関しては、`.env.example`を参考にしてください。  

### 実行

DevContainerに入り、以下のコマンドを実行してください。  

```shell
poetry run uvicorn app.main:app
```

これでローカルサーバが起動します。  

`sample.http`の内容を実行すると、Cognitoの認証フローを実行できます。  
※ `sample.http`はVSCodeの拡張機能「[REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)」をインストールすると、VSCode上で実行できます。  

開発用実行するには、以下のコマンドを実行します。  
これで、ファイルの変更を監視して、自動的にサーバが再起動します。  

```shell
poetry run uvicorn app.main:app --reload
```

## 実装したAPI

- [x] ユーザー登録
- [x] メールアドレスの検証
- [x] 検証トークンの再送信
- [x] ログイン
- [x] ログアウト
- [x] パスワードを忘れた場合の認証トークンの送信
- [x] パスワードを忘れた場合のパスワードのリセット
- [x] ユーザー情報の取得
- [x] ユーザー情報の更新
- [x] ユーザーの削除

## 参考文献

- [Cognito User Pool](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html)
- [Cognito User Pool Client](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html)
