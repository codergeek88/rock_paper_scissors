#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:06:52 2020

@author: kishanpatel
"""

import random

win = "you win!"
lose = "you lose, sorry"
tie = "you tied, try again"

def result(other, beat, loseTo, tieWith):
    if other == beat:
        return win
    elif other == loseTo:
        return lose
    elif other == tieWith:
        return tie

class Rock(object):
    def __init__(self):
        self.beat = None
        self.loseTo = None
        self.tieWith = self
    def assignVars(self, paper, scissors):
        self.beat = scissors
        self.loseTo = paper
    def getResult(self, other):
        return result(other, self.beat, self.loseTo, self.tieWith)
    def __str__(self):
        return "rock"

class Paper(object):
    def __init__(self):
        self.beat = None
        self.loseTo = None
        self.tieWith = self
    def assignVars(self, rock, scissors):
        self.beat = rock
        self.loseTo = scissors
    def getResult(self, other):
        return result(other, self.beat, self.loseTo, self.tieWith)
    def __str__(self):
        return "paper"


class Scissors(object):
    def __init__(self):
        self.beat = None
        self.loseTo = None
        self.tieWith = self
    def assignVars(self, rock, paper):
        self.beat = paper
        self.loseTo = rock
    def getResult(self, other):
        return result(other, self.beat, self.loseTo, self.tieWith)
    def __str__(self):
        return "scissors"

def buildDict():
    rock = Rock()
    paper = Paper()
    scissors = Scissors()
    
    rock.assignVars(paper, scissors)
    paper.assignVars(rock, scissors)
    scissors.assignVars(rock, paper)
    
    choicesDict = {}
    choicesDict["rock"] = rock
    choicesDict["paper"] = paper
    choicesDict["scissors"] = scissors
    return choicesDict

def getUserChoice(choicesDict):
    user_input = input("What would you like to play? (rock/paper/scissors)")
    try:
        user_choice = choicesDict[user_input]
        return user_choice
    except KeyError:
        print("Invalid choice")

def playRound(choicesDict, valsList):
    cpuChoice = random.choice(valsList)
    userChoice = getUserChoice(choicesDict)
    print("User choice:", userChoice)
    print("Computer choice:", cpuChoice)
    return userChoice.getResult(cpuChoice)

def playGame(choicesDict, valsList):
    roundResult = playRound(choicesDict, valsList)
    while roundResult == tie:
        print()
        print(tie)
        roundResult = playRound(choicesDict, valsList)
    print(roundResult)
    return roundResult
            
choicesDict = buildDict()
valsList = list(choicesDict.values())
playGame(choicesDict, valsList)