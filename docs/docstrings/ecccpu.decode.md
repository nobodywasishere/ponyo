<!-- markdownlint-disable -->

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/decode.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ecccpu.decode`





---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/decode.py#L4"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `findSymbols`

```python
findSymbols(imem: list[str]) → dict[str, str]
```

Find the symbols in the instruction memory, e.g. `main:` 



**Args:**
 
 - <b>`imem`</b> (list[str]):  Instruction memory 



**Returns:**
 
 - <b>`dict[str, int]`</b>:  Dictionary of symbols corresponding with their line numbers 


---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ecccpu/decode.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `decode`

```python
decode(pc: int, assembly: str, sym: dict[str, int]) → dict[str, str]
```

Decodes each instruction into a simpler format, replacing symbols, register aliases, and removing comments for the EccCPU ISA 



**Args:**
 
 - <b>`pc`</b> (int):  Program counter 
 - <b>`assembly`</b> (str):  Instruction to decode 
 - <b>`sym`</b> (dict[str, int]):  Symbol dictionary 



**Returns:**
 
 - <b>`dict[str, str]`</b>:  Decoded instruction 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
