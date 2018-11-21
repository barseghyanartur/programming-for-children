========================
Programming for children
========================
A quick presentation of some of the features of Arduino (lights, sound module,
button) and Microbit (lights, accelerometer). It's a workshop material for
children of 6-7 years old.

Material has been originally written in Dutch, but may be translated into
other languages.

Some of the code samples are taken from Internet.

If not stated otherwise, written by me (see the `Author`_).

Structure
=========
Project structure:

- `library`_
- `scripts`_
- `source`_

library
-------
Working code samples:

- `Arduino
  <https://github.com/barseghyanartur/programming-for-children/tree/master/library/arduino>`_.
- `Microbit
  <https://github.com/barseghyanartur/programming-for-children/tree/master/library/microbit>`_.

Make sure to check the `game
<https://github.com/barseghyanartur/programming-for-children/blob/master/library/microbit/game.py>`_
written for Microbit. Children seemed to like it a lot.

scripts
-------
Helper scripts (build docs, install docs requirements).

source
------
The course material:

- `Arduino
  <https://github.com/barseghyanartur/programming-for-children/blob/master/source/arduino.rst>`_
- `Microbit
  <https://github.com/barseghyanartur/programming-for-children/blob/master/source/microbit.rst>`_.

Build/generate the documentation
--------------------------------
**Install requirements**

.. code-block:: sh

    ./scripts/install.sh

**Build the docs**

.. code-block:: sh

    ./scripts/build_docs.sh

**Check the generated docs**

Documentation should be generated int two formats: HTML and PDF.
Check the `builddocs` directory.

License
=======
License is GPL 2.0.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
