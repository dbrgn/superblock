##########
superblock
##########

A script written in Python 2 to analyze the superblock of an ext2/ext3 formatted
file.

Such a file can be created as follows::

    $ dd count=4096 if=/dev/zero of=filesystem.ext3
    $ sudo mkfs.ext3 filesystem.ext3

It can be mounted with ::

    $ sudo mount -t ext3 -o loop filesystem.ext3 /mnt/mountpoint


Install
=======

You can either download ``superblock.py`` file and use it directly, or install
the ``superblock`` command via pip::

    $ sudo pip install superblock


Usage
=====

::

    $ superblock [dump|analyze] <filename>


License
=======

`MIT License <http://www.tldrlegal.com/license/mit-license>`_, see LICENSE file.


Examples
========

Dump
----

::

    Printing superblock (bytes 1024-1535) of file fs.ext2.

                         HEX                       ASCII      
     1:  40000000 00020000 19000000 e2010000  @...............
     2:  32000000 01000000 00000000 00000000  2...............
     3:  00200000 00200000 40000000 82bad550  . ... ..@......P
     4:  c4bcd550 0200ffff 53ef0100 01000000  ...P....S.......
     5:  968bd550 00000000 00000000 01000000  ...P............
     6:  00000000 0b000000 80000000 38000000  ............8...
     7:  02000000 01000000 dc0cb51b 2ab54967  ............*.Ig
     8:  8e602492 87974d10 65787065 72696d5f  .`$...M.experim_
     9:  65787432 00000000 2f686f6d 652f6461  ext2..../home/da
    10:  6e696c6f 2f50726f 6a656374 732f7375  nilo/Projects/su
    11:  70657262 6c6f636b 2f6d6e74 00000000  perblock/mnt....
    12:  00000000 00000000 00000000 00000000  ................
    13:  00000000 00000000 00000000 00000100  ................
    14:  00000000 00000000 00000000 00000000  ................
    15:  00000000 00000000 00000000 ff27f89c  .............'..
    16:  b5cb41d1 987de848 6b3e81ba 01000000  ..A..}.Hk>......
    17:  0c000000 00000000 968bd550 00000000  ...........P....
    18:  00000000 00000000 00000000 00000000  ................
    19:  00000000 00000000 00000000 00000000  ................
    20:  00000000 00000000 00000000 00000000  ................
    21:  00000000 00000000 00000000 00000000  ................
    22:  00000000 00000000 00000000 00000000  ................
    23:  01000000 00000000 00000000 00000000  ................
    24:  00000000 00000000 00000000 00000000  ................
    25:  00000000 00000000 00000000 00000000  ................
    26:  00000000 00000000 00000000 00000000  ................
    27:  00000000 00000000 00000000 00000000  ................
    28:  00000000 00000000 00000000 00000000  ................
    29:  00000000 00000000 00000000 00000000  ................
    30:  00000000 00000000 00000000 00000000  ................
    31:  00000000 00000000 00000000 00000000  ................
    32:  00000000 00000000 00000000 00000000  ................

Analyze
-------

::

    Analyzing superblock (bytes 1024-1535) of file fs.ext2.

    Total number of inodes: 64
    Filesystem size in blocks: 512
    Number of reserved blocks: 25
    Free blocks counter: 482
    Free inodes counter: 50
    Number of first block: 1
    Block size: 0 (1024 Byte)
    Fragment size: 0
    Number blocks per group: 8192
    Number fragments per group: 8192
    Number inodes per group: 64
    Number of block groups: 1
    Time of last mount: 1356184194 (2012-12-22 14:49:54)
    Time of last write: 1356184772 (2012-12-22 14:59:32)
    Mount operations counter: 2
    Number of mount operations before check: 65535
    Magic signature: 0XEF53
    Status flag: 1
    Behavior when detecting errors: 1
    Minor revision level: 0
    Time of last check: 1356172182 (2012-12-22 11:29:42)
    Time between checks: 0
    OS Filesystem created: 0
    Revision level: 1
    Default user ID for reserved blocks: 0
    Default group ID for reserved blocks: 0
    Number first nonreserved inode: 11
    Size of on-disk inode structure: 128
    Block group number of this superblock: 0
    Compatible features bitmap: 111000 (ext_attr resize_ino dir_index)
    Incompatible features bitmap: 00010 (filetype)
    Read-only features bitmap: 001 (sparse_super)
    128-bit filesystem identifier: dc0cb51b-2ab5-4967-8e60-249287974d10
    Volume name: experim_ext2
    Path of last mount point: /home/danilo/Projects/superblock/mnt
    Compression: 0X0
    Number of blocks to preallocate: 0
    Number of blocks to preallocate for directories: 0


Resources
=========

- `The Second Extended File System <http://www.nongnu.org/ext2-doc/ext2.html>`__
- `/usr/include/ext2fs/ext2_fs.h`
