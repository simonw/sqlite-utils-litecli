import sqlite_utils
from litecli.main import cli as litecli_cli
from litecli.main import LiteCli


original_connect = LiteCli.connect


def new_connect_method(self, *args, **kwargs):
    result = original_connect(self, *args, **kwargs)

    # Run connection plugins
    if self.sqlexecute.conn is not None:
        sqlite_utils.Database(self.sqlexecute.conn)

    return result


# Apply monkey patch
LiteCli.connect = new_connect_method


@sqlite_utils.hookimpl
def register_commands(cli):
    cli.add_command(litecli_cli, name="litecli")
