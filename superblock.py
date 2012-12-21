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


def block_printer(filename, offset, block_count):

    def nonprintable_replace(char):
        if char not in string.printable:
            return '.'
        if char in '\n\r\t\x0b\x0c':
            return '.'
        return char

    with open(filename, 'rb') as f:
        f.seek(offset * BLOCKSIZE)

        # Loop over blocks
        for i in xrange(block_count):

            # Loop over bytes
            for j in xrange(BLOCKSIZE / 8):
                part1 = f.read(4)
                part2 = f.read(4)
                print '{0:2}:  {1} {2}  {3}'.format(j+1, hexlify(part1), hexlify(part2), ''.join(map(nonprintable_replace, part1 + part2)))


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Usage: superblock.py <filename>'
        sys.exit(1)

    filename = sys.argv[1]
    print 'Printing superblock (bytes 1024-1535) of file %s.\n' % filename
    print ''.center(5) + 'HEX'.center(18) + 'ASCII'.center(8)
    block_printer(filename, 2, 1)
