# coding: utf-8
import re

from flask import flash


def get_guid_filter(args):
    res = {}
    if re.match(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}', args.get('guid', '').strip()):
        res['guid'] = args.get('guid').strip()
    elif args.get('guid'):
        flash("GUID имеет не верный формат", 'danger')

    return res


def build_instance_from_form(instance, form):
    for attr, value in list(form.items()):
        setattr(instance, attr, value)

    return instance
