# -*- coding: utf-8 -*-
"""
    consider.consider
    ~~~~~~~~~~~~~~~~~

    Consider is a parser for the ThinkGear protocol used by NeuroSky devices.

    :copyright: (c) 2012 lanius
    :license: MIT, see LICENSE for more details.
"""

from contextlib import closing
from itertools import islice
from socket import socket, AF_INET, SOCK_STREAM
from struct import unpack


class Consider(object):

    def __init__(self, host='127.0.0.1', port=13854):
        self.parser = Parser(host, port)
        self.is_running = False

    def get_packet(self):
        if not self.parser.is_synced:
            self.parser.sync()
        return self.parser.parse()

    def packet_generator(self):
        self.is_running = True
        if not self.parser.is_synced:
            self.parser.sync()
        while self.is_running:
            yield self.parser.parse()


class Parser(object):

    def __init__(self, host, port):
        raw = Raw(host, port)
        self.byte_stream = raw.byte_stream()
        self.is_synced = False

    def sync(self):
        sync_bytes = 0
        while sync_bytes != 2:
            if self.byte_stream.next() == '\xAA':
                sync_bytes += 1
        self.is_synced = True

    def parse(self):
        if not self.is_synced:
            raise SyncError("have not be synced.")
        packet = Packet()
        while True:
            code = self.byte_stream.next()
            if code == '\x02':
                packet.poor_signal = self.unpack_a_byte()
            elif code == '\x04':
                packet.attention = self.unpack_a_byte()
            elif code == '\x05':
                packet.meditation = self.unpack_a_byte()
            elif code == '\x81':
                packet.length = self.unpack_a_byte()
                packet.delta = self.unpack_four_bytes()
                packet.theta = self.unpack_four_bytes()
                packet.low_alpha = self.unpack_four_bytes()
                packet.high_alpha = self.unpack_four_bytes()
                packet.low_beta = self.unpack_four_bytes()
                packet.high_beta = self.unpack_four_bytes()
                packet.low_gamma = self.unpack_four_bytes()
                packet.high_gamma = self.unpack_four_bytes()
            elif code == '\xAA':
                self.byte_stream.next()  # discard sync code.
                break
            else:  # got abnormal signal
                self.is_synced = False
                break
        return packet

    def unpack_a_byte(self):
        byte = self.byte_stream.next()
        return unpack('>B', byte)[0]

    def unpack_four_bytes(self):
        four_bytes = ''.join([b for b in islice(self.byte_stream, 4)])
        return unpack('>f', four_bytes)[0]


class Raw(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.is_running = False

    def byte_stream(self):
        self.is_running = True
        with closing(socket(AF_INET, SOCK_STREAM)) as soc:
            soc.connect((self.host, self.port))
            while self.is_running:
                yield soc.recv(1)


class Packet(object):

    def __init__(self):
        self.length = 0
        self.delta = 0
        self.theta = 0
        self.low_alpha = 0
        self.high_alpha = 0
        self.low_beta = 0
        self.high_beta = 0
        self.low_gamma = 0
        self.high_gamma = 0
        self.attention = 0
        self.meditation = 0
        self.poor_signal = 0

    def _dict(self):
        return {
            'length': self.length,
            'delta': self.delta,
            'theta': self.theta,
            'low_alpha': self.low_alpha,
            'high_alpha': self.high_alpha,
            'low_beta': self.low_beta,
            'high_beta': self.high_beta,
            'low_gamma': self.low_gamma,
            'high_gamma': self.high_gamma,
            'attention': self.attention,
            'meditation': self.meditation,
            'poor_signal': self.poor_signal
            }

    def __repr__(self):
        return str(self._dict())

    def __str__(self):
        return str(self._dict())


class SyncError(Exception):
    pass
