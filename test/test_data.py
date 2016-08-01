#!/usr/bin/env python3
# coding:utf-8

initial_cordinates_of_test_data = [[15.307999610900879, 14.180000305175781, -2.9549999237060547], [13.364999771118164, 10.960000038146973, -3.638000011444092], [11.954999923706055, 8.303999900817871, -1.277999997138977], [12.336999893188477, 4.502999782562256, -1.1009999513626099], [8.697999954223633, 3.385999917984009, -1.4809999465942383], [9.689000129699707, -0.1589999943971634, -0.44600000977516174], [12.826000213623047, -1.9759999513626099, 0.7509999871253967], [14.081999778747559, -3.493000030517578, -2.5420000553131104], [15.680999755859375, -6.744999885559082, -1.3220000267028809], [18.302000045776367, -6.999000072479248, -4.0960001945495605], [20.139999389648438, -10.347999572753906, -4.236999988555908], [23.450000762939453, -9.487000465393066, -5.951000213623047], [26.086999893188477, -7.065000057220459, -4.61899995803833], [25.798999786376953, -5.071000099182129, -7.867000102996826], [22.673999786376953, -3.3429999351501465, -6.505000114440918], [22.42300033569336, -2.434999942779541, -2.805000066757202], [19.118999481201172, -3.194999933242798, -1.097000002861023], [17.812999725341797, -0.013000000268220901, 0.5379999876022339], [14.687999725341797, 0.4749999940395355, 2.6489999294281006], [11.649999618530273, 2.76200008392334, 2.9649999141693115], [12.01200008392334, 5.938000202178955, 5.057000160217285], [15.718999862670898, 6.26200008392334, 4.188000202178955], [16.908000946044922, 9.27299976348877, 2.1570000648498535], [18.569000244140625, 8.522000312805176, -1.2009999752044678], [20.018999099731445, 10.83899974822998, -3.872999906539917], [18.902999877929688, 9.663000106811523, -7.335999965667725], [21.764999389648438, 9.57699966430664, -9.866000175476074], [20.538999557495117, 8.9399995803833, -13.42300033569336], [17.67799949645996, 7.228000164031982, -15.305000305175781], [14.692000389099121, 9.612000465393066, -15.232000350952148], [12.225000381469727, 7.210999965667725, -16.891000747680664], [10.696000099182129, 4.373000144958496, -14.843000411987305], [13.13700008392334, 1.437999963760376, -14.597999572753906], [16.121999740600586, 0.9900000095367432, -12.243000030517578], [17.858999252319336, 4.26800012588501, -11.432000160217285], [21.013999938964844, 4.235000133514404, -9.289999961853027], [20.83300018310547, 6.24399995803833, -6.051000118255615], [23.715999603271484, 7.111000061035156, -3.6989998817443848], [23.222000122070312, 7.133999824523926, 0.09200000017881393], [24.538999557495117, 10.272000312805176, 1.8300000429153442], [25.201000213623047, 8.354000091552734, 5.067999839782715], [28.086000442504883, 6.034999847412109, 4.117000102996826], [28.283000946044922, 6.8379998207092285, 0.3880000114440918], [27.500999450683594, 3.4579999446868896, -1.2120000123977661], [25.961000442504883, 3.0199999809265137, -4.681000232696533], [22.829999923706055, 0.8619999885559082, -5.0269999504089355], [20.312000274658203, 0.5569999814033508, -7.883999824523926], [16.933000564575195, 1.4730000495910645, -6.343999862670898], [13.968999862670898, 0.17800000309944153, -8.373000144958496], [11.809000015258789, 2.989000082015991, -9.800999641418457], [8.670000076293945, 1.1829999685287476, -8.595000267028809], [10.321999549865723, 1.1009999513626099, -5.15500020980835], [11.125, 4.8420000076293945, -5.177000045776367], [9.199999809265137, 8.090999603271484, -5.690999984741211], [10.072999954223633, 11.789999961853027, -6.056000232696533], [9.020000457763672, 12.87600040435791, -2.5439999103546143]]

