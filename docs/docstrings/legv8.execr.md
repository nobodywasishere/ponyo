<!-- markdownlint-disable -->

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/execr.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `legv8.execr`





---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/execr.py#L1"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `immu2int`

```python
immu2int(immu: str) → int
```

Converts an immediate value into an integer 



**Args:**
 
 - <b>`immu`</b> (str):  Immediate value (e.g. `#10`, `0x03`, `b00101`) 



**Returns:**
 
 - <b>`int`</b>:  Value stored in immediate 


---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/legv8/execr.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `execr`

```python
execr(mem, instr: dict)
```

Executes the instruction on the simulator state for the LEGv8 ISA 



**Args:**
 
 - <b>`mem`</b> (legv8.mem):  ISA memory class 
 - <b>`instr`</b> (dict[str, str]):  Decoded instruction 



**Raises:**
 
 - <b>`Exception`</b>:  If an unsupported instruction is executed 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
