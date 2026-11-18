import nox

nox.options.sessions = ["integration"]


@nox.session(python=["3.9", "3.10", "3.11", "3.12"])
@nox.parametrize("mkdocs", ["1.5.0", "1.5.3", "1.6.1"])
# "latest" means the newest release pip can install next to that mkdocs and python
@nox.parametrize("pymdown", ["10.7", "latest"])
def integration(session, mkdocs, pymdown):
    pymdown_spec = "pymdown-extensions" if pymdown == "latest" else f"pymdown-extensions=={pymdown}"
    session.install(".", "pytest", f"mkdocs=={mkdocs}", pymdown_spec)
    session.run("pip", "check")
    session.run("pytest", "test/integration", *session.posargs)
