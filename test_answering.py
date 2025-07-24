from chains.answering import AnswerGenerator

if __name__ == "__main__":
    generator = AnswerGenerator()

    context = (
        "Artificial intelligence (AI) refers to the simulation of human intelligence in machines. "
        "These machines are programmed to think like humans and mimic their actions. "
        "The term may also be applied to any machine that exhibits traits associated with a human mind such as learning and problem-solving."
    )

    question = "What is artificial intelligence and how does it relate to human intelligence?"

    answer = generator.answer(question, context)
    print("\n📘 Answer:\n" + answer)
