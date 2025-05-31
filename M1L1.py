meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "ROFL se utiliza como reacción a algo gracioso, similar a LOL"
            }

word = input("Escribe una palabra moderna que no entiendas (¡utiliza mayúsculas!):")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Todavía no tenemos esta palabra... Pero estamos trabajando en ella.")
