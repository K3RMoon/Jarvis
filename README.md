# Jarvis

## What is a bot?

A bot is a piece of software that can execute commands, reply to messages or perform routine task, either automatically or with minimal human intervention. For this project, the bot will be an executable program that runs in the terminal/command prompt. 

## What is Jarvis?

Jarvis is a programming language that facilitates the creation of local bots. Its simple syntax makes it possible someone with no programming knowledge to create a bot with a variety of basic functions.

## Language Features

Jarvis allows the programmer to create a system of bots that the user can execute and interact with locally, each with their unique names, using a simple syntax. 

A Jarvis bot can:

1. Respond to user's input with predefined messages
2. Learn information as requested from the user

## Sample Bot System

```javascript
Friday{
    "Hey" : Response("Hello");
    "Learn that my ~param is ~param": Learn(param);
    "Forget ~param":Forget(param);
    "Hi" : Response("Hi" + name);
    "Tell me my ~param" : Response(param + "right?");
    "Sum numbers ~param ~param" : Action.Sum(param, param);
    "Substract ~param ~param" : Action.Subtract(param, param);
}
Jarvis{
    "Multiply ~param ~param" : Action.Multiply(param, param);
	"Whats ~param to the ~param power" : Action.Power(param, param);
    "Tell me a joke" : Action.Joke();
    "Throw de dice" : Action.RollDice();
    "What is the root of ~param" : Action.Root(param);
    "what is ~param over ~param" : Action.Divide(param, param);
    "what is ~param mod ~param" : Action.Modulo(param, param);
    "Give me a random number" : Action.Random();
}
```

## Install Jarvis

### Requirements

1. Python 3
2. ply

To install Jarvis in your computer simply clone this project on your computer

## Execute the program

After installing and creating your first bot, save the program to a file with extension .jvs

Your bot can now be executed from the command line (cmd, batch, etc) using python with the following command

> python path_to_project/Jarvis.py path_to_bot_file/file_name

notice that file_name does not contains the .jvs extension.
