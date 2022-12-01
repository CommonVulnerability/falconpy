"""FalconPy Request Payloads class.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
from typing import Optional, Dict, List, Union


class RequestPayloads:
    """This class contains all of the payloads sent as part of the API request."""

    # ____ ___ ___ ____ _ ___  _  _ ___ ____ ____
    # |__|  |   |  |__/ | |__] |  |  |  |___ [__
    # |  |  |   |  |  \ | |__] |__|  |  |___ ___]
    #
    _params: Optional[Dict[str, str]] = None
    _body: Optional[Dict[str, Union[str, int, dict, list, bytes]]] = None
    _data: Optional[Dict[str, Union[str, int, dict, list, bytes]]] = None
    _files: Optional[List[tuple]] = None

    # ____ ____ _  _ ____ ___ ____ _  _ ____ ___ ____ ____
    # |    |  | |\ | [__   |  |__/ |  | |     |  |  | |__/
    # |___ |__| | \| ___]  |  |  \ |__| |___  |  |__| |  \
    #
    def __init__(self,
                 params: dict = None,
                 body: dict or bytes = None,
                 data: dict or bytes = None,
                 files: list = None
                 ):
        if params is not None:
            self._params = params
        if body is not None:
            self._body = body
        if data is not None:
            self._data = data
        if files is not None:
            self._files = files

    # ___  ____ ____ ___  ____ ____ ___ _ ____ ____
    # |__] |__/ |  | |__] |___ |__/  |  | |___ [__
    # |    |  \ |__| |    |___ |  \  |  | |___ ___]
    #
    @property
    def params(self) -> dict:
        return self._params
    @params.setter
    def params(self, value: dict):
        self._params = value
    @property
    def body(self) -> dict or bytes:
        return self._body
    @body.setter
    def body(self, value: dict or bytes):
        self._body = value
    @property
    def data(self) -> dict or bytes:
        return self._data
    @data.setter
    def data(self, value: dict or bytes):
        self._data = value
    @property
    def files(self) -> list:
        return self._files
    @files.setter
    def files(self, value: list):
        self._files = value
