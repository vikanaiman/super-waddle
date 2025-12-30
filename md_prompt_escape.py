#!/usr/bin/env python3
"""
Утилита для преобразования markdown-текста в экранированную однострочную строку
для безопасной вставки в Python-код при отправке в API.
"""

import argparse
import sys
from typing import Optional


def escape_for_python(text: str) -> str:
    """
    Экранирует специальные символы для безопасной вставки в Python строку.
    
    Args:
        text: Исходный текст для экранирования
        
    Returns:
        Экранированная строка, готовая для вставки в Python код
    """
    escaped = text.replace('\\', '\\\\')
    escaped = escaped.replace('"', '\\"')
    escaped = escaped.replace("'", "\\'")
    escaped = escaped.replace('\n', '\\n')
    escaped = escaped.replace('\r', '\\r')
    escaped = escaped.replace('\t', '\\t')
    
    return escaped


def markdown_to_singleline(markdown_text: str, quote_style: str = 'double') -> str:
    """
    Преобразует markdown-текст в одну строку с экранированием для Python.
    
    Args:
        markdown_text: Исходный markdown-текст (может быть многострочным)
        quote_style: Стиль кавычек ('double', 'single', или 'triple')
        
    Returns:
        Строка, готовая для вставки в Python код
    """
    escaped_text = escape_for_python(markdown_text)
    
    if quote_style == 'double':
        return f'"{escaped_text}"'
    elif quote_style == 'single':
        return f"'{escaped_text}'"
    elif quote_style == 'triple':
        return f'"""{markdown_text}"""'
    else:
        raise ValueError(f"Неподдерживаемый стиль кавычек: {quote_style}")


def read_from_file(filepath: str) -> str:
    """
    Читает содержимое файла.
    
    Args:
        filepath: Путь к файлу
        
    Returns:
        Содержимое файла
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    """
    Главная функция CLI утилиты.
    """
    parser = argparse.ArgumentParser(
        description='Преобразует markdown-текст в экранированную однострочную строку для Python API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  # Из stdin
  echo "# Hello\\nWorld" | python md_prompt_escape.py
  
  # Из файла
  python md_prompt_escape.py -f prompt.md
  
  # С выбором стиля кавычек
  python md_prompt_escape.py -f prompt.md -q single
  
  # Вывод как готовой переменной Python
  python md_prompt_escape.py -f prompt.md -v prompt_text
        """
    )
    
    parser.add_argument(
        '-f', '--file',
        type=str,
        help='Путь к файлу с markdown-текстом'
    )
    
    parser.add_argument(
        '-q', '--quote-style',
        type=str,
        choices=['double', 'single', 'triple'],
        default='double',
        help='Стиль кавычек для обрамления строки (по умолчанию: double)'
    )
    
    parser.add_argument(
        '-v', '--variable',
        type=str,
        help='Имя переменной Python для вывода (например: prompt_text)'
    )
    
    parser.add_argument(
        '-c', '--copy',
        action='store_true',
        help='Попытаться скопировать результат в буфер обмена'
    )
    
    args = parser.parse_args()
    
    if args.file:
        try:
            markdown_text = read_from_file(args.file)
        except FileNotFoundError:
            print(f"Ошибка: Файл '{args.file}' не найден", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        if sys.stdin.isatty():
            print("Введите markdown-текст (Ctrl+D для завершения ввода):")
        markdown_text = sys.stdin.read()
    
    if not markdown_text:
        print("Ошибка: Пустой входной текст", file=sys.stderr)
        sys.exit(1)
    
    result = markdown_to_singleline(markdown_text, args.quote_style)
    
    if args.variable:
        output = f"{args.variable} = {result}"
    else:
        output = result
    
    print(output)
    
    if args.copy:
        try:
            import pyperclip
            pyperclip.copy(output)
            print("\n✓ Скопировано в буфер обмена", file=sys.stderr)
        except ImportError:
            print("\n⚠ Для копирования в буфер обмена установите: pip install pyperclip", file=sys.stderr)
        except Exception as e:
            print(f"\n⚠ Не удалось скопировать в буфер обмена: {e}", file=sys.stderr)


if __name__ == '__main__':
    main()
