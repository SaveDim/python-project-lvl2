
# -*- coding: utf-8 -*-

"""All files test diff."""

from gendiff.generate_diff import generate_diff
import pytest

from tests import get_path

@pytest.mark.parametrize(
    "test_input1,test_input2, formatter,  expected",
    [
        pytest.param(
            'file1_complex.json',
            'file2_complex.json',
            'stylish',
            'correct_complex_result.md',
        ),
        pytest.param(
            'file1_complex.yaml',
            'file2_complex.yml',
            'stylish',
            'correct_complex_result.md',
        ),
        pytest.param(
            'file1_flat.json',
            'file2_flat.json',
            'stylish',
            'correct_flat_result.md',
        ),
        pytest.param(
            'file1_flat.yaml',
            'file2_flat.yml',
            'stylish',
            'correct_flat_result.md',
        ),
        pytest.param(
            'file1_complex.json',
            'file2_complex.json',
            'json',
            'correct_json_complex_result.md',
        ),
        pytest.param(
            'file1_complex.json',
            'file2_complex.json',
            'plain',
            'correct_plain_complex_result.md',
        ),
        pytest.param(
            'file1_flat.json',
            'file2_flat.json',
            'plain',
            'correct_plain_flat_result.md',
        ),
    ],
)
def test_generare_diff(test_input1, test_input2, formatter, expected):
    expected_path = get_path(expected)
    with open(expected_path, 'r') as file:
        result_data = file.read()
        test_path1 = get_path(test_input1)
        test_path2 = get_path(test_input2)
        assert generate_diff(test_path1, test_path2, formatter) == result_data
