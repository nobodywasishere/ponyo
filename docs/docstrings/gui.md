<!-- markdownlint-disable -->

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/gui.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `gui`




**Global Variables**
---------------
- **font**
- **button_size**
- **layout**

---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/gui.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `currCode`

```python
currCode(sim, low: int = -5, high: int = 5) → str
```

String showing surrounding code to PC 



**Args:**
 
 - <b>`sim`</b> (ponyo.Simulator):  Current Simulator instance 
 - <b>`low`</b> (int, optional):  Number of lines before PC. Defaults to -5. 
 - <b>`high`</b> (int, optional):  Number of lines after PC. Defaults to 5. 



**Returns:**
 
 - <b>`str`</b>:  Section of code arround PC 


---

<a href="https://github.com/nobodywasishere/ponyo/blob/master/ponyo/gui.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `gui`

```python
gui(sim, isa)
```

Runs an interactive GUI for the simulator using PySimpleGUIQt 



**Args:**
 
 - <b>`sim`</b> (ponyo.Simulator):  Starting Simulator with loaded imem/dmem 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
