name = 't1'
params = ['New', 'york', 'city']
triggerType = 'PHRASE'

triggerMap = {}


trigger = eval(triggerType.capitalize()+'Trigger("'+" ".join(params)+'")')

print trigger
