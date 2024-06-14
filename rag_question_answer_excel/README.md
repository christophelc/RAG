# setup
```pip install -r requirements.txt```

Download a lamafile locally, for example llava and launch it.

# test
```python rag_test.py```

```Elapsed time:  22.070330381393433  seconds
 I know the following flowers:

1. Yellow Rose: symbolizes friendship and happiness
2. Gardenia: known for its delicate petals and sweet fragrance
3. Hydrangea: known for its large, round blooms and commonly used in floral arrangements.
```

# execute
sh run.sh

## Remarks

The result is not efficient with these data for several reasons:
- the correlation is weak whereas the word 'flower' is present for each entry of the database. It means maybe we should rework the embedding part.
- we should rework the prompt

Here the problem cannot be solve by rewriting the FAQ.
