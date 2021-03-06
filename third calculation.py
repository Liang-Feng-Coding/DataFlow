import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data_file1 = pd.read_csv('20180912_mudstone-1st.csv')
data_file2 = pd.read_csv('dilution_factor.csv')
data_file3 = pd.read_csv('w-2a_value.csv')

isotope = data_file1['isotope']
sensors1 = data_file1.loc[:,'isotope':'smp53']
sensors2 = data_file2.loc[:,'sample':'DF']
sensors3 = data_file3.loc[:,'isotope':'w-2a']

a1 = sensors1['smp1']

# before Rh103
def Rh(i):
    Rh = a1[8]*sensors2['spk_ppb'][i-1]/sensors2['spk_ppb'][0]/sensors1['smp'+str(i)+''][8]*sensors1['smp'+str(i)+''][0:9]
    return Rh

# before In115
def In(i):
    In = a1[11]*sensors2['spk_ppb'][i-1]/sensors2['spk_ppb'][0]/sensors1['smp'+str(i)+''][11]*sensors1['smp'+str(i)+''][9:12]
    return In

# before Re187
def Re(i):
    Re = a1[33]*sensors2['spk_ppb'][i-1]/sensors2['spk_ppb'][0]/sensors1['smp'+str(i)+''][33]*sensors1['smp'+str(i)+''][12:34]
    return Re

# around Bi209
def Bi(i):
    Bi = a1[33]*sensors2['spk_ppb'][i-1]/sensors2['spk_ppb'][0]/sensors1['smp'+str(i)+''][33]*sensors1['smp'+str(i)+''][12:34]
    return Bi

# Medium resolution Rh103
def RhM(i):
    RhM = a1[47]*sensors2['spk_ppb'][i-1]/sensors2['spk_ppb'][0]/sensors1['smp'+str(i)+''][47]*sensors1['smp'+str(i)+''][39:51]
    return RhM

# High resolution Bi209
def BiH(i):
    BiH = a1[47]*sensors2['spk_ppb'][i-1]/sensors2['spk_ppb'][0]/sensors1['smp'+str(i)+''][47]*sensors1['smp'+str(i)+''][39:51]
    return BiH

# spike calibration concat
def spike(i):
    spike = pd.concat([Rh(i),In(i),Re(i),Bi(i),RhM(i),BiH(i)])
    return spike

#result_spike = pd.concat([isotope,a1,spike(2),spike(3),spike(4),spike(5),spike(6),spike(7),spike(8),spike(9),spike(10),spike(11),spike(12),spike(13),spike(14),spike(15),spike(16),spike(17),spike(18),spike(19),spike(20),spike(21),spike(22),spike(23),spike(24),spike(25),spike(26),spike(27),spike(28),spike(29),spike(30),spike(31),spike(32),spike(33),spike(34),spike(35),spike(36),spike(37),spike(38),spike(39),spike(40),spike(41),spike(42),spike(43),spike(44),spike(45),spike(46),spike(47),spike(48),spike(49),spike(50),spike(51),spike(52),spike(53)], axis=1)
#result_spike.to_csv('TE_1Spike.csv')

#result_spike = pd.merge(isotope,a1,spike(2),spike(3),left_index=True,right_index=True,how='outer') 
#result_spike.to_csv('TE_1Spiked.csv')

#s2 = pd.concat([Rh(2),In(2),Re(2),Bi(2),RhM(2),BiH(2)])
#s3 = pd.concat([Rh(3),In(3),Re(3),Bi(3),RhM(3),BiH(3)])

#result_spike = pd.concat([isotope,a1,s2,s3],axis=1)
#result_spike.to_csv('TE_1Spikes.csv')

