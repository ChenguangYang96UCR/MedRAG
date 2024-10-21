from src.medrag import DTKGRAG
import json
import src.utils as ut


def write_answer_into_json(json_datas, question_path):
    with open(question_path, 'w') as r:
        json.dump(json_datas, r,)

question = "Can you give some introductions and backgrounds about digital twins of healthcare?"

dtkgrag = DTKGRAG(llm_name="OpenAI/gpt-3.5-turbo-16k", rag=True, retriever_name="Contriever", corpus_name="dtkg", corpus_cache=True)
answer, snippets, scores  = dtkgrag.answer(question=question, k=32)

result_path = '/home/cyang314/result/result.json'

with open(result_path, 'r+', encoding='utf-8') as file:
    # Get Questions from json file
    json_datas = json.load(file)
    for json_data in json_datas:
        Question = json_data["Question"]
        if question == Question:
            json_data["Second_step_Answer"] = answer

            triples = json_data["triples"]
            first_answer = json_data["First_step_Answer"]
            answer_prompt = f"""
You are a digital twin and reasoning expert,
Combine the answer from the Step 1 and the answer from Retrieval-Augmented Generation (RAG), please generage a final answer.
step 1 answer: {first_answer}
RAG answer: {answer}
"""
            answer_response, _, tokens = ut.get_completion(answer_prompt,
                                            model_name='gpt-3.5-turbo-16k',
                                            max_tokens=2000,
                                            temperature=0.1,
                                            top_p=0.5)
            json_data["Final_Answer"] = answer_response
    
write_answer_into_json(json_datas, result_path)

print(f"Final answer in json: {answer}") 
