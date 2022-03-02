# SimpleMultipleChoicePy

  <!-- /\* Font Definitions \*/ @font-face {font-family:"Cambria Math"; panose-1:0 0 0 0 0 0 0 0 0 0;} @font-face {font-family:Calibri; panose-1:2 15 5 2 2 2 4 3 2 4;} /\* Style Definitions \*/ p.MsoNormal, li.MsoNormal, div.MsoNormal {margin-top:0in; margin-right:0in; margin-bottom:10.0pt; margin-left:0in; line-height:115%; font-size:11.0pt; font-family:"Calibri","sans-serif";} .MsoPapDefault {margin-bottom:10.0pt; line-height:115%;} @page WordSection1 {size:8.5in 11.0in; margin:1.0in 1.0in 1.0in 1.0in;} div.WordSection1 {page:WordSection1;} -->

Objective: This program simulates how to generate a random Multiple Choice Question (MCQ).

**Objective**

:

This program simulates how to generate a random Multiple Choice Question (MCQ).

**Data Source**

:

The sources of the questions are from a dictionary, where its item has a key and a value. The key is the question itself, and the value consists of 4 (four) choices of answer.

We also pre-defined the key answer beforehand in a list.

**How**

:

Initially, we shuffle how questions order will appear using a random library and a dummy list.

Subsequently, during each iteration, we 'pop' which number will appear (i.e., 'index') and print the question to the user based on that index.

We then take the user's input and compare whether the key answer of the related index matches the input or not.
