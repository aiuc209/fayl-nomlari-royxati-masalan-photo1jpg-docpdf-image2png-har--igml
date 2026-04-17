import pytest

def get_extensions(file_names):
    return [file_name.split('.')[-1] for file_name in file_names]

def test_get_extensions():
    file_names = ["photo1.jpg", "doc.pdf", "image2.png"]
    expected_extensions = ["jpg", "pdf", "png"]
    assert get_extensions(file_names) == expected_extensions

def test_get_extensions_empty_list():
    file_names = []
    expected_extensions = []
    assert get_extensions(file_names) == expected_extensions

def test_get_extensions_no_extension():
    file_names = ["photo1", "doc", "image2"]
    expected_extensions = ["photo1", "doc", "image2"]
    assert get_extensions(file_names) == expected_extensions

def test_get_extensions_multiple_dots():
    file_names = ["photo1.jpg.png", "doc.pdf.txt", "image2"]
    expected_extensions = ["png", "txt", "image2"]
    assert get_extensions(file_names) == expected_extensions
