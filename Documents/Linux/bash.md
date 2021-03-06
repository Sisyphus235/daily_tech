# Shell 基本类型变量

> shell 开始执行时定义了一些和系统的工作环境相关的变量，用户可以重新定义

## shell 环境变量

- HOME 用于保存注册目录的完全路径名
- PATH 用于保存用冒号分割的目录路径名，shell 将按 PATH 变量给出的顺序检索，找到第一个与命令名称一致的可执行文件执行
- TERM 终端类型
- UID 当前用户的识别字，值是由数字构成的字符串
- PWD 当前工作目录的绝对路径名，取值随着 cd 命令的使用而变化
- PS1 主提示符，在特权用户下，默认的主提示符是 `#`，普通用户的默认提示符是 `$`
- PS2 在 shell 接收用户输入命令过程中，如果用户在输入行末尾输入 `\` 然后回车，或者用户回车 shell 判定输入命令未结束时，显示这个辅助提示符

## 用户定义变量

> 变量名=变量值，赋值时等号两侧不能有空格，变量名前不能有符号，若变量名有空格，则需要用双引号包裹。为了区分变量名和命令名，习惯上变量名是全部大写的。

- 保证只读性：readonly 变量名
- 全局变量设置：export 变量名/export 变量名=变量值

## 位置参数

- $0 代表当前 shell 程序的文件名，不是位置参数
- $1 代表第一个位置参数
- $2 代表第二个位置参数，以此类推

## 预定义变量

在 shell 启动时定义的变量，和环境变量不同的是，这些变量是不能被用户重新定义的。

- \$\# 位置参数的数量
- \$\* 所有位置参数的内容
- \$\? 命令执行后返回的状态，用于检查上一个命令执行是否正确，0 是正确，非 0 是出错
- \$\$ 当前进程的进程号，常用于暂存文件的名字，保证文件名字不会重复
- \$\! 后台运行的最后一个进程号
- \$0 当前执行的进程名

## 参数置换变量

- 变量=${参数-word}：设置了参数则变量值等于参数，否则等于 word
- 变量=${参数=word}：设置了参数则变量值等于参数，否则等于 word，并用 word 替换参数的值
- 变量=${参数?word}：设置了参数则变量值等于参数，否则显示 word 并从 shell 中退出，常用于出错指示
- 变量=${参数+word}：设置了参数则用 word 替换，否则不进行置换

# Shell 流程控制

## 测试命令

### 数值测试

- -eq 等于则为真
- -ne 不等于则为真
- -gt 大于则为真
- -ge 大于等于则为真
- -lt 小于则为真
- -le 小于等于则为真

### 字符串测试

- = 等于则为真
- != 不等于则为真
- -z 字符串 字符串长度伪则为真
- -n 字符串 字符串长度不伪则为真

### 文件测试

- -e 文件名 文件存在则为真
- -r 文件名 文件存在且可读则为真
- -w 文件名 文件存在且可写则为真
- -x 文件名 文件存在且可执行为为真
- -s 文件名 文件存在且至少有一个字符则为真
- -d 文件名 文件存在且为目录则为真
- -f 文件名 文件存在且为普通文件则为真
- -c 文件名 文件存在且为字符型特殊文件则为真
- -b 文件名 文件存在且为块特殊文件则为真

### 逻辑操作符

- 与 (! )
- 或 (-o)
- 非 (-a)

### 运算表达式

$[expression]

```bash
var1 = 2
var2 = $[var1*10+2]
```

## if 条件语句

```bash
if 条件命令穿
then
条件为真时的命令串
else
条件为假时的命令串
fi
```

## for 循环

```bash
for 变量名 [in数值列表]
do 若干个命令
done
```

变量名可以使用户选择的任何字符串，如果变量名是 `var`，则在 `in` 之后给出的数值将顺序替换循环命令列表中的 `$var`。  
如果省略了 `in`，则变量 `var` 取值是位置参数。

## while 循环

```bash
while
若干个命令行1
do
若干个命令行2
done
```

只要 `while` 的 “若干个命令行 1” 中最后一个命令的返回状态为真，`while` 循环就继续执行 `do...done` 之间的 “若干个命令行 2”

## until 循环

```bash
until
若干个命令行1
do
若干个命令行2
done
```

和 `while` 循环的区别是：`until` 在条件为假时继续执行循环
。

## case 条件选择

```bash
case string in
exp-1)
若干个命令行1
;;
exp-2)
若干个命令行2
;;
...
*)
其他命令行
esac
```

`shell` 通过计算字符串 string 的值，依次和 `exp-1`, `exp-2`, ... 等进行比较，找到匹配项后，执行下面的命令直到遇到一对分号为止

## 无条件控制语句

`break` 用于立即终止当前循环执行；
`continue` 用于结束当前循环，进入下一个循环的执行；
上面两个语句，只有放在 do 和 done 之间才有效。

## 函数定义

```bash
functionname
{
    若干命令行
}
```

函数定义无需参数说明，在调用函数可以带参数，会分别赋予相应位置的参数，`functionname param1 param2 ...`

## 命令分组

两种命令分组方法：() 和 {}。  
() 在 shell 中执行时会再创建一个子进程，由子进程去执行圆括号中的命令。通常用来执行希望隔离的命令，不影响当前进程的位置参数、环境变量、工作目录等。  
{} 用于将顺序执行的命令的输出结果用于另一个命令的输入，即管道模式。  
如果需要转译，则使用 `\(\)\{\}` 的方式

## 信号

`trap` 命令用于在 shell 程序中捕捉信号，有 3 种处理方式：

- （1）执行一段程序来处理信号；

```bash
# 接受到 signal-list 清单中数值相同的信号时，将执行双引号中的命令串
trap 'commands' signal-list
```

- （2）接受信号的默认操作；

```bash
trap signal-list
```

- （3）忽视信号

```bash
trap "" signal-list
```

> trap 语句对单双引号处理不同，shell 第一次执行到 trap 语句，将把 commands 中的命令扫描一遍。如果 commands 是单引号包围，shell 不会对 commands 中的变量和命令进行替换，否则会用当时具体的值来替换 commands 中的变量和命令。

# 运行 shell 的方法

## sh Shell 程序文件名

命令格式是 `bash Shell 程序文件名`，调用新的 `bash` 命令解释程序，把 Shell 程序文件名作为参数传递给它。新启动的 Shell 将读指定的文件，顺序执行文件中的可执行命令，优点是可以使用 Shell 的调试功能。

## sh

命令格式是 `bash<Shell 程序名`，利用输入重定向，使 Shell 命令解释程序的输入取自指定的程序文件。

## chmod 命令使 Shell 程序成为可执行的

Shell 程序在编辑器生成文件的时候，系统赋予的许可权是 `644(rw-r-r--)`。

> 调试时建议用 sh Shell 程序文件名的方式执行；投入生产的时候用 chmod 使 Shell 程序成为可执行的。

# bash 程序调试

通常用 `bash` 命令解释程序的选择项：

```bash
bash -选择项 Shell程序文件名
```

- \-e 如果一个命令失败立即退出
- \-n 读入命令但是不执行
- \-u 置换时把未设置的变量视为错误
- \-v 当读入 shell 输入航时把它们显示出来
- \-x 执行命令时把命令和相关参数显示出来

> 程序执行时通常使用 echo 将关键信息打印出来进行调试

# bash 内部命令

内部命令是 shell 提供的

- echo

```bash
# 在屏幕上显示由 arg 指定的字符串
echo arg
```

- eval

```bash
# shell 读入 args，将它们组成一个新命令执行
eval args
```

- exec

```bash
# 执行到 exec 的时候不会创建新的子进程，而是转去执行指定命令，执行完毕后 shell 终止，exec 后面的语句将不被执行
exec 命令参数
```

- export

```bash
# 用 export 将它的变量带入子 shell，让子进程继承父进程的环境变量，但不可反过来
# export 后面不带任何变量名的时候将现实所有 export 变量
export 变量名
export 变量名=变量值
```

- readonly

```bash
# 将一个用户定义的 shell 变量标识为不可变
readonly 变量名
```

- read

```bash
# 从标准输入设备读入一行，分解出若干字，赋值给 shell 程序内部定义的变量
read 变量名表
```

- shift

```bash
# 重新命名所有的位置参数变量，即 $2 变成 $1，每次使用都让所有位置参数依次向左移动一个位置，并使位置参数减一，直到 0 为止
```

- wait

```bash
# 使 shell 等待在后台启动的所有子进程结束，wait 的返回值总为真
```

- exit

```bash
# 退出 shell 程序，exit 后可有选择的指定一个数位作为返回状态
```

- "." [dot]

```bash
# 使 shell 读入指定的 shell 程序文件并依次执行文件中的所有语句
.Shell 程序文件名
```

# 比较运算符

## 文件比较运算符

-e filename， 如果 filename 存在则为真；  
-d filename， 如果 filename 为目录则为真；  
-f filename， 如果 filename 为常规文件则为真；  
-L filename， 如果 filename 为符号链接则为真；  
-r filename， 如果 filename 可读则为真；  
-w filename， 如果 filename 可写则为真；  
-x filename， 如果 filename 可执行则为真；  
-s filename， 如果 filename 不是空白文件则为真；  
-u filename， 如果 filename 有 SUID 属性则为真；  
-g filename， 如果 filename 有 SGID 属性则为真；  
-k filename， 如果 filename 有 sticky bit 属性则为真；  
filename1 -nt filename2， 如果 filename1 比 filename2 新则为真；  
filename1 -ot filename2， 如果 filename1 比 filenam2 旧则为真；

## 字符串比较运算符

-z string，如果 string 长度为零则为真；  
-n string，如果 string 长度非零则为真；  
string1=string2，如果 string1 与 string2 相同则为真；  
string1!=string2，如果 string1 与 string2 不同则为真；

## 算数比较运算符

num1 -eq num2，等于；  
num1 -ne num2，不等于；  
num1 -lt num2，小于；  
num1 -le num2，小于或等于；  
num1 -gt num2，大于；  
num1 -ge num2，大于或等于；

# 常用 snippet

## 无限循环

```bash
while [ 1 ];
do sleep 1;
ll;
done
```

## 有限循环

```bash
while [ $i -lt 10 ];
do echo $i;
let "i=$i+1";
done
```
