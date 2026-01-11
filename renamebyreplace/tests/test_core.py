from pytest import fixture
from tempfile import mkdtemp
from shutil import rmtree
from os import path,chdir

# It's good practice to make the test runner find the modules.
# This assumes you run pytest or unittest from the project root.
from renamebyreplace.core import renamebyreplace



@fixture
def test_fs(monkeypatch):
    """Set up a temporary directory with a file structure for each test."""
    # Suppress print output for all tests using this fixture
    monkeypatch.setattr('builtins.print', lambda *args, **kwargs: None)

    test_dir = mkdtemp()

    chdir(test_dir)
    # Create a structure inside the temp directory
    # test_dir/
    # ├── file1.txt
    # ├── empty_dir/
    # └── sub_dir/
    #     ├── file2.txt
    #     └── deep_empty_dir/
    fs = {
        "test_dir": test_dir,
        "a": path.join(test_dir, "file a.txt"),
        "b": path.join(test_dir, "file b.txt"),
        "c": path.join(test_dir, "file c.txt"),
    }

    create_file(fs["a"])
    create_file(fs["b"])
    create_file(fs["c"])



    yield fs

    # Teardown: remove the temporary directory
    rmtree(test_dir)

def create_file(name):
    with open(name, "w") as f:
        f.write(name)

def test_renamebyreplace():
    chdir(test_fs["test_dir"])
    renamebyreplace("a", "b", True, False)
    assert path.exists("b")
    assert not path.exists("a")