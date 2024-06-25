fa_threshold = 2e-5  #虚警率阈值          False alarm rate threshold
alpha = 0.5          #检测精度Sp的加权系数 The weighting coefficient of the performance score Sp
Pbase = 2.225          #基线的参数量 M      The parameters for the baseline (Unit: M)
Fbase = 12.56         #基线的运算量 GFlops The FLOPs for the baseline


# 输入模型测试得到的评价指标 Input evaluation indicators obtained from model testing
Fa = 1.8e-5 #虚警率 False alarm rate
Pd = 0.627   #检测率 Detection rate
IoU = 0.614  #平均交并比 average intersection over union
Params = 4.7 #模型参数量 M Parameters of your model (Unit: M)
Flops = 57.13 #模型运算量 GFlops of your model


#评分 Score
# Sp = alpha*IoU + (1-alpha)*Pd
if Fa > fa_threshold:#
    Sp = 0
else:
    Sp = alpha * IoU + (1 - alpha) * Pd

# Se
Se = 1 - ((Params/Pbase + Flops/Fbase) * 0.5)

# Spe = (Se +Sp)/2
Spe = (Sp + Se) *0.5

print("IoU: {:.2f}, Fa: {}, Pd: {:.2f}, Sp: {}".format(IoU, Fa, Pd, Sp))
print("Params: {:.1f}M , FLOPs: {:.2f}GFlops, Se: {}".format(Params, Flops, Se))
print("Spe: ",format(Spe))

'''
DNANet:
moiu:  0.6147957341293724
FA:  [1.80435181e-05 5.11169434e-06 2.01416016e-06 6.79016113e-07
 7.62939453e-08 1.52587891e-08 0.00000000e+00 0.00000000e+00
 0.00000000e+00 0.00000000e+00 0.00000000e+00]
PD:  [6.27598297e-01 4.26245930e-01 1.91835712e-01 9.21612822e-02
 2.37916354e-02 2.75482094e-03 2.50438267e-04 0.00000000e+00
 0.00000000e+00 0.00000000e+00 0.00000000e+00]
Params: 4.696888M
FLOPs: 57.128745GFLOPs
sp=0.62
se=-2.33
score=-0.855
Params和FLops过大，se分数太低
'''