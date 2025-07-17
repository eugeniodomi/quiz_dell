import random

def run_quiz(questions):
    score = 0
    results = []
    category_scores = {} # Novo dicionário para armazenar pontuações por categoria

    print("-------------------------------------------------")
    print("Bem-vindo(a) ao Quiz de Soluções Dell!")
    print("Teste seus conhecimentos sobre os produtos Dell.")
    print("-------------------------------------------------")

    random.shuffle(questions)

    for i, q in enumerate(questions):
        # Inicializa a categoria se ainda não existir
        if q["category"] not in category_scores:
            category_scores[q["category"]] = {"correct": 0, "total": 0}

        category_scores[q["category"]]["total"] += 1 # Incrementa o total de perguntas para a categoria

        print(f"\n--- Questão {i + 1} ({q['category']}) ---") # Mostra a categoria da pergunta
        print(q["question"])
        for j, alternative in enumerate(q["alternatives"]):
            print(f"{chr(65 + j)}. {alternative}")

        while True:
            user_answer = input("Sua resposta (A, B, C, or D): ").upper()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Entrada invalida. Por favor, adicione apenas A, B, C, or D.")

        correct_answer_index = q["correct_answer"]
        if user_answer == chr(65 + correct_answer_index):
            print("Correto!")
            score += 1
            category_scores[q["category"]]["correct"] += 1 # Incrementa a pontuação da categoria
            results.append({"question": q["question"], "status": "Correto", "category": q["category"]})
        else:
            print(f"Errouuu! A resposta correta é: {chr(65 + correct_answer_index)}. {q['alternatives'][correct_answer_index]}")
            results.append({"question": q["question"], "status": "Errado", "correct": q['alternatives'][correct_answer_index], "category": q["category"]})

    print("\n--- Quiz Acabouuuu! ---")
    print(f"Sua pontuação {score} de {len(questions)} perguntas.")

    print("\n--- Resultados Detalhados por Categoria ---")
    for category, scores in category_scores.items():
        print(f"- {category}: {scores['correct']} de {scores['total']} perguntas corretas.")

    print("\n--- Detalhes das Respostas ---")
    for res in results:
        if res["status"] == "Correto":
            print(f"✅ [{res['category']}] {res['question']} - Correto!")
        else:
            print(f"❌ [{res['category']}] {res['question']} - Tututu, tente novamente! (Resposta correta é: {res['correct']})")
# --- perguntas aqui ---
quiz_questions = [
    {
        "question": "Qual solução Dell é ideal para grandes volumes de dados não estruturados (vídeos, imagens, logs) com foco em escalabilidade e performance?",
        "alternatives": ["Dell PowerVault", "Dell PowerMax", "Dell PowerScale", "Dell PowerStore"],
        "correct_answer": 2,
        "category": "Storage" # Adicionado categoria
    },
    {
        "question": "Se o cliente precisa de um sistema que se expanda massivamente para bilhões de arquivos e objetos, qual a melhor opção?",
        "alternatives": ["Dell PowerEdge", "Dell VxRail", "Dell PowerScale", "Dell PowerProtect"],
        "correct_answer": 2,
        "category": "Storage" # Adicionado categoria
    },
    {
        "question": "Qual a principal vantagem de um servidor de borda em comparação com um servidor de data center tradicional?",
        "alternatives": ["Menor latência", "Maior capacidade de armazenamento", "Melhor desempenho gráfico", "Mais fácil de gerenciar"],
        "correct_answer": 0,
        "category": "Servidor de Borda" # Adicionado categoria
    },
    {
        "question": "Qual tecnologia é comumente usada em servidores de borda para processar dados localmente?",
        "alternatives": ["Cloud computing", "Virtualização", "Inteligência Artificial", "Nenhuma das anteriores"],
        "correct_answer": 2,
        "category": "Servidor de Borda" # Adicionado categoria
    }
]
# run quiz
if __name__ == "__main__":
    run_quiz(quiz_questions)
