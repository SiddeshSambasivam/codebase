# **A Brief Overview into Lexical Analysis**

> Lecture notes from Prof. YN Srikant lecutre on lexical analysis

A lexical analyzer is the first component in the compiler pipeline. It strips off blanks, tabs, newlines, and comments from the source program. It also keeps track of line numbers and associates error messges from the various parts of a compiler with line numbers.

LA is based in finite state automata, which are more efficient to implemnet than pushdown automata used for parsing.

**Keywords:**

1. Running example
2. Token
3. Pattern --> Regular Expression

   - `l(l+d+_)*` -> letter followed by any number of letters, digits and underscore

4. Lexeme

   - The sequence of characters matached by a pattern to form the corresponding token.

### **How to recognize tokens ?**

Transition diagrams, a varient of finite state automata, are used to implement regular definitions and to recognize tokens.

`symbols` are abstract entity (eg: letters and digits). if \sigma is an alphabet, then \sigma\* is the set of all strings over \sigma.

Language must have a finite representation which can be encoded bu a finite string.

> **Cardinality of a set** is a measure of number of elements in the set.

Regular expressions (regular languages can be represented), context-free grammars, context-sensitive grammars and type-0 grammars are finite represntation of respective languages.

Automate are machines that accept languages

- Finite state automata accept RLs
- Pushdown automata accept CFLs
- ...

Applications of automata

- switching circuit design
- lexical analyzer in a compiler
- state chars used in object-oriented design
- compilers
- parses of all types

## **Finite State Automaton**

An FSA is an acceptor or recognizer of regular languages. FSA is a 5-tuple.

- `Q`, finite set of states
- `\sigma`, input alphabet
- `\delta` atransition function, `\delta(q, a)` is state for each state q and input symbol 'a'
- `q0` is the start state
- `F` is the set of final/accepting states

A `Determinstic FSA` does not permit more than one transition from any state on a particular symbol whereas, `NFA` they allow 0, 1 or more transition from any given state.

**NFA**

An NFA is a 5-tuple as before, but the transition function `\delta` is different.

> `\delta(q,a)` = the set of all states p, such that there is a transition labelled a from q to p
