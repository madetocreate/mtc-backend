import pytest
from services.supabase_client import dummy_supabase
def test_supabase():
    assert dummy_supabase() == True
