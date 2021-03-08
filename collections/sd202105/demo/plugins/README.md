# Collections Plugins Directory

`plugins`ディレクトリには、ユーザが独自に配布したfilterなどのプラグインや、モジュール本体、ヘルパーモジュールを配置します。sd202105.demoコレクションは、必要最低限のデモ環境であるため、echoモジュールのみを提供しています。 

尚、通常のディレクトリ構造は以下の通りです。
```
└── plugins
    ├── action
    ├── become
    ├── cache
    ├── callback
    ├── cliconf
    ├── connection
    ├── filter
    ├── httpapi
    ├── inventory
    ├── lookup
    ├── module_utils
    ├── modules
    ├── netconf
    ├── shell
    ├── strategy
    ├── terminal
    ├── test
    └── vars
```

詳細については、公式ドキュメント([Working With Plugins](https://docs.ansible.com/ansible/2.9/plugins/plugins.html))をご一読ください。
