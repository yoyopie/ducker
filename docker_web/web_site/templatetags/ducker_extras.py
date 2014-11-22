#!/usr/bin/env python
# encoding: utf-8

from django import template

register = template.Library()


def find_port(ports):
    if ports:
        po = ports[0]
        return po.get('PublicPort')
    else:
        return None

register.filter('find_port', find_port)
