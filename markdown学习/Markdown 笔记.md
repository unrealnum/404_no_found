# Markdown 笔记



## 个人小记

**1. Typora语法与github语法，标准markdown语法均有出入**

**2. Typora 可以用类似代码的方法来实现插入网站，图片，甚至数学公式，这大大简化了知识的记录时间，提高了学习效率**



**Pandoc！**

**正在学习图片在github上的正常插入。。。。。。**



链接：[1](https://www.zhihu.com/question/385854845) 

## 语法

**shift +F12 进入开发者（前端）模式**

### 划线

* 二级及以上的标题在typora中自带不同的下划线

* ------------------------

* （如上）输入2个以上的-

* 在标准语法中的下划线不完全与typora相同

* 删除线（~~adgflsfdnmfkds~~）

* 下划线<u>jhdsfkldksjfflshfk</u>（ctrl +u）

### 插入

* 图片

* ![]()(ctrl shift l)

* ! [] ()

* 代码`ehufjsdbk`

* url   [url]()

  * 或者：[url][1]

  * ctrl+k

  * [1]:https://www.baidu.com

* 引用（>）

  * > hdsfk

* 转义\

* 

### 字体处理

* **加粗**
* 标题（ctrl +1-6）

* ==高亮==

* span!mode

  * ```html
    <span style='color:文字颜色;background:背景颜色;font-size:文字大小;font-family:字体;'>文字</span>
    ```

* [color:red]变色（需要前端的知识）

  * 或者......<font color=blue>文字文字文字</font>

* *斜体*

* _djkf_或者是这样（两个_）

* <br>换行符

* 代码`dshil`

* 居中 <center>fdjfdj<center>

 <center>fdjfdj<center>

* 左！

 <left>fdjfdj<left>

* 

* 

### 制表

* 无序列表：* space（+ - 等也可）

* 有序列表：在typora中直接敲入1.与空格即可

* 通过tab与tab+shift来进退

  * 1
    * 2
      * 3
        * 4
      * 3

* 代码块：输入2个以上的~（同下）

* ~~~
  
  ~~~

* 表格

* 公式块（敲两个$+回车）
  $$
  sqrt(a+b)=12
  $$

* 表格

* | dskjfkdn |      |
  | -------- | ---- |
  |          |      |
  |          |      |
  | fdhfj    |      |
  |          |      |

* 任务列表-+space+[space]+space

* 或者无序列表+[ ]<-中间有space！

* [x] clear markdown

*  内联数学公式

* TOC!

[TOC]

* 脚注

AAAAAAAAAAAAAAA[^DNJSKFHKJSDJKSJD]

* sequence(```+words)

[detail](http://flowchart.js.org/)

```sequence
```

* flow(```+words)

[detail](http://flowchart.js.org/)

```flow
```

* mermaid(```+words)

[detail](http://flowchart.js.org/)

```mermaid
```



### 快捷键

| 快捷键      | 作用               | 快捷键       | 作用           |
| ----------- | ------------------ | ------------ | -------------- |
| Ctrl+1      | 一阶标题           | Ctrl+B       | 字体加粗       |
| Ctrl+2      | 二阶标题           | Ctrl+I       | 字体倾斜       |
| Ctrl+3      | 三阶标题           | Ctrl+U       | 下划线         |
| Ctrl+4      | 四阶标题           | Ctrl+Home    | 返回Typora顶部 |
| Ctrl+5      | 五阶标题           | Ctrl+End     | 返回Typora底部 |
| Ctrl+6      | 六阶标题           | Ctrl+T       | 创建表格       |
| Ctrl+L      | 选中某句话         | Ctrl+K       | 创建超链接     |
| Ctrl+D      | 选中某个单词       | Ctrl+F       | 搜索           |
| Ctrl+E      | 选中相同格式的文字 | Ctrl+H       | 搜索并替换     |
| Alt+Shift+5 | 删除线             | Ctrl+Shift+I | 插入图片       |



* 通过快捷键Command+F（Windows：Ctrl+F）调出查找面板，在 查找面板上可以设置是否“区分大小写”和是否“查找整个单词”
* 打字机模式：光标始终位于屏幕的中间。
* 专注模式：只高亮显示光标所在行，其余内容全部变灰
* 全屏：最大化文件窗口，排除其他软件的干扰。
* reveal.js : 好用的PPT工具
* gitbook?!
* [markdown语法大全](https://blog.csdn.net/m0_46168848/article/details/120379487?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522163642180116780271540273%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=163642180116780271540273&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-120379487.pc_search_result_hbase_insert&utm_term=typora+%E8%A1%8C%E5%88%97%E5%BC%8F&spm=1018.2226.3001.4187)

### 数学语法

* #### 矩阵

$$
D_n = \left|
\matrix{ 
1         &      1    & \cdots &1     \\  
x_1       &    x_2    &   ...  &x_n    \\
x^2_1     &     x^2_2 &   ...  & x^2_n \\ 
\vdots    &    \vdots & \ddots &\vdots \\
x_1^{n-1} & x_2^{n-1} &    ... & x_n^{n-1}
}
\right|
			
					
$$

* 上下标

$$
v_{dfgshkjfklksd}
$$

$$
v^{dslkgjnldkfjg}
$$

