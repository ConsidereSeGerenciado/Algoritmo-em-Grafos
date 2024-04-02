listaaa = []
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] > 0 and (i, j) not in listaaa and (j, i) not in listaaa:
            print(i, j)
            listaaa.append((i, j))
            listaaa.append((j, i))
            if i == 0 and j == 1:
                matrizCaminho[i][j] = 27.70
                matrizCaminho[j][i] = 27.70

            if i == 0 and j == 2:
                matrizCaminho[i][j] = 38.38
                matrizCaminho[j][i] = 38.38

            if i == 1 and j == 3:
                matrizCaminho[i][j] = 59.31
                matrizCaminho[j][i] = 59.31

            if i == 1 and j == 4:
                matrizCaminho[i][j] = 55.31
                matrizCaminho[j][i] = 55.31

            if i == 1 and j == 5:
                matrizCaminho[i][j] = 51.52
                matrizCaminho[j][i] = 51.52

            if i == 2 and j == 6:
                matrizCaminho[i][j] = 70.82
                matrizCaminho[j][i] = 70.82

            if i == 2 and j == 7:
                matrizCaminho[i][j] = 53.73
                matrizCaminho[j][i] = 53.73

            if i == 2 and j == 8:
                matrizCaminho[i][j] = 56.50
                matrizCaminho[j][i] = 56.50

            if i == 3 and j == 6:
                matrizCaminho[i][j] = 72.85
                matrizCaminho[j][i] = 72.85

            if i == 3 and j == 9:
                matrizCaminho[i][j] = 57.40
                matrizCaminho[j][i] = 57.40

            if i == 4 and j == 9:
                matrizCaminho[i][j] = 56.92
                matrizCaminho[j][i] = 56.92

            if i == 4 and j == 10:
                matrizCaminho[i][j] = 100.75
                matrizCaminho[j][i] = 100.75

            if i == 4 and j == 11:
                matrizCaminho[i][j] = 42.65
                matrizCaminho[j][i] = 42.65

            if i == 5 and j == 8:
                matrizCaminho[i][j] = 63.83
                matrizCaminho[j][i] = 63.83

            if i == 5 and j == 11:
                matrizCaminho[i][j] = 53.22
                matrizCaminho[j][i] = 53.22

            if i == 5 and j == 12:
                matrizCaminho[i][j] = 92.63
                matrizCaminho[j][i] = 92.63

            if i == 6 and j == 13:
                matrizCaminho[i][j] = 64.47
                matrizCaminho[j][i] = 64.47

            if i == 6 and j == 14:
                matrizCaminho[i][j] = 52.89
                matrizCaminho[j][i] = 52.89

            if i == 7 and j == 14:
                matrizCaminho[i][j] = 71.35
                matrizCaminho[j][i] = 71.35

            if i == 7 and j == 15:
                matrizCaminho[i][j] = 91.37
                matrizCaminho[j][i] = 91.37

            if i == 7 and j == 16:
                matrizCaminho[i][j] = 55.39
                matrizCaminho[j][i] = 55.39

            if i == 8 and j == 16:
                matrizCaminho[i][j] = 54.52
                matrizCaminho[j][i] = 54.52

            if i == 8 and j == 17:
                matrizCaminho[i][j] = 93.62
                matrizCaminho[j][i] = 93.62

            if i == 9 and j == 18:
                matrizCaminho[i][j] = 70.69
                matrizCaminho[j][i] = 70.69

            if i == 9 and j == 19:
                matrizCaminho[i][j] = 110.86
                matrizCaminho[j][i] = 110.86

            if i == 10 and j == 19:
                matrizCaminho[i][j] = 54.13
                matrizCaminho[j][i] = 54.13

            if i == 11 and j == 20:
                matrizCaminho[i][j] = 99.18
                matrizCaminho[j][i] = 99.18

            if i == 11 and j == 21:
                matrizCaminho[i][j] = 39.11
                matrizCaminho[j][i] = 39.11

            if i == 12 and j == 17:
                matrizCaminho[i][j] = 60.90
                matrizCaminho[j][i] = 60.90

            if i == 12 and j == 22:
                matrizCaminho[i][j] = 52.48
                matrizCaminho[j][i] = 52.48

            if i == 13 and j == 23:
                matrizCaminho[i][j] = 60.03
                matrizCaminho[j][i] = 60.03

            if i == 13 and j == 24:
                matrizCaminho[i][j] = 63.40
                matrizCaminho[j][i] = 63.40

            if i == 14 and j == 25:
                matrizCaminho[i][j] = 127.67
                matrizCaminho[j][i] = 127.67

            if i == 14 and j == 26:
                matrizCaminho[i][j] = 51.41
                matrizCaminho[j][i] = 51.41

            if i == 15 and j == 27:
                matrizCaminho[i][j] = 30.89
                matrizCaminho[j][i] = 30.89

            if i == 16 and j == 28:
                matrizCaminho[i][j] = 66.98
                matrizCaminho[j][i] = 66.98

            if i == 16 and j == 29:
                matrizCaminho[i][j] = 94.11
                matrizCaminho[j][i] = 94.11

            if i == 18 and j == 30:
                matrizCaminho[i][j] = 20.71
                matrizCaminho[j][i] = 20.71

            if i == 18 and j == 31:
                matrizCaminho[i][j] = 102.24
                matrizCaminho[j][i] = 102.24

            if i == 19 and j == 31:
                matrizCaminho[i][j] = 98.54
                matrizCaminho[j][i] = 98.54

            if i == 19 and j == 32:
                matrizCaminho[i][j] = 57.79
                matrizCaminho[j][i] = 57.79

            if i == 19 and j == 33:
                matrizCaminho[i][j] = 75.79
                matrizCaminho[j][i] = 75.79

            if i == 20 and j == 33:
                matrizCaminho[i][j] = 23.33
                matrizCaminho[j][i] = 23.33

            if i == 21 and j == 22:
                matrizCaminho[i][j] = 51.86
                matrizCaminho[j][i] = 51.86

            if i == 21 and j == 34:
                matrizCaminho[i][j] = 116.69
                matrizCaminho[j][i] = 116.69

            if i == 22 and j == 35:
                matrizCaminho[i][j] = 113.67
                matrizCaminho[j][i] = 113.67

            if i == 22 and j == 36:
                matrizCaminho[i][j] = 61.91
                matrizCaminho[j][i] = 61.91

            if i == 23 and j == 25:
                matrizCaminho[i][j] = 55.32
                matrizCaminho[j][i] = 55.32

            if i == 23 and j == 37:
                matrizCaminho[i][j] = 51.50
                matrizCaminho[j][i] = 51.50

            if i == 23 and j == 38:
                matrizCaminho[i][j] = 63.40
                matrizCaminho[j][i] = 63.40

            if i == 24 and j == 30:
                matrizCaminho[i][j] = 57.06
                matrizCaminho[j][i] = 57.06

            if i == 24 and j == 38:
                matrizCaminho[i][j] = 47.41
                matrizCaminho[j][i] = 47.41

            if i == 25 and j == 39:
                matrizCaminho[i][j] = 48.61
                matrizCaminho[j][i] = 48.61

            if i == 25 and j == 40:
                matrizCaminho[i][j] = 55.85
                matrizCaminho[j][i] = 55.85

            if i == 26 and j == 40:
                matrizCaminho[i][j] = 128.63
                matrizCaminho[j][i] = 128.63

            if i == 26 and j == 41:
                matrizCaminho[i][j] = 30.64
                matrizCaminho[j][i] = 30.64

            if i == 28 and j == 42:
                matrizCaminho[i][j] = 37.77
                matrizCaminho[j][i] = 37.77

            if i == 28 and j == 43:
                matrizCaminho[i][j] = 78.65
                matrizCaminho[j][i] = 78.65

            if i == 30 and j == 44:
                matrizCaminho[i][j] = 39.79
                matrizCaminho[j][i] = 39.79

            if i == 31 and j == 45:
                matrizCaminho[i][j] = 47.34
                matrizCaminho[j][i] = 47.34

            if i == 31 and j == 46:
                matrizCaminho[i][j] = 66.26
                matrizCaminho[j][i] = 66.26

            if i == 32 and j == 46:
                matrizCaminho[i][j] = 112.48
                matrizCaminho[j][i] = 112.48

            if i == 32 and j == 47:
                matrizCaminho[i][j] = 38
                matrizCaminho[j][i] = 38

            if i == 32 and j == 48:
                matrizCaminho[i][j] = 60.21
                matrizCaminho[j][i] = 60.21

            if i == 33 and j == 34:
                matrizCaminho[i][j] = 44.56
                matrizCaminho[j][i] = 44.56

            if i == 33 and j == 48:
                matrizCaminho[i][j] = 41.99
                matrizCaminho[j][i] = 41.99

            if i == 34 and j == 35:
                matrizCaminho[i][j] = 47.30
                matrizCaminho[j][i] = 47.30

            if i == 35 and j == 49:
                matrizCaminho[i][j] = 52.32
                matrizCaminho[j][i] = 52.32

            if i == 35 and j == 50:
                matrizCaminho[i][j] = 35.04
                matrizCaminho[j][i] = 35.04

            if i == 37 and j == 39:
                matrizCaminho[i][j] = 56.49
                matrizCaminho[j][i] = 56.49

            if i == 37 and j == 51:
                matrizCaminho[i][j] = 61.53
                matrizCaminho[j][i] = 61.53

            if i == 37 and j == 52:
                matrizCaminho[i][j] = 61.83
                matrizCaminho[j][i] = 61.83

            if i == 38 and j == 44:
                matrizCaminho[i][j] = 60.04
                matrizCaminho[j][i] = 60.04

            if i == 38 and j == 52:
                matrizCaminho[i][j] = 53.21
                matrizCaminho[j][i] = 53.21

            if i == 39 and j == 53:
                matrizCaminho[i][j] = 61.99
                matrizCaminho[j][i] = 61.99

            if i == 39 and j == 54:
                matrizCaminho[i][j] = 78.95
                matrizCaminho[j][i] = 78.95

            if i == 40 and j == 55:
                matrizCaminho[i][j] = 20.48
                matrizCaminho[j][i] = 20.48

            if i == 44 and j == 45:
                matrizCaminho[i][j] = 99.26
                matrizCaminho[j][i] = 99.26

            if i == 44 and j == 56:
                matrizCaminho[i][j] = 56.59
                matrizCaminho[j][i] = 56.59

            if i == 45 and j == 57:
                matrizCaminho[i][j] = 62.32
                matrizCaminho[j][i] = 62.32

            if i == 45 and j == 58:
                matrizCaminho[i][j] = 72.74
                matrizCaminho[j][i] = 72.74

            if i == 46 and j == 58:
                matrizCaminho[i][j] = 35.57
                matrizCaminho[j][i] = 35.57

            if i == 46 and j == 59:
                matrizCaminho[i][j] = 43.16
                matrizCaminho[j][i] = 43.16

            if i == 48 and j == 49:
                matrizCaminho[i][j] = 90.34
                matrizCaminho[j][i] = 90.34

            if i == 48 and j == 60:
                matrizCaminho[i][j] = 31.49
                matrizCaminho[j][i] = 31.49

            if i == 49 and j == 61:
                matrizCaminho[i][j] = 62.63
                matrizCaminho[j][i] = 62.63

            if i == 49 and j == 62:
                matrizCaminho[i][j] = 18.03
                matrizCaminho[j][i] = 18.03

            if i == 51 and j == 53:
                matrizCaminho[i][j] = 62.55
                matrizCaminho[j][i] = 62.55

            if i == 51 and j == 63:
                matrizCaminho[i][j] = 51.75
                matrizCaminho[j][i] = 51.75

            if i == 51 and j == 64:
                matrizCaminho[i][j] = 59.75
                matrizCaminho[j][i] = 59.75

            if i == 52 and j == 56:
                matrizCaminho[i][j] = 60.48
                matrizCaminho[j][i] = 60.48

            if i == 52 and j == 64:
                matrizCaminho[i][j] = 63.72
                matrizCaminho[j][i] = 63.72

            if i == 53 and j == 65:
                matrizCaminho[i][j] = 23.62
                matrizCaminho[j][i] = 23.62

            if i == 54 and j == 65:
                matrizCaminho[i][j] = 50.15
                matrizCaminho[j][i] = 50.15

            if i == 56 and j == 57:
                matrizCaminho[i][j] = 93.68
                matrizCaminho[j][i] = 93.68

            if i == 56 and j == 66:
                matrizCaminho[i][j] = 61.16
                matrizCaminho[j][i] = 61.16

            if i == 57 and j == 67:
                matrizCaminho[i][j] = 62.18
                matrizCaminho[j][i] = 62.18

            if i == 57 and j == 68:
                matrizCaminho[i][j] = 75.81
                matrizCaminho[j][i] = 75.81

            if i == 58 and j == 68:
                matrizCaminho[i][j] = 64.49
                matrizCaminho[j][i] = 64.49

            if i == 59 and j == 69:
                matrizCaminho[i][j] = 94.41
                matrizCaminho[j][i] = 94.41

            if i == 63 and j == 70:
                matrizCaminho[i][j] = 49.94
                matrizCaminho[j][i] = 49.94

            if i == 63 and j == 71:
                matrizCaminho[i][j] = 56.70
                matrizCaminho[j][i] = 56.70

            if i == 64 and j == 66:
                matrizCaminho[i][j] = 60.39
                matrizCaminho[j][i] = 60.39

            if i == 64 and j == 71:
                matrizCaminho[i][j] = 53.75
                matrizCaminho[j][i] = 53.75

            if i == 65 and j == 72:
                matrizCaminho[i][j] = 73.13
                matrizCaminho[j][i] = 73.13

            if i == 66 and j == 67:
                matrizCaminho[i][j] = 89.69
                matrizCaminho[j][i] = 89.69

            if i == 66 and j == 73:
                matrizCaminho[i][j] = 54.08
                matrizCaminho[j][i] = 54.08

            if i == 67 and j == 74:
                matrizCaminho[i][j] = 53.62
                matrizCaminho[j][i] = 53.62

            if i == 67 and j == 75:
                matrizCaminho[i][j] = 85.22
                matrizCaminho[j][i] = 85.22

            if i == 68 and j == 69:
                matrizCaminho[i][j] = 50.78
                matrizCaminho[j][i] = 50.78

            if i == 68 and j == 75:
                matrizCaminho[i][j] = 60.08
                matrizCaminho[j][i] = 60.08

            if i == 69 and j == 76:
                matrizCaminho[i][j] = 60.29
                matrizCaminho[j][i] = 60.29

            if i == 70 and j == 72:
                matrizCaminho[i][j] = 63.56
                matrizCaminho[j][i] = 63.56

            if i == 70 and j == 78:
                matrizCaminho[i][j] = 48.19
                matrizCaminho[j][i] = 48.19

            if i == 70 and j == 79:
                matrizCaminho[i][j] = 59.04
                matrizCaminho[j][i] = 59.04

            if i == 71 and j == 73:
                matrizCaminho[i][j] = 60.70
                matrizCaminho[j][i] = 60.70

            if i == 71 and j == 79:
                matrizCaminho[i][j] = 54.78
                matrizCaminho[j][i] = 54.78

            if i == 72 and j == 80:
                matrizCaminho[i][j] = 50.89
                matrizCaminho[j][i] = 50.89

            if i == 72 and j == 81:
                matrizCaminho[i][j] = 35.81
                matrizCaminho[j][i] = 35.81

            if i == 73 and j == 74:
                matrizCaminho[i][j] = 88.58
                matrizCaminho[j][i] = 88.58

            if i == 73 and j == 82:
                matrizCaminho[i][j] = 62.44
                matrizCaminho[j][i] = 62.44

            if i == 74 and j == 83:
                matrizCaminho[i][j] = 74.12
                matrizCaminho[j][i] = 74.12

            if i == 74 and j == 84:
                matrizCaminho[i][j] = 92.14
                matrizCaminho[j][i] = 92.14

            if i == 75 and j == 76:
                matrizCaminho[i][j] = 52.74
                matrizCaminho[j][i] = 52.74

            if i == 75 and j == 84:
                matrizCaminho[i][j] = 51.65
                matrizCaminho[j][i] = 51.65

            if i == 76 and j == 85:
                matrizCaminho[i][j] = 50.85
                matrizCaminho[j][i] = 50.85

            if i == 76 and j == 86:
                matrizCaminho[i][j] = 19.80
                matrizCaminho[j][i] = 19.80

            if i == 78 and j == 80:
                matrizCaminho[i][j] = 62.22
                matrizCaminho[j][i] = 62.22

            if i == 78 and j == 87:
                matrizCaminho[i][j] = 69.06
                matrizCaminho[j][i] = 69.06

            if i == 79 and j == 82:
                matrizCaminho[i][j] = 54.92
                matrizCaminho[j][i] = 54.92

            if i == 79 and j == 88:
                matrizCaminho[i][j] = 114.28
                matrizCaminho[j][i] = 114.28

            if i == 80 and j == 89:
                matrizCaminho[i][j] = 71.46
                matrizCaminho[j][i] = 71.46

            if i == 82 and j == 83:
                matrizCaminho[i][j] = 86.91
                matrizCaminho[j][i] = 86.91

            if i == 82 and j == 91:
                matrizCaminho[i][j] = 62.57
                matrizCaminho[j][i] = 62.57

            if i == 83 and j == 92:
                matrizCaminho[i][j] = 60.22
                matrizCaminho[j][i] = 60.22

            if i == 83 and j == 93:
                matrizCaminho[i][j] = 34.11
                matrizCaminho[j][i] = 34.11

            if i == 84 and j == 85:
                matrizCaminho[i][j] = 52.47
                matrizCaminho[j][i] = 52.47

            if i == 84 and j == 94:
                matrizCaminho[i][j] = 88.08
                matrizCaminho[j][i] = 88.08

            if i == 85 and j == 95:
                matrizCaminho[i][j] = 96.09
                matrizCaminho[j][i] = 96.09

            if i == 87 and j == 88:
                matrizCaminho[i][j] = 63.39
                matrizCaminho[j][i] = 63.39

            if i == 87 and j == 89:
                matrizCaminho[i][j] = 61.95
                matrizCaminho[j][i] = 61.95

            if i == 87 and j == 96:
                matrizCaminho[i][j] = 80.22
                matrizCaminho[j][i] = 80.22

            if i == 88 and j == 97:
                matrizCaminho[i][j] = 86.28
                matrizCaminho[j][i] = 86.28

            if i == 88 and j == 98:
                matrizCaminho[i][j] = 54.37
                matrizCaminho[j][i] = 54.37

            if i == 89 and j == 99:
                matrizCaminho[i][j] = 73.65
                matrizCaminho[j][i] = 73.65

            if i == 91 and j == 92:
                matrizCaminho[i][j] = 85.21
                matrizCaminho[j][i] = 85.21

            if i == 91 and j == 98:
                matrizCaminho[i][j] = 49.79
                matrizCaminho[j][i] = 49.79

            if i == 92 and j == 101:
                matrizCaminho[i][j] = 51.01
                matrizCaminho[j][i] = 51.01

            if i == 93 and j == 94:
                matrizCaminho[i][j] = 63.38
                matrizCaminho[j][i] = 63.38

            if i == 93 and j == 102:
                matrizCaminho[i][j] = 109.75
                matrizCaminho[j][i] = 109.75

            if i == 94 and j == 95:
                matrizCaminho[i][j] = 56.67
                matrizCaminho[j][i] = 56.67

            if i == 94 and j == 103:
                matrizCaminho[i][j] = 109.64
                matrizCaminho[j][i] = 109.64

            if i == 95 and j == 104:
                matrizCaminho[i][j] = 107.70
                matrizCaminho[j][i] = 107.70

            if i == 95 and j == 105:
                matrizCaminho[i][j] = 20.82
                matrizCaminho[j][i] = 20.82

            if i == 96 and j == 97:
                matrizCaminho[i][j] = 65.58
                matrizCaminho[j][i] = 65.58

            if i == 96 and j == 99:
                matrizCaminho[i][j] = 60.74
                matrizCaminho[j][i] = 60.74

            if i == 96 and j == 106:
                matrizCaminho[i][j] = 42.92
                matrizCaminho[j][i] = 42.92

            if i == 97 and j == 107:
                matrizCaminho[i][j] = 26.42
                matrizCaminho[j][i] = 26.42

            if i == 97 and j == 108:
                matrizCaminho[i][j] = 54.22
                matrizCaminho[j][i] = 54.22

            if i == 98 and j == 101:
                matrizCaminho[i][j] = 86.36
                matrizCaminho[j][i] = 86.36

            if i == 98 and j == 108:
                matrizCaminho[i][j] = 88.34
                matrizCaminho[j][i] = 88.34

            if i == 99 and j == 109:
                matrizCaminho[i][j] = 34.42
                matrizCaminho[j][i] = 34.42

            if i == 101 and j == 102:
                matrizCaminho[i][j] = 37.68
                matrizCaminho[j][i] = 37.68

            if i == 101 and j == 110:
                matrizCaminho[i][j] = 93.91
                matrizCaminho[j][i] = 93.91

            if i == 102 and j == 103:
                matrizCaminho[i][j] = 66.28
                matrizCaminho[j][i] = 66.28

            if i == 102 and j == 111:
                matrizCaminho[i][j] = 87.13
                matrizCaminho[j][i] = 87.13

            if i == 103 and j == 104:
                matrizCaminho[i][j] = 56.32
                matrizCaminho[j][i] = 56.32

            if i == 103 and j == 112:
                matrizCaminho[i][j] = 50.26
                matrizCaminho[j][i] = 50.26

            if i == 104 and j == 113:
                matrizCaminho[i][j] = 49.13
                matrizCaminho[j][i] = 49.13

            if i == 104 and j == 114:
                matrizCaminho[i][j] = 27.99
                matrizCaminho[j][i] = 27.99

            if i == 108 and j == 110:
                matrizCaminho[i][j] = 78.43
                matrizCaminho[j][i] = 78.43

            if i == 108 and j == 115:
                matrizCaminho[i][j] = 21.57
                matrizCaminho[j][i] = 21.57

            if i == 112 and j == 113:
                matrizCaminho[i][j] = 56.15
                matrizCaminho[j][i] = 56.15

            if i == 112 and j == 116:
                matrizCaminho[i][j] = 28.86
                matrizCaminho[j][i] = 28.86

            if i == 113 and j == 118:
                matrizCaminho[i][j] = 33.73
                matrizCaminho[j][i] = 33.73

