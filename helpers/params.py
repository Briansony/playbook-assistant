import argparse

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help='commands')

# A create command
create_parser = subparsers.add_parser('create', help='Create playbook')
create_parser.add_argument('-t', '--task', choices=('create', 'add'), required=True, help='Task name')
create_parser.add_argument('-m', '--mode', choices=('full', 'default'), help='Mode of playbook')
create_parser.add_argument('-r', '--roles', nargs='+', required=True, help='List of roles')
create_parser.add_argument('-n', '--name', action='store', required=True, help='Name of playbook')
create_parser.add_argument('-p', '--path', action='store', required=True, help='Path where playbooks are stored')
create_parser.add_argument('-w', '--without_inventory', action='store_true', default=False, help='Whether use inventory')

add_parser = subparsers.add_parser('add', help='Add role to playbook')
create_parser.add_argument('-t', '--task', choices=('create', 'add'), required=True, help='Task name')
add_parser.add_argument('-n', '--name', action='store', required=True, help='Name of playbook')
create_parser.add_argument('-r', '--roles', nargs='+', required=True, help='List of roles')

args = parser.parse_args()
print(args)
print(vars(args))
