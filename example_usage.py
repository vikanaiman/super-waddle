#!/usr/bin/env python3
"""
Примеры использования md_prompt_escape в коде.
"""

from md_prompt_escape import markdown_to_singleline, escape_for_python


def example_1_basic_usage():
    """Базовое использование."""
    markdown_text = """# Hello
    
This is a **markdown** text with "quotes"."""
    
    escaped = markdown_to_singleline(markdown_text)
    print("Example 1 - Basic usage:")
    print(escaped)
    print()


def example_2_api_request():
    """Пример для API запроса."""
    prompt = """You are a helpful AI assistant.

Please answer the following question:
- Be concise
- Be accurate

Question: "What is Python?"
"""
    
    escaped_prompt = markdown_to_singleline(prompt)
    
    print("Example 2 - API Request:")
    print("# Вставьте это в ваш Python код:")
    print(f"api_request = {{'prompt': {escaped_prompt}}}")
    print()
    
    import json
    request_data = {
        'prompt': eval(escaped_prompt),
        'max_tokens': 100
    }
    print("# JSON для отправки:")
    print(json.dumps(request_data, indent=2, ensure_ascii=False))
    print()


def example_3_different_quote_styles():
    """Примеры с разными стилями кавычек."""
    text = "Line 1\nLine 2"
    
    print("Example 3 - Different quote styles:")
    print(f"Double quotes: {markdown_to_singleline(text, 'double')}")
    print(f"Single quotes: {markdown_to_singleline(text, 'single')}")
    print(f"Triple quotes: {markdown_to_singleline(text, 'triple')}")
    print()


def example_4_code_generation():
    """Генерация Python кода с промптом."""
    prompt_template = """Analyze this code:
```python
{code}
```

Provide feedback on:
1. Code style
2. Performance
3. Security"""
    
    code_sample = """def process_data(data):
    return [x * 2 for x in data]"""
    
    final_prompt = prompt_template.format(code=code_sample)
    escaped = markdown_to_singleline(final_prompt)
    
    print("Example 4 - Generated Python code:")
    print(f"PROMPT = {escaped}")
    print()


def example_5_openai_style():
    """Пример в стиле OpenAI API."""
    system_prompt = """You are a code review assistant.
Focus on:
- Code quality
- Best practices
- Security"""
    
    user_prompt = """Review this function:
```python
def login(user, pwd):
    if user == "admin" and pwd == "123":
        return True
```"""
    
    print("Example 5 - OpenAI style:")
    print("messages = [")
    print(f"    {{'role': 'system', 'content': {markdown_to_singleline(system_prompt)}}},")
    print(f"    {{'role': 'user', 'content': {markdown_to_singleline(user_prompt)}}}")
    print("]")
    print()


if __name__ == '__main__':
    example_1_basic_usage()
    example_2_api_request()
    example_3_different_quote_styles()
    example_4_code_generation()
    example_5_openai_style()
