from answer_generator import AnswerGenerator

if __name__ == '__main__':
    ag = AnswerGenerator()
    try:
        ag.initialize()
        print('Initialized OK')
        ans = ag.generate_answer('What is polymorphism in object oriented programming?')
        print('---ANSWER START---')
        print(ans)
        print('---ANSWER END---')
    except Exception as e:
        import traceback
        traceback.print_exc()
