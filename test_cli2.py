#!/usr/bin/env python3

from click.testing import CliRunner

from cli2 import cli


def test_cli_click():
    runner = CliRunner()
    result = runner.invoke(cli, ['hello', '--count', '3', 'abc'])
    assert result.exit_code == 0
    assert result.output == 'Hello abc!\nHello abc!\nHello abc!\n'


if __name__ == '__main__':
    test_cli_click()
