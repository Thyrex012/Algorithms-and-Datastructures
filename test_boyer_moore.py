import unittest
from boyer_moore import boyer_moore

#Made by chatgpt
class TestBoyerMoore(unittest.TestCase):

    def test_cases(self):
        tests = [
            ("abc", "abc", [0]),
            ("abc", "abcabcabc", [0, 3, 6]),
            ("abc", "aaaaaa", []),
            ("aba", "ababa", [0, 2]),
            ("aaa", "aaaaaa", [0, 1, 2, 3]),
            ("hello", "hello world", [0]),
            ("world", "hello world", [6]),
            ("algorithm", "algorithm", [0]),
            ("abcdef", "abc", []),
            ("a", "banana", [1, 3, 5]),
            ("aaaa", "aaaaaaaa", [0, 1, 2, 3, 4]),
            ("abab", "abababab", [0, 2, 4]),
            ("abcd", "abcxabcxabcd", [8]),
            ("ababa", "abababababa", [0, 2, 4, 6]),
            ("xyz", "aaaaaaaaaaaaaaaaaaaa", []),
            ("abba", "abbabbaabba", [0, 3, 7]),
            ("aaaab", "aaaaaaaaaab", [6]),
        ]

        for pattern, text, expected in tests:
            with self.subTest(pattern=pattern, text=text):
                self.assertEqual(boyer_moore(pattern, text), expected)

    def test_long_string(self):
        # Very long text
        text = "abcde" * 10000 + "xyzabcde" + "abcde" * 10000
        pattern = "xyzabcde"
        expected = [10000 * 5]  # 50,000

        matches = boyer_moore(pattern, text)
        self.assertEqual(matches, expected)


if __name__ == "__main__":
    unittest.main()