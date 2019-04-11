# Mathd Module

This is a mathematical module that does complex calculations usually to do with sequences

### Requirements
* Python 3.6 and up

### Setup
```python
import mathd

>> mathd = mathd()
>> mathd.square_nums(5)
>> 1, 4, 9, 16, 25
```

### Methods
#### ` fib(terms{integer})`
Returns fibonacci sequence with as many terms as specified

#### `tri_nums(terms{integer})`
Return triangle numbers with as many terms as specified

#### `linear_seq(sequence{list of integers}, terms{integer})`
Finds the term given in any given linear sequence 

#### `quadr_seq(sequence{list of integers}, terms{integer}, return_nth{boolean})`
Find the value of any given term in any given quadratic sequence"
if True, return nth will return the nth term formula.

#### `square_nums(terms{integer})`
Return square numbers with as many terms as specified

#### `lcm(x{integer}, y{integer})`
Returns the lowest common multiple of two numbers specified

#### `hcf(x{integer}, y{integer})`
Returns the highest common factor of two numbers specified

#### `avg(data{list})`
Returns the average of a given dataset

#### `mode(data{list})`
Returns the most common element in a given dataset, if one is not present then it will return the lowest value.