final_cordinates_of_test_data = [[78.43315887451172, 35.51805877685547, 5.556694507598877], [81.96025085449219, 34.197322845458984, 5.211187362670898], [83.4459228515625, 32.309913635253906, 8.214234352111816], [86.54580688476562, 32.78153610229492, 10.283455848693848], [87.27523803710938, 29.12166976928711, 10.972208976745605], [90.48776245117188, 29.972257614135742, 12.840511322021484], [91.9996566772461, 33.13146209716797, 14.205047607421875], [94.91548156738281, 33.22194290161133, 11.658781051635742], [98.11425018310547, 34.15675735473633, 13.611642837524414], [100.4653091430664, 35.51393508911133, 10.87629222869873], [103.88807678222656, 36.9473876953125, 11.813323974609375], [104.58187866210938, 38.52876281738281, 8.416688919067383], [102.20338439941406, 40.99657440185547, 6.6855034828186035], [102.55950164794922, 38.534576416015625, 3.850598096847534], [99.4938735961914, 36.746421813964844, 5.195196151733398], [96.98335266113281, 38.897064208984375, 7.092864036560059], [95.92755126953125, 37.986778259277344, 10.65024185180664], [92.20399475097656, 37.824371337890625, 11.2726411819458], [90.41583251953125, 36.66209411621094, 14.384759902954102], [87.25629425048828, 34.48030471801758, 15.161192893981934], [83.79753875732422, 36.194786071777344, 15.146379470825195], [84.10186767578125, 39.16248321533203, 12.753555297851562], [82.3707046508789, 38.951995849609375, 9.447654724121094], [84.77000427246094, 38.92145538330078, 6.477579116821289], [83.79460906982422, 39.453548431396484, 2.805020809173584], [85.86894226074219, 37.30231857299805, 0.23087258636951447], [87.25152587890625, 39.253562927246094, -2.7537155151367188], [87.89486694335938, 36.94953918457031, -5.6786789894104], [88.94159698486328, 33.47360610961914, -6.871370315551758], [85.4085922241211, 31.920467376708984, -6.591397762298584], [86.52474212646484, 28.410659790039062, -5.669405937194824], [88.62825775146484, 27.654245376586914, -2.663381814956665], [92.5344467163086, 28.129783630371094, -2.943727970123291], [94.52381896972656, 31.197216033935547, -1.6968928575515747], [91.8978271484375, 34.00438690185547, -1.9192579984664917], [91.72053527832031, 37.45264434814453, -0.3666795492172241], [89.22759246826172, 38.9824104309082, 2.026475429534912], [88.68406677246094, 42.533382415771484, 3.072687864303589], [87.50738525390625, 44.069976806640625, 6.320072650909424], [84.7143325805664, 46.64250946044922, 6.477212905883789], [86.32901000976562, 48.02796173095703, 9.612631797790527], [89.1877670288086, 50.31990051269531, 8.408884048461914], [89.72052001953125, 48.9617805480957, 4.894818305969238], [92.80072021484375, 46.91524124145508, 5.471734046936035], [93.32341766357422, 43.78317642211914, 3.206293821334839], [94.39198303222656, 40.27346420288086, 4.278508186340332], [93.91532897949219, 36.79694747924805, 2.6064579486846924], [91.84101104736328, 33.87779998779297, 4.021574020385742], [93.01341247558594, 30.362733840942383, 2.8328311443328857], [90.69708251953125, 27.198871612548828, 2.49924898147583], [92.56083679199219, 26.002023696899414, 5.522829532623291], [90.57273864746094, 28.683368682861328, 7.602810859680176], [87.17500305175781, 28.812206268310547, 5.842682838439941], [83.84363555908203, 27.10403823852539, 5.492925643920898], [80.37438201904297, 27.99285125732422, 4.288708686828613], [79.1759033203125, 29.027931213378906, 7.75678825378418]]
