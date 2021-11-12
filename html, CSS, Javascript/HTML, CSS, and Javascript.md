# HTML, CSS, and JavaScript



## HTML

#### 特点与常用标签

- **标签化编程**

- 块级元素与内联元素

  - 包成一个“块”

    - <h1>块</h1>

  - 文本的“修饰”

    - <b>修饰</b>

- 标题和字号大小从H1~H6<title>

- <div id="xxx">
      <h3>div!</h3>
  </div>

- <p>分段

- <b>加粗

- <i>斜体

- <sup><sub>上标与下标

- <br>换行

- <hr>一条水平线

- 加粗.强调<strong>

- <em>斜体

- 较短的引用和较长的引用。

  - <blockquote>

  - <q>

- <abbr>首字母缩写

- <cite>

  - 引用，会被标注为斜体。

- <dfn>

  - 用于表示一个新术语的定义。

- <address>

  - 设计者的地址信息

- <ins>

  - 下划线

- <del><s>

  - 删除线

- <head><body>

  #### 列表

- <ol>有序列表

  - <li>起始标签和结束标签

- <ul>无序列表

- <dl>定义列表

  - <dt>

  - <dd>

- 嵌套列表

#### 网站链接，表格与图像

- <a>建立网站之间的链接。

  - 用法<a href="xxx">XXX</a>

  - 如果没有指定文件名，会自动返回到index

  - 链接到相同的文件夹中文件不需要加前缀

  - 链接到子文件夹，需要加一个文件名与/

  - 链接到父文件夹需要加上.../

  - 链接到孙子或者祖父，甚至更高更低级的文件夹，要加上多个xxx/或.../

  - 链接到电子邮件：mailto :前缀

  - 在新窗口中打开 后缀target="xxx"
    - 一般来说为_blank

- 通过ID返回到页面的某个特定位置

  - 使用方法:<id="xxx">

  - 建立链接:<a href="#xxx">

  - 链接到其他页面的某个特定位置，利用套娃就可以了

- 往网站里面插入图像

  - 不论如何还是得注意版权问题

  - <img src>

    - img没有结束标签

    - src: 相对url

    - alt: 如果无法查看

    - title特性在这里可以使用

  - 指定图片的宽度和长度

    - height

    - width

    - 也可以用css

    - 在段落之前，段落的起始处和段落之中插入图片会造成不同的影响。

  - <figure>说明图像(把图像和图像说明框起来)

  - <figcaption>图片的说明(放在上述的框里面)

- 插入表格

  - <table>

  - <tr></tr>代表一行的开始

  - <td></td>每个单元格

  - <th></th>表示列或行的标题

    - <th scope="row">

    - row/col这是一个行/列标题

    - colspan=""表明单元格所要跨越的列数

    - rowspan=""表明单元格所要跨越的行数

  - 长表格

    - thead
      - 表格的标题
    - tbody
      - 表格主体
    - tfoot
      - 表格的脚注

#### 表单

#### 引入音频与视频

* /<video>
* /<audio>
* **flash 已经几近退出！**



## CSS



<center><h3><font color=purple>"块式"编程</font></h3></center>



**<font color=red>CSS将样式规则与HTML相关联！</font>**

**CSS==<font color=orange>选择器</font>+<font color=oran>声明</font>**

```css
p={
	font-family: Arial;
}
```

**声明==<font color=red>属性</font>+<font color=orange>值</font>**

#### 链接外部CSS

* <link href="xxx" type="test/css" ref="xxxx"/>

在HTML内的CSS

* <style>
      
  </style>

#### 选择器

见图片（链接未应用！）

* <font color="blue">作用优先级</font>
  * 就近原则
  * 具体性原则
  * 重要性

#### 继承

> 继承特性也算老朋友了

#### 外部样式表

> 就和库的封装一样，这样在大规模代码中更方便维护





## JavaScript



#### JavaScript使用

* JavaScript代码可以直接嵌在网页的任何地方，不过通常我们 都把JavaScript代码放到 <head> 中
* 由 &lt</script&gt； 包含的代码就是 JavaScript代码，它将直接被浏览器执行。
* 把JavaScript代码放入一个单独的 .js 文件中更利于维护代 码，并且多个页面可以各自引用同一份 .js 文件。
* 让JavaScript引擎自动加分号在某些情况下会改变程序 的语义，导致运行结果与期望不一致。
* 变量命名等其实与C等相差无几，或者。。。更像python一点？
* JavaScript引擎有一个在行末自动添加分号的机制
  * ......呵呵（无奈（`”C语言的猜测“`）——zi zuo cong ming）



#### 函数？

* console.log(a)：查看一个变量的内容
* alert：消息反馈
* var 定义一个变量
* `function abs(x)`定义函数
* `var abs = function (x)`定义一个匿名函数，可通过abs调用
* KEY WORD：`arguments`只在函数内部起作用，并且永远指向当前函数的调用者传入的所有参数。
* `rest`参数只能写在最后，前面用` ... `标识，从运行结果可知， 传入的参数先绑定 a 、 b ，多余的参数以数组形式交给变量 `rest`
* 如果传入的参数连正常定义的参数都没填满，rest 参数会接收一个空数组.

##### “高阶函数”~~（套娃函数）~~

