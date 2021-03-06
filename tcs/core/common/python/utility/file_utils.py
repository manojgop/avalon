# Copyright 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
file_utils.py -- file utility routines

NOTE: functions defined in this file are designed to be run
before logging is enabled.
"""

import os
import errno

__all__ = [
    'find_file_in_path',
    'read_json_file'
    ]

# -----------------------------------------------------------------
# -----------------------------------------------------------------
def find_file_in_path(filename, search_path) :
    """general utility to search for a file name in a path

    :param str filename: name of the file to locate, absolute path ignores search_path
    :param list(str) search_path: list of directories where the files may be located
    """

    # os.path.abspath only works for full paths, not relative paths
    # this check should catch './abc'
    if os.path.split(filename)[0] :
        if os.path.isfile(filename) :
            return filename
        raise FileNotFoundError(errno.ENOENT, "file does not exist", filename)

    for path in search_path :
        full_filename = os.path.join(path, filename)
        if os.path.isfile(full_filename) :
            return full_filename

    raise FileNotFoundError(errno.ENOENT, "unable to locate file in search path", filename)

# -----------------------------------------------------------------
def read_json_file(input_file, data_dir = ['./', '../', '/']) :
    """
    Utility function to read a JSON file
    """
    file_name = find_file_in_path(input_file, data_dir)
    with open(file_name, "r") as input_json_file :
        input_json = input_json_file.read().rstrip('\n')
    return input_json
