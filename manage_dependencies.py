import os
import sys
import subprocess
import platform

def install_requirements(os_type):
    filename = 'u_requirements.txt' if os_type == 'Linux' else 'w_requirements.txt'
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', filename])
        print(f'Successfully installed packages from {filename}')
    except subprocess.CalledProcessError:
        print(f'Failed to install packages from {filename}')

def append_requirement(os_type, package_name):
    filename = 'u_requirements.txt' if os_type == 'Linux' else 'w_requirements.txt'
    with open(filename, 'a') as file:
        file.write(f'{package_name}\n')
    print(f'Added "{package_name}" to {filename}')

def freeze_requirements(os_type):
    filename = 'u_requirements.txt' if os_type == 'Linux' else 'w_requirements.txt'
    try:
        with open(filename, 'a') as file:
            subprocess.check_call([sys.executable, '-m', 'pip', 'freeze'], stdout=file)
        print(f'Successfully appended current environment packages to {filename}')
    except subprocess.CalledProcessError:
        print(f'Failed to append packages to {filename}')

if __name__ == '__main__':
    os_type = platform.system()

    if len(sys.argv) < 2:
        print('Usage: python manage_dependencies.py [install|append|freeze] [package_name (optional for append)]')
        sys.exit(1)

    action = sys.argv[1]
    package_name = sys.argv[2] if len(sys.argv) > 2 and action == 'append' else None

    if action == 'install':
        install_requirements(os_type)
    elif action == 'append' and package_name:
        append_requirement(os_type, package_name)
    elif action == 'freeze':
        freeze_requirements(os_type)
    else:
        print('Invalid usage or missing package name for append action.')
