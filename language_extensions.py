from config import EXTENSION_MAP


def infer_language(file_name: str):
    """
    Infers the programming language based on the file extension.

    Args:
        file_name (str): The name of the file with its extension.

    Returns:
        str: The inferred programming language or 'Unknown' if not recognized.
    """
    # Extract the extension from the file name
    extension = "." + file_name.split(".")[-1].lower() if "." in file_name else ""

    # Handle special cases for files with no standard extensions
    special_cases = {"makefile": "Makefile", "dockerfile": "Dockerfile"}

    # Check for special cases first
    base_name = file_name.lower()
    if base_name in special_cases:
        return special_cases[base_name]

    # Lookup the extension in the map
    return EXTENSION_MAP.get(extension, "Unknown")
