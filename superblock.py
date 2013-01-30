#!/usr/bin/env python2
"""
Analyze superblock in ext2 filesystem.

Author: Danilo Bargen <gezuru@gmail.com>
License: MIT License

"""
import sys
import string
from binascii import hexlify
from datetime import datetime

BLOCKSIZE = 512


def dump(filename):

    def nonprintable_replace(char):
        if char not in string.printable:
            return '.'
        if char in '\n\r\t\x0b\x0c':
            return '.'
        return char

    with open(filename, 'rb') as f:
        f.seek(2 * BLOCKSIZE)
        for i in xrange(BLOCKSIZE / 16):
            row = f.read(4), f.read(4), f.read(4), f.read(4)
            hex_string = ' '.join(map(hexlify, row))
            ascii_string = ''.join(map(nonprintable_replace, ''.join(row)))
            print '{0:2}:  {1}  {2}'.format(i + 1, hex_string, ascii_string)


def analyze(filename):

    # Binary conversion functions

    def lsb2hex(b_string):
        """Take a binary string (from ``file.read()``) and convert it into a
        hex string by assuming 2 byte little endian byte order."""
        msb_string = hexlify(b_string)
        lsb_string = ''.join([msb_string[x:x + 2] for x in range(0, len(msb_string), 2)][::-1])
        return lsb_string

    def lsb2ascii(b_string):
        """Take a binary string (from ``file.read()``) and convert it to an
        ascii string."""
        msb_string = hexlify(b_string)
        pairs = (msb_string[x:x + 2] for x in range(0, len(msb_string), 2))
        values = (int(x, 16) for x in pairs)
        return ''.join(map(chr, values))

    def lsb2int(b_string):
        """Take a binary string (from ``file.read()``) and convert it into a
        integer by assuming 2 byte little endian byte order."""
        lsb_string = lsb2hex(b_string)
        return int(lsb_string, 16)

    # Formatting functions

    def uuid(h_string):
        """Format a hex string like an UUID."""
        split = lambda x: [x[:8], x[8:12], x[12:16], x[16:20], x[20:]]
        return '-'.join(split(h_string))

    def timestamp(seconds):
        return datetime.fromtimestamp(seconds)

    def map_bitmap(value, mapping):
        """Map a bitmap to the corresponding human readable strings."""
        return ' '.join([t[1] for t in mapping if value & t[0]])

    # Process superblock

    with open(filename, 'rb') as f:
        f.seek(2 * BLOCKSIZE)

        # Bytes 0-15
        inodes_total = lsb2int(f.read(4))
        print 'Total number of inodes: {0:d}'.format(inodes_total)
        print 'Filesystem size in blocks: {0:d}'.format(lsb2int(f.read(4)))
        print 'Number of reserved blocks: {0:d}'.format(lsb2int(f.read(4)))
        print 'Free blocks counter: {0:d}'.format(lsb2int(f.read(4)))

        # Bytes 16-31
        print 'Free inodes counter: {0:d}'.format(lsb2int(f.read(4)))
        print 'Number of first block: {0:d}'.format(lsb2int(f.read(4)))
        val = lsb2int(f.read(4))
        print 'Block size: {0:d} ({1:d} Byte)'.format(val, 1024 * 2 ** val)
        print 'Fragment size: {0:d}'.format(lsb2int(f.read(4)))

        # Bytes 32-47
        print 'Number blocks per group: {0:d}'.format(lsb2int(f.read(4)))
        print 'Number fragments per group: {0:d}'.format(lsb2int(f.read(4)))
        inodes_per_group = lsb2int(f.read(4))
        print 'Number inodes per group: {0:d}'.format(inodes_per_group)
        print 'Number of block groups: {0:d}'.format(inodes_total / inodes_per_group)
        mtime = lsb2int(f.read(4))
        print 'Time of last mount: {0:d} ({1:%Y-%m-%d %H:%M:%S})'.format(mtime, timestamp(mtime))

        # Bytes 48-63
        wtime = lsb2int(f.read(4))
        print 'Time of last write: {0:d} ({1:%Y-%m-%d %H:%M:%S})'.format(wtime, timestamp(wtime))
        print 'Mount operations counter: {0:d}'.format(lsb2int(f.read(2)))
        print 'Number of mount operations before check: {0:d}'.format(lsb2int(f.read(2)))
        print 'Magic signature: {0:#X}'.format(lsb2int(f.read(2)))
        print 'Status flag: {0:d}'.format(lsb2int(f.read(2)))
        print 'Behavior when detecting errors: {0:d}'.format(lsb2int(f.read(2)))
        print 'Minor revision level: {0:d}'.format(lsb2int(f.read(2)))

        # Bytes 64-79
        lastcheck = lsb2int(f.read(4))
        print 'Time of last check: {0} ({1:%Y-%m-%d %H:%M:%S})'.format(lastcheck, timestamp(lastcheck))
        checkinterval = lsb2int(f.read(4))
        print 'Time between checks: {0:d}'.format(checkinterval)
        print 'OS Filesystem created: {0:d}'.format(lsb2int(f.read(4)))
        print 'Revision level: {0:d}'.format(lsb2int(f.read(4)))

        # Bytes 80-95
        print 'Default user ID for reserved blocks: {0:d}'.format(lsb2int(f.read(2)))
        print 'Default group ID for reserved blocks: {0:d}'.format(lsb2int(f.read(2)))
        print 'Number first nonreserved inode: {0:d}'.format(lsb2int(f.read(4)))
        print 'Size of on-disk inode structure: {0:d}'.format(lsb2int(f.read(2)))
        print 'Block group number of this superblock: {0:d}'.format(lsb2int(f.read(2)))
        feature_compat = lsb2int(f.read(4))
        feature_compat_s = map_bitmap(feature_compat, (
            (0x1, 'dir_prealloc'),
            (0x2, 'imagic_inodes'),
            (0x4, 'has_journal'),
            (0x8, 'ext_attr'),
            (0x10, 'resize_ino'),
            (0x20, 'dir_index'),
        ))
        print 'Compatible features bitmap: {0:06b} ({1})'.format(feature_compat, feature_compat_s)

        # Bytes 96-103
        feature_incompat = lsb2int(f.read(4))
        feature_incompat_s = map_bitmap(feature_incompat, (
            (0x1, 'compression'),
            (0x2, 'filetype'),
            (0x4, 'recover'),
            (0x8, 'journal_dev'),
            (0x10, 'meta_bg'),
        ))
        print 'Incompatible features bitmap: {0:05b} ({1})'.format(feature_incompat, feature_incompat_s)
        feature_ro_compat = lsb2int(f.read(4))
        feature_ro_compat_s = map_bitmap(feature_ro_compat, (
            (0x1, 'sparse_super'),
            (0x2, 'large_file'),
            (0x4, 'btree_dir'),
        ))
        print 'Read-only features bitmap: {0:03b} ({1})'.format(feature_ro_compat, feature_ro_compat_s)

        # Bytes 104-119
        print '128-bit filesystem identifier: {0}'.format(uuid(hexlify(f.read(16))))

        # Bytes 120-135
        print 'Volume name: {0}'.format(lsb2ascii(f.read(16)))

        # Bytes 136-199
        print 'Path of last mount point: {0}'.format(lsb2ascii(f.read(64)))

        # Bytes 200-205
        print 'Compression: {0:#X}'.format(lsb2int(f.read(4)))
        print 'Number of blocks to preallocate: {0:d}'.format(lsb2int(f.read(1)))
        print 'Number of blocks to preallocate for directories: {0:d}'.format(lsb2int(f.read(1)))


def run():

    if '-h' in sys.argv or '--help' in sys.argv:
        print 'This is a script to analyze the superblock of a ext2 formatted file.\n'
        print 'Such a file can be created as follows:\n'
        print '    $ dd count=1024 if=/dev/zero of=filesystem.ext2'
        print '    $ sudo mkfs.ext2 filesystem.ext2\n'
        print 'It can be mounted with :\n'
        print '    $ sudo mount -t ext2 -o loop filesystem.ext2 /mnt/mountpoint\n'

    if len(sys.argv) < 3 or sys.argv[1] not in ['dump', 'analyze']:
        print 'Usage: superblock.py [-h|--help] [dump|analyze] <filename>'
        sys.exit(1)

    action = sys.argv[1]
    filename = sys.argv[2]

    if action == 'dump':
        print '\nPrinting superblock (bytes 1024-1535) of file %s.\n' % filename
        print ' ' * 5 + 'HEX'.center(35) + '  ' + 'ASCII'.center(16)
        dump(filename)
    elif action == 'analyze':
        print '\nAnalyzing superblock (bytes 1024-1535) of file %s.\n' % filename
        analyze(filename)


if __name__ == '__main__':
    run()
