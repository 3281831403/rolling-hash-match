import pytest

from scan import rolling_hash as mod

CASES = [
    ('poly_hash', ['abc', 31, 1000000007], 96354, False),
    ('poly_hash', ['', 31, 1000000007], 0, False),
    ('rolling_hashes', ['abcd', 2, 31, 1000000007], [3105, 3137, 3169], False),
    ('find_substring', ['abcabc', 'bc', 31, 1000000007], 1, False),
    ('find_substring', ['abc', 'z', 31, 1000000007], -1, False),
    ('verify_at', ['abc', 1, 'bc'], True, False),
    ('count_occurrences', ['aaaa', 'aa', 31, 1000000007], 3, False),
    ('count_occurrences', ['abc', '', 31, 1000000007], 0, False),
    ('poly_hash', ['a', 31, 97], 0, False),
    ('rolling_hashes', ['a', 2, 31, 97], [], False),
    ('find_substring', ['aaaa', 'aa', 31, 97], 0, False),
    ('verify_at', ['abc', 0, 'ab'], True, False),
    ('count_occurrences', ['', 'a', 31, 97], 0, False),
    ('count_occurrences', ['abab', 'ab', 31, 97], 2, False),
    ('rolling_hashes', ['abc', 3, 31, 97], [33], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_rolling_hash_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
