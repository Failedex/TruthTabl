# Truth Tabl Generator!!!

*"We had to draw so many truth tables in the tutorials." - Chair-and-Table*

Python script that generates propositional logic tables (truth tables). Made for my Discrete Mathematics course because I'm too lazy to make these by hand.

## Example
```
logic: !(p&!q)
 p  q  !q  (p&!q)  !(p&!q)
 0  0  1     0        1
 0  1  0     0        1
 1  0  1     1        0
 1  1  0     0        1

logic: (!p>q)|(!p&!q)
 p  q  !p  (!p>q)  !q  (!p&!q)  ((!p>q)|(!p&!q))
 0  0  1     0     1      1            1
 0  1  1     1     0      0            1
 1  0  0     1     1      0            1
 1  1  0     1     0      0            1
```

## Syntax/Usage
Operators | Syntax | Priority
--- | --- | ---
not | `!` | 1
and | `&` | 3
or | `|` | 4
implies | `>` | 5

Operators with the lowest priority is evaluated first, but parenthesis could be used to prioritize certain operations (see examples).

I forgot to implement biconditional. Let me think about the syntax first.

To quit the program, you can input "!!!", but you can also `<C-c>`. This is just the average python script.

## Bugs and Issues
I haven't fully tested the program for bugs, there may be issues. 

If you find any bugs, fix it yourself.

Shout out to [Chair-and-Table](https://github.com/Chair-and-table) for designing the algorithm to parse the user input into actual logic.
