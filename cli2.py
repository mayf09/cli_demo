import builtins

import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--count', default=1, type=int, help='次数')
@click.argument('name')
def hello(name, count=1):
    for x in range(count):
        print('Hello %s!' % name)


@cli.command()
@click.argument('func', nargs=1)
@click.argument('args', type=int, nargs=-1)
def cal(func, args):
    if func in ['sum', 'max', 'min']:
        f = getattr(builtins, func)
        print('{} = {}'.format(func, f(args)))
    else:
        raise ValueError('func_name error')


if __name__ == '__main__':
    cli()
