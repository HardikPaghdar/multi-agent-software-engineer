def plan(request):
    request = request.strip()
    if len(request) < 8:
        raise ValueError('Describe the task in at least eight characters')
    low = request.lower()
    criteria = [
        {'id':'AC1','description':'Requested behavior is implemented without unrelated changes','verify':'Review the proposed diff'},
        {'id':'AC2','description':'Invalid inputs and failure paths are handled','verify':'Add negative tests'},
        {'id':'AC3','description':'Existing behavior remains compatible','verify':'Run regression tests'},
    ]
    if any(w in low for w in ('csv','export')):
        criteria.append({'id':'AC4','description':'Export handles quoting and Unicode','verify':'Test commas, quotes and Unicode'})
    risks = ['Proposed changes require human review']
    if any(w in low for w in ('delete','production','payment','secret')):
        risks.insert(0, 'High-impact operation requires human approval and rollback plan')
    return {'request':request,'acceptance_criteria':criteria,'steps':['Inspect relevant code and tests','Choose the smallest implementation','Add focused tests','Run relevant checks','Document evidence and limitations'],'risks':risks}
def run(request):
    p = plan(request)
    issues = ['Human approval required'] if any('requires human approval' in r for r in p['risks']) else []
    return {'plan':p,'test_plan':[{'criterion':c['id'],'verification':c['verify'],'status':'not_run'} for c in p['acceptance_criteria']],'review':{'ready':not issues,'issues':issues},'execution':{'code_modified':False,'tests_executed':False}}
