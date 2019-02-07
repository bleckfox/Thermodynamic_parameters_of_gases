import sys
from lariel_v2 import *
import math

from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Начало кода

        # Параметры воздуха
        self.ui.result_air.clicked.connect(self.air)
        self.ui.result_air.clicked.connect(self.air2)
        self.ui.result_air.clicked.connect(self.air3)
        self.ui.result_air.clicked.connect(self.air4)

        # Параметры водяного пара
        self.ui.result_wat_vap.clicked.connect(self.water_vapor)
        self.ui.result_wat_vap.clicked.connect(self.water_vapor2)
        self.ui.result_wat_vap.clicked.connect(self.water_vapor3)
        self.ui.result_wat_vap.clicked.connect(self.water_vapor4)

        # Параметры кислорода
        self.ui.result_oxy.clicked.connect(self.oxygen)
        self.ui.result_oxy.clicked.connect(self.oxygen2)
        self.ui.result_oxy.clicked.connect(self.oxygen3)
        self.ui.result_oxy.clicked.connect(self.oxygen4)

        # Параметры азота
        self.ui.result_nitro.clicked.connect(self.nitrogen)
        self.ui.result_nitro.clicked.connect(self.nitrogen2)
        self.ui.result_nitro.clicked.connect(self.nitrogen3)
        self.ui.result_nitro.clicked.connect(self.nitrogen4)

        #Параметры амтосферного азота
        self.ui.result_nitro_diox.clicked.connect(self.nitrogen_dioxide)
        self.ui.result_nitro_diox.clicked.connect(self.nitrogen_dioxide2)
        self.ui.result_nitro_diox.clicked.connect(self.nitrogen_dioxide3)
        self.ui.result_nitro_diox.clicked.connect(self.nitrogen_dioxide4)

        #Параметры водорода
        self.ui.result_hydro.clicked.connect(self.hydrogen)
        self.ui.result_hydro.clicked.connect(self.hydrogen2)
        self.ui.result_hydro.clicked.connect(self.hydrogen3)
        self.ui.result_hydro.clicked.connect(self.hydrogen4)

        #Параметры углекислого газа
        self.ui.result_carb_diox.clicked.connect(self.carbone_dioxide)
        self.ui.result_carb_diox.clicked.connect(self.carbone_dioxide2)
        self.ui.result_carb_diox.clicked.connect(self.carbone_dioxide3)
        self.ui.result_carb_diox.clicked.connect(self.carbone_dioxide4)

        #Параметры оксида углерода
        self.ui.result_carbone.clicked.connect(self.carbone)
        self.ui.result_carbone.clicked.connect(self.carbone2)
        self.ui.result_carbone.clicked.connect(self.carbone3)
        self.ui.result_carbone.clicked.connect(self.carbone4)



    #Параметры воздуха
    def air(self):
        try:
            t = self.ui.temp_C_point_air.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                        T = float(t) + 273.15
                        self.ui.temp_K_point_air.setText(str(round(T,3)))
                        tt = T / 1000
                        log = math.log(T / 1000)
                        bs = 29.438205
                        n = -1
                        weight = 28.9596308
                        pr_entropy = bs * log
                        sum_entropy = 0

                        air_coef_entropy = [0, 230.1763, -1.610822, -5.9958719,
                                                22.942794, -24.559982, 12.976701,
                                                -3.4848967, 0.3807486]

                        for i in range(len(air_coef_entropy)):
                            entropy = air_coef_entropy[i] * (tt ** n)
                            n = n + 1
                            sum_entropy += entropy
                        S_entropy = sum_entropy + pr_entropy
                        result_entropy = S_entropy / weight

                        # Выводим результат энтропии
                        self.ui.mol_entropy_point_air.setText(str(round(S_entropy,3)))
                        self.ui.entropy_point_air.setText(str(round(result_entropy,3)))


                        # Энтальпия
                        bh = 0
                        N = 0
                        pr_enthalpy = bh * log
                        sum_enthalpy = 0
                        air_coef_enthalpy = [-542, 29438.265, -805.41099, -3997.2481,
                                            17207.096, -19647.986, 10813.917, -2987.0543,
                                            333.15502]

                        for i in range(len(air_coef_enthalpy)):
                            enthalpy = air_coef_enthalpy[i] * (tt ** N)
                            N = N + 1
                            sum_enthalpy += enthalpy
                        S_enthalpy = sum_enthalpy + pr_enthalpy + 487.6
                        result_enthalpy = S_enthalpy / weight

                        # Выводим результат энтальпии
                        self.ui.mol_enthalpy_point_air.setText(str(round(S_enthalpy,3)))
                        self.ui.enthalpy_point_air.setText(str(round(result_enthalpy,3)))
            else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Ошибка ввода!')
                    msg.setText('Диапозон температур от -50 до 1500')
                    msg.setIcon(msg.Warning)
                    msg.exec()
        except ValueError:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Введите числа, но не буквы')
                msg.setIcon(msg.Warning)
                msg.exec()
    def air2(self):
        try:
            t = self.ui.temp_C_point_air_2.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                    T = float(t) + 273.15
                    self.ui.temp_K_point_air_2.setText(str(round(T,3)))
                    tt = T / 1000
                    log = math.log(T / 1000)
                    bs = 29.438205
                    n = -1
                    weight = 28.9596308
                    pr_entropy = bs * log
                    sum_entropy = 0

                    air_coef_entropy = [0, 230.1763, -1.610822, -5.9958719,
                                            22.942794, -24.559982, 12.976701,
                                            -3.4848967, 0.3807486]

                    for i in range(len(air_coef_entropy)):
                        entropy = air_coef_entropy[i] * (tt ** n)
                        n = n + 1
                        sum_entropy += entropy
                    S_entropy = sum_entropy + pr_entropy
                    result_entropy = S_entropy / weight

                    # Выводим результат энтропии
                    self.ui.mol_entropy_point_air_2.setText(str(round(S_entropy,3)))
                    self.ui.entropy_point_air_2.setText(str(round(result_entropy,3)))


                    # Энтальпия
                    bh = 0
                    N = 0
                    pr_enthalpy = bh * log
                    sum_enthalpy = 0
                    air_coef_enthalpy = [-542, 29438.265, -805.41099, -3997.2481,
                                        17207.096, -19647.986, 10813.917, -2987.0543,
                                        333.15502]

                    for i in range(len(air_coef_enthalpy)):
                        enthalpy = air_coef_enthalpy[i] * (tt ** N)
                        N = N + 1
                        sum_enthalpy += enthalpy
                    S_enthalpy = sum_enthalpy + pr_enthalpy + 487.6
                    result_enthalpy = S_enthalpy / weight

                    # Выводим результат энтальпии
                    self.ui.mol_enthalpy_point_air_2.setText(str(round(S_enthalpy,3)))
                    self.ui.enthalpy_point_air_2.setText(str(round(result_enthalpy,3)))
            else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Ошибка ввода!')
                    msg.setText('Диапозон температур от -50 до 1500')
                    msg.setIcon(msg.Warning)
                    msg.exec()
        except ValueError:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Введите числа, но не буквы')
                msg.setIcon(msg.Warning)
                msg.exec()
    def air3(self):
        try:
            t = self.ui.temp_C_point_air_3.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                    T = float(t) + 273.15
                    self.ui.temp_K_point_air_3.setText(str(round(T,3)))
                    tt = T / 1000
                    log = math.log(T / 1000)
                    bs = 29.438205
                    n = -1
                    weight = 28.9596308
                    pr_entropy = bs * log
                    sum_entropy = 0

                    air_coef_entropy = [0, 230.1763, -1.610822, -5.9958719,
                                            22.942794, -24.559982, 12.976701,
                                            -3.4848967, 0.3807486]

                    for i in range(len(air_coef_entropy)):
                        entropy = air_coef_entropy[i] * (tt ** n)
                        n = n + 1
                        sum_entropy += entropy
                    S_entropy = sum_entropy + pr_entropy
                    result_entropy = S_entropy / weight

                    # Выводим результат энтропии
                    self.ui.mol_entropy_point_air_3.setText(str(round(S_entropy,3)))
                    self.ui.entropy_point_air_3.setText(str(round(result_entropy,3)))


                    # Энтальпия
                    bh = 0
                    N = 0
                    pr_enthalpy = bh * log
                    sum_enthalpy = 0
                    air_coef_enthalpy = [-542, 29438.265, -805.41099, -3997.2481,
                                        17207.096, -19647.986, 10813.917, -2987.0543,
                                        333.15502]

                    for i in range(len(air_coef_enthalpy)):
                        enthalpy = air_coef_enthalpy[i] * (tt ** N)
                        N = N + 1
                        sum_enthalpy += enthalpy
                    S_enthalpy = sum_enthalpy + pr_enthalpy + 487.6
                    result_enthalpy = S_enthalpy / weight

                    # Выводим результат энтальпии
                    self.ui.mol_enthalpy_point_air_3.setText(str(round(S_enthalpy,3)))
                    self.ui.enthalpy_point_air_3.setText(str(round(result_enthalpy,3)))
            else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Ошибка ввода!')
                    msg.setText('Диапозон температур от -50 до 1500')
                    msg.setIcon(msg.Warning)
                    msg.exec()
        except ValueError:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Введите числа, но не буквы')
                msg.setIcon(msg.Warning)
                msg.exec()
    def air4(self):
        try:
            t = self.ui.temp_C_point_air_4.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                    T = float(t) + 273.15
                    self.ui.temp_K_point_air_4.setText(str(round(T,3)))
                    tt = T / 1000
                    log = math.log(T / 1000)
                    bs = 29.438205
                    n = -1
                    weight = 28.9596308
                    pr_entropy = bs * log
                    sum_entropy = 0

                    air_coef_entropy = [0, 230.1763, -1.610822, -5.9958719,
                                            22.942794, -24.559982, 12.976701,
                                            -3.4848967, 0.3807486]

                    for i in range(len(air_coef_entropy)):
                        entropy = air_coef_entropy[i] * (tt ** n)
                        n = n + 1
                        sum_entropy += entropy
                    S_entropy = sum_entropy + pr_entropy
                    result_entropy = S_entropy / weight

                    # Выводим результат энтропии
                    self.ui.mol_entropy_point_air_4.setText(str(round(S_entropy,3)))
                    self.ui.entropy_point_air_4.setText(str(round(result_entropy,3)))


                    # Энтальпия
                    bh = 0
                    N = 0
                    pr_enthalpy = bh * log
                    sum_enthalpy = 0
                    air_coef_enthalpy = [-542, 29438.265, -805.41099, -3997.2481,
                                        17207.096, -19647.986, 10813.917, -2987.0543,
                                        333.15502]

                    for i in range(len(air_coef_enthalpy)):
                        enthalpy = air_coef_enthalpy[i] * (tt ** N)
                        N = N + 1
                        sum_enthalpy += enthalpy
                    S_enthalpy = sum_enthalpy + pr_enthalpy + 487.6
                    result_enthalpy = S_enthalpy / weight

                    # Выводим результат энтальпии
                    self.ui.mol_enthalpy_point_air_4.setText(str(round(S_enthalpy,3)))
                    self.ui.enthalpy_point_air_4.setText(str(round(result_enthalpy,3)))
            else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Ошибка ввода!')
                    msg.setText('Диапозон температур от -50 до 1500')
                    msg.setIcon(msg.Warning)
                    msg.exec()
        except ValueError:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Введите числа, но не буквы')
                msg.setIcon(msg.Warning)
                msg.exec()

    # Параметры водяного пара
    def water_vapor(self):
        try:
            t = self.ui.temp_C_point_wat_vap.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_wat_vap.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 27.885805
                n = -1
                weight = 18.016
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [-0.731476, 221.9783, 8.4430197,
                    5.9926485, -5.3640779, 3.4089868,
                    -1.29458, 0.1481876, 0]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_wat_vap.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_wat_vap.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 731.476
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [2012.947, 27885.805, 4221.5098, 3995.099,
                    -4023.058, 2727.2546, -1078.8167,
                    169.87509, 0]

                for i in range(len(air_coef_enthalpy)):
                    enthaply = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthaply
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_wat_vap.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_wat_vap.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Введите числа, но не буквы')
                msg.setIcon(msg.Warning)
                msg.exec()
    def water_vapor2(self):
        try:
            t = self.ui.temp_C_point_wat_vap_2.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_wat_vap_2.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 27.885805
                n = -1
                weight = 18.016
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [-0.731476, 221.9783, 8.4430197,
                    5.9926485, -5.3640779, 3.4089868,
                    -1.29458, 0.1481876, 0]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_wat_vap_2.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_wat_vap_2.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 731.476
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [2012.947, 27885.805, 4221.5098, 3995.099,
                    -4023.058, 2727.2546, -1078.8167,
                    169.87509, 0]

                for i in range(len(air_coef_enthalpy)):
                    enthaply = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthaply
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_wat_vap_2.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_wat_vap_2.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Введите числа, но не буквы')
                msg.setIcon(msg.Warning)
                msg.exec()
    def water_vapor3(self):
        try:
            t = self.ui.temp_C_point_wat_vap_3.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_wat_vap_3.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 27.885805
                n = -1
                weight = 18.016
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [-0.731476, 221.9783, 8.4430197,
                    5.9926485, -5.3640779, 3.4089868,
                    -1.29458, 0.1481876, 0]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_wat_vap_3.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_wat_vap_3.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 731.476
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [2012.947, 27885.805, 4221.5098, 3995.099,
                    -4023.058, 2727.2546, -1078.8167,
                    169.87509, 0]

                for i in range(len(air_coef_enthalpy)):
                    enthaply = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthaply
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_wat_vap_3.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_wat_vap_3.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Введите числа, но не буквы')
                msg.setIcon(msg.Warning)
                msg.exec()
    def water_vapor4(self):
        try:
            t = self.ui.temp_C_point_wat_vap_4.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_wat_vap_4.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 27.885805
                n = -1
                weight = 18.016
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [-0.731476, 221.9783, 8.4430197,
                    5.9926485, -5.3640779, 3.4089868,
                    -1.29458, 0.1481876, 0]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_wat_vap_4.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_wat_vap_4.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 731.476
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [2012.947, 27885.805, 4221.5098, 3995.099,
                    -4023.058, 2727.2546, -1078.8167,
                    169.87509, 0]

                for i in range(len(air_coef_enthalpy)):
                    enthaply = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthaply
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_wat_vap_4.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_wat_vap_4.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Введите числа, но не буквы')
                msg.setIcon(msg.Warning)
                msg.exec()

    # Параметры кислорода
    def oxygen(self):
        try:
            t = self.ui.temp_C_point_oxy.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_oxy.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 33.051759
                n = -1
                weight = 32
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 252.4995, -41.834166, 74.012048,
                    -68.340764, 36.342, -10.458144,
                    1.2628462, 0]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_oxy.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_oxy.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [-300.3, 33051.759, -20917.083, 49341.367,
                    -51255.572, 29073.599, -8715.1202,
                    1082.4395, 0]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_oxy.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_oxy.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def oxygen2(self):
        try:
            t = self.ui.temp_C_point_oxy_2.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_oxy_2.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 33.051759
                n = -1
                weight = 32
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 252.4995, -41.834166, 74.012048,
                    -68.340764, 36.342, -10.458144,
                    1.2628462, 0]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_oxy_2.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_oxy_2.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [-300.3, 33051.759, -20917.083, 49341.367,
                    -51255.572, 29073.599, -8715.1202,
                    1082.4395, 0]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_oxy_2.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_oxy_2.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def oxygen3(self):
        try:
            t = self.ui.temp_C_point_oxy_3.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_oxy_3.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 33.051759
                n = -1
                weight = 32
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 252.4995, -41.834166, 74.012048,
                    -68.340764, 36.342, -10.458144,
                    1.2628462, 0]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_oxy_3.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_oxy_3.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [-300.3, 33051.759, -20917.083, 49341.367,
                    -51255.572, 29073.599, -8715.1202,
                    1082.4395, 0]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_oxy_3.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_oxy_3.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def oxygen4(self):
        try:
            t = self.ui.temp_C_point_oxy_4.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_oxy_4.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 33.051759
                n = -1
                weight = 32
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 252.4995, -41.834166, 74.012048,
                    -68.340764, 36.342, -10.458144,
                    1.2628462, 0]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_oxy_4.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_oxy_4.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [-300.3, 33051.759, -20917.083, 49341.367,
                    -51255.572, 29073.599, -8715.1202,
                    1082.4395, 0]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_oxy_4.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_oxy_4.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()

    # Параметры азота
    def nitrogen(self):
        try:
            t = self.ui.temp_C_point_nitro.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_nitro.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 28.298404
                n = -1
                weight = 28.016
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 223.9189, 12.689906, -36.209046,
                    61.787635, -55.105807, 27.471033,
                    -7.3015678, 0.8088504]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_nitro.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_nitro.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [25.45, 28298.404, 6344.9526, -24139.364, 46340.725,
                    -44084.647, 22892.528, -6258.4868, 707.7441]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_nitro.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_nitro.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def nitrogen2(self):
        try:
            t = self.ui.temp_C_point_nitro_2.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_nitro_2.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 28.298404
                n = -1
                weight = 28.016
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 223.9189, 12.689906, -36.209046,
                    61.787635, -55.105807, 27.471033,
                    -7.3015678, 0.8088504]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_nitro_2.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_nitro_2.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [25.45, 28298.404, 6344.9526, -24139.364, 46340.725,
                    -44084.647, 22892.528, -6258.4868, 707.7441]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_nitro_2.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_nitro_2.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def nitrogen3(self):
        try:
            t = self.ui.temp_C_point_nitro_3.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_nitro_3.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 28.298404
                n = -1
                weight = 28.016
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 223.9189, 12.689906, -36.209046,
                    61.787635, -55.105807, 27.471033,
                    -7.3015678, 0.8088504]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_nitro_3.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_nitro_3.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [25.45, 28298.404, 6344.9526, -24139.364, 46340.725,
                    -44084.647, 22892.528, -6258.4868, 707.7441]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_nitro_3.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_nitro_3.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def nitrogen4(self):
        try:
            t = self.ui.temp_C_point_nitro_4.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_nitro_4.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 28.298404
                n = -1
                weight = 28.016
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 223.9189, 12.689906, -36.209046,
                    61.787635, -55.105807, 27.471033,
                    -7.3015678, 0.8088504]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_nitro_4.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_nitro_4.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [25.45, 28298.404, 6344.9526, -24139.364, 46340.725,
                    -44084.647, 22892.528, -6258.4868, 707.7441]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_nitro_4.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_nitro_4.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()

    #Параметры амтосферного азота
    def nitrogen_dioxide(self):
        try:
            t = self.ui.temp_C_point_nitro_diox.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_nitro_diox.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 28.15164
                n = -1
                weight = 28.15
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 223.2219, 13.197123, -37.241056,
                    63.327875, -56.654199, 28.408351,
                    -7.6067499, 0.84982197]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_nitro_diox.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_nitro_diox.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [40.1, 28151.964, 6598.5613, -24827.371,
                    47495.9, -45323.358, 23673.626,
                    -6520.071, 743.5942]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_nitro_diox.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_nitro_diox.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def nitrogen_dioxide2(self):
        try:
            t = self.ui.temp_C_point_nitro_diox_2.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_nitro_diox_2.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 28.15164
                n = -1
                weight = 28.15
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 223.2219, 13.197123, -37.241056,
                    63.327875, -56.654199, 28.408351,
                    -7.6067499, 0.84982197]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_nitro_diox_2.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_nitro_diox_2.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [40.1, 28151.964, 6598.5613, -24827.371,
                    47495.9, -45323.358, 23673.626,
                    -6520.071, 743.5942]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_nitro_diox_2.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_nitro_diox_2.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def nitrogen_dioxide3(self):
        try:
            t = self.ui.temp_C_point_nitro_diox_3.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_nitro_diox_3.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 28.15164
                n = -1
                weight = 28.15
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 223.2219, 13.197123, -37.241056,
                    63.327875, -56.654199, 28.408351,
                    -7.6067499, 0.84982197]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_nitro_diox_3.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_nitro_diox_3.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [40.1, 28151.964, 6598.5613, -24827.371,
                    47495.9, -45323.358, 23673.626,
                    -6520.071, 743.5942]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_nitro_diox_3.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_nitro_diox_3.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def nitrogen_dioxide4(self):
        try:
            t = self.ui.temp_C_point_nitro_diox_4.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_nitro_diox_4.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 28.15164
                n = -1
                weight = 28.15
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 223.2219, 13.197123, -37.241056,
                    63.327875, -56.654199, 28.408351,
                    -7.6067499, 0.84982197]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_nitro_diox_4.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_nitro_diox_4.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [40.1, 28151.964, 6598.5613, -24827.371,
                    47495.9, -45323.358, 23673.626,
                    -6520.071, 743.5942]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_nitro_diox_4.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_nitro_diox_4.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()

    #Параметры водорода
    def hydrogen(self):
        try:
            t = self.ui.temp_C_point_hydro.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_hydro.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 40.01059
                n = -1
                weight = 2.016
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [1.7412059, 179.3853, -23.707024,
                                    9.6099679, 0.48559888, -2.1266412,
                                    0.82772475, -0.11031765, 0]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_hydro.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_hydro.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = -1741.2059
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [-4684.72, 40010.59, -11853.512,
                                    6406.6451, 364.19916, -1701.313,
                                    689.77065, -94.557986, 0]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_hydro.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_hydro.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def hydrogen2(self):
        try:
            t = self.ui.temp_C_point_hydro_2.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_hydro_2.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 40.01059
                n = -1
                weight = 2.016
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [1.7412059, 179.3853, -23.707024,
                                    9.6099679, 0.48559888, -2.1266412,
                                    0.82772475, -0.11031765, 0]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_hydro_2.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_hydro_2.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = -1741.2059
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [-4684.72, 40010.59, -11853.512,
                                    6406.6451, 364.19916, -1701.313,
                                    689.77065, -94.557986, 0]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_hydro_2.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_hydro_2.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def hydrogen3(self):
        try:
            t = self.ui.temp_C_point_hydro_3.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_hydro_3.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 40.01059
                n = -1
                weight = 2.016
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [1.7412059, 179.3853, -23.707024,
                                    9.6099679, 0.48559888, -2.1266412,
                                    0.82772475, -0.11031765, 0]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_hydro_3.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_hydro_3.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = -1741.2059
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [-4684.72, 40010.59, -11853.512,
                                    6406.6451, 364.19916, -1701.313,
                                    689.77065, -94.557986, 0]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_hydro_3.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_hydro_3.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def hydrogen4(self):
        try:
            t = self.ui.temp_C_point_hydro_4.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_hydro_4.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 40.01059
                n = -1
                weight = 2.016
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [1.7412059, 179.3853, -23.707024,
                                    9.6099679, 0.48559888, -2.1266412,
                                    0.82772475, -0.11031765, 0]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_hydro_4.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_hydro_4.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = -1741.2059
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [-4684.72, 40010.59, -11853.512,
                                    6406.6451, 364.19916, -1701.313,
                                    689.77065, -94.557986, 0]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_hydro_4.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_hydro_4.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()

    #Параметры углекислого газа
    def carbone_dioxide(self):
        try:
            t = self.ui.temp_C_point_carb_diox.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_carb_diox.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 17.640049
                n = -1
                weight = 44.01
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 211.7171, 93.726944, -65.187329,
                    51.323515, -34.999006, 16.630372,
                    -4.5964181, 0.5471162]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_carb_diox.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_carb_diox.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [847.4, 17640.049, 46863.472, -43458.218,
                    38492.636, -27999.206, 13858.643,
                    -3939.7868, 478.72667]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_carb_diox.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_carb_diox.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def carbone_dioxide2(self):
        try:
            t = self.ui.temp_C_point_carb_diox_2.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_carb_diox_2.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 17.640049
                n = -1
                weight = 44.01
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 211.7171, 93.726944, -65.187329,
                    51.323515, -34.999006, 16.630372,
                    -4.5964181, 0.5471162]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_carb_diox_2.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_carb_diox_2.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [847.4, 17640.049, 46863.472, -43458.218,
                    38492.636, -27999.206, 13858.643,
                    -3939.7868, 478.72667]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_carb_diox_2.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_carb_diox_2.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def carbone_dioxide3(self):
        try:
            t = self.ui.temp_C_point_carb_diox_3.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_carb_diox_3.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 17.640049
                n = -1
                weight = 44.01
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 211.7171, 93.726944, -65.187329,
                    51.323515, -34.999006, 16.630372,
                    -4.5964181, 0.5471162]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_carb_diox_3.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_carb_diox_3.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [847.4, 17640.049, 46863.472, -43458.218,
                    38492.636, -27999.206, 13858.643,
                    -3939.7868, 478.72667]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_carb_diox_3.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_carb_diox_3.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()
    def carbone_dioxide4(self):
        try:
            t = self.ui.temp_C_point_carb_diox_4.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_carb_diox_4.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 17.640049
                n = -1
                weight = 44.01
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 211.7171, 93.726944, -65.187329,
                    51.323515, -34.999006, 16.630372,
                    -4.5964181, 0.5471162]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_carb_diox_4.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_carb_diox_4.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [847.4, 17640.049, 46863.472, -43458.218,
                    38492.636, -27999.206, 13858.643,
                    -3939.7868, 478.72667]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_carb_diox_4.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_carb_diox_4.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()

    #Параметры оксида углерода
    def carbone(self):
        try:
            t = self.ui.temp_C_point_carbone.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_carbone.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 24.161791
                n = -1
                weight = 28.01
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 232.9405, 4.135004, -21.887391,
                    48.743499, -48.832394, 26.18109,
                    -7.3483677, 0.85143506]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_carbone.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_carbone.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [-32.54, 29161.791, 2067.502,
                                    -14591.594, 36557.624, -39065.915,
                                    21817.574, -6298.6014, 745.00568]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_carbone.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_carbone.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()



        # Конец кода
    def carbone2(self):
        try:
            t = self.ui.temp_C_point_carbone_2.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_carbone_2.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 24.161791
                n = -1
                weight = 28.01
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 232.9405, 4.135004, -21.887391,
                    48.743499, -48.832394, 26.18109,
                    -7.3483677, 0.85143506]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_carbone_2.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_carbone_2.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [-32.54, 29161.791, 2067.502,
                                    -14591.594, 36557.624, -39065.915,
                                    21817.574, -6298.6014, 745.00568]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_carbone_2.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_carbone_2.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()



        # Конец кода
    def carbone3(self):
        try:
            t = self.ui.temp_C_point_carbone_3.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_carbone_3.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 24.161791
                n = -1
                weight = 28.01
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 232.9405, 4.135004, -21.887391,
                    48.743499, -48.832394, 26.18109,
                    -7.3483677, 0.85143506]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_carbone_3.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_carbone_3.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [-32.54, 29161.791, 2067.502,
                                    -14591.594, 36557.624, -39065.915,
                                    21817.574, -6298.6014, 745.00568]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_carbone_3.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_carbone_3.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()



        # Конец кода
    def carbone4(self):
        try:
            t = self.ui.temp_C_point_carbone_4.text()
            if t == '':
                pass
            elif -50 <= float(t) <= 1500:
                T = float(t) + 273.15
                self.ui.temp_K_point_carbone_4.setText(str(round(T,3)))
                tt = T / 1000
                log = math.log(T / 1000)
                bs = 24.161791
                n = -1
                weight = 28.01
                pr_entropy = bs * log
                sum_entropy = 0

                air_coef_entropy = [0, 232.9405, 4.135004, -21.887391,
                    48.743499, -48.832394, 26.18109,
                    -7.3483677, 0.85143506]

                for i in range(len(air_coef_entropy)):
                    entropy = air_coef_entropy[i] * (tt ** n)
                    n = n + 1
                    sum_entropy += entropy
                S_entropy = sum_entropy + pr_entropy
                result_entropy = S_entropy / weight

                # Выводим результат энтропии
                self.ui.mol_entropy_point_carbone_4.setText(str(round(S_entropy,3)))
                self.ui.entropy_point_carbone_4.setText(str(round(result_entropy,3)))


                # Энтальпия
                bh = 0
                N = 0
                pr_enthalpy = bh * log
                sum_enthalpy = 0
                air_coef_enthalpy = [-32.54, 29161.791, 2067.502,
                                    -14591.594, 36557.624, -39065.915,
                                    21817.574, -6298.6014, 745.00568]

                for i in range(len(air_coef_enthalpy)):
                    enthalpy = air_coef_enthalpy[i] * (tt ** N)
                    N = N + 1
                    sum_enthalpy += enthalpy
                S_enthalpy = sum_enthalpy + pr_enthalpy
                result_enthalpy = S_enthalpy / weight

                # Выводим результат энтальпии
                self.ui.mol_enthalpy_point_carbone_4.setText(str(round(S_enthalpy,3)))
                self.ui.enthalpy_point_carbone_4.setText(str(round(result_enthalpy,3)))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода!')
                msg.setText('Диапозон температур от -50 до 1500')
                msg.setIcon(msg.Warning)
                msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите числа, но не буквы')
            msg.setIcon(msg.Warning)
            msg.exec()



        # Конец кода

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
