
import pdfplumber  # 关键在这个库
import pandas as pd


def func(src, dest='pdf.xlsx'):
    pdf = pdfplumber.open(src)
    size = len(pdf.pages)  #pdf有多少页

    with pd.ExcelWriter(dest) as writer:# 多页表格内容写入一个Excel
        count = 0
        j = 0 
        is_start = False
        for i in range(size):
            print('reading page %d' % i)
            page = pdf.pages[i]
            content = page.extract_text()
            # 这段代码是为了匹配表开始的地方
            if not is_start:
            	# 判断表开始的文字
                if content.lstrip().startswith('附表：网下投资者初步配售明细'):
                    is_start = True
                else:
                    continue
            # 提取表格，非表格就跳过
            try:
                table = page.extract_table()
            except:
                continue
            # 表格内容会转化为dataframe
            df = pd.DataFrame(table)
            #避免出现多个dataframe的表头
            if count == 0:
                df.to_excel(writer, header=False, index=False, startrow=count)
            else:
                df[1:].to_excel(writer, header=False, index=False, startrow=count - j)
                j += 1  # 避免出现空行

            count += len(df)
            pass

        writer.save()
        writer.close()
        pass


if __name__ == '__main__':
    func('test.PDF')


