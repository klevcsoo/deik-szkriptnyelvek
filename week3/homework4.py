import sys


def main():
    inp = input("Do you really want to quit [y/Y/yes]? ")
    if inp in ["y", "Y", "yes"]:  # <- egyszerűbben?
        print('bye')
        sys.exit(0)
    # for any other input:
    print('The show goes on...')


##############################################################################

if __name__ == "__main__":
    main()
