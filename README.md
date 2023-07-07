#**`conbase.py` library**
<br>
---
<br>
##**Import the library as follows.**
###**Examples**
```python
import conbase
```
<br>
---
<br>
##**Create thumbnails**
The following script is an example of converting a binary number with the meaning of 12 in decimal into an octal number. <br>
```python
import conbase

n = conbase.convertBase(1100,2,8)
print(n)
```
<br>
---
<br>
##**Functions**
1. 'fromDecimal(num, base)' <br>
Convert a decimal number into a number with the other base excluding decimal numbers. <br>
###**PARAMETERS:**
* __num__ - Decimal number you want to convert. Write an integer. <br>
* __base__ - The base you want to convert. Write an integer. <br>
<br>
2. 'toDecimal(num, base)' <br>
Convert a non-decimal number into a decimal number. <br>
###**PARAMETERS:**
* __num__ - Non-Decimal number you want to convert. Write an integer. <br>
* __base__ - The base of the 'num'. <br>
<br>
3. 'convertBase(num, before_base, after_base)' <br>
Convert a number into the other number with the other base. <br>
###**PARAMETERS:**
* __num__ - A number you want to convert. Write an integer. <br>
* __before_base__ - The present base. <br>
* __after_base__ - The base you want to convert. Write an integer. <br>
<br>
---
<br>
##**WARNING**
**It is not work if the base value is 0**