* 一个函数可以接收另一个函数作为参数
* map() 作为高阶函数，事实上它把运算规则抽象了

##### this

> 个人认为这是js中一个重要的特性

##### generator（生成器）

> ES6标准引入的新的数据类型。一个 generator看上去像一个函数，但可以返回多次
>
> 又是一个重要特性
>
> 定义时加一个*

#### 包装对象

> 过分了，这也抄（java）

* var b = new Boolean(true)

* 类型已经变为 object 了

* 用类型比较’===‘返回False

**函数在执行过程中，如果没有遇到 return 语句（函数末尾 如果没有 return ，就是隐含的 return undefined！**



#### 变量与数据结构

> 感觉没有做很大的区分，有时一个var能解决所有问题

```
123; // 整数123
0.456; // 浮点数0.456
1.2345e3; // 科学计数法表示1.2345x1000，等同于1234.5
-99; // 负数
NaN; // NaN表示Not a Number，当无法计算结果时用NaN表示
Infinity; // Infinity表示无限大，当数值超过了
JavaScript的Number所能表示的最大值时，就表示为Infinity
null 空类型
underfined 
```

* 运算符同C。
* if 与while for等('几乎完全相同'（for...in例外)
* 数组定义相同：`var arr = [1, 2, 3.14, 'Hello', null, true]`
  * 什么类型都能放！
* 索引超出了范围则返回undefined。
* JavaScript的对象是一组由键-值组成的无序集合（这货也是个集合与映射）

```javascript
var JoJo{
	name: 'kongjojotailang';
	age: 18;
	stand name: 'Star platinum';
	ability: 'the world';
	tags; ['无敌','欧拉欧拉欧拉欧拉......']
}
```

获取一个对象的属性用 对象变量.属性名 的方法

set相关用法

```javascript
var m = new Map(); // 空Map
m.set('Adam', 67); // 添加新的key-value
m.set('Bob', 59);
m.has('Adam'); // 是否存在key 'Adam': true
m.get('Adam'); // 67
m.delete('Adam'); // 删除key 'Adam'
m.get('Adam'); // undefined

摘自廖雪峰相关教材
ES6标准
```

遍历 Array 可以采用下标循环，遍历 Map 和 Set 就无法使 用下标。

> 您搁着卡迭代器呢！(ES6)

` iterable`： 具有 iterable 类型的集合可以通过新的 for ... of 循环 来遍历。

* for ... in 遍历的实际上是<font color=red>**对象的属性名称**</font>。
* for ... of只循环<font color=red>**集合本身的元素**</font>
* iterable 内置的 forEach 方 法，它接收一个函数，每次迭代就自动回调该函数。

> ES5.1

* `person.name;`
* `in`检测...是否具备XX属性。
* ` for ... in`循环对象检查

* 字符串： JavaScript的字符串就是用 '' 或 "" 括起来的字符表示
  * 转义等处理与C相似
  * 要获取字符串某个指定位置的字符，使用类似Array的下标操 作
    * ‘字符数组（滑稽）’
    * **字符串是<font color=red>不可变</font>的**
    * JavaScript为字符串提供了一些常用方法，调用这些方 法本身不会改变原有字符串的内容，而是**返回一个新字符串**
      * ??? 有点与python等语言不同了
      * `toUpperCase() `把一个字符串全部变为大写
      * `toLowerCase() `把一个字符串全部变为小写
      * `indexof()` 会搜索指定字符串出现的位置
      * `substring()` 返回指定索引区间的子串
      * 照搬python？
      * python才是照搬的？
      * **统一标准？？？**（标准化思想）
* 数组：可以包含任意数据类型，并通过索引来访 问每个元素。
  * `arr.length; `获取长度
  * 直接给 Array 的 length 赋一个新的值？（+underfined）
  * 通过索引赋值时，索引超过了范围，同样会引起数组大小的变化
  * `indexof`
  * `slice() `就是对应String的 substring() 版本
  * `push()` 向 Array 的末尾添加若干元素
  * `pop()` 把Array 的最后一个元素删除掉
  *  `unshift() `往 Array 的头部添加若干元素
  * `shift()`把 Array 的第一个元素删掉
  * sort（快排真香）
  * `reverse() `反转字符串
  * `splice()`可以从指定的索引开始删除若干元素，然后再从该位置添加若干元素
  * `concat()`把当前的 Array 和另一个 Array 连接起 来，并返回一个新的 Array
  * `join() `把当前 Array 的每 个元素都用指定的字符串连接起来，然后返回连接后的字符串
  * 多维数组
  * `filter() `把传入的函数依次作用于每 个元素，然后根据返回值是 true 还是 false 决定保留还是丢弃该元素。
* 

#### 严格模式

* 'use strict';

#### 日期

* `new date`

```javascript
var d = new Date(1435146562875);
d.toLocaleString(); // '2015/6/24 下午7:49:22'，
本地时间（北京时区+8:00），显示的字符串与操作系统设定的
格式有关
d.toUTCString(); // 'Wed, 24 Jun 2015 11:49:22
GMT'，UTC时间，与本地时间相差8小时
```

```
if (Date.now) {
 alert(Date.now()); // 老版本IE没有now()方法
} else {
 alert(new Date().getTime());
}
```

`module.exports = greet;`

> 模块化输出



## HTML，CSS，JavaScript三者间的关系

