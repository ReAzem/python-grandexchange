#
#    Copyright (C) 2014 Alexandre Viau <alexandre@alexandreviau.net>
#
#    This file is part of python-grandexchange.
#
#    python-grandexchange is free software: you can redistribute it and/or
#    modify it under the terms of the GNU General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    python-grandexchange is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with python-grandexchange.  If not, see
#    <http://www.gnu.org/licenses/>.
#

import requests


class GrandExchange(object):
    api_url = 'http://services.runescape.com/m=itemdb_rs/api'

    def __init__(self):
        pass

    def json_request(self, method, url, **kwargs):
        resp = requests.request(
            method,
            GrandExchange.api_url + url,
            **kwargs
        )
        return resp.json()

    def get_item(self, id):
        return self.json_request('GET', '/catalogue/detail.json?item=%d' % id)['item']
