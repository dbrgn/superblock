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
