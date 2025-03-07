from app.main import main

def test_main_function():
    # Assuming the main function returns a value
    expected_value = "Hello, World!"  # Example expected output
    result = main()
    assert result == expected_value
