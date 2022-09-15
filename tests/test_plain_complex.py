
# -*- coding: utf-8 -*-

"""JSON files test diff."""

from gendiff.generate_diff import generate_diff


def test1_complex_plain():
    correct = generate_diff('./tests/fixtures/file1_complex.json',
                            './tests/fixtures/file2_complex.json',
                            format='plain'
                            )
    expected = open('./tests/fixtures'
                    '/correct_plain_complex_result.md', 'r').read()
    assert correct == expected
