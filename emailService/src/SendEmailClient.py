#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import logging.config

sys.path.append('../lib/')
from sendEmail import SendEmail

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = SendEmail.Client(protocol)

    # Connect!
    print 'connecting ...'
    transport.open()
    b = client.send("no@no.com", u'主题', u'内容')
    transport.close()


if __name__ == '__main__':
    main()