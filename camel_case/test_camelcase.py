import unittest
from unittest.mock import patch
import camel

class TestCamelCase(unittest.TestCase):

    def test_capitalize(self):

        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        capitalized = 'Abc'

        for word in input_words:
            self.assertEqual(camel.capitalize(word), capitalized)


    def test_lower(self):
        # this isn't really needed, since we can assume that Python's library functions work correctly :)
        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        lower = 'abc'

        for word in input_words:
            self.assertEqual(camel.lowercase(word), lower)


    def test_camel_case(self):

        input_and_expected_outputs = {
            '' : '' ,
            'hello' : 'hello',
            'Hello' : 'hello',
            'Hello world' : 'helloWorld',
            'HELLO WORLD' : 'helloWorld',
            'hELLO wORLD' : 'helloWorld',
            'this is a sentence' : 'thisIsASentence',
            'Here is a long sentence with many words' : 'hereIsALongSentenceWithManyWords'
        }

        for input_val in input_and_expected_outputs.keys():
            self.assertEqual(camel.camel_case(input_val), input_and_expected_outputs[input_val])


    def test_input_and_output(self):

        # Patch the input. Using with context manager automatically takes care of unpatching.
        with patch('builtins.input', return_value='This IS another SENTenCE'):

            # And, patch the output
            with patch('builtins.print') as mock_print:

                camel.main()
                mock_print.assert_called_with('thisIsAnotherSentence')



if __name__ == '__main__':
    unittest.main()
