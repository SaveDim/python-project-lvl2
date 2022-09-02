
# -*- coding: utf-8 -*-

"""JSON files test diff."""

from gendiff.generate_diff import generate_diff
import tests.fixtures.correct_answers as expected


def test1_flat_yaml():
    correct = generate_diff('./tests/fixtures/file1_flat.yaml',
                            './tests/fixtures/file2_flat.yml',
                            )
    assert correct == expected.CORRECT_FLAT_RESULT
