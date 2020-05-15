
import requests

def main():
    #accedemos a la URL de una página que nos devuelve una conversión
    res = requests.get("http://api.fixer.io/latest?base=USD&symbols=EUR")
    #Si la respuesta de la request es diferente a 200 (200 = OK) nos devuelve un mensaje de error.
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    #Le pedimos a pyton que nos devuelva la info en formato JSON.
    data=res.json()
    #Finalmente le pedimos que nos muestre la info
    print(data)

if __name__=="__main__":
    main()
