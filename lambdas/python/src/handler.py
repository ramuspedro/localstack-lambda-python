import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv

load_dotenv()


def handler():
    print("\n ***** CHEGAMOS ATEH AQUI ***** \n")