# git personal learning notebook



## 错误修正

* 关于.ssh被错误删除的问题解决
  * 删除.ssh文件，通过`ssh-keygen -t rsa -C "XXX@email.XXX"`指令重新生成（可能需要重新删除repository中的.git文件，并重新初始化设置）
* 关于远程git pull 报错fatal: refusing to merge unrelated histories的问题
  * 在你操作命令后面加`--allow-unrelated-histories`（摘自[CSDN](https://blog.csdn.net/wd2014610/article/details/80854807)）
  * ==（问题）== 输入指令后弹出窗口，要求输入（这么做的）理由，但不能进行输入。**（未解决）**
  * 第二次使用上述代码不会出现上述现象
* 关于github远程repository无法上传文件的几种原因
  * 本地的.ssh私钥不能解码githu上公钥（公私钥不对应）
  * 两端都进行了修改，无法进行fast-forward(快速合并)
  * remote origin 设置错误
* git无法返回命令视窗的问题（一般出现在git commit 手贱忘写-m的情况，或是输入`git log`）
  * 尝试多次按下Esc
  * **（摘自google）按下Esc以退出<insert>mode，按下":"光标出现到最下方时输入q!，点击enter。**



## 代码记录



`git remote -v`：查看所有远程库。

`git log`：查看修改情况。
