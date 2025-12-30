#!/usr/bin/env python3
"""
Интеграционный тест для проверки всех функций утилиты.
"""

import sys
import subprocess
import tempfile
import os


def test_cli_with_file():
    """Тест CLI с файлом."""
    print("Test 1: CLI с файлом...", end=" ")
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write('# Test\nWith "quotes"')
        temp_file = f.name
    
    try:
        result = subprocess.run(
            ['python', 'md_prompt_escape.py', '-f', temp_file],
            capture_output=True,
            text=True,
            cwd='/home/engine/project'
        )
        
        if result.returncode == 0 and r'\"quotes\"' in result.stdout:
            print("✓ PASS")
            return True
        else:
            print("✗ FAIL")
            print(f"  Output: {result.stdout}")
            print(f"  Error: {result.stderr}")
            return False
    finally:
        os.unlink(temp_file)


def test_cli_with_stdin():
    """Тест CLI со stdin."""
    print("Test 2: CLI со stdin...", end=" ")
    
    result = subprocess.run(
        ['python', 'md_prompt_escape.py'],
        input='Hello\nWorld',
        capture_output=True,
        text=True,
        cwd='/home/engine/project'
    )
    
    if result.returncode == 0 and r'\n' in result.stdout:
        print("✓ PASS")
        return True
    else:
        print("✗ FAIL")
        print(f"  Output: {result.stdout}")
        return False


def test_cli_with_variable():
    """Тест CLI с выводом переменной."""
    print("Test 3: CLI с переменной...", end=" ")
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write('Test')
        temp_file = f.name
    
    try:
        result = subprocess.run(
            ['python', 'md_prompt_escape.py', '-f', temp_file, '-v', 'PROMPT'],
            capture_output=True,
            text=True,
            cwd='/home/engine/project'
        )
        
        if result.returncode == 0 and 'PROMPT = ' in result.stdout:
            print("✓ PASS")
            return True
        else:
            print("✗ FAIL")
            print(f"  Output: {result.stdout}")
            return False
    finally:
        os.unlink(temp_file)


def test_python_import():
    """Тест импорта в Python."""
    print("Test 4: Python импорт...", end=" ")
    
    try:
        from md_prompt_escape import escape_for_python, markdown_to_singleline
        
        test_text = 'Line 1\nLine 2 with "quotes"'
        escaped = escape_for_python(test_text)
        
        if r'\n' in escaped and r'\"' in escaped:
            print("✓ PASS")
            return True
        else:
            print("✗ FAIL")
            return False
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False


def test_different_quote_styles():
    """Тест различных стилей кавычек."""
    print("Test 5: Разные стили кавычек...", end=" ")
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write('Test')
        temp_file = f.name
    
    try:
        for style in ['double', 'single', 'triple']:
            result = subprocess.run(
                ['python', 'md_prompt_escape.py', '-f', temp_file, '-q', style],
                capture_output=True,
                text=True,
                cwd='/home/engine/project'
            )
            
            if result.returncode != 0:
                print(f"✗ FAIL (style={style})")
                return False
        
        print("✓ PASS")
        return True
    finally:
        os.unlink(temp_file)


def test_unit_tests():
    """Запуск unit тестов."""
    print("Test 6: Unit тесты...", end=" ")
    
    result = subprocess.run(
        ['python', 'test_md_prompt_escape.py'],
        capture_output=True,
        text=True,
        cwd='/home/engine/project'
    )
    
    if result.returncode == 0 and 'OK' in result.stderr:
        print("✓ PASS")
        return True
    else:
        print("✗ FAIL")
        print(f"  Output: {result.stdout}")
        print(f"  Error: {result.stderr}")
        return False


def test_special_characters():
    """Тест специальных символов."""
    print("Test 7: Специальные символы...", end=" ")
    
    try:
        from md_prompt_escape import escape_for_python
        
        test_cases = [
            ('\\', r'\\'),
            ('"', r'\"'),
            ("'", r"\'"),
            ('\n', r'\n'),
            ('\t', r'\t'),
        ]
        
        for input_char, expected in test_cases:
            result = escape_for_python(input_char)
            if expected not in result:
                print(f"✗ FAIL: {repr(input_char)} -> {repr(result)}, expected {repr(expected)}")
                return False
        
        print("✓ PASS")
        return True
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return False


def main():
    """Запуск всех тестов."""
    print("=" * 60)
    print("Интеграционное тестирование md_prompt_escape")
    print("=" * 60)
    print()
    
    tests = [
        test_cli_with_file,
        test_cli_with_stdin,
        test_cli_with_variable,
        test_python_import,
        test_different_quote_styles,
        test_unit_tests,
        test_special_characters,
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print()
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Результат: {passed}/{total} тестов прошли")
    
    if passed == total:
        print("✓ ВСЕ ТЕСТЫ ПРОШЛИ!")
        print("=" * 60)
        return 0
    else:
        print("✗ НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОШЛИ")
        print("=" * 60)
        return 1


if __name__ == '__main__':
    sys.exit(main())
