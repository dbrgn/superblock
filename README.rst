##########
superblock
##########

A script written in Python to analyze the superblock of a ext2 formatted file.

Such a file can be created as follows::

    $ dd count=1024 if=/dev/zero of=filesystem.ext2
    $ sudo mkfs.ext2 filesystem.ext2

It can be mounted with ::

    $ sudo mount -t ext2 -o loop filesystem.ext2 /mnt/mountpoint


Usage
=====

::

    $ ./superblock.py [dump|analyze] <filename>


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
     1:  40000000 00020000 19000000 e4010000  @...............
     2:  35000000 01000000 00000000 00000000  5...............
     3:  00200000 00200000 40000000 d20dd550  . ... ..@......P
     4:  d20dd550 0200ffff 53ef0000 01000000  ...P....S.......
     5:  df97d350 00000000 00000000 01000000  ...P............
     6:  00000000 0b000000 80000000 38000000  ............8...
     7:  02000000 01000000 0557f72d 519b45ff  .........W.-Q.E.
     8:  b72037db c87ae22d 00000000 00000000  . 7..z.-........
     9:  00000000 00000000 2f6d6e74 2f646174  ......../mnt/dat
    10:  612f4472 6f70626f 782f4853 522f4273  a/Dropbox/HSR/Bs
    11:  7973312f 7531342f 66736d6f 756e7400  ys1/u14/fsmount.
    12:  00000000 00000000 00000000 00000000  ................
    13:  00000000 00000000 00000000 00000100  ................
    14:  00000000 00000000 00000000 00000000  ................
    15:  00000000 00000000 00000000 188c66cf  ..............f.
    16:  2f744e14 bbac9576 0ded5dde 01000000  /tN....v..].....
    17:  0c000000 00000000 df97d350 00000000  ...........P....
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
    Free blocks counter: 484
    Free inodes counter: 53
    Number of first block: 1
    Block size: 0
    Fragment size: 0
    Number blocks per group: 8192
    Number fragments per group: 8192
    Number inodes per group: 64
    Time of last mount: 2012-12-22 02:33:06
    Time of last write: 2012-12-22 02:33:06
    Mount operations counter: 2
    Number of mount operations before check: 65535
    Magic signature: 0XEF53
    Status flag: 0
    Behavior when detecting errors: 1
    Minor revision level: 0
    Time of last check: 2012-12-20 23:57:35
    Time between checks: 0
    OS Filesystem created: 0
    Revision level: 1
    Default user ID for reserved blocks: 0
    Default group ID for reserved blocks: 0
    Number first nonreserved inode: 11
    Size of on-disk inode structure: 128
    Block group number of this superblock: 0
    Compatibility features bitmap: 0X38
    Incompatible features bitmap: 0X2
    Read-only compatible features bitmap: 0X1
    128-bit filesystem identifier: 0X2DE27AC8DB3720B7FF459B512DF75705
    Volume name: 0X0
    Path of last mount point: 0X746E756F6D73662F3431752F31737973422F5253482F786F62706F72442F617461642F746E6D2F
    Compression: 0X1000000000000
    Number of blocks to preallocate: 0
    Number of blocks to preallocate for directories: 0
