
DICTIONARY = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'yo',
        'ж': 'zh',
        'и': 'i',
        'й': 'i',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'ц': 'c',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'sch',
        'ъ': '',
        'э': '',
        'ю': '',
        'я': 'ya'
    }

RUS_ALPHABET = {
        'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з',
        'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
        'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
        'ш', 'щ', 'ъ', 'э', 'ю', 'я'
    }

SYMBOLS = ['*', '/', '#', '$', '№', '@']


def is_russian(word: str):
    pattern = word.lower()
    for alpha in RUS_ALPHABET:
        if alpha in pattern:
            return True
    return False


def йцукен_to_qwerty(phrase: str):
    return ''.join([DICTIONARY.get(x, '') for x in phrase.lower()])


def prepare_input_data(data: list):
    data_string = ''
    for phrase in data:
        if is_russian(phrase):
            phrase = йцукен_to_qwerty(phrase)
        data_string += phrase
        upper_phrase = phrase.upper()
        if upper_phrase != phrase:
            data_string += upper_phrase
    return data_string + ''.join(SYMBOLS)
