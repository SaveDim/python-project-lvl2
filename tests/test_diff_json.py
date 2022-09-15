
# -*- coding: utf-8 -*-

"""JSON files test diff."""

from gendiff.generate_diff import generate_diff


def test1_flat_json():
    correct = generate_diff('./tests/fixtures/file1_flat.json',
                            './tests/fixtures/file2_flat.json',
                            )
    expected = open('./tests/fixtures'
                    '/correct_flat_result.txt', 'r').read()
    assert correct == expected
