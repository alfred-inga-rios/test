def to_whale_speak(text):
    """
    Convert text to whale language by removing all vowels.

    Args:
        text (str): The input text to convert

    Returns:
        str: Text with all vowels removed
    """
    vowels = set("aeiouAEIOU")
    return "".join(char for char in text if char not in vowels)
