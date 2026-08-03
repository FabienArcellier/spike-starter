import alfred


@alfred.command("install", help="install python dependencies")
def install():
    poetry = alfred.sh("poetry", "poetry is missing")
    alfred.run(poetry, ["install"])


@alfred.command("dist", help="build distribution archives")
def dist():
    poetry = alfred.sh("poetry", "poetry is missing")
    alfred.run(poetry, ["build"])
    python = alfred.sh("python", "python is missing")
    alfred.run(python, ["-u", "-m", "unittest", "discover", "tests/check"])


@alfred.command(
    "deploy_current_version",
    help="tag and push the current spike-starter version to trigger deployment",
)
def deploy_current_version():
    alfred.invoke_command("install")
    python = alfred.sh("python", "python is missing")
    alfred.run(python, ["scripts/deploy_current_version.py"])


@alfred.command("cd", help="run continuous deployment process on spike-starter")
def cd():
    alfred.invoke_command("dist")
    poetry = alfred.sh("poetry", "poetry is missing")
    alfred.run(poetry, ["publish"])
