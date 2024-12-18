from code_loader import load_code_files
from build_training_data import build_training_data
from config import DIRECTORY


def main():
    """
    Run the training data builder.
    """
    code = load_code_files(DIRECTORY)
    build_training_data(code, verbose=True)


if __name__ == "__main__":
    main()
