import pyperclip
def latex_table(mat: list, title = None, scale: int = 1, copy: bool = True) -> str:
    """生成表格的 latex 代码

    Args:
        mat (list(list)): 表格内容
        title (list, optional): 表格标题，默认取 mat 首行
        scale (int, optional): 放大倍数. Defaults to 1.
        copy (bool, optional): 是否复制到剪贴板. Defaults to True.
    
    Returns:
        str: LaTeX 代码
    
    表格样式：
       - 表头深色，内容灰白相间
       - 文字居中
       - 带边框线
    """
    # 设置标题
    if title is not None: 
        mat = [title] + mat
    # 检查输入
    assert len(mat), "不能输入空列表"
    # 数据格式转字符串
    mat = [[str(i) for i in line] for line in mat] 
    # 行数，列数
    m,n = len(mat), len(mat[0]) 
    
    # 表格头部
    beg = r"""\begin{table}[h]
\centering
\scalebox{%.3f}{
\rowcolors{2}{gray!25}{white}
\begin{tabular}{|%s|}
\rowcolor{gray!50}
\hline
"""%(scale, 'c' * n)
    # 表格尾部
    end = '\n\\end{tabular}}\n\\end{table}'
    # 内容部分
    content = "\n".join(["&".join(line) + r"\\\hline" for line in mat])
    
    # 首尾连接
    out = beg + content + end
    if copy: # 复制到剪贴板
        pyperclip.copy(out)
    return out

def latex_matrix(mat: list, hrows = None, hcols = None, copy = True) -> str:
    """矩阵的 latex 代码

    Args:
        mat (list): 矩阵主体
        hrows (set, optional): 设置行线. Defaults to None.
        hcols (set, optional): 设置列线. Defaults to None.
        copy (bool, optional): 是否复制到剪贴板. Defaults to True.

    Returns:
        str: LaTeX 代码
    
    注：
        hrows = {0, 1} 代表顶行和第 1 行画线
    """
    # 检查输入
    assert len(mat), "输入为空矩阵"
    # 数据转字符串
    mat = [[str(i) for i in line] for line in mat]
    # 行数，列数
    m,n = len(mat), len(mat[0])
    # 设置列线
    if hcols is None:
        hcols = {}
    f = lambda i: '|c' if i in hcols else "c"
    # 设置行线
    if hrows is None:
        hrows = {}
    g = lambda i: r'\\\hline' if i in hrows else r'\\'
    
    # 头部
    s = "".join(f(i) for i in range(n))
    if n in hcols: # 设置列线
        s += '|'
    beg = r"""\begin{align*}
\left(\begin{array}{%s}
"""%s
    # 尾部
    end = "\n\\end{array}\\right)\n\\end{align*}"
    # 内容部分
    content = "\\hline\n" if 0 in hrows else ""
    content += "\n".join(["&".join(line) + g(i) for i, line in enumerate(mat)])
    
    # 输出结果
    out = beg + content[:-2] + end
    if copy: # 复制到剪贴板
        pyperclip.copy(out)
    return out

def markdown_table(content: list, title = None, copy = True) -> str:
    """将列表转化为 Markdown 格式

    Args:
        content (list): 表格内容
        title (list, optional): 表格标题，默认取 mat 首行
        copy (bool, optional): 是否复制到剪贴板. Defaults to True.

    Returns:
        str: markdown 代码
    """
    ''''''
    # 表格第二行格式（居中）
    align = "|".join([":-:"] * len(content[0]))
    # 行内元素用 | 分割
    content = ["|".join(str(i) for i in line) for line in content] 
    # 设置标题
    if title is None: # 标题未定义，提取列表第一行作为标题
        title = content[0]
        content = content[1:]
    else:
        title = "|".join(str(i) for i in title)
    # 合并，导出文本
    txt = "\n".join([title, align, *content]) 
    if copy: # 复制到剪贴板
        pyperclip.copy(txt)
    return txt

def latex_array_table(mat: list, title = None, copy: bool = True) -> str:
    """生成表格的 latex 代码

    Args:
        mat (list): 表格内容
        title ([type], optional): 表格标题，默认取 mat 首行
        copy (bool, optional): 是否复制到剪贴板. Defaults to True.

    Returns:
        str: LaTex 代码
    """

    # 设置标题
    if title is not None: 
        mat = [title] + mat
    # 检查输入
    assert len(mat), "不能输入空列表"
    # 数据格式转字符串
    mat = [[str(i) for i in line] for line in mat] 
    # 行数，列数
    n = len(mat[0]) 
    
    # 表格头部
    beg = """\\begin{array}{|c|%s|}\n\\hline\n"""%('c'*(n-1))
    # 表格尾部
    end = '\n\\end{array}'
    # 内容部分
    content = "\n".join(["&".join(line) + r"\\\hline" for line in mat])
    # 首尾连接
    out = beg + content + end
    if copy: # 复制到剪贴板
        pyperclip.copy(out)
    return out

def MDtable_to_array_table(txt: str, copy: bool = True) -> str:
    """markdown 格式的字符串转化为数组形式

    Args:
        txt (str): [description]
        copy (bool, optional): 是否复制到剪贴板. Defaults to True.
        
    Returns:
        str: [description]
    """
    lines = txt.split("\n") # 按行拆分
    lines.pop(1) # 去掉格式行
    lines = [line.split("|") for line in lines]
    return latex_array_table(lines, copy=copy)
    

    