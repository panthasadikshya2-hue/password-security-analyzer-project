from password_analyzer import calculate_entropy, analyze_password


def test_empty_password_entropy():
    assert calculate_entropy("") == 0.0


def test_password_with_lowercase():
    result = calculate_entropy("hello")
    assert result > 0


def test_common_password():
    result = analyze_password("password123")
    assert result["common_password"] is True


def test_repeated_characters():
    result = analyze_password("Hellooo123")
    assert "ooo" in result["repeated_patterns"]


def test_sequential_patterns():
    result = analyze_password("hello123")
    assert "123" in result["sequential_patterns"]


def test_keyboard_patterns():
    result = analyze_password("qwerty123")
    assert "qwe" in result["keyboard_patterns"]


def test_score_range():
    result = analyze_password("BlueTiger!47")
    assert 0 <= result["score"] <= 100


def test_password_rating():
    result = analyze_password("password123")
    assert result["rating"] == "Weak"