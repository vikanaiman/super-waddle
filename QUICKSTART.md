# Быстрый старт

## Установка

```bash
git clone <repository>
cd <repository>
```

## Использование за 30 секунд

### 1. Базовый пример

Создайте файл `my_prompt.md`:
```markdown
# Instructions

You are a helpful AI assistant.
Please answer with "precision" and clarity.
```

Преобразуйте в Python строку:
```bash
python md_prompt_escape.py -f my_prompt.md -v PROMPT
```

Результат:
```python
PROMPT = "# Instructions\n\nYou are a helpful AI assistant.\nPlease answer with \"precision\" and clarity.\n"
```

### 2. Использование в коде

```python
from md_prompt_escape import markdown_to_singleline

# Ваш промпт
prompt = """Analyze this code:
```python
def hello():
    print("Hello, World!")
```"""

# Преобразование
escaped = markdown_to_singleline(prompt)

# Использование в API
import requests
response = requests.post(
    'https://api.example.com/chat',
    json={'message': eval(escaped)}
)
```

### 3. Из командной строки

```bash
# Из файла
python md_prompt_escape.py -f prompt.md

# Из stdin
echo "# Hello\nWorld" | python md_prompt_escape.py

# С разными стилями кавычек
python md_prompt_escape.py -f prompt.md -q single
python md_prompt_escape.py -f prompt.md -q triple

# Сразу как переменная
python md_prompt_escape.py -f prompt.md -v system_prompt
```

## Примеры использования

### OpenAI API
```python
from md_prompt_escape import markdown_to_singleline

system = "You are an expert coder."
user = "Write a hello world in Python"

messages = [
    {'role': 'system', 'content': eval(markdown_to_singleline(system))},
    {'role': 'user', 'content': eval(markdown_to_singleline(user))}
]

# Отправить в OpenAI API
```

### Anthropic Claude API
```python
from md_prompt_escape import markdown_to_singleline

prompt = """Analyze this text: "Hello World"
Provide insights."""

escaped_prompt = eval(markdown_to_singleline(prompt))

# Отправить в Claude API
```

## Зачем это нужно?

При работе с AI API часто нужно:
- ✅ Вставлять многострочные промпты в Python код
- ✅ Экранировать специальные символы (кавычки, слеши)
- ✅ Безопасно передавать текст в JSON

Эта утилита автоматизирует всё это!

## Что дальше?

Смотрите:
- `README.md` - полная документация
- `example_usage.py` - примеры в коде
- `demo_api_usage.py` - реальные примеры для API
- `test_md_prompt_escape.py` - тесты

## Запуск примеров

```bash
# Все примеры
python example_usage.py

# API примеры
python demo_api_usage.py

# Тесты
python test_md_prompt_escape.py
```
