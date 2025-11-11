# **Receiver**

正常情况下不需要手动创建Receiver对象，可以通过Signal的connect方法自动创建

```python
from CheeseSignal import Receiver
```

## **`def __init__(self, fn: Callable, key: str | None = None, *, run_type: Literal['SEQUENTIAL', 'PARALLEL', 'NO_BLOCK'] = 'SEQUENTIAL', receive_num_expected: int = 0, auto_remove: bool = False)`**

- **Args**

    - **fn**

        接收器函数

    - **key**

        接收器键值，若不设置则自动生成一个uuid格式的字符串

    - **run_type**

        运行类型

        - **SEQUENTIAL**

            顺序执行，等待函数执行完成后再执行下一个函数

        - **PARALLEL**

            并行执行，等待所有函数执行完成后再继续

        - **NO_BLOCK**

            非阻塞执行，函数在后台执行，不等待函数执行完成

    - **receive_num_expected**

        期望接收总数

    - **auto_remove**

        是否在达到期望接收总数后自动移除接收器

## **`self.run_type: Literal['SEQUENTIAL', 'PARALLEL', 'NO_BLOCK']`**

运行方式

- **SEQUENTIAL**

    顺序执行，等待函数执行完成后再执行下一个函数

- **PARALLEL**

    并行执行，等待所有函数执行完成后再继续

- **NO_BLOCK**

    非阻塞执行，函数在后台执行，不等待函数执行完成

## **`self.receive_num_expected: int`**

期望接收总数

## **`self.receive_num: int`**

接收总数

## **`self.auto_remove: bool`**

是否在达到期望接收总数后自动移除接收器

## **`self.receive_num_remaining: int`**

剩余接收总数

## **`self.is_active: bool`**

是否处于激活状态

## **`def reset(self)`**

重置统计数据
