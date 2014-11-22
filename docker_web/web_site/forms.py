#!/usr/bin/env python
# encoding: utf-8

from django import forms
from django.core.exceptions import ValidationError
import models


class HostForm(forms.ModelForm):
    class Meta:
        model = models.Hostinfo


class ContainerForm(forms.ModelForm):
    class Meta:
        model = models.Container
        exclude = ('conid',)
