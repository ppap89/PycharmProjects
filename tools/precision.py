import pandas as pd

def Precision(tp,b):
    P = tp / b
    return P
def recall(tp,all):
    R = tp / all 
    return R


data = {'':['crosswalk0.7','sidewalk0.7','motorroad0.7','non-motorroad0.7','crosswalk0.3','sidewalk0.3','motorroad0.3','non-motorroad0.3',
            'YUHANG_crosswalk','YUHANG_sidewalk','YUHANG_motorraod','YUHANG_non-motorroad'],
        '精确率':[
                f'{Precision(776,776 + 197 + 39 + 327):.2%}',
                f'{Precision(2830,2830 + 889 + 20 + 715):.2%}',
                f'{Precision(3329,3389 + 1571 + 119 + 2):.2%}',
                f'{Precision(2355,2355 + 154 + 0 + 1512):.2%}',
                f'{Precision(321 ,321 + 14 + 38 + 203):.2%}',
                f'{Precision(1258,1258 + 24 + 224 + 558):.2%}',
                f'{Precision(1604,1604 + 25 + 3 + 675):.2%}',
                f'{Precision(769,769 + 50 + 0 + 624):.2%}',
                f'{Precision(452, 452 + 93 + 4 + 180):.2%}',
                f'{Precision(629, 629 + 58 + 67 + 456):.2%}',
                f'{Precision(663, 663 + 68 + 15 + 157):.2%}',
                f'{Precision(2267, 2267 + 16 + 281 + 9):.2%}'
                ],
        '召回率':[
                f'{recall(776,918):.2%}',
                f'{recall(2830,3142):.2%}',
                f'{recall(3389,5813):.2%}',
                f'{recall(2355,5142):.2%}',
                f'{recall(321,393):.2%}',
                f'{recall(1258,1345):.2%}',
                f'{recall(1604,2488):.2%}',
                f'{recall(769,2203):.2%}',
                f'{recall(452,587):.2%}',
                f'{recall(629,664):.2%}',
                f'{recall(663,1102):.2%}',
                f'{recall(2267,3058):.2%}',
                ]}



df = pd.DataFrame(data)
print(df)