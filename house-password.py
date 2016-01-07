#!/bin/python
print("house-password")
import re

def checkio(password):
    lengthCheck    = (len(password) >= 10)
    digitCheck     = (len(re.findall("[0-9]", password)) > 0)
    upperCaseCheck = (len(re.findall("[A-Z]", password)) > 0)
    lowerCaseCheck = (len(re.findall("[a-z]", password)) > 0)

    return lengthCheck and digitCheck and upperCaseCheck and lowerCaseCheck

results = []
results.append(checkio('A1213pokl') == False)
results.append(checkio('bAse730onE') == True)
results.append(checkio('asasasasasasasaas') == False)
results.append(checkio('QWERTYqwerty') == False)
results.append(checkio('123456123456') == False)
results.append(checkio('QwErTy911poqqqq') == True)

print("results: ", results)
