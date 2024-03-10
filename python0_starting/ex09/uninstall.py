import os


def main():
    """
    Remove all files and folders from package installation
    Call pip uninstall command to uninstall package
    """
    os.system("rm -rf build dist ft_package.egg* ft_package/__pycache__")
    os.system("pip uninstall -y ft_package")


if __name__ == "__main__":
    main()
