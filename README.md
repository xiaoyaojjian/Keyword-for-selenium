关键字驱动框架
===================
关键字驱动框架是一种功能自动化测试框架，它也被称为表格驱动测试或者基于动作字的测试。关键字驱动的框架的基本工作是将测试用例分成四个不同的部分。首先是测试步骤（Test Step），二是测试步骤中的对象（Test Object），三是测试对象执行的动作(Action)，四是测试对象需要的数据（Test Data）。

> Test Step：是一个小的测试步骤的描述或者测试对象的一个操作说明。

> Test Object：是指页面对象或元素，就像用户名、密码。

> Action：指页面操作的动作，打开浏览器，点击一个按钮，文本框输入一串文本等。

> Test Data：是任何对象操作时所需要的值，就像用户名、密码进行输入时的输入内容。


## 组件结构

 1. Excel Sheet: 是我们存放测试用例（Test Case）、测试步骤(Test Step)、测试对象(Test Object)和操作动作(Action)的关键字驱动数据(TestData)表。
 2. Object Repository: 是个属性文件，用来存放HTML应用中的一些元素属性（可看做元素的对象仓库），该文件与测试对象进行链接。
 3. Keyword Function Library: 这是一个方法库文件，这个组件在关键字驱动框架中起着很重要的作用，它主要存放执行的Action，每一个操作动作都可以从这个文件中调用。
 4. Data Sheet: Excel表格存储，测试对象在执行操作时所需要的数据值。
 5. Execution Engine: 是唯一的测试脚本，它包含了所有的代码，通过关键字框架从Excel表格、方法库、属性文件中进行推动测试。

----------
通用工作流程图
-------------
![enter image description here](http://images.cnitblog.com/blog/686364/201411/181003531911864.png)

##Demo 结构

* DataEngine  存放的data.xls文件

* config      存放关键字方法定义脚本 actionKeyword.py

* public      存放Base.py 重定义webdriver的一些方法和自定义方法

* result      存放生成的测试结果目录

* ExecutionEngine.py  是测试脚本的入口

###表格解析

![enter image description here](https://dn-coding-net-production-static.qbox.me/e5b7181d-9648-4c42-ad34-98d022d37fd5.png)

#伪代码

For  功能 in 功能列表:

    If 功能.Runmode == Y:
    
            TCID = 功能.TCID
            
            for 用例 in 用例列表:
            
    	        if 用例.TCID == TCID && 用例.Runmode == Y:
    	        
                    for  步骤 in 步骤列表:
                    
    		        if 步骤.TCID == TCID:
    		        
    	                do 判断关键字，进行执行
    	                
- - -
[QQ交流群：342294158](http://shang.qq.com/wpa/qunwpa?idkey=5e4d5bfec6c8b10f9b08fa37ea7870922cf4d08797de9657c09a1b70d255710e)
