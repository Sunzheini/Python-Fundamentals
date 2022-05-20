def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    import requests
    import json

    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "d2de62eb31894bba8a9f957afc2ee71c"
    }
    main_url = " https://newsapi.org/v1/articles"
    res = requests.get(main_url, params=query_params)
    load = json.loads(res.text)
    speak('Here you listen to top BBC news')
    speak('first...')

    for i in range(10):
        print(load['articles'][i]['title'])
        speak(load['articles'][i]['title'])
        speak('next news')
