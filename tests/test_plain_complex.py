
# -*- coding: utf-8 -*-

"""JSON files test diff."""

from gendiff.generate_diff import generate_diff
import tests.fixtures.correct_answers as expected


def test1_complex_plain():
    correct = generate_diff('./tests/fixtures/file1_complex.json',
                            './tests/fixtures/file2_complex.json',
                            format='plain'
                            )
    assert correct == expected.CORRECT_PLAIN_COMPLEX_RESULT
