# WTF-Lang: Minimal Interpreted Language

WTF-Lang is a language I made to learn about how a programming langauge works. 

# What can it do right now?

For now, it can do most of the basic things expected from a programming language. However, various modern features like loops, methods, etc are missing. And I'm not planning on adding them into this language as it is a language I created to learn how programming langauges work and especially, FOR FUN.

# Working with WTF-Lang 

WTF-Lang provides very minimal features, it can only perform arithmetic operations and conditional operations.

# Hello Netherworld! in WTF-Lang 
Unlike other languages, in WTF-Lang you have to store the *STRING* in a variable to print it out. **However**, you don't have to store an *INTEGER* in a variable to print it out, same goes for all the arithmetic and conditional operations.

**HELLO NETHERWORLD!**
```
message := "Hello Netherworld!"
$message
```

**BREAKDOWN**
- `message` is the identifier of the variable.
- `:=` assigns the expression into a variable.
- `$` fetches the value from the variable.

**ARITHMETIC OPERATORS**
- `+` - `EXPRESSION + EXPRESSION`
- `-` - `EXPRESSION - EXPRESSION`
- `*` - `EXPRESSION * EXPRESSION`
- `/` - `EXPRESSION / EXPRESSION`
- `%` - `EXPRESSION % EXPRESSION`

**CONDITIONAL OPERATORS**
- `>` - `EXPRESSION > EXPRESSION`
- `<` - `EXPRESSION < EXPRESSION`
- `==` - `EXPRESSION == EXPRESSION`
- `!=` - `EXPRESSION != EXPRESSION`

**COMMENTS**
```
// This is a comment.
// Anything after these are ignored.
```

# Minimal Program 

```
y := 342
z := $y % 2

$z == 0
```
