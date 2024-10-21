class Node:
def _init_(self, node_type, value=None, left=None, right=None):
        self.node_type = node_type  # "operator" or "operand"
        self.value = value          # Used for operand nodes
        self.left = left            # Left child (used for operators)
        self.right = right          # Right child (used for operators)

    def _repr_(self):
        return f"Node({self.node_type}, {self.value}, {self.left}, {self.right})"
def create_rule(rule_string):
    # Placeholder for parsing logic; assume simple parsing for now
    if "AND" in rule_string:
        conditions = rule_string.split("AND")
        left = create_rule(conditions[0].strip())
        right = create_rule(conditions[1].strip())
        return Node("operator", "AND", left, right)
    elif "OR" in rule_string:
        conditions = rule_string.split("OR")
        left = create_rule(conditions[0].strip())
        right = create_rule(conditions[1].strip())
        return Node("operator", "OR", left, right)
    else:
        # Operand node (e.g., age > 30)
        attr, comparison = rule_string.split(">")
        return Node("operand", {"attribute": attr.strip(), "operator": ">", "value": int(comparison.strip())})
 rule1 = create_rule("age > 30 AND department = 'Sales'")
print(rule1)
 def combine_rules(rules):
    if len(rules) == 1:
        return rules[0]

    # Combining multiple rules with AND logic
    root = rules[0]
    for rule in rules[1:]:
        root = Node("operator", "AND", root, rule)
    return root
rule1 = create_rule("age > 30 AND department = 'Sales'")
rule2 = create_rule("salary > 50000 OR experience > 5")
combined_rule = combine_rules([rule1, rule2])
print(combined_rule)
def evaluate_rule(ast, data):
    if ast.node_type == "operator":
        if ast.value == "AND":
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == "OR":
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)
    elif ast.node_type == "operand":
        attribute = ast.value["attribute"]
        operator = ast.value["operator"]
        value = ast.value["value"]

        if operator == ">":
            return data.get(attribute, 0) > value
        elif operator == "==":
            return data.get(attribute, "") == value
        # Add more operators as needed
    return False
 rule = create_rule("age > 30 AND department = 'Sales'")
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
print(evaluate_rule(rule, data))  # Should return True
CREATE TABLE rules (
    id SERIAL PRIMARY KEY,
    rule_name VARCHAR(255),
    rule_ast JSONB
)
from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route("/rules", methods=["POST"])
def create_rule_endpoint():
    rule_string = request.json.get("rule")
    rule = create_rule(rule_string)
    # Save rule to DB (assuming you've implemented DB logic)
    return jsonify({"rule_ast": rule._repr_()})

@app.route("/rules/combine", methods=["POST"])
def combine_rules_endpoint():
    rule_strings = request.json.get("rules")
    rules = [create_rule(r) for r in rule_strings]
    combined_rule = combine_rules(rules)
    return jsonify({"combined_rule": combined_rule._repr_()})

@app.route("/rules/evaluate", methods=["POST"])
def evaluate_rule_endpoint():
    rule_ast = request.json.get("rule_ast")
    data = request.json.get("data")
    result = evaluate_rule(rule_ast, data)
    return jsonify({"result": result})

if _name_ == "_main_":
    app.run(debug=True)