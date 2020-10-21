
import sys
import os


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SquirrelProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Make sure Django is installed and available on your environment."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
