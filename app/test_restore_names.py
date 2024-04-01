import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("first_name, last_name, full_name, expected_first_name", [
    (None, "Holy", "Jack Holy", "Jack"),  # Test when first_name is None
    ("", "Adams", "Mike Adams", ""),  # Test when first_name is an empty string
    ("John", "Doe", "John Doe", "John"),  # Test when first_name is already set
])
def test_restore_names(
        first_name,
        last_name,
        full_name,
        expected_first_name) -> None:
    users = \
        [{
            "first_name": first_name,
            "last_name": last_name,
            "full_name": full_name
        }]
    restore_names(users)
    assert users[0]["first_name"] == expected_first_name
