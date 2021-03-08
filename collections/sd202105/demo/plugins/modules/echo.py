#!/usr/bin/python

# Copyright: (c) 2021, Hideki Saito <saito@fgrep.org>
# GNU General Public License v3.0+ (see COPYING or
#  https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: hello

short_description: This module is for testing

version_added: "0.0.1"

description: hello module is for testing to build and use private collection

options:
    message:
        description: This is a greeting message
        required: false
        type: str
        default: 'Hello, Ansible!'

author:
    - Hideki Saito (@saito-hideki)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  sd202105.demo.echo:
    message: "Hello, World!"
'''

RETURN = r'''
message:
    description: The output message that the hello module generates.
    type: str
    returned: always
    sample: {
        'message': 'Hello, Ansible!',
        'time': 1615164954.1205683,
    }
'''

import time
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        message=dict(type='str', required=False, default='Hello, Ansible!'),
    )

    result = dict(
        changed=False,
        message='',
        time=None,
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    result['message'] = module.params['message']
    result['time'] = time.time()
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()

#
# [EOF]
#
