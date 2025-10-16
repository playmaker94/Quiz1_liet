import pytest
import random
import string
from similarity import calculate_similarity  # Import your string matcher here

def generate_valid_plate():
    letters = string.ascii_uppercase
    digits = string.digits
    plate = (
        random.choice(letters) +
        random.choice(letters) +
        random.choice(digits) +
        random.choice(digits) +
        random.choice(letters) +
        random.choice(letters) +
        random.choice(digits) +
        random.choice(digits) +
        random.choice(digits) +
        random.choice(digits)
    )
    return plate

def generate_invalid_plate():
    letters = string.ascii_letters + string.punctuation + ' '
    digits = string.digits
    length = random.choice([3,5,11,12])
    plate = ''.join(random.choice(letters + digits) for _ in range(length))
    return plate

valid_plates = [generate_valid_plate() for _ in range(500)]
invalid_plates = [generate_invalid_plate() for _ in range(500)]

test_pairs = []
for i in range(0, 500, 10):
    for j in range(0, 500, 10):
        test_pairs.append((valid_plates[i], valid_plates[j]))
        test_pairs.append((valid_plates[i], invalid_plates[j]))
        test_pairs.append((invalid_plates[i], invalid_plates[j]))

@pytest.mark.parametrize("s1,s2", test_pairs)
def test_similarity(s1, s2):
    similarity, matches, total = calculate_similarity(s1, s2)
    assert 0 <= similarity <= 100

def test_summary():
    total_similarity = 0
    count = 0
    for s1, s2 in test_pairs:
        similarity, _, _ = calculate_similarity(s1, s2)
        total_similarity += similarity
        count += 1
    avg_similarity = total_similarity / count
    print(f"\nTested {count} pairs. Average similarity: {avg_similarity:.2f}%")
