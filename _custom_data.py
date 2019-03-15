# ----------------------------------------------------------------------
# |
# |  _custom_data.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2019-02-28 13:17:19
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2019
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Data used by both Setup_custom.py and Activate_custom.py"""

import os

import CommonEnvironment

# ----------------------------------------------------------------------
_script_fullpath                            = CommonEnvironment.ThisFullpath()
_script_dir, _script_name                   = os.path.split(_script_fullpath)
#  ----------------------------------------------------------------------

_CUSTOM_DATA                                = [
    (
        "MSVC - 15.9.7",
        "1DDA9BD6014CB01EA2D3B7405238146AE1DC3916AB5839B83F542FB3F78D1EBD",
        [
            "Tools",
            "MSVC",
            "v15.9.7",
            "Windows",
        ],
    ),
    ("Windows Kits - 10.0.17763.0", "4148B22C5C910A97630327DD4DF54CD29EDBFDE190C44E559816FE5A963670D4", ["Libraries", "Windows Kits", "10"]),
]
