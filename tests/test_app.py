import pytest
from unittest.mock import patch

# Імпортуємо функцію, яку будемо тестувати
from your_module import to_upper_case

# Тест для функції to_upper_case
def test_to_upper_case():
    # Використовуємо mock для input
    with patch('builtins.input', return_value='test'):
        result = to_upper_case()
    # Перевіряємо, чи результат вірно перетворено в верхній регістр
    assert result == 'TEST'