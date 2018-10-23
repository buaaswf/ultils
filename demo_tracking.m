clear all;
clc;

addpath('../utils');
addpath('../models');
addpath('../vital');

run ../matconvnet/matlab/vl_setupnn ;

global gpu;
gpu=true;
    
%test_seq='uav0000003_00000_s';
test_seq={'uav0000003_00000_s','uav0000072_06672_s','uav0000076_00241_s','uav0000107_01763_s','uav0000126_07915_s',...
    'uav0000144_01980_s','uav0000144_03200_s','uav0000147_00000_s','uav0000148_00840_s','uav0000149_00317_s','uav0000159_00000_s','uav0000160_00000_s',...
    'uav0000169_00000_s','uav0000170_00000_s','uav0000171_00000_s','uav0000172_00000_s','uav0000173_00781_s','uav0000174_00000_s',...
    'uav0000175_00000_s','uav0000175_00697_s','uav0000176_00000_s','uav0000178_00025_s','uav0000182_01075_s','uav0000198_00000_s',...
   'uav0000200_00000_s', 'uav0000204_00000_s', 'uav0000205_00000_s', 'uav0000209_00000_s','uav0000217_00001_s','uav0000221_10400_s',...
'uav0000222_00900_s', 'uav0000223_00300_s', 'uav0000226_05370_s', 'uav0000232_00960_s', 'uav0000235_00001_s','uav0000235_01032_s',...
'uav0000236_00001_s', 'uav0000237_00001_s', 'uav0000238_00001_s','uav0000238_01280_s','uav0000239_11136_s','uav0000240_00001_s',...
'uav0000252_00001_s','uav0000300_00000_s','uav0000303_00000_s','uav0000303_01250_s','uav0000304_00253_s','uav0000307_04531_s',...
'uav0000308_04600_s', 'uav0000325_01656_s','uav0000329_00276_s','uav0000331_02691_s','uav0000342_01518_s','uav0000348_02415_s',...
'uav0000349_02668_s','uav0000352_00759_s'};
for i=4:length(test_seq)
    ts = test_seq(i);

    conf = genConfig('otb',ts{1});

    net=fullfile('../models/otbModel.mat');
    % data=conf.gt;
    % save('gt.mat','data');

    result = vital_run(conf.imgList, conf.gt(1,:), net, true,ts);
end


    


