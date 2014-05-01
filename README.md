```shell
pip install git+https://github.com/natb1/test_data.git
```
... a collection of domain models and domain objects for testing purposes.

For example, the "zoo" domain:
```python
>>> import test_data.zoo
>>> test_data.zoo.geese # doctest: +NORMALIZE_WHITESPACE
(< grace, the goose that likes < penny the fat penguin > >, 
 < gale, the goose that likes < prince the cool penguin > >,
 < ginger, the goose that likes < puck the boring penguin > >)

```
