#!/usr/bin/env python
import logging
import os
import unittest

tests_dir = 'tests'

for file in os.listdir(tests_dir):
    #logging.basicConfig(level=logging.DEBUG)

    if (file.startswith('.') or not file.endswith('.py') or file.startswith('__') and file.endswith('.py')) or file.endswith('.pyc'):
        continue
    qual_file = os.path.join(tests_dir, file)
    module = qual_file.replace('/', '.')[:-3]  # leave off .py
    print 'Testing module %s' % module
    unittest.main(module, exit=False)