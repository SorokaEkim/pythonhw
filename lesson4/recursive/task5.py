""" Задача 5. Редакционное расстояние """

def levenshtein_distance(s1, s2):
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    
    if s1[0] == s2[0]:
        cost = 0
    else:
        cost = 1
    
    deletion = levenshtein_distance(s1[1:], s2) + 1
    insertion = levenshtein_distance(s1, s2[1:]) + 1
    substitution = levenshtein_distance(s1[1:], s2[1:]) + cost
    
    return min(deletion, insertion, substitution)

# Пример использования
word1 = "kitten"
word2 = "sitting"
result = levenshtein_distance(word1, word2)
print(f"Редакционное расстояние между '{word1}' и '{word2}': {result}")