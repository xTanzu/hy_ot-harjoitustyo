from invoke import task
import platform

@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    if platform.system() == 'Linux':
        if 'Microsoft' in platform.release():
            ctx.run("python.exe src/index.py")
        else:
            ctx.run("python3 src/index.py")
    elif platform.system() == 'Windows':
        ctx.run("python src/index.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage report -m")

@task
def coverage_html_report(ctx):
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")