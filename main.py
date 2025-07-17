import random

def run_quiz(questions):
    score = 0
    results = []
    category_scores = {}

    print("-------------------------------------------------")
    print("Bem-vindo(a) ao Quiz de Soluções Dell!")
    print("Teste seus conhecimentos sobre os produtos Dell.")
    print("-------------------------------------------------")

    random.shuffle(questions)
    # Take only the first 10 questions from the shuffled list
    questions_to_ask = questions[:10]

    for i, q in enumerate(questions_to_ask): # odificado para ajustar quantidade de questoes
        # Inicializa a categoria se ainda não existir
        if q["category"] not in category_scores:
            category_scores[q["category"]] = {"correct": 0, "total": 0}

        category_scores[q["category"]]["total"] += 1

        print(f"\n--- Questão {i + 1} ({q['category']}) ---")
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
            category_scores[q["category"]]["correct"] += 1
            results.append({"question": q["question"], "status": "Correto", "category": q["category"]})
        else:
            print(f"Errouuu! A resposta correta é: {chr(65 + correct_answer_index)}. {q['alternatives'][correct_answer_index]}")
            results.append({"question": q["question"], "status": "Errado", "correct": q['alternatives'][correct_answer_index], "category": q["category"]})

    print("\n--- Quiz Acabouuuu! ---")
    print(f"Sua pontuação {score} de {len(questions_to_ask)} perguntas.") # modificado para ajustar quantidade de questoes
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
        "category": "Storage de Arquivos e Objetos (PowerScale)"
    },
    {
        "question": "Se o cliente precisa de um sistema que se expanda massivamente para bilhões de arquivos e objetos, qual a melhor opção?",
        "alternatives": ["Dell PowerEdge", "Dell VxRail", "Dell PowerScale", "Dell PowerProtect"],
        "correct_answer": 2,
        "category": "Storage de Arquivos e Objetos (PowerScale)"
    },
    {
        "question": "Para análise de dados em grande escala e colaboração em dados não estruturados, qual produto Dell oferece a flexibilidade necessária?",
        "alternatives": ["Dell PERC", "Dell HBA", "Dell PowerSwitch", "Dell PowerScale"],
        "correct_answer": 3,
        "category": "Storage de Arquivos e Objetos (PowerScale)"
    },
    {
        "question": "Quando o desafio é gerenciar arquivos e objetos de forma eficiente e com acesso multi-protocolo, qual solução é mais indicada?",
        "alternatives": ["Dell PowerScale", "Dell PowerVault", "Dell PowerMax", "Dell PowerFlex"],
        "correct_answer": 0,
        "category": "Storage de Arquivos e Objetos (PowerScale)"
    },
    {
        "question": "Um cliente busca uma plataforma para construir um 'data lake' com dados não estruturados em escala de petabytes. Qual produto você recomendaria?",
        "alternatives": ["Dell PowerStore", "Dell VxRail", "Dell PowerScale", "Dell PowerEdge"],
        "correct_answer": 2,
        "category": "Storage de Arquivos e Objetos (PowerScale)"
    },
    {
        "question": "Para simplificar e integrar servidores, armazenamento e virtualização em uma única plataforma, qual a melhor escolha?",
        "alternatives": ["Dell PowerEdge", "Dell PowerFlex", "Dell VxRail", "Dell PowerSwitch"],
        "correct_answer": 2,
        "category": "Infraestrutura Hiperconvergente (VxRail)"
    },
    {
        "question": "Se o objetivo é ter uma solução 'pronta para usar' (turn-key) e otimizada para VMware vSphere, qual produto se destaca?",
        "alternatives": ["Dell PowerStore", "Dell VxRail", "Dell PowerMax", "Dell PowerVault"],
        "correct_answer": 1,
        "category": "Infraestrutura Hiperconvergente (VxRail)"
    },
    {
        "question": "Qual tecnologia Dell ajuda a reduzir a complexidade de gerenciamento do datacenter ao consolidar recursos?",
        "alternatives": ["Servidores blade PowerEdge", "Controladores PERC", "Infraestrutura Hiperconvergente (HCI) como VxRail", "Switches de rede"],
        "correct_answer": 2,
        "category": "Infraestrutura Hiperconvergente (VxRail)"
    },
    {
        "question": "Um cliente quer escalar seu ambiente virtualizado de forma fácil e rápida, adicionando nós conforme a necessidade. Qual a solução ideal?",
        "alternatives": ["Dell PowerVault", "Dell VxRail", "Dell ECS Object Scale", "Dell HBA"],
        "correct_answer": 1,
        "category": "Infraestrutura Hiperconvergente (VxRail)"
    },
    {
        "question": "Qual produto Dell é a base para uma estratégia de nuvem híbrida que busca simplificar a operação de ambientes virtualizados on-premises?",
        "alternatives": ["Dell PowerMax", "Dell PowerScale", "Dell PowerFlex", "Dell VxRail"],
        "correct_answer": 3,
        "category": "Infraestrutura Hiperconvergente (VxRail)"
    },
    {
        "question": "Qual solução Dell oferece deduplicação avançada e imutabilidade de dados para proteção contra ransomware em backups?",
        "alternatives": ["Dell PowerStore", "Dell PowerProtect / Data Domain", "Dell ECS Object Scale", "Dell PowerVault"],
        "correct_answer": 1,
        "category": "Proteção de Dados (PowerProtect/Data Domain)"
    },
    {
        "question": "Para acelerar o tempo de backup e reduzir o espaço necessário para armazenamento de cópias, qual a tecnologia chave dos produtos Dell de proteção de dados?",
        "alternatives": ["Deduplicação de alta taxa", "Criptografia de ponta a ponta", "Replicação síncrona", "Armazenamento all-flash"],
        "correct_answer": 0,
        "category": "Proteção de Dados (PowerProtect/Data Domain)"
    },
    {
        "question": "Um cliente busca uma solução que garanta a recuperação rápida de dados após um ataque de ransomware. Qual produto é focado nisso?",
        "alternatives": ["Dell PowerEdge", "Dell PowerSwitch", "Dell HBA", "Dell PowerProtect / Data Domain"],
        "correct_answer": 3,
        "category": "Proteção de Dados (PowerProtect/Data Domain)"
    },
    {
        "question": "Qual linha de produtos Dell é especializada em gerenciamento e otimização do ciclo de vida dos backups?",
        "alternatives": ["Dell PowerMax", "Dell PowerScale", "Dell PowerProtect", "Dell PowerFlex"],
        "correct_answer": 2,
        "category": "Proteção de Dados (PowerProtect/Data Domain)"
    },
    {
        "question": "Para clientes com grandes volumes de dados que precisam de eficiência na retenção de backups a longo prazo, qual solução Dell é a mais adequada?",
        "alternatives": ["Dell Data Domain", "Dell PowerStore", "Dell VxRail", "Dell PERC"],
        "correct_answer": 0,
        "category": "Proteção de Dados (PowerProtect/Data Domain)"
    },
    {
        "question": "Para latência ultrabaixa e performance extrema em aplicações de missão crítica como bancos de dados transacionais, qual a principal solução Dell?",
        "alternatives": ["Dell PowerVault", "Dell PowerMax", "Dell PowerScale", "Dell PowerStore"],
        "correct_answer": 1,
        "category": "Storage de Bloco (PowerMax)"
    },
    {
        "question": "Qual produto Dell oferece a maior disponibilidade (seis noves) e recursos de continuidade de negócios para os ambientes mais exigentes?",
        "alternatives": ["Dell PowerEdge", "Dell VxRail", "Dell PowerMax", "Dell PowerFlex"],
        "correct_answer": 2,
        "category": "Storage de Bloco (PowerMax)"
    },
    {
        "question": "Se um cliente busca um sistema de armazenamento all-flash projetado para as cargas de trabalho mais intensas, qual a melhor recomendação?",
        "alternatives": ["Dell PowerMax", "Dell PowerVault", "Dell PowerScale", "Dell ECS Object Scale"],
        "correct_answer": 0,
        "category": "Storage de Bloco (PowerMax)"
    },
    {
        "question": "Para garantir que aplicações críticas como SAP HANA ou Oracle tenham o desempenho máximo de armazenamento, qual produto Dell é o líder de mercado?",
        "alternatives": ["Dell PowerStore", "Dell PowerMax", "Dell PowerScale", "Dell PowerProtect"],
        "correct_answer": 1,
        "category": "Storage de Bloco (PowerMax)"
    },
    {
        "question": "Um cliente precisa de uma solução que combine inteligência artificial para otimização de desempenho com resiliência inigualável. Qual Dell oferece isso?",
        "alternatives": ["Dell PowerFlex", "Dell VxRail", "Dell PowerMax", "Dell PowerStore"],
        "correct_answer": 2,
        "category": "Storage de Bloco (PowerMax)"
    }
]

# run quiz
if __name__ == "__main__":
    run_quiz(quiz_questions)
