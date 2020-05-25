# Final Project - Automata Theory

## Execution
```
>> python -m PythonCodes.app"
```

## Input Style
```
Usage:
    run [input_string] on [Language_CODE]
        input_string    The string you want to check.
        Language_CODE   You can see Language_CODE in doc (number from 1 to 5)
    exit
        Exit python app
```


## Output Style
For each automatons we have specific output
### FA
For FA automatons like the first two languages it just prints the current state and print the next state that it goes with the transition. finally prints "Halt" if it Halts.
### PDA
For languages with code 3 and 4 we need PDA automatons. we may have some possible cases that can accept the string, soo we should check all the cases. PDA's printing is just like the FA's but it prints the stack too and if we have many cases it checks all of them and print them with one more tab to showing the recursion.
### Turing
For Turing automatons like the last language it prints the tape that the two dollar signs shows the first and the last item in the tape. In each step it prints the next state's name too. At the end it prints "Halt" if it Halts.

## Implementation

### Models Files
We have automatons such as fa, pda & turing. Also it contains main component such as states and all kinds of transitions. The automatons classes have start_checking method that recursively checks if the string is acceptable or not.
### App Class
It shows a simple ui for the user to run and check the string in bottom languages. It uses the language files for initialization. First we make the states and the transitions in the language class.
### Languages Class
Languages contains the codes that convert the diagrams to the python class to do calculation on them.

## Languages

It checks whether the input accepted from bottom languages or not.

 - [X] 𝐿1 = { 𝑤 | 𝑤 ∊ {𝑎, 𝑏, 𝑐}^∗, len(w) % 2 == 0 } 
 - [X] 𝐿2 = { 𝑤 | 𝑤 ∊ {𝑎, 𝑏, 𝑐}^∗, (𝑛𝑎(𝑤) − 𝑛𝑏(𝑤) % 3 == 1 } 
 - [X] 𝐿3 = { 𝑤𝑐𝑤^𝑟 | 𝑤 ∊ {𝑎, 𝑏}^∗ } 
 - [X] 𝐿4 = { 𝑎^𝑛 𝑏^(𝑛+𝑚) 𝑎^𝑚 | 𝑚, 𝑛 ≥ 1 } 
 - [X] 𝐿5 = { 𝑤𝑤 | 𝑤 ∊ {𝑎, 𝑏, 𝑐}^∗}