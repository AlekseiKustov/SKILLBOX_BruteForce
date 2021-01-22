import itertools

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


email = 'viktim@mail.ru'
other_data = ['89214112691', '17.03.1991', 'Кустов Алексей Алексеевич']


def create_combinations(combined_data_data, min_pass_length=4, max_pass_length=4):
    return (
        ''.join(variant)
        for r in range(min_pass_length, max_pass_length + 1)
        for variant in itertools.product(combined_data_data, repeat=r)
    )


def create_short_combinations(combined_data_data: str, min_pass_length=4, max_pass_length=4):
    """
    Doesn't work correctly :((
    """
    pairs = [f"{x[0]}{x[1]}" for x in zip(combined_data_data, combined_data_data[1:])]
    pairs.extend(SYMBOLS)
    return create_combinations(pairs, min_pass_length=min_pass_length, max_pass_length=max_pass_length)


def run_test(searching_pattern, variants):
    for v in variants:
        if v == searching_pattern:
            print('Found:', v)
            break


if __name__ == '__main__':
    # test_correct_pattern = '17*Ku*al*91*al'
    test_correct_pattern = '17*Ku'
    prepared_data = prepare_input_data(other_data)
    short_variants = create_short_combinations(prepared_data, max_pass_length=5)
    all_variants = create_combinations(prepared_data, max_pass_length=5)
    run_test(test_correct_pattern, short_variants)
    run_test(test_correct_pattern, all_variants)
