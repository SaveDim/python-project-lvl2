# -*- coding: utf-8 -*-

"""Expected results."""

CORRECT_FLAT_RESULT = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

CORRECT_COMPLEX_RESULT = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:  
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

CORRECT_PLAIN_FLAT_RESULT = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""

CORRECT_PLAIN_COMPLEX_RESULT = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

CORRECT_JSON_COMPLEX_RESULT = """[
    {
        "name": "common",
        "status": "nested",
        "children": [
            {
                "name": "follow",
                "status": "added",
                "data": false
            },
            {
                "name": "setting1",
                "status": "not changed",
                "data": "Value 1"
            },
            {
                "name": "setting2",
                "status": "deleted",
                "data": 200
            },
            {
                "name": "setting3",
                "status": "changed",
                "data before": true,
                "data after": null
            },
            {
                "name": "setting4",
                "status": "added",
                "data": "blah blah"
            },
            {
                "name": "setting5",
                "status": "added",
                "data": {
                    "key5": "value5"
                }
            },
            {
                "name": "setting6",
                "status": "nested",
                "children": [
                    {
                        "name": "doge",
                        "status": "nested",
                        "children": [
                            {
                                "name": "wow",
                                "status": "changed",
                                "data before": "",
                                "data after": "so much"
                            }
                        ]
                    },
                    {
                        "name": "key",
                        "status": "not changed",
                        "data": "value"
                    },
                    {
                        "name": "ops",
                        "status": "added",
                        "data": "vops"
                    }
                ]
            }
        ]
    },
    {
        "name": "group1",
        "status": "nested",
        "children": [
            {
                "name": "baz",
                "status": "changed",
                "data before": "bas",
                "data after": "bars"
            },
            {
                "name": "foo",
                "status": "not changed",
                "data": "bar"
            },
            {
                "name": "nest",
                "status": "changed",
                "data before": {
                    "key": "value"
                },
                "data after": "str"
            }
        ]
    },
    {
        "name": "group2",
        "status": "deleted",
        "data": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    {
        "name": "group3",
        "status": "added",
        "data": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
]"""
