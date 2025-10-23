# **Signal**

```python
from CheeseSignal import Signal
```

## **`self.receivers: OrderedDict[str, Receiver]`**

连接的接收器

## **`self.sendNum: int`**

发送总数

## **`def getReceiver(self, key: str) -> Receiver | None`**

获取接收器

## **`def getReceiver(self, fn: Callable) -> Receiver | None`**

获取接收器

## **`def connect(self, fn: Callable, key: str | None = None, *, index: int = -1, insert: tuple[str | Callable | Receiver, Literal['BEFORE', 'AFTER']] | None = None, runType: Literal['SEQUENTIAL', 'PARALLEL', 'NO_BLOCK'] = 'SEQUENTIAL', receiveNum_expected: int = 0, autoRemove: bool = False)`**

```python
from CheeseSignal import Signal

signal = Signal()

def handler():
    print('Handler executed')
signal.connect(handler)
```

连接接收器

- **Args**

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

    - **index**

        插入位置索引（仅对runType为SEQUENTIAL的接收器有效）

    - **insert**

        插入位置；若设置index，则忽略此参数（仅对runType为SEQUENTIAL的接收器有效）

        - **BEFORE**

            插入到指定接收器之前

        - **AFTER**

            插入到指定接收器之后

## **`def connect(self, key: str | None = None, *, index: int = -1, insert: tuple[str | Callable | Receiver, Literal['BEFORE', 'AFTER']] | None = None, runType: Literal['SEQUENTIAL', 'PARALLEL', 'NO_BLOCK'] = 'SEQUENTIAL', receiveNum_expected: int = 0, autoRemove: bool = False)`**

```python
from CheeseSignal import Signal

signal = Signal()

@signal.connect()
def handler():
    print('Handler executed')
```

连接接收器

- **Args**

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

    - **index**

        插入位置索引（仅对runType为SEQUENTIAL的接收器有效）

    - **insert**

        插入位置；若设置index，则忽略此参数（仅对runType为SEQUENTIAL的接收器有效）

        - **BEFORE**

            插入到指定接收器之前

        - **AFTER**

            插入到指定接收器之后

## **`def disconnect(self, key: str)`**

断开接收器

## **`def disconnect(self, fn: Callable)`**

断开接收器

## **`def disconnect(self, receiver: Receiver)`**

断开接收器

## **`def disconnectAll(self)`**

断开所有接收器

## **`def reset(self)`**

重置信号系统

## **`def send(self, key: str, *, args: tuple[any, ...], kwargs: dict[str, any])`**

发送信号

- **Args**

    - **args**

        *args参数

    - **kwargs**

        **kwargs参数

## **`def send(self, keys: Iterable[str], *, args: tuple[any, ...], kwargs: dict[str, any])`**

发送信号

- **Args**

    - **args**

        *args参数

    - **kwargs**

        **kwargs参数

## **`def send(self, *, args: tuple[any, ...], kwargs: dict[str, any])`**

发送信号

- **Args**

    - **args**

        *args参数

    - **kwargs**

        **kwargs参数

## **`async def async_send(self, key: str, *, args: tuple[any, ...], kwargs: dict[str, any])`**

发送信号

- **Args**

    - **args**

        *args参数

    - **kwargs**

        **kwargs参数

## **`async def async_send(self, keys: Iterable[str], *, args: tuple[any, ...], kwargs: dict[str, any])`**

发送信号

- **Args**

    - **args**

        *args参数

    - **kwargs**

        **kwargs参数

## **`async def async_send(self, *, args: tuple[any, ...], kwargs: dict[str, any])`**

发送信号

- **Args**

    - **args**

        *args参数

    - **kwargs**

        **kwargs参数
