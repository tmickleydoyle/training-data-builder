from tree_sitter import Language, Parser
import tree_sitter_python as tspython

# Configuration Variables
DIRECTORY = "/Users/thomasmickley-doyle/repos/language_model"  # Directory to search for code snippets
INCLUDED_EXTENSIONS = (".py",)  # File extensions to include in the search

# Correct initialization of the Language object
PYTHON_LANGUAGE = Language(tspython.language())

# Initialize the parser
parser = Parser(PYTHON_LANGUAGE)

LANGUAGE_PARSERS = {
    ".py": parser,
}

# Language extension map
EXTENSION_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".c": "C",
    ".cpp": "C++",
    ".h": "C/C++ Header",
    ".cs": "C#",
    ".rb": "Ruby",
    ".php": "PHP",
    ".go": "Go",
    ".swift": "Swift",
    ".kt": "Kotlin",
    ".rs": "Rust",
    ".sh": "Shell Script",
    ".bat": "Batch File",
    ".html": "HTML",
    ".css": "CSS",
    ".scss": "SCSS",
    ".xml": "XML",
    ".json": "JSON",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".sql": "SQL",
    ".r": "R",
    ".pl": "Perl",
    ".lua": "Lua",
    ".dart": "Dart",
    ".jsx": "JavaScript (React)",
    ".tsx": "TypeScript (React)",
    ".md": "Markdown",
    ".tex": "LaTeX",
    ".makefile": "Makefile",
    ".dockerfile": "Dockerfile",
    ".toml": "TOML",
    ".ini": "INI",
    ".cfg": "Configuration File",
}
