from fixture.application import Application
import pytest

@pytest.fixture(scope="session") # создается 1 фикстура на все тесты
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture