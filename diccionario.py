meme_dict = {
            "SUPERCALIFRAGILISTICOESPIALIDOSO": "extraordianariamente bien",
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "SHEESH": "ligera desaprobación",
            "MUCHOSIDAD":"ser tu mismo,vencer tus miedos,creer en ti",
            "LOL": "una respuesta a algo gracioso",
            "CRINGE":"algo raro o embarazoso",
            "ROFL":"una respuesta a una broma"}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print("El significado es:")
    print(meme_dict[word])
else:
    print("esa palabra no se encuentra en este diccionario")
