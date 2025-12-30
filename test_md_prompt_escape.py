#!/usr/bin/env python3
"""
Тесты для утилиты md_prompt_escape.
"""

import unittest
from md_prompt_escape import escape_for_python, markdown_to_singleline


class TestEscapeForPython(unittest.TestCase):
    """Тесты для функции escape_for_python."""
    
    def test_escape_backslash(self):
        """Тест экранирования обратного слеша."""
        result = escape_for_python('path\\to\\file')
        self.assertEqual(result, 'path\\\\to\\\\file')
    
    def test_escape_double_quotes(self):
        """Тест экранирования двойных кавычек."""
        result = escape_for_python('He said "Hello"')
        self.assertEqual(result, 'He said \\"Hello\\"')
    
    def test_escape_single_quotes(self):
        """Тест экранирования одинарных кавычек."""
        result = escape_for_python("It's working")
        self.assertEqual(result, "It\\'s working")
    
    def test_escape_newlines(self):
        """Тест экранирования переводов строк."""
        result = escape_for_python('Line 1\nLine 2\nLine 3')
        self.assertEqual(result, 'Line 1\\nLine 2\\nLine 3')
    
    def test_escape_tabs(self):
        """Тест экранирования табуляции."""
        result = escape_for_python('Column1\tColumn2')
        self.assertEqual(result, 'Column1\\tColumn2')
    
    def test_escape_carriage_return(self):
        """Тест экранирования возврата каретки."""
        result = escape_for_python('Text\rOverwrite')
        self.assertEqual(result, 'Text\\rOverwrite')
    
    def test_complex_markdown(self):
        """Тест экранирования сложного markdown-текста."""
        markdown = """# Title\n\n## Subtitle\n\nSome text with "quotes" and 'apostrophes'."""
        result = escape_for_python(markdown)
        expected = r"# Title\n\n## Subtitle\n\nSome text with \"quotes\" and \'apostrophes\'."
        self.assertEqual(result, expected)


class TestMarkdownToSingleline(unittest.TestCase):
    """Тесты для функции markdown_to_singleline."""
    
    def test_double_quotes_style(self):
        """Тест с двойными кавычками."""
        result = markdown_to_singleline('Hello World', quote_style='double')
        self.assertEqual(result, '"Hello World"')
    
    def test_single_quotes_style(self):
        """Тест с одинарными кавычками."""
        result = markdown_to_singleline('Hello World', quote_style='single')
        self.assertEqual(result, "'Hello World'")
    
    def test_triple_quotes_style(self):
        """Тест с тройными кавычками."""
        result = markdown_to_singleline('Hello\nWorld', quote_style='triple')
        self.assertEqual(result, '"""Hello\nWorld"""')
    
    def test_invalid_quote_style(self):
        """Тест с недопустимым стилем кавычек."""
        with self.assertRaises(ValueError):
            markdown_to_singleline('Hello', quote_style='invalid')
    
    def test_multiline_markdown(self):
        """Тест с многострочным markdown."""
        markdown = """# API Request

This is a **bold** statement.

- Item 1
- Item 2

Code: `print("hello")`"""
        
        result = markdown_to_singleline(markdown, quote_style='double')
        self.assertIn('\\n', result)
        self.assertNotIn('\n', result.strip('"'))
    
    def test_markdown_with_special_chars(self):
        """Тест с специальными символами."""
        markdown = 'Path: C:\\Users\\Test\nQuote: "Example"'
        result = markdown_to_singleline(markdown, quote_style='double')
        expected = r'"Path: C:\\Users\\Test\nQuote: \"Example\""'
        self.assertEqual(result, expected)


class TestRealWorldExamples(unittest.TestCase):
    """Тесты с примерами из реальной жизни."""
    
    def test_api_prompt_example(self):
        """Тест с примером промпта для API."""
        prompt = """You are a helpful assistant.

Please help me with:
1. Task one
2. Task two

Be concise and "accurate"."""
        
        result = markdown_to_singleline(prompt, quote_style='double')
        
        code = f"prompt = {result}"
        self.assertIn(r'prompt = "You are a helpful assistant.\n\n', code)
        self.assertIn(r'\"accurate\"', code)
    
    def test_code_in_markdown(self):
        """Тест с кодом внутри markdown."""
        prompt = """Write a function:

```python
def hello():
    print("Hello")
```

Explain it."""
        
        result = markdown_to_singleline(prompt, quote_style='double')
        self.assertIn(r'\n', result)
        self.assertIn(r'\"Hello\"', result)


if __name__ == '__main__':
    unittest.main()
