from Website_tests import website_app
from Mobile_tests import mobile_app
from sys import argv


def main():
    """Main function launching the tests."""
    if len(argv) > 1:
        if argv[1] == "web":
            website_app.run()
        elif argv[1] == "mobile":
            mobile_app.run()
        else:
            print("Please launch the script with 'web' or 'mobile' as a parameter")


if __name__ == '__main__':
    main()
