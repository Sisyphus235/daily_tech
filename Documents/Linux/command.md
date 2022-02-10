# 端口

```bash
lsof -i:$port
```

# 按照大小排序查看进程的内存占用情况

```bash
ps -aux --sort -rss
```

# 文件内容查看

## cat

```bash
cat [选项] [文件]

cat -b /etc/profile 查看文件内容，对非空白行进行编号
cat -n /etc/profile 查看文件内容，对所有行进行编号
cat -E /etc/profile 查看文件内容，在每行结尾加上 $
cat /etc/profile | more 对于大文件内容，传送到 more 工具分页查看
```
