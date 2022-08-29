
# -*- coding: utf-8 -*-

"""JSON files test diff."""

from gendiff.generate_diff import generate_diff
import tests.correct_answers as expected


def test1_flat_json():
    correct = generate_diff('./tests/fixtures/file1_flat.json',
                            './tests/fixtures/file2_flat.json',
                            )
    assert correct == expected.CORRECT_FLAT_RESULT
