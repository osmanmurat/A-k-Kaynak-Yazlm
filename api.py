import requests

def get_example():
    url = 'https://jsonplaceholder.typicode.com/posts/1'  # Örnek bir API endpoint'i
    response = requests.get(url)

    if response.status_code == 200:  # İstek başarılı olduysa
        data = response.json()  # Yanıtı JSON formatına dönüştür
        print("Başlık:", data['title'])
        print("İçerik:", data['body'])
    else:
        print("İstek başarısız. Status Code:", response.status_code)

if __name__ == "__main__":
    get_example()
