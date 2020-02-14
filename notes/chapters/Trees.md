#### Inorder Traversal
```python
def dfs(curr):
    if curr.left: dfs(curr.left)
    vals.append(curr.val)
    if curr.right: dfs(curr.right)
```


#### Pre Order Traversal
```python
def dfs(curr):
    vals.append(curr.val)
    if curr.left: dfs(curr.left)
    if curr.right: dfs(curr.right)
```

#### Post Order Traversal
```python
def dfs(curr):
    if curr.left: dfs(curr.left)
    if curr.right: dfs(curr.right)
    vals.append(curr.val)
```