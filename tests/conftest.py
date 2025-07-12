import pytest

@pytest.fixture
def set_up():
    print("Начало теста")
    yield
    print("Конец теста")