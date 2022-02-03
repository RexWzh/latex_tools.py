

## LaTeX 代码工具

正则表达式是一个很强大的字符串处理工具，几乎任何关于字符串的操作都可以使用正则表达式来完成。

---

<!--  注：本篇放函数代码，网站增加在线编程功能后，再写篇工具在线使用。 -->

## 示例
### LaTeX 表格

1. 生成前 8 阶二项式系数表格的 LaTeX 代码

2. 方法一， LaTeX 的 `table` 环境
    ```py
    from latextool import latex_table
    n = 8
    title = ["(m,n)"] + list(range(1,n+1))
    mat = [ [j] + [binomial(j,i) for i in range(1,n+1)] for j in range(1,n+1)] # binomial 为 sagemath 自带函数
    latex_table(mat,title=title)
    ```
    输出效果：表格效果为首行深色，其余各行“灰白交替”
    ![binomial](https://cdn.jsdelivr.net/gh/RexWzh/PicBed@picgo/picgo_folder/%E6%B7%B1%E5%BA%A6%E6%88%AA%E5%9B%BE_%E9%80%89%E6%8B%A9%E5%8C%BA%E5%9F%9F_20210923203428.png)

3. 方法二， LaTeX 的 `array` 环境
    ```py
    from latextool import latex_array_table
    n = 8
    title = ["(m,n)"] + list(range(1,n+1))
    mat = [ [j] + [binomial(j,i) for i in range(1,n+1)] for j in range(1,n+1)] # binomial 为 sagemath 自带函数
    latex_array_table(mat,title=title)
    ```
    输出效果：
    ![深度截图_选择区域_20220202104519](https://cdn.jsdelivr.net/gh/zhihongecnu/PicBed2/picgo/深度截图_选择区域_20220202104519.png)

> 注：网页常用的 KaTeX 和 MathJax 均不支持 `table` 环境，此时可用 `array` 来显示表格。


### LaTeX 矩阵

1. 计算矩阵的 5 次幂，并导出 LaTeX 代码
    ![深度截图_选择区域_20220203104314](https://cdn.jsdelivr.net/gh/zhihongecnu/PicBed2/picgo/深度截图_选择区域_20220203104314.png)

2. 输入：
    ```py
    from latextool import latex_matrix
    mat = matrix([[1,2,3],[2,3,4],[4,5,6]]) # matrix 为 sagemath 自带函数
    latex_matrix(list(mat^5))
    ```

3. tex 效果：
    ![matrix](https://cdn.jsdelivr.net/gh/RexWzh/PicBed@picgo/picgo_folder/%E6%B7%B1%E5%BA%A6%E6%88%AA%E5%9B%BE_%E9%80%89%E6%8B%A9%E5%8C%BA%E5%9F%9F_20210923215320.png)


###  Markdown 表格

1. 打印表格，输入如下：
    ```py
    from latextool import markdown_table, MDtable_to_array_table
    ### 方法一 指定 title ###
    content = [[1,2,3],[2,3,4]]
    title = ["a","b","c"]
    markdown_table(content,title=title)

    ### 方法二 不指定 title ###
    content = [["a","b","c"],[1,2,3],[2,3,4]]
    markdown_table(content)
    ```

2. 显示效果：
    a|b|c
    :-:|:-:|:-:
    1|2|3
    2|3|4

> 注：使用 `MDtable_to_array_table` 可将 markdown 的表格代码转为 array 形式


### Dynkin 图

毕业论文要画很多图，之前用 tikz + python 写绘图工具，做了一部分，工具完整成型再逐步更新。

