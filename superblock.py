#!/usr/bin/env python2
"""
Analyze superblock in ext2 filesystem.

Usage:
    superblock.py <filename>
"""
import sys
import string
from binascii import hexlify


BLOCKSIZE = 512


def nonprintable_replace(char):
    if char not in string.printable:
        return '.'
    if char in '\n\r\t\x0b\x0c':
        return '.'
    return char


def dump(filename):
    with open(filename, 'rb') as f:
        f.seek(2 * BLOCKSIZE)
        for i in xrange(BLOCKSIZE / 16):
            word = f.read(4), f.read(4), f.read(4), f.read(4)
            hex_string = ' '.join(map(hexlify, word))
            ascii_string = ''.join(map(nonprintable_replace, ''.join(word)))
            print '{0:2}:  {1}  {2}'.format(i + 1, hex_string, ascii_string)


if __name__ == '__main__':

    if len(sys.argv) < 3 or sys.argv[1] not in ['dump', 'analyze']:
        print 'Usage: superblock.py [dump|analyze] <filename>'
        sys.exit(1)

    action = sys.argv[1]
    filename = sys.argv[2]

    if action == 'dump':
        print '\nPrinting superblock (bytes 1024-1535) of file %s.\n' % filename
        print ' ' * 5 + 'HEX'.center(35) + '  ' + 'ASCII'.center(16)
        dump(filename)
    elif action == 'analyze':
        print '\nAnalyzing superblock (bytes 1024-1535) of file %s.\n' % filename
        print 'TODO'

