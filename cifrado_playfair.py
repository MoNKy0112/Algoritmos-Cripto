alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


class CifradoPlayfair:
    nombre = "Cifrado Playfair"

    def __init__(self, alfabeto, console_mode=False):
        self.alfabeto = alfabeto
        console_mode if self.console_config() else self.ui_config
        pass

    def console_config(self):
        self.size = int(input("Ingrese el tamaño de la matriz: "))
        clave = input("Ingrese la clave: ")
        self.matriz = [[0 for i in range(self.size)] for j in range(self.size)]
        self.crear_matriz(clave)
        pass

    def ui_config(self):
        pass

    def crear_matriz(self, clave):
        self.dict = {}
        clave = clave.upper()
        fila = 0
        col = 0
        for letra in clave:
            if self.dict.get(letra) is None:
                self.matriz[fila][col] = letra
                if letra == "I":
                    self.dict["J"] = {"fila": fila, "col": col}
                if letra == "J":
                    self.dict["I"] = {"fila": fila, "col": col}
                self.dict[letra] = {"fila": fila, "col": col}
            else:
                continue
            if (col == self.size-1):
                col = 0
                fila += 1
            else:
                col += 1

        for letra in alfabeto:
            if self.dict.get(letra) is None:
                if letra == "I":
                    self.dict["J"] = {"fila": fila, "col": col}
                if letra == "J":
                    self.dict["I"] = {"fila": fila, "col": col}
                self.matriz[fila][col] = letra
                self.dict[letra] = {"fila": fila, "col": col}
            else:
                continue
            if (col == self.size-1):
                col = 0
                fila += 1
            else:
                col += 1

    def cifrar(self, texto: str):
        texto = texto.upper().replace(" ", "")
        texto_cifrado = ""
        while len(texto) > 0:
            par = texto[0:2]
            if len(par) == 1:
                par = par + "X"
                texto = texto[1:]
            elif par[0] == par[1]:
                texto = par[1] + texto[2:]
                par = par[0] + "X"
            else:
                texto = texto[2:]

            fila1 = self.dict[par[0]]["fila"]
            col1 = self.dict[par[0]]["col"]
            fila2 = self.dict[par[1]]["fila"]
            col2 = self.dict[par[1]]["col"]
            # Caso1 misma fila
            if fila1 == fila2:
                new_char1 = self.matriz[fila1][(col1 + 1) % self.size]
                new_char2 = self.matriz[fila2][(col2 + 1) % self.size]
            elif col1 == col2:
                new_char1 = self.matriz[(fila1 + 1) % self.size][col1]
                new_char2 = self.matriz[(fila2 + 1) % self.size][col2]
            else:
                new_char1 = self.matriz[fila1][col2]
                new_char2 = self.matriz[fila2][col1]
            texto_cifrado += new_char1 + new_char2
            # print(par, " -> ", new_char1, new_char2)
        return texto_cifrado

    def descifrar(self, texto: str):
        texto = texto.upper().replace(" ", "")
        texto_descifrado = ""
        while len(texto) > 0:
            par = texto[0:2]
            if len(par) == 1:
                par = par + "X"
                texto = texto[1:]
            elif par[0] == par[1]:
                texto = par[1] + texto[2:]
                par = par[0] + "X"
            else:
                texto = texto[2:]

            fila1 = self.dict[par[0]]["fila"]
            col1 = self.dict[par[0]]["col"]
            fila2 = self.dict[par[1]]["fila"]
            col2 = self.dict[par[1]]["col"]
            # Caso1 misma fila
            if fila1 == fila2:
                new_char1 = self.matriz[fila1][(col1 - 1) % self.size]
                new_char2 = self.matriz[fila2][(col2 - 1) % self.size]
            elif col1 == col2:
                new_char1 = self.matriz[(fila1 - 1) % self.size][col1]
                new_char2 = self.matriz[(fila2 - 1) % self.size][col2]
            else:
                new_char1 = self.matriz[fila1][col2]
                new_char2 = self.matriz[fila2][col1]
            texto_descifrado += new_char1 + new_char2
            # print(par, " -> ", new_char1, new_char2)
        return texto_descifrado

    def print_matriz(self):
        for fila in self.matriz:
            print(fila)


# playfair = cifrado_playfair(alfabeto, "JorgeYMaria")

# playfair.print_matriz()

# print("TExto a encriptarr")
# texto_cif = playfair.cifrar("TExto a encriptarr")
# print(texto_cif)
# texto_cif = playfair.descifrar(texto_cif)
# print(texto_cif)
