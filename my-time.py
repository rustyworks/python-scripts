from datetime import datetime
import random

SUCCESS = datetime(year=2020, month=5, day=17)
MOTIVATION_QUOTE = [
    "Please don't waste your time",
    'Are you already chasing your dream?',
    'Are you already makes the world recognize you?',
]

def string_wrapper(sentences, wrapper_char='=', number_of_wrapper_char=33):
    wrapped_sentences = (wrapper_char * number_of_wrapper_char)
    wrapped_sentences += '\n' + sentences + '\n'
    wrapped_sentences += (wrapper_char * number_of_wrapper_char)
    return wrapped_sentences

if __name__ == '__main__':
    now = datetime.now()
    time_remaining = SUCCESS - now
    if time_remaining.days > 0:
        print(string_wrapper('Your remaining days before 34 is {remaining:5}'
                .format(remaining=time_remaining.days)))
        print('{quote}'.format(quote=random.choice(MOTIVATION_QUOTE)))
