import App.App as App
from os import sep as os_seperator


def main():
    try:
        (App.App()).run()
    except Exception as e:
        print("An Error occurred:", str(e), sep=os_seperator)


if __name__ == "__main__":
    main()
