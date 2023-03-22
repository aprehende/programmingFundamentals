
<img src="https://drive.google.com/uc?export=view&id=1AJJE7Vp-jCW4pjp79w7VVOSGMldbdb6e" width="300" style="float:right;" />

# Primitive Data Types

Primitive data types are the basic representation of data, which can be defined and manipulated.

Among the main ones we have:

- **Boolean (bool):** It's the representation of the bit, the minimum unit of data, whose value can be 0 or 1, true or false.
- **Character (char):** It's the representation of a character, whose value can be alphanumeric, symbolic and more.
- **String (string):** It's the union of two or more characters, whose value can represent a phrase, word, or symbology.
- **Integer (int):** It's the representation of a number that can only be an integer.
- **Float (float):** It's the representation of a number with decimals

## **In each programming language there is a variety of primitive data types, which derive from the main ones, I invite you to investigate the primitive data types of your preferred language.**

In a **strongly typed language**, it's necessary to understand how the type assignment affects the storage capacity of the data.
As we already know, a variable is a data store, which through an identifier allows us to access its value from any part of our program.

But from the physical point of view, when we define a variable, we are reserving a space in the **RAM**. Depending on the type of data, this space can be very small or very large.

Let's imagine a **RAM**, like a group of boxes where we will store our data. Each one of these little boxes has a specific size (1 byte / 8 bits).

<img src="https://drive.google.com/uc?export=view&id=1FN5-8Olv86dtptcw4Ac-Buh3DxDxiDvP"/>

When we declare a variable we are reserving a specific number of little boxes, for example if in C# we use the byte data type, we will be reserving a little box.

<img src="https://drive.google.com/uc?export=view&id=1xgq4RYzZeGWXvp4ea1VHWxNTy_tmKvfF"/>

If we choose the int data type, we will be reserving 4 boxes.

<img src="https://drive.google.com/uc?export=view&id=1dmv97taF2hD2bX9CA2hepr9clEpPgg6z"/>

The value that we store in the variable could occupy all the space of the cells or a fraction of it. That is why a data type has a minimum value and a maximum value, for example if the value 255 is stored in the variable declared with byte, it will completely fill the reserved box.

<img src="https://drive.google.com/uc?export=view&id=1yYMot2GHPTc60P5tihjv8Xak-A4fAR3U"/>

But if the value 127 is stored, it will fill almost half of the box and the rest will go to waste. Therefore, in a strongly typed language it is very important to choose the best way to declare the variable according to the context, *so as not to waste **RAM.***

<img src="https://drive.google.com/uc?export=view&id=1dSvF-yAIl6XvOsrrBXo4SyauH5y_jxDT"/>

Let's give an example, if in our program we need to store the age of a person, we must analyze the following:

- It can't be negative.
- It is unlikely that the value will exceed 100
- It is counted, therefore it is an integer

With this premise we can better choose the type of data, which in this case would be byte, because the maximum value of a byte is 255 and an age will never exceed that number or fill half the box.

But if we decide to define it as uint, our variable will behave in the same way, but it will have more reserved space and therefore garbage space that will never be used.

<img src="https://drive.google.com/uc?export=view&id=1JzjjxYc3sJ1zj-TIoPa_4s9jdL7pmLjD"/>

**And remember that in Aprehende, you really learn**
