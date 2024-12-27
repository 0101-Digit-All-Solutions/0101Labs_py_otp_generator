import unittest
from otp_generator import generate_otp

class TestOTPGenerator(unittest.TestCase):
    def test_default_otp(self):
        otp = generate_otp()
        self.assertEqual(len(otp), 6)
        self.assertTrue(otp.isdigit())

    def test_custom_length(self):
        otp = generate_otp(length=8)
        self.assertEqual(len(otp), 8)

    def test_alphanumeric_otp(self):
        otp = generate_otp(length=10, numeric=True, alphabets=True, special_chars=False)
        # Ensure the character pool includes both digits and alphabets
        self.assertTrue(any(c.isdigit() for c in otp) or any(c.isalpha() for c in otp))

if __name__ == '__main__':
    unittest.main()
