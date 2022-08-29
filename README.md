
# Impact Analytics Assessment Test

This is just an assessment test for recruitment for python developer profile.


## Question
In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. You are not allowed to miss classes for four or more consecutive days. Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

    1. The number of ways to attend classes over N days.
    2. The probability that you will miss your graduation ceremony.


## Built with
Python 3.8

## Approach
On any given day there could be two possibilties either you attend the classes or you miss the classes. I am generating all possible permutation of attending classes (i.e. 2 ^ No_of_days).

Next I am filtering all permutation which has 4 or more consecutive days of absence.

To compute probability I am simply dividing count of invalid permutation by total permutation.
## Getting Started
For run the project you simply need to follow the Prerequisites and run the command given below:-
## Prerequisites
Python 3 must be installed in your local machine.
## How to run ?
To run the assignment execute following command:
    
    python main.py
    

## Authors

Tej Kumar Sahu
- [@tejk1996]()