'''''s4 = pd.concat([Rh(4),In(4),Re(4),Bi(4),RhM(4),BiH(4)])
s5 = pd.concat([Rh(5),In(5),Re(5),Bi(5),RhM(5),BiH(5)])
s6 = pd.concat([Rh(6),In(6),Re(6),Bi(6),RhM(6),BiH(6)])
s7 = pd.concat([Rh(7),In(7),Re(7),Bi(7),RhM(7),BiH(7)])
s8 = pd.concat([Rh(8),In(8),Re(8),Bi(8),RhM(8),BiH(8)])
s9 = pd.concat([Rh(9),In(9),Re(9),Bi(9),RhM(9),BiH(9)])
s10 = pd.concat([Rh(10),In(10),Re(10),Bi(10),RhM(10),BiH(10)])
s11 = pd.concat([Rh(11),In(11),Re(11),Bi(11),RhM(11),BiH(11)])
s12 = pd.concat([Rh(12),In(12),Re(12),Bi(12),RhM(12),BiH(12)])
s13 = pd.concat([Rh(13),In(13),Re(13),Bi(13),RhM(13),BiH(13)])
s14 = pd.concat([Rh(14),In(14),Re(14),Bi(14),RhM(14),BiH(14)])
s15 = pd.concat([Rh(15),In(15),Re(15),Bi(15),RhM(15),BiH(15)])
s16 = pd.concat([Rh(16),In(16),Re(16),Bi(16),RhM(16),BiH(16)])
s17 = pd.concat([Rh(17),In(17),Re(17),Bi(17),RhM(17),BiH(17)])
s18 = pd.concat([Rh(18),In(18),Re(18),Bi(18),RhM(18),BiH(18)])
s19 = pd.concat([Rh(19),In(19),Re(19),Bi(19),RhM(19),BiH(19)])
s20 = pd.concat([Rh(20),In(20),Re(20),Bi(20),RhM(20),BiH(20)])
s21 = pd.concat([a21,b21,c21,d21,e21,f21])
s22 = pd.concat([a22,b22,c22,d22,e22,f22])
s23 = pd.concat([a23,b23,c23,d23,e23,f23])
s24 = pd.concat([a24,b24,c24,d24,e24,f24])
s25 = pd.concat([a25,b25,c25,d25,e25,f25])
s26 = pd.concat([a26,b26,c26,d26,e26,f26])
s27 = pd.concat([a27,b27,c27,d27,e27,f27])
s28 = pd.concat([a28,b28,c28,d28,e28,f28])
s29 = pd.concat([a29,b29,c29,d29,e29,f29])
s30 = pd.concat([a30,b30,c30,d30,e30,f30])
s31 = pd.concat([a31,b31,c31,d31,e31,f31])
s32 = pd.concat([a32,b32,c32,d32,e32,f32])
s33 = pd.concat([a33,b33,c33,d33,e33,f33])
s34 = pd.concat([a34,b34,c34,d34,e34,f34])
s35 = pd.concat([a35,b35,c35,d35,e35,f35])
s36 = pd.concat([a36,b36,c36,d36,e36,f36])
s37 = pd.concat([a37,b37,c37,d37,e37,f37])
s38 = pd.concat([a38,b38,c38,d38,e38,f38])
s39 = pd.concat([a39,b39,c39,d39,e39,f39])
s40 = pd.concat([a40,b40,c40,d40,e40,f40])
s41 = pd.concat([a41,b41,c41,d41,e41,f41])
s42 = pd.concat([a42,b42,c42,d42,e42,f42])
s43 = pd.concat([a43,b43,c43,d43,e43,f43])
s44 = pd.concat([a44,b44,c44,d44,e44,f44])
s45 = pd.concat([a45,b45,c45,d45,e45,f45])
s46 = pd.concat([a46,b46,c46,d46,e46,f46])
s47 = pd.concat([a47,b47,c47,d47,e47,f47])
s48 = pd.concat([a48,b48,c48,d48,e48,f48])
s49 = pd.concat([a49,b49,c49,d49,e49,f49])
s50 = pd.concat([a50,b50,c50,d50,e50,f50])
'''''


#spike(53)
#result_spike = pd.concat([isotope,a1,spike(2)],axis=1)
#result_spike.to_csv('TE_1Spike.csv')

# Substract blank

blk = input('Please enter blank name\n')

def SubBlank(i):
    if i = 1:
        subblk = a1 - blk
    else:
        subblk = spike(i) - blk
        return subblk[i]
    
