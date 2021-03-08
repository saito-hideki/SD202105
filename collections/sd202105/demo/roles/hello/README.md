Role Name
=========

hello role shows greeting message for demo

Requirements
------------

None

Role Variables
--------------

`msg`: Greeting message to show at run time

Dependencies
------------

None

Example Playbook
----------------

```

- hosts: servers
  roles:
     - role: sd202105.demo.hello
       vars:
         msg: 'Hello, World!'
```

License
-------

GPL-2.0-or-later

Author Information
------------------

Hideki Saito <saito@fgrep.org>
