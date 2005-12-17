# -*- coding: iso-8859-1 -*-
# Copyright (C) 2005 Bastian Kleineidam
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
package file
"""
import unittest


class StandardTest (unittest.TestCase):
    """
    Functional test class with ability to test local files.
    """

    def setUp (self):
        """
        Check resources, using the provided function check_resources()
        from test.py.
        """
        super(StandardTest, self).setUp()
        if hasattr(self, "needed_resources"):
            self.check_resources(self.needed_resources)


def make_suite (prefix, namespace):
    """
    Add all TestCase classes starting with given prefix to a test suite.

    @return: test suite
    @rtype: unittest.TestSuite
    """
    classes = [value for key, value in namespace.items() \
               if (key.startswith(prefix) or key.startswith('Test')) \
                  and issubclass(value, unittest.TestCase)]
    loader = unittest.defaultTestLoader
    tests = [loader.loadTestsFromTestCase(clazz) for clazz in classes]
    return unittest.TestSuite(tests)
