from django.test import SimpleTestCase

from .utils import get_name_from_host, name_to_subdomain


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

        # Test with spaces
        assert get_name_from_host("first--last.is.heccin.gay") == "First Last"
        assert get_name_from_host("j-flinn--last.is.heccin.gay") == "J-Flinn Last"

    def test_name_to_subdomain(self):
        # Test with valid samples
        assert name_to_subdomain("Amy") == "amy"
        assert name_to_subdomain("Jim") == "jim"
        assert name_to_subdomain("BOB") == "bob"

        # Test numbers
        assert name_to_subdomain("Amy1") == "amy1"
        assert name_to_subdomain("Jim2") == "jim2"
        assert name_to_subdomain("BOB3") == "bob3"

        # Test space stripping
        assert name_to_subdomain("Amy F") == "amy--f"
        assert name_to_subdomain("Jim D") == "jim--d"
        assert name_to_subdomain("BOB  ") == "bob"

        # Test with dashes
        assert name_to_subdomain("J-Flinn Last") == "j-flinn--last"
