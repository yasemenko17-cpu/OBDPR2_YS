import sys
import os

# Додаємо корінь проєкту до шляхів пошуку модулів
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from conftest import load
from helpers import S, F, ATTRS_2, FDS_2
import variants.variant_08 as M

@pytest.mark.parametrize("args, expected", [
    (
        (S("customer_id customer_name order_id"), F("order_id -> customer_id; customer_id -> customer_name")), 
        [S("customer_id customer_name"), S("customer_id order_id")]
    ),
    (
        (ATTRS_2, FDS_2), 
        [S("grade student teacher"), S("subject teacher")]
    ),
])
def test_my_cases(args, expected):
    result = M.decompose_bcnf(*args)
    assert sorted([frozenset(r) for r in result], key=sorted) == sorted([frozenset(r) for r in expected], key=sorted)