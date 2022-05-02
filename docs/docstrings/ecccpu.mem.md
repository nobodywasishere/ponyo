<!-- markdownlint-disable -->

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/mem.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ecccpu.mem`






---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/mem.py#L1"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `mem`
Memory class for the EccCPU ISA 

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/mem.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(dmem=[], dmemNum=16)
```

Init the memory 



**Args:**
 
 - <b>`dmem`</b> (list, optional):  Initial ram. Defaults to []. 
 - <b>`dmemNum`</b> (int, optional):  Length of zeroed ram when `dmem` is default. Defaults to 16. 




---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/mem.py#L89"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `mem2str`

```python
mem2str()
```

For GUI, returns a string of the values stored in memory 



**Returns:**
 
 - <b>`str`</b>:  Formatted memory values 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/mem.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `pcfl2str`

```python
pcfl2str()
```

For GUI, returns a string of the values stored in PC and flags 



**Returns:**
 
 - <b>`str`</b>:  Formatted PC and flag values 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/mem.py#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `print`

```python
print()
```

Prints the data in the registers and memory to stdout 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/mem.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `ram_read`

```python
ram_read(addr: int) → int
```

Read from ram 



**Args:**
 
 - <b>`addr`</b> (int):  Byte-address to read from 



**Returns:**
 
 - <b>`int`</b>:  Stored value 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/mem.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `ram_write`

```python
ram_write(value: int, addr: int)
```

Write to ram 



**Args:**
 
 - <b>`value`</b> (int):  Value to be stored 
 - <b>`addr`</b> (int):  Byte-address to store at 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/mem.py#L110"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reg2str`

```python
reg2str()
```

For GUI, returns a string of the values stored in registers 



**Returns:**
 
 - <b>`str`</b>:  Formatted register values 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/mem.py#L53"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `regs_read`

```python
regs_read(reg: str) → int
```

Read the value stored in a register 



**Args:**
 
 - <b>`reg`</b> (str):  Register string (e.g. `r9`, `1`) 



**Returns:**
 
 - <b>`int`</b>:  Value stored in register 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/mem.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `regs_write`

```python
regs_write(reg: str, value: int)
```

Write a value to a register 



**Args:**
 
 - <b>`reg`</b> (str):  Register string (e.g. `r9`, `1`) 
 - <b>`value`</b> (int):  Value to store 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/mem.py#L137"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reset`

```python
reset()
```

Resets the memory to initialized values 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
