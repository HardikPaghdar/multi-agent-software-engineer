import pytest
from software_engineer.workflow import plan, run

def test_export_criteria():
    assert any('Unicode' in c['description'] for c in plan('Add CSV export to customers')['acceptance_criteria'])
def test_production_requires_review():
    result=run('Delete production customer records')
    assert not result['review']['ready'] and not result['execution']['code_modified']
def test_short_request_rejected():
    with pytest.raises(ValueError): plan('fix it')
