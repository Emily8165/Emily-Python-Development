import pytest


@pytest.fixture
def db_access(django_db_blocker):
    with django_db_blocker.unblock():
        pass
