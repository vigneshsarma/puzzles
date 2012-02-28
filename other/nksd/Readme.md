#Numeric Keypad SMS Decoder

Assume that you’re on the T9 SMS mode [Manual Mode]. In this case:
a would be 2 or 2222 etc
b would be 22
c would be 222
d would be 3 etc

**IMPORTANT:** To send 2 letters in sequence from the same cell phone button, the user must “pause” before pressing the same button a second time. Use a space character to indicate a pause. 

For example: ```“ab”``` would be ```“2 22”```

**Example:**
```“multunus”``` would be ```6885558 8866887777```

Finally, as you might expect, pressing zero will send a space. 

**Example:**
```“ruby multunus”``` would be ```777882299906885558 8866887777```

The above describes how the encoder works. But your task is to write a decoder instead. 

**Example:**
Input: ``` 2 2202223033 333```
Output:``` ab cd ef```

To keep things simple you do not need to consider Capitals and Numbers.
Taken from [Multunus Careers Page](http://www.multunus.com/careers/how-to-apply/application-form-for-developers/)
