1.	Description
The Rule Engine with AST is a flexible and dynamic system for creating, combining, and evaluating rules based on user attributes such as age, department, and salary.
Utilizing an Abstract Syntax Tree (AST), the project efficiently processes complex conditions and adapts to changing business requirement
2.	Table of Contents
-	[Features](#features)
-	[Installation](#installation)
-	[Usage](#usage)
-	[Testing](#testing)
-	[Contributing](#contributing)
 
-	[License](#license)
-	[Acknowledgments](#acknowledgments)
-	[Contact Information](#contact-information)


3.	Features
-	Dynamic rule creation and modification
-	Efficient evaluation of combined rules
-	Error handling and attribute validation
-	Persistent storage in a database
4.	Installation
bash
git clone https://github.com/yourusername/rule-engine-with-ast.git cd rule-engine-with-ast
pip install -r requirements.txt
5.	Usage Create a Rule POST /api/rules
{
"rule": "age > 30 AND department = 'Sales'"
}
Evaluate a Rule
POST /api/evaluate
{
"data": {
"age": 35, "department": "Sales", "salary": 60000,
 
"experience": 3
}
}
6.	Testing
To run tests, use: pytest tests/


7.	Contributing
If you would like to contribute, please fork the repository and submit a pull request.
8.	License
This project is licensed under the MIT License.
9.	Acknowledgments
Special thanks to [any libraries or resources] that assisted in the development of this project
1010.	Contact Information Sindhu B H 8147082532
1011.	sindhubh789@gmail.com https://github.com/student-rubeena/weather_monitor


