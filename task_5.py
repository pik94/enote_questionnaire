import argparse
from typing import NoReturn

from task_5 import Node, LinkedList
from task_5.utils import generate_fibonacci


def main(args: argparse.Namespace) -> NoReturn:
    n = args.number
    numbers = [Node(value=value) for value in generate_fibonacci(n)]
    linked_list = LinkedList(nodes=numbers)
    linked_list.reverse()
    print(linked_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',
                        '--number',
                        type=int,
                        default=100,
                        help='The first N numbers of Fibonacci to generate.')
    args = parser.parse_args()
    main(args)
