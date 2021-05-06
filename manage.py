#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import django
import configurations

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')

    configurations.setup()
    django.setup()

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
