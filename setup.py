#!/usr/bin/env python3
"""
Setup script for md-prompt-escape package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="md-prompt-escape",
    version="1.0.0",
    author="CTO.new",
    description="Утилита для преобразования markdown-текста в экранированную однострочную строку для Python API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/md-prompt-escape",
    py_modules=["md_prompt_escape"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: Markdown",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "clipboard": ["pyperclip>=1.8.0"],
    },
    entry_points={
        "console_scripts": [
            "md-prompt-escape=md_prompt_escape:main",
        ],
    },
)
