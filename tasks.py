import os
import sys

from invoke import task

from utils.utils import new_solution, sort_katas


@task
def check_venv(ctx):
    """Checks if virtualenv is active"""
    # Is pyenv active?
    pyenv = os.environ.get('PYENV_VIRTUAL_ENV', False)

    # Is virtualenv on linux active?
    virtualenv_unix = hasattr(sys, 'real_prefix')

    # Is virtualenv on unix active?
    virtualenv_windows = sys.base_prefix != sys.exec_prefix

    # ToDo: Check if unix venv check can be removed
    if not any([pyenv, virtualenv_unix, virtualenv_windows]):
        raise EnvironmentError('Activate virtual environment before!')


@task(check_venv)
def update(ctx):
    """Updates virtual environments"""
    python = '~/.pyenv/versions/codewars/bin'

    ctx.run('pur -r requirements.txt')
    ctx.run('{}/pip install -r requirements.txt'.format(python))


@task(check_venv)
def sort(ctx):
    """Sorts kata"""
    sort_katas()


@task(check_venv)
def new(ctx, slug):
    new_solution(slug)


@task(check_venv)
def test(ctx):
    ctx.run('python -m pytest --doctest-modules solutions tests')


@task(check_venv)
def syntax(ctx):
    ctx.run('python -m pylint solutions tests')
