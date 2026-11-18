import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def test_with_mkdocs():
    # dependency versions come from the environment; see noxfile.py
    with tempfile.TemporaryDirectory() as temp:
        shutil.copytree(
            Path(__file__).parent.joinpath("fixtures", "input"),
            temp,
            dirs_exist_ok=True,
        )

        run_mkdocs_build = subprocess.run(
            [sys.executable, "-m", "mkdocs", "build"],
            cwd=temp,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        assert run_mkdocs_build.returncode == 0

        assert (
            "mkdocs_plantuml_local: Rendering diagram 1 of page index.md"
            in run_mkdocs_build.stderr.decode("utf-8")
        )
        assert (
            "mkdocs_plantuml_local: Handled diagram 1 of page index.md in"
            in run_mkdocs_build.stderr.decode("utf-8")
        )
        assert "Documentation built" in run_mkdocs_build.stderr.decode("utf-8")

        created_cache_files = [
            str(f).replace(temp, "")
            for f in Path(temp).joinpath(".cache").glob("**/*")
            if f.is_file()
        ]

        assert (
            created_cache_files[0] == "/.cache/plantuml_local"
            "/c50fzkyTHubJdpR5b14l0iPPBTr4D14x1VvJ4ZvaP1Q"
            "/pIdGyucMROfhBbWUqtM43dEFyTwctEWkC6aqt4W6aeU"
            "/eHgNvJ3T-j3rtNN_mHPX0Ssqxc8c0iouXWbWVb9anDk"
        )
