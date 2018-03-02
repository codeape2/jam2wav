from jam2wav import jam2wav
from unittest import TestCase


class TestJam2Wav(TestCase):
    def test_works_as_expected(self):
        with open('REC_#08.JAM', 'rb') as f:
            jambytes = f.read()

        self.assertEqual(2092240, len(jambytes))
        wavbytes = jam2wav(jambytes)
        self.assertEqual(2091720, len(wavbytes))
