import random


def get_random_records(records: list, count: int = 1) -> list:
    return random.sample(records, count)


def get_random_delay(delay: float, rand_degree: float) -> float:
    assert 0 <= rand_degree <= 1, 'Randomization degree should be between 0 and 1.'
    return random.randint(int(delay - rand_degree * delay), int(delay + rand_degree * delay))
