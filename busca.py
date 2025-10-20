from collections import Counter # counter para contar frequências de letras


def filtrar_palavras(candidatas, padrao):
    
    novas_candidatas = []
    tamanho_palavra = len(padrao)
    
    letras_reveladas = {letra for letra in padrao if letra != '_'}
    
    for palavra in candidatas:
        if len(palavra) != tamanho_palavra:
            continue
        
        eh_compativel = True
        for i in range(tamanho_palavra):
            letra_padrao = padrao[i]
            letra_palavra = palavra[i]
            
            if letra_padrao != '_' and letra_padrao != letra_palavra:
                eh_compativel = False
                break
            
            if letra_padrao == '_' and letra_palavra in letras_reveladas:
                eh_compativel = False
                break
            
        if eh_compativel:
            novas_candidatas.append(palavra)
        
    return novas_candidatas        

def filtrar_por_erro(candidatas, letra_errada):
    
    novas_candidatas = []
    for palavra in candidatas:
        if letra_errada not in palavra:
            novas_candidatas.append(palavra)
    return novas_candidatas 

def escolher_proxima_letra(candidatas, tentadas):
    
    if not candidatas:
        return None
    
    todas_as_letras = ''.join(candidatas)
    frequencias = Counter(todas_as_letras)
    
    for letra in tentadas:
        if letra in frequencias:
            del frequencias[letra]
            
    if frequencias:
        letra_mais_comum = frequencias.most_common(1)[0][0]
        return letra_mais_comum

    return None
    