#result_SubBlank = pd.concat([isotope,a1-blk,s2-blk,s3-s49,s4-s49,s5-s49,s6-s49,s7-s49,s8-s49,s9-s49,s10-s49,s11-s49,s12-s49,s13-s49,s14-s49,s15-s49,s16-s49,s17-s49,s18-s49,s19-s49,s20-s49,s21-s49,s22-s49,s23-s49,s24-s49,s25-s49,s26-s49,s27-s49,s28-s49,s29-s49,s30-s49,s31-s49,s32-s49,s33-s49,s34-s49,s35-s49,s36-s49,s37-s49,s38-s49,s39-s49,s40-s49,s41-s49,s42-s49,s43-s49,s44-s49,s45-s49,s46-s49,s47-s49,s48-s49,s49-s49,s50-s49], axis=1)
#result_SubBlank.to_csv('TE_2BLK.csv')
#print('complete')

# Dilution factor

#result_DF = pd.concat([isotope,(a1-s49)*sensors2['DF'][0],(s2-s49)*sensors2['DF'][1],(s3-s49)*sensors2['DF'][2],(s4-s49)*sensors2['DF'][3],(s5-s49)*sensors2['DF'][4],(s6-s49)*sensors2['DF'][5],(s7-s49)*sensors2['DF'][6],(s8-s49)*sensors2['DF'][7],(s9-s49)*sensors2['DF'][8],(s10-s49)*sensors2['DF'][9],(s11-s49)*sensors2['DF'][10],(s12-s49)*sensors2['DF'][11],(s13-s49)*sensors2['DF'][12],(s14-s49)*sensors2['DF'][13],(s15-s49)*sensors2['DF'][14],(s16-s49)*sensors2['DF'][15],(s17-s49)*sensors2['DF'][16],(s18-s49)*sensors2['DF'][17],(s19-s49)*sensors2['DF'][18],(s20-s49)*sensors2['DF'][19],(s21-s49)*sensors2['DF'][20],(s22-s49)*sensors2['DF'][21],(s23-s49)*sensors2['DF'][22],(s24-s49)*sensors2['DF'][23],(s25-s49)*sensors2['DF'][24],(s26-s49)*sensors2['DF'][25],(s27-s49)*sensors2['DF'][26],(s28-s49)*sensors2['DF'][7],(s29-s49)*sensors2['DF'][28],(s30-s49)*sensors2['DF'][29],(s31-s49)*sensors2['DF'][30],(s32-s49)*sensors2['DF'][31],(s33-s49)*sensors2['DF'][32],(s34-s49)*sensors2['DF'][33],(s35-s49)*sensors2['DF'][34],(s36-s49)*sensors2['DF'][35],(s37-s49)*sensors2['DF'][36],(s38-s49)*sensors2['DF'][37],(s39-s49)*sensors2['DF'][38],(s40-s49)*sensors2['DF'][39],(s41-s49)*sensors2['DF'][40],(s42-s49)*sensors2['DF'][41],(s43-s49)*sensors2['DF'][42],(s44-s49)*sensors2['DF'][43],(s45-s49)*sensors2['DF'][44],(s46-s49)*sensors2['DF'][45],(s47-s49)*sensors2['DF'][46],(s48-s49)*sensors2['DF'][47],(s49-s49)*sensors2['DF'][48],(s50-s49)*sensors2['DF'][49]], axis=1)
#result_DF.to_csv('TE_3DF.csv')
#print('complete')

def DF(i):
    df = (spike(i) - blk)*sensors2['DF'][i-1]
    return df

