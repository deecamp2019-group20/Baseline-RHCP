# Baseline-RHCP

原型链接：[CSDN](https://blog.csdn.net/sm9sun/article/details/70787814)

## 使用说明

- 先运行
    ```bash
    cd build
    cmake ..
    ```

- 会根据自己系统环境在`build`创建相应项目，然后

    - Windows下的话，用vs打开`env.sln`，然后build一个`x64`的`Release`方案即可

    - \*Unix 没试过

- 最后，看`run.py`的`自娱自乐`函数，就是自己和自己对抗，里面有基本的接口调用。如果想看和AI对接的例子，看一下`run.py`里的`ai_play`函数即可。

- 其他不懂得，来353-3找我
