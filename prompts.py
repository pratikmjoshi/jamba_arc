SHOT_ARC_DATA = """
    input: {challenge}
    output: {solution}
"""

FEWSHOT_ARC_DATA = """
{training_shot_arc_data}
test_input: {test_input}
test_output: {test_output}
"""

FEWSHOT_ARC_DATA_WITH_DSL = """{example_key}:
{fewshot_arc_data}
    Logic for solving: {dsl_logic}
"""

FEWSHOT_ARC_DATA_WITH_DESCRIPTION = """{example_key}:
{fewshot_arc_data}
    Logic for solving: {logic_description}
"""

ARC_INSTRUCTION_PROMPT = """You are given a challenge to solve. Each input is a grid of numbers (which represent colors), and output is a transformed grid that uses the input based on some logic. 
Each example has multiple input/output pairs, and logic on how to solve it for that specific example. Your task is to figure out the logic for the test example and apply it to the final challenge.
The output should be a json object with the key as the example number and the value as the solution grid. Here are examples/solution pairs to get you started:
{few_shot_arc_data_with_logic}

Solve this following example:
{test_challenge}

Output your solution as JSON here:
"""
