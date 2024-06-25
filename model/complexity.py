from thop import profile
import torch
from net import *
from DNANet import *


if __name__ == '__main__':

    input_img = torch.rand(1,3,512,512).cuda()
    # net = LightWeightNetwork().cuda()
    net = DNANet(num_classes=1, input_channels=3, block=Res_CBAM_block, num_blocks=[1, 1, 1, 1],
                           nb_filter=[16, 32, 64, 128, 256], deep_supervision='True').cuda()
    flops, params = profile(net, inputs=(input_img, ))
    print('Params: %2fM' % (params/1e6))
    print('FLOPs: %2fGFLOPs' % (flops/1e9))

