# Ansible Collection - demo.hello

Software Design 2021年5月号のAnsible問題解決マップで紹介したデモ用のCollectionです。利用方法は以下の通りです。

`ansible-galaxy`コマンドを利用してPrivate GalaxyからCollectionコンテンツをダウンロードする

```
$ ansible-galaxy collection install sd202105.demo
```

デモ用の[Playbook](./demo.yml)を実行する

```
$ ansible-playbook -i inventory demo.yml
```
