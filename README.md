# SimpleMultipleChoicePy


|     |     |     |
| --- | --- | --- |
| **Objective** | :   | This program simulates how to generate a random Multiple Choice Question (MCQ). |
| **Data Source** | :   | The sources of the questions are from a dictionary, where its item has a key and a value. The key is the question itself, and the value consists of 4 (four) choices of answer.<br><br>We also pre-defined the key answer beforehand in a list. |
| **How** | :   | Initially, we shuffle how questions order will appear using a random library and a dummy list.<br><br>Subsequently, during each iteration, we 'pop' which number will appear (i.e., 'index') and print the question to the user based on that index.<br><br>We then take the user's input and compare whether the key answer of the related index matches the input or not. |
