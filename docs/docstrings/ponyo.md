<!-- markdownlint-disable -->

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ponyo.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ponyo`





---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ponyo.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `main`

```python
main()
```






---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ponyo.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Simulator`
ISA Simulator 

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ponyo.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(mem, decode, execr, imem: list, dmem: list = [])
```

Initializes simulator 



**Args:**
 
 - <b>`mem`</b> (ISA.mem):  mem class for the chosen ISA 
 - <b>`decode`</b> (ISA.decode):  decode function for the chosen ISA 
 - <b>`execr`</b> (ISA.execr):  execute function for the chosen ISA 
 - <b>`imem`</b> (list):  Instruction memory as a list, split on newlines 
 - <b>`dmem`</b> (list, optional):  Initial data memory. Defaults to []. 




---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ponyo.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run()
```

Step through the code until it reaches the end 

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/ponyo.py#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `step`

```python
step()
```

Execute a single instruction 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
