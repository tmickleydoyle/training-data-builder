# Code Analysis and Training Data Generator

A Python tool that analyzes code files, extracts meaningful components, and generates training data using the Qwen 2.5 Coder language model.

## Overview

This project provides a framework for:
- Recursively scanning directories for code files
- Parsing code using Tree-sitter
- Extracting functions and classes from the code
- Generating questions and summaries about the code using LLM

## Prerequisites

- Python 3.x
- Ollama with qwen2.5-coder:7b model installed
- Tree-sitter Python bindings

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>

2. Install the required dependencies:


```shellscript
pip install tree-sitter ollama
```

3. Ensure you have Ollama running with the qwen2.5-coder:7b model:


```shellscript
ollama run qwen2.5-coder:7b
```

## Configuration

The project configuration is stored in `config.py`. Key settings include:

- `DIRECTORY`: The root directory to search for code files
- `INCLUDED_EXTENSIONS`: File extensions to process (currently set to `.py`)
- `EXTENSION_MAP`: Mapping of file extensions to programming languages


## Usage

Run the main script to process code files and generate training data:

```shellscript
python main.py
```

## Project Structure

- `main.py`: Entry point of the application
- `config.py`: Configuration settings and constants
- `code_loader.py`: Code file loading and parsing functionality
- `language_extensions.py`: Language detection utilities
- `build_training_data.py`: Training data generation using LLM


## Features

### Code Loading

- Recursive directory scanning
- Support for multiple programming languages
- Tree-sitter parsing for accurate code analysis


### Training Data Generation

- LLM-powered question generation
- Code summary generation
