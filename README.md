# Markdown Prompt Escape для Python

Утилита для преобразования markdown-текста (промптов) в экранированную однострочную строку для безопасной вставки в Python-код при отправке в API.

## Описание

При работе с API (OpenAI, Anthropic, и др.) часто нужно передавать большие промпты в формате markdown. Эта утилита помогает:
- Преобразовать многострочный markdown в одну строку
- Экранировать все специальные символы (кавычки, слеши, переводы строк)
- Подготовить текст для безопасной вставки в Python-код

## Установка

```bash
git clone <repository>
cd <repository>
chmod +x md_prompt_escape.py
```

Опционально (для копирования в буфер обмена):
```bash
pip install pyperclip
```

## Использование

### CLI (командная строка)

#### Из файла:
```bash
python md_prompt_escape.py -f example_prompt.md
```

#### Из stdin:
```bash
echo "# Hello\nWorld" | python md_prompt_escape.py
```

#### С выбором стиля кавычек:
```bash
python md_prompt_escape.py -f prompt.md -q single   # одинарные кавычки
python md_prompt_escape.py -f prompt.md -q double   # двойные (по умолчанию)
python md_prompt_escape.py -f prompt.md -q triple   # тройные (для многострочных)
```

#### Вывод как переменной Python:
```bash
python md_prompt_escape.py -f prompt.md -v system_prompt
# Вывод: system_prompt = "escaped text..."
```

#### Копирование в буфер обмена:
```bash
python md_prompt_escape.py -f prompt.md -v prompt -c
```

### В Python коде

```python
from md_prompt_escape import markdown_to_singleline, escape_for_python

# Базовое использование
markdown_text = """# Title
Some **bold** text with "quotes"
"""

escaped = markdown_to_singleline(markdown_text)
print(escaped)
# Вывод: "# Title\nSome **bold** text with \"quotes\"\n"

# Для API запроса
prompt = markdown_to_singleline(markdown_text)
api_request = {
    'messages': [
        {'role': 'system', 'content': eval(prompt)}
    ]
}
```

## Примеры

### Пример 1: Простой промпт

Входной файл `prompt.md`:
```markdown
# System Prompt

You are a helpful assistant.
Be "accurate" and concise.
```

Команда:
```bash
python md_prompt_escape.py -f prompt.md -v PROMPT
```

Результат:
```python
PROMPT = "# System Prompt\n\nYou are a helpful assistant.\nBe \"accurate\" and concise.\n"
```

### Пример 2: OpenAI API

```python
from md_prompt_escape import markdown_to_singleline

system_prompt = """You are an expert code reviewer.

Focus on:
1. Security
2. Performance
3. Best practices"""

user_prompt = """Review this code:
```python
def unsafe_function(user_input):
    eval(user_input)
```"""

messages = [
    {'role': 'system', 'content': eval(markdown_to_singleline(system_prompt))},
    {'role': 'user', 'content': eval(markdown_to_singleline(user_prompt))}
]

# Отправка в API
# response = openai.ChatCompletion.create(model="gpt-4", messages=messages)
```

### Пример 3: Anthropic Claude API

```python
from md_prompt_escape import markdown_to_singleline

prompt = """Analyze the following:

<document>
Important text with "quotes" and special chars: \\ / \n
</document>

Provide a summary."""

escaped_prompt = eval(markdown_to_singleline(prompt))

# request_data = {
#     "model": "claude-3",
#     "messages": [{"role": "user", "content": escaped_prompt}]
# }
```

## Запуск тестов

```bash
python test_md_prompt_escape.py
```

Или с более подробным выводом:
```bash
python test_md_prompt_escape.py -v
```

## Запуск примеров

```bash
python example_usage.py
```

## Функции

### `escape_for_python(text: str) -> str`

Экранирует специальные символы для Python строк:
- `\` → `\\`
- `"` → `\"`
- `'` → `\'`
- `\n` → `\\n`
- `\r` → `\\r`
- `\t` → `\\t`

### `markdown_to_singleline(markdown_text: str, quote_style: str = 'double') -> str`

Преобразует markdown в экранированную строку с кавычками.

Параметры:
- `markdown_text`: исходный текст
- `quote_style`: `'double'`, `'single'`, или `'triple'`

Возвращает готовую строку для вставки в Python код.

## CLI опции

```
-f, --file FILE          Путь к файлу с markdown
-q, --quote-style STYLE  Стиль кавычек: double, single, triple
-v, --variable NAME      Имя переменной для вывода
-c, --copy              Копировать в буфер обмена
-h, --help              Показать справку
```

## Особенности

- ✅ Корректное экранирование всех специальных символов Python
- ✅ Поддержка различных стилей кавычек
- ✅ Работа с stdin и файлами
- ✅ Генерация готовых Python переменных
- ✅ Опциональное копирование в буфер обмена
- ✅ Поддержка Unicode и emoji
- ✅ Полное покрытие тестами

## Лицензия

MIT

## Автор

Created with cto.new
