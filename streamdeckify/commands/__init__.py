from ..common import Manager
from .inspect import inspect  # noqa: F401
from .make_dirs import make_dirs  # noqa: F401
from .run import run  # noqa: F401
from .api import *  # noqa: F401, F403
from .brightness import brightness  # noqa: F401

from .base import cli


def main():
    try:
        cli()
    except SystemExit as exc:
        Manager.exit(exc.code)
    except Exception:
        Manager.exit(1, 'Oops...', log_exception=True)
    else:
        Manager.exit(0)
