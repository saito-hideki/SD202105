# Software Design 2021年5月号 - Ansible問題解決マップ

## Private Galaxyのインストール

デモサイトを構築するための、仮想マシンインスタンスの仕様は以下の通り。

| Key | Value |
| --- | ----- |
| ホスト名 | galaxyng |
| OS | CentOS Linux release 8.3.2011 |
| vCPU数 | 1 |
| Memoryサイズ | 4GB |
| Diskサイズ | 10GB |
| pulpcoreバージョン | 3.8.1 |
| pulp-ansibleバージョン | 0.5.6 |
| pulp-containerバージョン | 2.1.0 |
| galaxy-ngバージョン | 4.2.2 |

## デモ用のCollection(sd202105)のビルドとアップロード

 Software Design 2021年5月号のAnsible問題解決マップで紹介したデモ用のCollectionです。利用方法は以下の通りです。

demo collectionのアーカイブをビルドする。ビルドが完了すると、demo collectionのアーカイブ(`sd202105-demo-VERSION.tar.gz`)が作成される

```
$ git clone https://github.com/saito-hideki/sd202105.git
$ cd collections/sd202105/demo/
$ ansible-galaxy collection build .
```

Private Galaxyに`admin`ユーザとしてログインする

![LOGIN](./images/galaxyng_login.png)

My Namespacesから、デモ用のネームスペース(`sd202105`)を作成する。Namespace ownersは`admins`とする。

![CREATE_NAMESPACE](./images/galaxyng_create_ns.png)

demo collectionのアーカイブ((`sd202105-demo-VERSION.tar.gz`)をアップロードする

![UPLOAD_COLLECTION](./images/galaxyng_upload_collection.png)

`ansible-galaxy`コマンドでダウンロードして利用する

ansible.cfgを作成する
```
[galaxy]
server_list = published_repo,community_repo
[galaxy_server.published_repo]
url=https://galaxyng.example.com/api/galaxy/content/published/
token=取得したトークン
[galaxy_server.community_repo]
url=https://galaxyng.example.com/api/galaxy/content/community/
token=取得したトークン
```
ansible-galaxyコマンド
```
$ ansible-galaxy collection install -c -v sd202105.demo
$ ansible-galaxy collection install -c -v community.general
```
```