''''r1 = (a1-s49)*sensors2['DF'][0]
r2 = (s2-s49)*sensors2['DF'][1]
r3 = (s3-s49)*sensors2['DF'][2]
r4 = (s4-s49)*sensors2['DF'][3]
r5 = (s5-s49)*sensors2['DF'][4]
r6 = (s6-s49)*sensors2['DF'][5]
r7 = (s7-s49)*sensors2['DF'][6]
r8 = (s8-s49)*sensors2['DF'][7]
r9 = (s9-s49)*sensors2['DF'][8]
r10 = (s10-s49)*sensors2['DF'][9]
r11 = (s11-s49)*sensors2['DF'][10]
r12 = (s12-s49)*sensors2['DF'][11]
r13 = (s13-s49)*sensors2['DF'][12]
r14 = (s14-s49)*sensors2['DF'][13]
r15 = (s15-s49)*sensors2['DF'][14]
r16 = (s16-s49)*sensors2['DF'][15]
r17 = (s17-s49)*sensors2['DF'][16]
r18 = (s18-s49)*sensors2['DF'][17]
r19 = (s19-s49)*sensors2['DF'][18]
r20 = (s20-s49)*sensors2['DF'][19]
r21 = (s21-s49)*sensors2['DF'][20]
r22 = (s22-s49)*sensors2['DF'][21]
r23 = (s23-s49)*sensors2['DF'][22]
r24 = (s24-s49)*sensors2['DF'][23]
r25 = (s25-s49)*sensors2['DF'][24]
r26 = (s26-s49)*sensors2['DF'][25]
r27 = (s27-s49)*sensors2['DF'][26]
r28 = (s28-s49)*sensors2['DF'][27]
r29 = (s29-s49)*sensors2['DF'][28]
r30 = (s30-s49)*sensors2['DF'][29]
r31 = (s31-s49)*sensors2['DF'][30]
r32 = (s32-s49)*sensors2['DF'][31]
r33 = (s33-s49)*sensors2['DF'][32]
r34 = (s34-s49)*sensors2['DF'][33]
r35 = (s35-s49)*sensors2['DF'][34]
r36 = (s36-s49)*sensors2['DF'][35]
r37 = (s37-s49)*sensors2['DF'][36]
r38 = (s38-s49)*sensors2['DF'][37]
r39 = (s39-s49)*sensors2['DF'][38]
r40 = (s40-s49)*sensors2['DF'][39]
r41 = (s41-s49)*sensors2['DF'][40]
r42 = (s42-s49)*sensors2['DF'][41]
r43 = (s43-s49)*sensors2['DF'][42]
r44 = (s44-s49)*sensors2['DF'][43]
r45 = (s45-s49)*sensors2['DF'][44]
r46 = (s46-s49)*sensors2['DF'][45]
r47 = (s47-s49)*sensors2['DF'][46]
r48 = (s48-s49)*sensors2['DF'][47]
r49 = (s49-s49)*sensors2['DF'][48]
r50 = (s50-s49)*sensors2['DF'][49]'''

# External standard calibration

def extcali(i):
    
    if i<=14:
        t[i] = DF[i]-(DF[14]-DF[1])/13*0
    elif 15 >= i <= 25:
        t[i] = DF[i]-(DF[25]-DF[1])/11*1
    elif 26 >= i <= 36:
        t[i] = DF[i]-(DF[36]-DF[1])/11*1



t1 = r1-(r14-r1)/13*0
t2 = r2-(r14-r1)/13*1
t3 = r3-(r14-r1)/13*2
t4 = r4-(r14-r1)/13*3
t5 = r5-(r14-r1)/13*4
t6 = r6-(r14-r1)/13*5
t7 = r7-(r14-r1)/13*6
t8 = r8-(r14-r1)/13*7
t9 = r9-(r14-r1)/13*8
t10 = r10-(r14-r1)/13*9
t11 = r11-(r14-r1)/13*10
t12 = r12-(r14-r1)/13*11
t13 = r13-(r14-r1)/13*12
t14 = r14-(r14-r1)/13*13
t15 = r15-(r25-r1)/11*1
t16 = r16-(r25-r1)/11*2
t17 = r17-(r25-r1)/11*3
t18 = r18-(r25-r1)/11*4
t19 = r19-(r25-r1)/11*5
t20 = r20-(r25-r1)/11*6
t21 = r21-(r25-r1)/11*7
t22 = r22-(r25-r1)/11*8
t23 = r23-(r25-r1)/11*9
t24 = r24-(r25-r1)/11*10
t25 = r25-(r25-r1)/11*11

t26 = r26-(r36-r1)/11*1
t27 = r27-(r36-r1)/11*2
t28 = r28-(r36-r1)/11*3
t29 = r29-(r36-r1)/11*4
t30 = r30-(r36-r1)/11*5
t31 = r31-(r36-r1)/11*6
t32 = r32-(r36-r1)/11*7
t33 = r33-(r36-r1)/11*8
t34 = r34-(r36-r1)/11*9
t35 = r35-(r36-r1)/11*10
t36 = r36-(r36-r1)/11*11

t37 = r37-(r50-r1)/14*1
t38 = r38-(r50-r1)/14*2
t39 = r39-(r50-r1)/14*3
t40 = r40-(r50-r1)/14*4
t41 = r41-(r50-r1)/14*5
t42 = r42-(r50-r1)/14*6
t43 = r43-(r50-r1)/14*7
t44 = r44-(r50-r1)/14*8
t45 = r45-(r50-r1)/14*9
t46 = r46-(r50-r1)/14*10
t47 = r47-(r50-r1)/14*11
t48 = r48-(r50-r1)/14*12
t49 = r49-(r50-r1)/14*13
t50 = r50-(r50-r1)/14*14


