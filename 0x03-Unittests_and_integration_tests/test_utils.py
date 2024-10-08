#!/usr/bin/env python3
"""Parameterize a unit test
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map utils methods"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the correct value"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that access_nested_map raises KeyError for missing keys"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(str(err.exception), f"'{expected}'")


class TestGetJson(unittest.TestCase):
    """get_json Test Class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json returns the correct payload"""
        config = {'return_value.json.return_value': test_payload}
        with patch('requests.get', **config) as mock:
            self.assertEqual(get_json(test_url), test_payload)
            mock.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Memoize test class"""

    def test_memoize(self):
        """Test that memoize caches the result of a method"""
        class TestClass:
            """A test class to apply memoize decorator"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
            TestClass, 'a_method', return_value=42
        ) as mock_method:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
