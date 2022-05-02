<!-- markdownlint-disable -->

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/mem.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `legv8.mem`






---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/mem.py#L1"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `mem`
Memory class for the LEGv8 ISA 

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/mem.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(dmem: list = [], dmem_num: int = 512)
```

Initialize the memory 



**Args:**
 
 - <b>`dmem`</b> (list, optional):  Initial data memory. Defaults to []. 
 - <b>`dmem_num`</b> (int, optional):  Length of zeroed data memory when `dmem` is default. Defaults to 512. 




---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/mem.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dmem_read`

```python
dmem_read(addr: int, offset: int, size: int) → int
```

Read from data memory 



**Args:**
 
 - <b>`addr`</b> (int):  Address to start from 
 - <b>`offset`</b> (int):  Offset from address 
 - <b>`size`</b> (int):  Number of bytes to read 



**Returns:**
 
 - <b>`int`</b>:  Value stored in data memory 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/mem.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dmem_write`

```python
dmem_write(value: int, addr: int, offset: int, size: int)
```

Write to data memory 



**Args:**
 
 - <b>`value`</b> (int):  Value to be stored 
 - <b>`addr`</b> (int):  Address to start from 
 - <b>`offset`</b> (int):  Offset from address 
 - <b>`size`</b> (int):  Number of bytes to write 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/mem.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `mem2str`

```python
mem2str() → str
```

For GUI, returns a string of the values stored in memory 



**Returns:**
 
 - <b>`str`</b>:  Formatted memory values 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/mem.py#L136"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `pcfl2str`

```python
pcfl2str() → str
```

For GUI, returns a string of the values stored in PC and flags 



**Returns:**
 
 - <b>`str`</b>:  Formatted PC and flag values 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/mem.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `print`

```python
print()
```

Prints the data in the registers and memory to stdout 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/mem.py#L123"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reg2str`

```python
reg2str() → str
```

For GUI, returns a string of the values stored in registers 



**Returns:**
 
 - <b>`str`</b>:  Formatted register values 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/mem.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `regs_read`

```python
regs_read(reg: str) → int
```

Read the value stored in a register 



**Args:**
 
 - <b>`reg`</b> (str):  Register string (e.g. `X9`, `X11`) 



**Returns:**
 
 - <b>`int`</b>:  Value stored in register 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/mem.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `regs_write`

```python
regs_write(reg: str, value: int)
```

Write a value to a register 



**Args:**
 
 - <b>`reg`</b> (str):  Register string (e.g. `X9`, `X11`) 
 - <b>`value`</b> (int):  Value to store 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/mem.py#L146"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reset`

```python
reset()
```

Resets the memory to initialized values 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
