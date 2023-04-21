import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# from dotenv import load_dotenv

# load_dotenv()


# handler.py
def handle(event, context):
   print("evento recebido: " + str(event))
   a = event["a"]
   b = event["b"]
   resultado = a + b
   return { "resultado": resultado }

if __name__ == "__main__":
    resultado = handle({"a": 1, "b": 2}, None)
    print("Resultado: " + str(resultado))