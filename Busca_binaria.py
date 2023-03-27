def busca_binaria_recurs(inicio, meio, fim, alvo, arr):
    if alvo == arr[meio]:
        return True
    
    elif inicio > fim:
        return False
    
    elif alvo > arr[meio]:
        return busca_binaria_recurs(meio + 1, ((meio + 1) + fim) // 2, fim, alvo, arr)
        
    elif alvo < arr[meio]:
        return busca_binaria_recurs(inicio, (inicio + (meio - 1)) // 2, meio - 1, alvo, arr)
    
