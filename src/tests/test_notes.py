"""
import tempfile

import pytest


class C:
    def f(self):
        return 1

    def g(self):
        return 2


@pytest.fixture
def c_instance():
    return C()


@pytest.fixture
def tempory_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture  # scope is defined in there args.
def setup_teardown(autouse=True, scope="session"):
    print("setup")
    yield
    print("teardown")


@pytest.fixture(name="fix")  # this renames the fixures which is called below.
def ksdjfkdsjkfjd():
    return 5


# -----------
@pytest.fixture(params=(1, 2, 3, 4))
def an_int(request):  # this sets up a forloop that will add 1 onto each of the params
    # the params are brought into the function from the fixutre using the request thing.
    yield request.param + 2


def test_int(an_int):
    print(f"get {an_int=}")


# --------------
def test_with_setup_teardown(fix):  # this lets you
    # pullin a whole fixture to do some actions. this hleps with setting up specific conditions.

    print(f"in test{fix=}")


def test_f(c_instance):
    c = C()
    assert c.f() == 1


@pytest.mark.usefixtures(
    "setup_teardown"
)  # this is for if you don't need a specific value form a pytest.
# it is a way of avoiceing having to add the argument in to the test_g.
def test_g(c_instance, tempory_dir):
    print(tempory_dir)
    assert c_instance.g() == 2
"""
