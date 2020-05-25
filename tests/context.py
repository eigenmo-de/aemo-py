# this allows files in the tests/ folder to
# import the module conveniently,
# courtesy of:
# https://docs.python-guide.org/writing/structure/

import os
import sys
sys.path.insert(
        0,
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), 
                '..',
                ),
            ),
        )

import aemo
