from pytest import fixture, raises
from tempfile import mkdtemp
from shutil import rmtree
from os import path,chdir
from renamebyreplace.core import renamebyreplace, main

@fixture
def test_fs(monkeypatch):
    """Set up a temporary directory with a file structure for each test and changes into it."""
    # Suppress print output for all tests using this fixture
    monkeypatch.setattr('builtins.print', lambda *args, **kwargs: None)
    test_dir = mkdtemp()
    monkeypatch.chdir(test_dir)
    # Create a structure inside the temp directory
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

def test_renamebyreplace(test_fs):
    renamebyreplace("a", "b", True, False)
    assert path.exists(test_fs["b"])
    assert not path.exists(test_fs["a"])

def test_main_with_no_args(monkeypatch):
    """Test that main exits when no arguments are provided."""
    # Prevent sys.argv from being used by argparse
    monkeypatch.setattr('sys.argv', ['renamebyreplace'])
    with raises(SystemExit) as e:
        main()
    assert e.type == SystemExit
    assert e.value.code == 2

def test_main_with_args(monkeypatch, test_fs):
    """Test that main exits when no arguments are provided."""
    # Prevent sys.argv from being used by argparse"
    monkeypatch.setattr('sys.argv', ['renamebyreplace', "--search", "a", "--replace", "b", "--write"])
    main()
    assert path.exists(test_fs["b"])
    assert not path.exists(test_fs["a"])
