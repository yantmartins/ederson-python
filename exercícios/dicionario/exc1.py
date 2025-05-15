
tradutor = {
    "apple": "maçã", "banana": "banana", "house": "casa", "dog": "cachorro", "cat": "gato",
    "car": "carro", "book": "livro", "school": "escola", "sun": "sol", "moon": "lua",
    "star": "estrela", "tree": "árvore", "water": "água", "fire": "fogo", "earth": "terra",
    "wind": "vento", "sky": "céu", "flower": "flor", "food": "comida", "drink": "bebida",
    "milk": "leite", "bread": "pão", "butter": "manteiga", "cheese": "queijo", "meat": "carne",
    "fish": "peixe", "egg": "ovo", "sugar": "açúcar", "salt": "sal", "pepper": "pimenta",
    "rice": "arroz", "beans": "feijão", "computer": "computador", "mouse": "mouse", "keyboard": "teclado",
    "screen": "tela", "phone": "telefone", "table": "mesa", "chair": "cadeira", "window": "janela",
    "door": "porta", "bed": "cama", "bathroom": "banheiro", "kitchen": "cozinha", "living room": "sala de estar",
    "garden": "jardim", "street": "rua", "city": "cidade", "country": "país", "world": "mundo",
    "family": "família", "mother": "mãe", "father": "pai", "brother": "irmão", "sister": "irmã",
    "friend": "amigo", "boy": "menino", "girl": "menina", "baby": "bebê", "man": "homem",
    "woman": "mulher", "teacher": "professor", "student": "aluno", "doctor": "médico", "nurse": "enfermeira",
    "police": "polícia", "fireman": "bombeiro", "driver": "motorista", "pilot": "piloto", "artist": "artista",
    "singer": "cantor", "actor": "ator", "dancer": "dançarino", "engineer": "engenheiro", "lawyer": "advogado",
    "bookstore": "livraria", "library": "biblioteca", "hospital": "hospital", "market": "mercado", "restaurant": "restaurante",
    "hotel": "hotel", "airport": "aeroporto", "station": "estação", "bus": "ônibus", "train": "trem",
    "bicycle": "bicicleta", "motorcycle": "moto", "truck": "caminhão", "road": "estrada", "bridge": "ponte",
    "river": "rio", "lake": "lago", "sea": "mar", "ocean": "oceano", "mountain": "montanha",
    "hill": "colina", "forest": "floresta", "desert": "deserto", "island": "ilha", "valley": "vale",
    "animal": "animal", "bird": "pássaro", "insect": "inseto", "horse": "cavalo", "cow": "vaca",
    "pig": "porco", "sheep": "ovelha", "goat": "cabra", "chicken": "galinha", "duck": "pato",
    "color": "cor", "red": "vermelho", "blue": "azul", "green": "verde", "yellow": "amarelo",
    "black": "preto", "white": "branco", "gray": "cinza", "brown": "marrom", "pink": "rosa",
    "purple": "roxo", "orange": "laranja", "number": "número", "one": "um", "two": "dois",
    "three": "três", "four": "quatro", "five": "cinco", "six": "seis", "seven": "sete",
    "eight": "oito", "nine": "nove", "ten": "dez", "day": "dia", "night": "noite",
    "morning": "manhã", "afternoon": "tarde", "evening": "anoitecer", "today": "hoje", "tomorrow": "amanhã",
    "yesterday": "ontem", "week": "semana", "month": "mês", "year": "ano", "time": "tempo",
    "hour": "hora", "minute": "minuto", "second": "segundo", "happy": "feliz", "sad": "triste",
    "angry": "com raiva", "tired": "cansado", "hungry": "com fome", "thirsty": "com sede", "cold": "frio",
    "hot": "quente", "big": "grande", "small": "pequeno", "fast": "rápido", "slow": "devagar",
    "new": "novo", "old": "velho", "good": "bom", "bad": "ruim", "beautiful": "bonito",
    "ugly": "feio", "easy": "fácil", "difficult": "difícil", "open": "abrir", "close": "fechar",
    "start": "começar", "finish": "terminar", "read": "ler", "write": "escrever", "speak": "falar",
    "listen": "ouvir", "see": "ver", "walk": "andar", "run": "correr", "jump": "pular"
}


palavra = input("Digite uma palavra em inglês para traduzir: ").lower()


if palavra in tradutor:
    print(f"A tradução de '{palavra}' é: {tradutor[palavra]}")
else:
    print(f"A palavra '{palavra}' não está no dicionário.")
