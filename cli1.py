import builtins
import sys


def hello(name, count=1):
    for x in range(count):
        print('Hello %s!' % name)


def cal(func, args):
    if func in ['sum', 'max', 'min']:
        f = getattr(builtins, func)
        print('{} = {}'.format(func, f(args)))
    else:
        raise ValueError('func_name error')


def parse(argv):
    # print(len(argv))
    opts, args = {}, []
    i = 2  # 从 argv[2] 开始
    length = len(argv)
    while i < length:
        if argv[i].startswith('-'):
            opts[argv[i]] = argv[i+1]
            i += 2
        else:
            args.append(argv[i])
            i += 1
    # print(opts, args)
    return opts, args


def handle(argv):
    opts, args = parse(argv)
    sub_command = argv[1]
    if sub_command == 'hello':
        name = args[0]
        count = int(opts.get('--count', 1))
        hello(name, count)
    elif sub_command == 'cal':
        func = args.pop(0)
        args = [int(arg) for arg in args]
        cal(func, args)
    else:
        raise TypeError('sub_command error.')


if __name__ == '__main__':
    handle(sys.argv)
