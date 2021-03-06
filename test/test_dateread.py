#!/usr/bin/python

import unittest
import datetime

from logmerge import LogFile


class TestDateread(unittest.TestCase):

    def test_empty(self):
        res = LogFile.get_dateread('')
        self.assertIsNone(res)

    def test_ovs(self):
        res = LogFile.get_dateread('2016-06-02T20:39:51.876Z|')
        self.assertEquals(res, datetime.datetime(2016, 06, 02, 20, 39, 51, 876000))

    def test_neutron(self):
        res = LogFile.get_dateread('2016-06-02 20:42:23.325 0000')
        self.assertEquals(res, datetime.datetime(2016, 06, 02, 20, 42, 23, 325000))

    def test_chefclient(self):
        res = LogFile.get_dateread('[2016-06-02T19:58:58+00:00] INFO')
        self.assertEquals(res, datetime.datetime(2016, 06, 02, 19, 58, 58, 000000))

    def test_messages(self):
        res = LogFile.get_dateread('2016-06-27T06:00:11.386456+00:00 hostname')
        self.assertEquals(res, datetime.datetime(2016, 06, 27, 06, 00, 11, 386456))

    def test_novacompute(self):
        res = LogFile.get_dateread('2016-06-02 20:45:28.166 0000')
        self.assertEquals(res, datetime.datetime(2016, 06, 02, 20, 45, 28, 166000))

    def test_pacemaker(self):
        res = LogFile.get_dateread('Jun 26 06:00:22 [13084]')
        self.assertEquals(res, datetime.datetime(2016, 06, 26, 06, 00, 22, 000000))

    def test_apache(self):
        res = LogFile.get_dateread('[Wed Jun 22 15:12:20.427073 2016] [wsgi:error]')
        self.assertEquals(res, datetime.datetime(2016, 06, 22, 15, 12, 20, 427073))

    def test_crowbar_production(self):
        res = LogFile.get_dateread('I, [2016-07-12T13:45:20.130379 #2515:0x007fccab486f28]')
        self.assertEquals(res, datetime.datetime(2016, 07, 12, 13, 45, 20, 130379))

    def test_crowbar_join(self):
        res = LogFile.get_dateread('2016-07-18 08:11:56 -0700')
        self.assertEquals(res, datetime.datetime(2016, 07, 18, 8, 11, 56, 000000))

