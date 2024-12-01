<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>C++ Quiz</title>
    <style>
        body {
            background-color: #000000;
            color: #00FF00;
            font-family: 'Consolas', monospace;
        }
        .question {
            font-size: 24px;
            margin: 30px;
        }
        .option {
            background-color: #000000;
            color: #00FF00;
            border: 2px solid red;
            padding: 20px;
            margin: 10px;
            cursor: pointer;
            width: 200px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="question" id="question"></div>
    <div id="options"></div>
    <script>
        // List of questions and answers for the C++ quiz
        const questions = [
            {"question": "1 .What is the output when checking the type of the number 3.14 in Python?", "options": ["A. int", "B. float", "C. complex", "D. str"], "correct": "B"},
            {"question": "2 .What happens when you append 4 to a list [1, 2, 3]?", "options": ["A.Adds 4 to every element of the list", "B. Adds 4 as a new element to the list", "C. Replaces the last element with 4", "D. Does nothing"], "correct": "B"},
            {"question": "3 .Which of the following is a valid variable name in Python?", "options": ["A. 2name", "B. name_2", "C.name-2", "D.name 2"], "correct": "B"},
            {"question": "4 .What will be the result of repeating the string 'Hello' three times in Python?", "options": ["A. Hello3", "B. Hello Hello Hello", "C. HelloHelloHello", "D. Error"], "correct": "C"},
            {"question": "5 .What is the correct way to import a module in Python?", "options": ["A. import module", "B. include module", "C. require module", "D. using module"], "correct": "A"},
            {"question": "6 .What does the len() function return when applied to the string '2", "C.name-2", "D.name 2"], "correct": "B"},
            {"question": "4 .What will be the result of repeating the string 'Hello' three times in Python?", "options": ["A. Hello3", "B. Hello Hello Hello", "C. HelloHelloHello", "D. Error"], "correct": "C"},
            {"question": "5 .What is the correct way to import a module in Python?", "options": ["A. import module", "B. include module", "C. require module", "D. using module"], "correct": "A"},
            {"question": "6 .What does the len() function return when applied to the string 'Python'?", "options": ["A. 5", "B. 6", "C. 7", "D. Error"], "correct": "B"},
            {"question": "7 .Which of these data types is mutable in Python?", "options": ["A. tuple", "B. list", "C. string", "D. int"], "correct": "B"},
            {"question": "8 .What will be the result of dividing 5 by 2 using floor division in Python?", "options": ["A. : 2.5", "B. 2", "C. 3", "D. Error"], "correct": "B"},
            {"question": "9 .What does the break statement do in a loop?", "options": ["A. Skips the current iteration", "B. Terminates the loop", "C. Restart the loop", "D. None of the above"], "correct": "B"},
            {"question": "10 .What is the keyword used to define a function in Python?", "options": ["A. func", "B. def", "C. function", "D. define"], "correct": "B"}
        ];

        let currentQuestion = 0;
        let score = 0;

        function displayQuestion() {
            const questionElement = document.getElementById('question');
            const optionsElement = document.getElementById('options');

            questionElement.innerText = questions[currentQuestion].question;
            optionsElement.innerHTML = '';

            questions[currentQuestion].options.forEach((option, index) => {
                const button = document.createElement('div');
                button.className = 'option';
                button.innerText = option;
                button.onclick = () => nextQuestion(option[0]);
                optionsElement.appendChild(button);
            });
        }

        function nextQuestion(answer) {
            if (answer === questions[currentQuestion].correct) {
                score++;
            }

            if (currentQuestion < questions.length - 1) {
                currentQuestion++;
                displayQuestion();
            } else {
                alert(`Quiz Over! Your final score is: ${score}/10`);
            }
        }

        displayQuestion();
    </script>
</body>
</html>