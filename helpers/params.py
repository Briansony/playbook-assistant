import argparse

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help='commands')

# A create command
create_parser = subparsers.add_parser('create', help='Create playbook')
create_parser.add_argument('-m', '--mode', choices=('full', 'default'), help='Mode of playbook')
create_parser.add_argument('-r', '--roles', nargs='+', required=True, help='List of roles')
create_parser.add_argument('-n', '--name', action='store', required=True, help='Name of playbook')
create_parser.add_argument('-w', '--without_inventory', action='store_true', default=False, help='Whether use inventory')

# def params_parse():
#
#     args = parser.parse_args()
#     if args.without_inventory is None:
#         args.mode = 'default'

args = parser.parse_args()
print(args)