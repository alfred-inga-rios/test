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


def make_whale_sound(intensity=1):
    """
    Generate a whale sound based on intensity level.

    Args:
        intensity (int): Sound intensity from 1-3. Default is 1.

    Returns:
        str: A whale sound of varying length
    """
    if not 1 <= intensity <= 3:
        raise ValueError("Intensity must be between 1 and 3")
    return "O" * intensity + "ooo" * intensity
