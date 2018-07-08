#!/usr/bin/python

from ansible.module_utils.basic import *
import datetime


def main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=False),
        )
    )
    args = module.params

    path = args.get('path') or './timelog.txt'
    date = str(datetime.datetime.now())

    f = open(path, 'a')
    f.write("%s\n"%(date))

    message = "%s %s" % (path, date)

    module.exit_json(message=message, changed=True)


if __name__ == '__main__':
    main()
