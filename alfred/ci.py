import alfred


@alfred.command("ci", help="run the project CI (lint + format + tests + dist)")
def ci():
    alfred.invoke_command("ci.lint")
    alfred.invoke_command("ci.format")
    alfred.invoke_command("ci.tests")
    alfred.invoke_command("dist")


@alfred.command("ci.lint", help="run static analysis on spike-starter")
@alfred.option("--fix", is_flag=True, default=False, help="apply ruff fixes")
def ci_lint(fix: bool):
    ruff = alfred.sh("ruff", "ruff is missing")
    args = ["check", "--config", "pyproject.toml", "src/spike_starter", "tests"]
    if fix:
        args.append("--fix")
    alfred.run(ruff, args)


@alfred.command("ci.format", help="check project formatting with ruff format")
@alfred.option(
    "--fix", is_flag=True, default=False, help="apply ruff formatting instead of checking"
)
def ci_format(fix: bool):
    ruff = alfred.sh("ruff", "ruff is missing")
    args = ["format", "."] if fix else ["format", "--check", "."]
    alfred.run(ruff, args)


@alfred.command("ci.tests", help="run automatic testing on spike-starter")
def ci_tests():
    alfred.invoke_command("ci.tests.unit")
    alfred.invoke_command("ci.tests.integration")


@alfred.command("ci.tests.unit", help="run only units testing on spike-starter")
def ci_tests_unit():
    python = alfred.sh("python", "python is missing")
    alfred.run(python, ["-u", "-m", "unittest", "discover", "tests/units"])


@alfred.command("ci.tests.integration", help="run only integrations testing on spike-starter")
def ci_tests_integration():
    python = alfred.sh("python", "python is missing")
    alfred.run(python, ["-u", "-m", "unittest", "discover", "tests/integrations"])
