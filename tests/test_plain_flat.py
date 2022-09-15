
# -*- coding: utf-8 -*-

"""JSON files test diff."""

from gendiff.generate_diff import generate_diff


def test1_flat_plain():
    correct = generate_diff('./tests/fixtures/file1_flat.json',
                            './tests/fixtures/file2_flat.json',
                            format='plain'
                            )
    expected = open('./tests/fixtures'
                    '/correct_plain_flat_result.md', 'r').read()
    assert correct == expected
