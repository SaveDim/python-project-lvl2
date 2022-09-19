[
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
                "data_before": true,
                "data_after": null
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
                                "data_before": "",
                                "data_after": "so much"
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
                "data_before": "bas",
                "data_after": "bars"
            },
            {
                "name": "foo",
                "status": "not changed",
                "data": "bar"
            },
            {
                "name": "nest",
                "status": "changed",
                "data_before": {
                    "key": "value"
                },
                "data_after": "str"
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
]