result_ExtCali = pd.concat([isotope,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30,t31,t32,t33,t34,t35,t36,t37,t38,t39,t40,t41,t42,t43,t44,t45,t46,t47,t48,t49,t50], axis=1)
result_ExtCali.to_csv('TE_4ExtCali.csv')
print('complete')

# 5_Standard Value Calibration

v1 = 0.001*sensors3['w-2a']
v2 = 0.001*t2*sensors3['w-2a']/t1
v3 = 0.001*t3*sensors3['w-2a']/t1
v4 = 0.001*t4*sensors3['w-2a']/t1
v5 = 0.001*t5*sensors3['w-2a']/t1
v6 = 0.001*t6*sensors3['w-2a']/t1
v7 = 0.001*t7*sensors3['w-2a']/t1
v8 = 0.001*t8*sensors3['w-2a']/t1
v9 = 0.001*t9*sensors3['w-2a']/t1
v10 = 0.001*t10*sensors3['w-2a']/t1
v11 = 0.001*t11*sensors3['w-2a']/t1
v12 = 0.001*t12*sensors3['w-2a']/t1
v13 = 0.001*t13*sensors3['w-2a']/t1
v14 = 0.001*t14*sensors3['w-2a']/t1
v15 = 0.001*t15*sensors3['w-2a']/t1
v16 = 0.001*t16*sensors3['w-2a']/t1
v17 = 0.001*t17*sensors3['w-2a']/t1
v18 = 0.001*t18*sensors3['w-2a']/t1
v19 = 0.001*t19*sensors3['w-2a']/t1
v20 = 0.001*t20*sensors3['w-2a']/t1
v21 = 0.001*t21*sensors3['w-2a']/t1
v22 = 0.001*t22*sensors3['w-2a']/t1
v23 = 0.001*t23*sensors3['w-2a']/t1
v24 = 0.001*t24*sensors3['w-2a']/t1
v25 = 0.001*t25*sensors3['w-2a']/t1
v26 = 0.001*t26*sensors3['w-2a']/t1
v27 = 0.001*t27*sensors3['w-2a']/t1
v28 = 0.001*t28*sensors3['w-2a']/t1
v29 = 0.001*t29*sensors3['w-2a']/t1
v30 = 0.001*t30*sensors3['w-2a']/t1
v31 = 0.001*t31*sensors3['w-2a']/t1
v32 = 0.001*t32*sensors3['w-2a']/t1
v33 = 0.001*t33*sensors3['w-2a']/t1
v34 = 0.001*t34*sensors3['w-2a']/t1
v35 = 0.001*t35*sensors3['w-2a']/t1
v36 = 0.001*t36*sensors3['w-2a']/t1
v37 = 0.001*t37*sensors3['w-2a']/t1
v38 = 0.001*t38*sensors3['w-2a']/t1
v39 = 0.001*t39*sensors3['w-2a']/t1
v40 = 0.001*t40*sensors3['w-2a']/t1
v41 = 0.001*t41*sensors3['w-2a']/t1
v42 = 0.001*t42*sensors3['w-2a']/t1
v43 = 0.001*t43*sensors3['w-2a']/t1
v44 = 0.001*t44*sensors3['w-2a']/t1
v45 = 0.001*t45*sensors3['w-2a']/t1
v46 = 0.001*t46*sensors3['w-2a']/t1
v47 = 0.001*t47*sensors3['w-2a']/t1
v48 = 0.001*t48*sensors3['w-2a']/t1
v49 = 0.001*t49*sensors3['w-2a']/t1
v50 = 0.001*t50*sensors3['w-2a']/t1

pd.cut(data,4,precision=2)
#pd.set_option('display.precision',2)
result_Final = pd.concat([isotope,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30,v31,v32,v33,v34,v35,v36,v37,v38,v39,v40,v41,v42,v43,v44,v45,v46,v47,v48,v49,v50], axis=1)
result_Final.to_csv('TE_5Final.csv',index = False,float_format = '%.4f')

print('complete')
