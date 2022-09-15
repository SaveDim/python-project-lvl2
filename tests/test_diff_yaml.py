
# -*- coding: utf-8 -*-

"""JSON files test diff."""

from gendiff.generate_diff import generate_diff


def test1_flat_yaml():
    correct = generate_diff('./tests/fixtures/file1_flat.yaml',
                            './tests/fixtures/file2_flat.yml',
                            )
    expected = open('./tests/fixtures'
                    '/correct_flat_result.md', 'r').read()
    assert correct == expected
