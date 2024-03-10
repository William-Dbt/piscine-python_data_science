import os


def main():
    """
    Create source distribution of package
    Install package from source distribution
    Print package version
    """
    # Creating source distribution
    os.system("python3 setup.py sdist bdist_wheel")

    # Install the package
    print("--------------------")
    os.system("pip install ./dist/ft_package-0.0.1.tar.gz")

    # Show version
    print("--------------------")
    os.system("pip show -v ft_package")


if __name__ == "__main__":
    main()
