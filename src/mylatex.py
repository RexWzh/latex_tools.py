import pyperclip
def latex_table(mat,title=None, scale=1, copy=True):
    '''生成表格的 latex 代码
    默认样式：
       - 表格不放缩
       - 表头深色，内容灰白相间
       - 文字居中
       - 带边框线
    必要参数：
       - mat 表格内容，list 形式
    可选参数：
       - title 表格标题，默认取 mat 首行
       - scale 表格放缩比例
       - copy 自动复制到剪贴板
    '''
    # 设置标题
    if title is not None: 
        mat = [title] + mat
    # 检查输入
    assert len(mat),"不能输入空列表"
    # 数据格式转字符串
    mat = [[str(i) for i in line] for line in mat] 
    # 行数，列数
    m,n = len(mat),len(mat[0]) 
    
    # 表格头部
    beg = r"""\begin{table}[h]
\centering
\scalebox{%.3f}{
\rowcolors{2}{gray!25}{white}
\begin{tabular}{|%s|}
\rowcolor{gray!50}
\hline
"""%(scale,'c'*n)
    # 表格尾部
    end = '\n\\end{tabular}}\n\\end{table}'
    # 内容部分
    content = "\n".join(["&".join(line)+r"\\\hline" for line in mat])
    
    # 首尾连接
    out = beg + content + end
    if copy: pyperclip.copy(out)
    return out




def latex_matrix(mat, hrows=None, hcols=None, copy=True):
    '''矩阵的 latex 代码
    必要参数：
       - mat 矩阵
    可选参数：
       - hrows 设置行线
       - hcols 设置列线
    例：hrows={0,1} 代表顶行和第1行画线'''
    # 检查输入
    assert len(mat),"输入为空矩阵"
    # 数据转字符串
    mat = [[str(i) for i in line] for line in mat]
    # 行数，列数
    m,n = len(mat),len(mat[0])
    # 设置列线
    if hcols is None: hcols = {}
    f = lambda i: '|c' if i in hcols else "c"
    # 设置行线
    if hrows is None: hrows = {}
    g = lambda i: r'\\\hline' if i in hrows else r'\\'
    
    # 头部
    s = "".join(f(i) for i in range(n))
    if n in hcols: s += '|'
    beg = r"""\begin{align*}
\left(\begin{array}{%s}
"""%s
    # 尾部
    end = "\n\\end{array}\\right)\n\\end{align*}"
    # 内容部分
    content = "\\hline\n" if 0 in hrows else ""
    content += "\n".join(["&".join(line)+g(i) for i,line in enumerate(mat)])
    
    # 输出结果
    out = beg + content[:-2] + end
    if copy: pyperclip.copy(out)
    return out

def list_to_MDTable(content, title=None,copy=True):
    '''将列表转化为 Markdown 格式'''
    # 表格第二行格式（居中）
    align = "|".join([":-:"]*len(content[0]))
    # 行内元素用 | 分割
    content = ["|".join(str(i) for i in line) for line in content] 
    # 设置标题
    if title is None: # 标题未定义，提取列表第一行作为标题
        title = content[0]
        content = content[1:]
    else:
        title = "|".join(str(i) for i in title)
    # 合并，导出文本
    txt = "\n".join([title,align,*content]) 
    if copy: pyperclip.copy(txt)
    return txt
