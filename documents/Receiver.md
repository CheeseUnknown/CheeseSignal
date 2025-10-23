# **Receiver**

正常情况下不需要手动创建Receiver对象，可以通过Signal的connect方法自动创建

```python
from CheeseSignal import Receiver
```

## **`def __init__(self, fn: Callable, key: str | None = None, *, runType: Literal['SEQUENTIAL', 'PARALLEL', 'NO_BLOCK'] = 'SEQUENTIAL', receiveNum_expected: int = 0, autoRemove: bool = False)`**

- **Args**

    - **fn**

        接收器函数

    - **key**

        接收器键值，若不设置则自动生成一个uuid格式的字符串

    - **runType**

        运行类型

        - **SEQUENTIAL**

            顺序执行，等待函数执行完成后再执行下一个函数

        - **PARALLEL**

            并行执行，等待所有函数执行完成后再继续

        - **NO_BLOCK**

            非阻塞执行，函数在后台执行，不等待函数执行完成

    - **receiveNum_expected**

        期望接收总数

    - **autoRemove**

        是否在达到期望接收总数后自动移除接收器

## **`self.runType: Literal['SEQUENTIAL', 'PARALLEL', 'NO_BLOCK']`**

运行方式

- **SEQUENTIAL**

    顺序执行，等待函数执行完成后再执行下一个函数

- **PARALLEL**

    并行执行，等待所有函数执行完成后再继续

- **NO_BLOCK**

    非阻塞执行，函数在后台执行，不等待函数执行完成

## **`self.receiveNum_expected: int`**

期望接收总数

## **`self.receiveNum: int`**

接收总数

## **`self.autoRemove: bool`**

是否在达到期望接收总数后自动移除接收器

## **`self.receiveNum_remaining: int`**

剩余接收总数

## **`self.is_active: bool`**

是否处于激活状态

## **`def reset(self)`**

重置统计数据
