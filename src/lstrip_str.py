#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 10, 2014

@author: anroco

In python how to remove one or more leading characters of a string?

En python ¿como remover uno o varios caracteres del inicio de un string?
'''

#create a str
s = '____I thought a thought____'
print(s)

#generates a copy of the string with the leading characters removed.
s_new = s.lstrip('_')
print(s_new)

#create a str
s = '    I thought a thought     '
print(s)

#if the character is not defined by defaults to removing whitespace.
#Whitespace characters are those defined in the systme Unicode as
#'Other' or 'Separator'.
s_new = s.lstrip()
print(s_new)
