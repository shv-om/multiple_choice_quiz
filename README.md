# multiple_choice_quiz

Question A
There are 1000 students attempting x questions in a competitive examination, where x is your birthdate coded as ddmmyyyy format. For example if your birthday was on 11/12/2000, then x=11122000. Each student can score one mark per right answer, and a penalty of-0.5 marks per wrong answer. The negative marks increases per wrong answer as a penalty p=0.5*n, where n represents the nth wrong answer. The questions are categorised into 5 topics, with number of questions in the categories in the ratio 10:4:3:2:1. All the questions are multiple choice questions (MCQ) type, with possibly more than one correct answer. Write a program to automatically read the answers, assign marks, and rank the students based on their performance in each of the five topic categories. Your aim should be to reduce time and space complexity, at the same time ensure accurate results.

Solution:
There are 1000 students attempting x questions in a competitive examination, where x is your birthdate coded as ddmmyyyy format. As the questions are categorised in ratio given as 10:4:3:2:1. So we will be taking this as an important part for our solution.
In this approach I’m going to use B+Tree, Dictionary, and List as the data structure which will handle all the pain to create and distribute marks among the students.
At first, we will look at our Data Structures we used in our project approach:
B+Tree: This is a user defined tree data structure. B+ Tree is a variant of BTree. B+ Tree only stores data in the leaf of the tree.
Dictionary: Dictionaries are used to store data values in key:value pairs. It is a collection which is unordered, changeable and does not allow duplicates. Dictionaries are written with curly brackets, and have keys and values.
List: Lists are used to store multiple items in a single variable. Lists are created using square brackets.

The whole code of this approach contains:
 	B+ Tree code having insert, search method etc.
 	Quiz Class for attempting questions for each student.
 	Creating random questions for testing.
 	Searching and evaluating the result for each student.
 	Picking up the 5 toppers of each category


Brief Explanation of the Solution
To solve this problem I use three types of data structure: One user defined and two inbuilt.
This approach includes the method to store and retrieve data from BPlusTree leaf node. This will provide us the speed of a tree for storing questions and answers in a list as a values of the dictionary. This dictionary will be available for the students to attempt questions and comparing the responses with the answers in the list. If the response matches the correct answers it will increment the total marks by 1 in each category or if the response does not matches the answers then it will decrement the total marks by number of total wrong attempts multiplies 0.5 (half mark). This increments marks by multiplying 0.5 with the total numbers of wrong attempts.
Now when we are able to find all the marks for every students. We can use now the dataset for calculating the Ranks and the 5 or 10 toppers of the Quiz in each Category.


Note:	Each code block have comments for understanding the solution’s working process.
