import nox

nox.options.sessions = ["integration"]


@nox.session(python=["3.11", "3.12", "3.13", "3.14", "3.15"])
@nox.parametrize("mkdocs", ["1.5.0", "1.5.3", "1.6.1"])
# "latest" means the newest release pip can install next to that mkdocs and python
@nox.parametrize("pymdown", ["10.7", "latest"])
def integration(session, mkdocs, pymdown):
    pymdown_spec = (
        "pymdown-extensions"
        if pymdown == "latest"
        else f"pymdown-extensions=={pymdown}"
    )
    session.install(".", "pytest", f"mkdocs=={mkdocs}", pymdown_spec)
    session.run("pip", "check")
    session.run("pytest", "test/integration", *session.posargs)
