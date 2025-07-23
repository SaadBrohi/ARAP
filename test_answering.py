from chains.answering import AnswerGenerator

if __name__ == "__main__":
    generator = AnswerGenerator()

    # Example test
    question = "What is artificial intelligence?"
    context = "Artificial intelligence is the simulation of human intelligence in machines that are programmed to think and learn."

    answer = generator.answer(question, context)
    print("\n📘 Answer:\n" + answer)
