#!/usr/bin/env python3
"""
Визуальный тест для демонстрации работы утилиты.
"""

from md_prompt_escape import markdown_to_singleline, escape_for_python


def demo():
    """Демонстрация работы."""
    print("=" * 70)
    print("ДЕМОНСТРАЦИЯ: Преобразование Markdown в Python строку")
    print("=" * 70)
    print()
    
    # Пример 1: Простой текст
    print("📝 Пример 1: Простой markdown")
    print("-" * 70)
    
    md1 = """# Hello
World with "quotes" and 'apostrophes'"""
    
    print("ВХОД (markdown):")
    print(md1)
    print()
    print("ВЫХОД (Python строка):")
    print(markdown_to_singleline(md1))
    print()
    
    # Пример 2: Код в markdown
    print("📝 Пример 2: Markdown с кодом")
    print("-" * 70)
    
    md2 = """Analyze this code:
```python
def hello():
    print("Hello, World!")
```
Provide feedback."""
    
    print("ВХОД (markdown):")
    print(md2)
    print()
    print("ВЫХОД (Python строка):")
    print(markdown_to_singleline(md2))
    print()
    
    # Пример 3: Специальные символы
    print("📝 Пример 3: Специальные символы")
    print("-" * 70)
    
    md3 = r"""Path: C:\Users\Admin
Quote: "example"
Tab:	separated
Newline below:

End"""
    
    print("ВХОД (markdown):")
    print(md3)
    print()
    print("ВЫХОД (Python строка):")
    result = markdown_to_singleline(md3)
    print(result)
    print()
    
    # Пример 4: Использование в коде
    print("📝 Пример 4: Использование в Python коде")
    print("-" * 70)
    
    api_prompt = """You are a helpful assistant.
Answer with "precision"."""
    
    print("Ваш prompt:")
    print(api_prompt)
    print()
    print("Вставьте в код так:")
    print(f"prompt = {markdown_to_singleline(api_prompt)}")
    print()
    print("Или с eval():")
    escaped = markdown_to_singleline(api_prompt)
    print(f"prompt = eval({repr(escaped)})")
    print()
    print("Результат eval():")
    print(repr(eval(escaped)))
    print()
    
    print("=" * 70)
    print("✓ Готово! Теперь можно безопасно вставлять в Python код")
    print("=" * 70)


if __name__ == '__main__':
    demo()
