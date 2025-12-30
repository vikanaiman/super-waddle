#!/usr/bin/env python3
"""
Демонстрация использования утилиты для реальных API запросов.
Эти примеры показывают, как использовать экранированные промпты в реальном коде.
"""

from md_prompt_escape import markdown_to_singleline


def demo_openai_api():
    """Демонстрация для OpenAI API."""
    print("=" * 60)
    print("DEMO: OpenAI ChatGPT API")
    print("=" * 60)
    
    system_prompt = """You are an expert Python developer.
Your task is to review code and provide:
1. **Code quality** assessment
2. **Security** vulnerabilities
3. **Performance** improvements

Be thorough and "constructive"."""
    
    user_message = """Please review this code:

```python
import pickle
import os

def load_config(filename):
    with open(filename, 'rb') as f:
        config = pickle.load(f)
    return config

def process(data):
    result = eval(data)
    return result
```

Focus on security issues."""
    
    print("\n# Python код для отправки:")
    print("-" * 60)
    print("import openai\n")
    print("messages = [")
    print(f"    {{'role': 'system', 'content': {markdown_to_singleline(system_prompt)}}},")
    print(f"    {{'role': 'user', 'content': {markdown_to_singleline(user_message)}}}")
    print("]\n")
    print("# response = openai.ChatCompletion.create(")
    print("#     model='gpt-4',")
    print("#     messages=messages")
    print("# )")
    print()


def demo_anthropic_api():
    """Демонстрация для Anthropic Claude API."""
    print("=" * 60)
    print("DEMO: Anthropic Claude API")
    print("=" * 60)
    
    prompt = """Analyze the following document:

<document>
User authentication flow:
1. User enters credentials
2. System validates against DB
3. JWT token is generated with "secret_key_123"
4. Token is sent to client
</document>

Questions:
- Is this secure?
- What improvements do you suggest?
"""
    
    print("\n# Python код для отправки:")
    print("-" * 60)
    print("import anthropic\n")
    print(f"prompt = {markdown_to_singleline(prompt)}\n")
    print("# client = anthropic.Anthropic(api_key='your-api-key')")
    print("# message = client.messages.create(")
    print("#     model='claude-3-opus-20240229',")
    print("#     max_tokens=1024,")
    print("#     messages=[")
    print("#         {'role': 'user', 'content': prompt}")
    print("#     ]")
    print("# )")
    print()


def demo_custom_api():
    """Демонстрация для кастомного API."""
    print("=" * 60)
    print("DEMO: Кастомный API с requests")
    print("=" * 60)
    
    instruction = """Generate a summary of the text.

Requirements:
- Max 3 sentences
- Focus on main points
- Include "key insights"

Text: {{text}}
"""
    
    print("\n# Python код для отправки:")
    print("-" * 60)
    print("import requests\nimport json\n")
    print(f"INSTRUCTION_TEMPLATE = {markdown_to_singleline(instruction)}\n")
    print("text = 'Your long text here...'")
    print("instruction = INSTRUCTION_TEMPLATE.replace('{{text}}', text)\n")
    print("payload = {")
    print("    'instruction': instruction,")
    print("    'temperature': 0.7,")
    print("    'max_tokens': 200")
    print("}\n")
    print("# response = requests.post(")
    print("#     'https://api.example.com/v1/complete',")
    print("#     headers={'Authorization': 'Bearer YOUR_API_KEY'},")
    print("#     json=payload")
    print("# )")
    print()


def demo_multi_language():
    """Демонстрация с текстом на разных языках."""
    print("=" * 60)
    print("DEMO: Многоязычный промпт")
    print("=" * 60)
    
    multilang_prompt = """Ты профессиональный переводчик.

Task: Translate the following text from English to Russian.

Guidelines:
- Maintain the original tone and style
- Preserve technical terms when appropriate
- Be "accurate" and natural

Text to translate: {{input_text}}
"""
    
    print("\n# Python код:")
    print("-" * 60)
    print(f"TRANSLATION_PROMPT = {markdown_to_singleline(multilang_prompt)}\n")
    print("# Теперь можно использовать в любом API:")
    print("prompt = TRANSLATION_PROMPT.replace('{{input_text}}', user_text)")
    print()


def demo_json_serialization():
    """Демонстрация безопасной сериализации в JSON."""
    print("=" * 60)
    print("DEMO: JSON сериализация")
    print("=" * 60)
    
    prompt = """Classify the sentiment:

Text: "This product is amazing! Best purchase ever."

Options:
- Positive
- Negative  
- Neutral

Provide your answer in JSON format."""
    
    escaped = markdown_to_singleline(prompt)
    
    print("\n# Способ 1: С eval() - для быстрой вставки в код")
    print("-" * 60)
    print(f"prompt_str = {escaped}")
    print(f"content = eval(prompt_str)")
    print()
    
    print("\n# Способ 2: Прямое присваивание - безопаснее")
    print("-" * 60)
    import json
    prompt_actual = eval(escaped)
    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "user", "content": prompt_actual}
        ]
    }
    print(f"import json\n")
    print(f"data = {json.dumps(data, indent=4, ensure_ascii=False)}")
    print()


if __name__ == '__main__':
    demo_openai_api()
    demo_anthropic_api()
    demo_custom_api()
    demo_multi_language()
    demo_json_serialization()
    
    print("=" * 60)
    print("Все примеры показаны!")
    print("=" * 60)
