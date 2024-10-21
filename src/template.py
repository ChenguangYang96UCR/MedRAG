from liquid import Template

general_cot_system = '''You are a digital twins expert, and your task is to answer a digital twins question. Please first think step-by-step and then give your answer. Organize your output in a json formatted as Dict{"Raw_Answer": Str(explanation)}. Your responses will be used for research purposes only, so please have a definite answer.'''

general_cot = Template('''
Here is the question:
{{question}}

Please think step-by-step and generate your output in json:
''')

general_medrag_system = '''You are a digital twins expert, and your task is to answer a digital twins question using the relevant documents. Please first think step-by-step and then give your answer. Organize your output in a json formatted as Dict{"Raw_Answer": Str(explanation)}. Your responses will be used for research purposes only, so please have a definite answer.'''

general_medrag = Template('''
Here are the relevant documents:
{{context}}

Here is the question:
{{question}}

Please think step-by-step and generate your output in json:
''')

meditron_cot = Template('''
### User:
Here is the question:
...

Please think step-by-step and generate your output in json.

### Assistant:
{"Raw_Answer": ...}

### User:
Here is the question:
{{question}}

Please think step-by-step and generate your output in json.

### Assistant:
''')

meditron_medrag = Template('''
Here are the relevant documents:
{{context}}

### User:
Here is the question:
...

Please think step-by-step and generate your output in json.

### Assistant:
{"Raw_Answer": ...}

### User:
Here is the question:
{{question}}

Please think step-by-step and generate your output in json.

### Assistant:
''')

simple_medrag_system = '''You are a digital twins expert, and your task is to answer a medical question using the relevant documents.'''
simple_medrag_prompt = Template('''Here are the relevant documents:\n{{context}}\nHere is the question:\n{{question}}''')

i_medrag_system = '''You are a digital twins assistant, and your task is to answer the given question following the instructions given by the user. '''

follow_up_instruction_ask = '''Please first analyze all the information in a section named Analysis (## Analysis). Then, use key terms from previous answers to form specific and direct questions. Generate {} concise, context-specific queries to search for additional information in an external knowledge base, in a section named Queries (## Queries). Each query should be simple and focused, directly relating to the key terms used in the answers. Wait for responses from the user before proceeding.'''
follow_up_instruction_answer = '''Please first think step-by-step to analyze all the information in a section named Analysis (## Analysis). Then, please give your answer in a section named Answer (## Answer).'''