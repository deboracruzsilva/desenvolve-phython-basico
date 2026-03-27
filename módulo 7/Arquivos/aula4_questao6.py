musicas_por_ano ={}

with open("spotify-2023.csv","r",encoding='latin-1') as arquivo:
    next(arquivo)

    for linha in arquivo:
        linha = linha.strip()

        campos = linha.split(",")

        if len(campos)<9:
            continue

        try:
            track_name = campos[0]
            artist_name = campos[1]
            released_year = int(campos[3])
            streams = int(campos[8])
        except:
            continue
        if 2012 <= released_year <= 2022:
            if(released_year not in musicas_por_ano or
               streams > musicas_por_ano[released_year][3]):
                musicas_por_ano[released_year]=[
                    track_name,
                    artist_name,
                    released_year,
                    streams
                ]


    
resultado = [musicas_por_ano[ano] for ano in sorted (musicas_por_ano)]

print(resultado)

    
        
