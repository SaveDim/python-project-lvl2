
# -*- coding: utf-8 -*-

"""JSON files test diff."""

from gendiff.generate_diff import generate_diff
import tests.fixtures.correct_answers as expected


def test1_complex_yaml():
    correct = generate_diff('./tests/fixtures/file1_complex.yaml',
                            './tests/fixtures/file2_complex.yml',
                            )
    assert correct == expected.CORRECT_COMPLEX_RESULT
