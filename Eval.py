fa_threshold = 1e-4  #虚警率阈值          False alarm rate threshold
alpha = 0.5          #检测精度Sp的加权系数 The weighting coefficient of the performance score Sp
Pbase = 2.225          #基线的参数量 M      The parameters for the baseline (Unit: M)
Fbase = 12.56         #基线的运算量 GFlops The FLOPs for the baseline


# 输入模型测试得到的评价指标 Input evaluation indicators obtained from model testing
Fa = 1.913179e-05 #虚警率 False alarm rate
Pd = 0.5555   #检测率 Detection rate
IoU = 0.36217  #平均交并比 average intersection over union
Params = 0.914057 #模型参数量 M Parameters of your model (Unit: M)
Flops = 5.1789169 #模型运算量 GFlops of your model


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

print("IoU: {:.3f}, Fa: {}, Pd: {:.3f}, Sp: {}".format(IoU, Fa, Pd, Sp))
print("Params: {:.3f}M , FLOPs: {:.3f}GFlops, Se: {}".format(Params, Flops, Se))
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

UNet:
mean_IOU: 0.583555451832017
PD: [5.47134159e-01 3.38862062e-01 1.80138568e-01 9.99370145e-02
 4.95486038e-02 1.51165232e-02 2.51942053e-03 2.09951711e-04
 0.00000000e+00 0.00000000e+00 0.00000000e+00]
FA: [2.00271606e-05 1.00173950e-05 8.00704956e-06 3.46374512e-06
 1.44386292e-06 7.45773315e-07 1.50680542e-07 0.00000000e+00
 0.00000000e+00 0.00000000e+00 0.00000000e+00]
Params: 0.914057M
FLOPs: 5.178917GFLOPs

LW:
'''
