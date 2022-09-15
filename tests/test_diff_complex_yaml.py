
# -*- coding: utf-8 -*-

"""JSON files test diff."""

from gendiff.generate_diff import generate_diff


def test1_complex_yaml():
    correct = generate_diff('./tests/fixtures/file1_complex.yaml',
                            './tests/fixtures/file2_complex.yml',
                            )
    expected = open('./tests/fixtures'
                    '/correct_complex_result.md', 'r').read()
    assert correct == expected
