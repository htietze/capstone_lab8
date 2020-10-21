import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin

class TestBitcoinRate(TestCase):

    @patch('bitcoin.get_current_BTC_rate')
    def test_bitcoin_to_USD(self, mock_exchange):
        mock_rate = 500
        # Edited the api response down to use the same keys needed for the method, didn't need anything but USD and could remove the timing data.
        test_api_response = {"bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"11,932.9618","description":"United States Dollar","rate_float":11932.9618}}}
        mock_exchange.side_effect = [ test_api_response ]
        converted = bitcoin.convert_BTC_to_USD(20, 500)
        expected = 10000
        self.assertEqual(expected, converted)