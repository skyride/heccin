from django.test import SimpleTestCase

from .utils import get_name_from_host


class UtilTests(SimpleTestCase):
    def test_get_name_from_host(self):
        # Test with sample names
        assert get_name_from_host("amy.is.heccin.gay") == "Amy"
        assert get_name_from_host("jim.is.heccin.gay") == "Jim"
        assert get_name_from_host("bob.is.heccin.gay") == "Bob"

        # Test with dash
        assert get_name_from_host("j-flinn.is.heccin.gay") == "J-Flinn"

        # Test with port
        assert get_name_from_host("amy.is.heccin.gay:8000") == "Amy"
        assert get_name_from_host("jim.is.heccin.gay:4000") == "Jim"
        assert get_name_from_host("bob.is.heccin.gay:22") == "Bob"
