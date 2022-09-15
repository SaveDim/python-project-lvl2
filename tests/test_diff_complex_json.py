
# -*- coding: utf-8 -*-

"""JSON files test diff."""

from gendiff.generate_diff import generate_diff


def test1_complex_json():
    correct = generate_diff('./tests/fixtures/file1_complex.json',
                            './tests/fixtures/file2_complex.json',
                            )
    expected = open('./tests/fixtures'
                    '/correct_complex_result.txt', 'r').read()
    assert correct == expected
